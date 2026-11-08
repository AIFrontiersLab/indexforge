"""Smoke tests for the public facade."""

from reranking_gateway.pipeline import run


def test_happy_path_returns_evidence_backed_answer():
    result = run({"query": "demo", "evidence_ids": ["ev-1"], "require_evidence": True})
    assert result["abstain"] is False
    assert result["answer"]["evidence_ids"] == ["ev-1"]
    assert result["events"], "stages should emit events"


def test_missing_evidence_abstains():
    result = run({"query": "demo", "evidence_ids": [], "require_evidence": True})
    assert result["abstain"] is True
    assert result["answer"] is None


def test_concept_metadata_present():
    result = run({"query": "demo", "evidence_ids": ["ev-1"]})
    assert result["concept_id"] == 37
    assert 'Reranking Gateway' in result["concept_name"]
