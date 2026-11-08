from reranking_gateway.domain.models import Candidate, PipelineContext, Request
from reranking_gateway.stages.audit import AuditStage


def test_appends_record_without_raw_query(services):
    ctx = PipelineContext(run_id="r1", request=Request.from_dict({"query": "secret question", "tenant": "acme"}), candidates=[Candidate("a")])
    AuditStage("audit", services).process(ctx)
    record = services.audit.records()[-1]
    assert record["run_id"] == "r1" and record["candidate_ids"] == ["a"]
    assert "secret question" not in str(record)
