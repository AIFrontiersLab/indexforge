"""Contract tests for the Gateway Controller component (role: ingest)."""

import pytest

from reranking_gateway.components.gateway_controller import CONFIG, ROLE, build
from reranking_gateway.components.gateway_controller.errors import GatewayControllerContractViolation
from reranking_gateway.components.gateway_controller.models import GatewayControllerInput, GatewayControllerReport
from reranking_gateway.components.gateway_controller.validators import validate_input, validate_output
from reranking_gateway.domain.models import Candidate, PipelineContext, Request


def _ctx(candidates, **request):
    req = Request.from_dict({"query": "evidence retrieval policy", **request})
    return PipelineContext(run_id="run_test", request=req, candidates=candidates)


def _cands():
    return [
        Candidate("d1", "evidence retrieval policy overview", prior_score=0.9, score=0.9, classification="public"),
        Candidate("d2", "unrelated cooking notes", prior_score=0.5, score=0.5, classification="internal"),
        Candidate("d3", "retrieval evidence and policy controls", prior_score=0.7, score=0.7, classification="internal"),
    ]


def test_role_and_name(services):
    stage = build(services)
    assert ROLE == "ingest"
    assert stage.name == CONFIG.name == "gateway_controller"
    assert stage.describe()["display_name"] == 'Gateway Controller'


def test_process_records_report(services):
    stage = build(services)
    ctx = _ctx(_cands())
    stage.process(ctx)
    report = ctx.metadata["reports"]["gateway_controller"]
    assert report["stage"] == "gateway_controller"
    assert report["candidates_in"] == 3
    assert services.metrics.counter("component_gateway_controller_runs_total") == 1


def test_output_has_no_duplicate_ids(services):
    stage = build(services)
    ctx = _ctx(_cands())
    stage.process(ctx)
    ids = [c.doc_id for c in ctx.candidates]
    assert len(ids) == len(set(ids))


def test_input_bound_is_enforced():
    from dataclasses import replace

    ctx = _ctx(_cands())
    with pytest.raises(GatewayControllerContractViolation):
        validate_input(ctx, replace(CONFIG, max_input_candidates=1))


def test_unknown_ids_rejected_unless_allowed():
    from dataclasses import replace

    ctx = _ctx(_cands())
    before = GatewayControllerInput(query="q", candidate_ids=("d1",))
    strict = replace(CONFIG, may_introduce_ids=False, enforce_sorted_output=False)
    with pytest.raises(GatewayControllerContractViolation):
        validate_output(ctx, before, strict)
    validate_output(ctx, before, replace(strict, may_introduce_ids=True))


def test_report_diff():
    report = GatewayControllerReport.diff("gateway_controller", GatewayControllerInput("q", ("a", "b")), ["b", "c"])
    assert report.added == ("c",)
    assert report.removed == ("a",)
    assert report.to_dict()["candidates_out"] == 2
