"""Pre- and post-conditions for Reranker Engine.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from reranking_gateway.components.reranker_engine.config import RerankerEngineConfig
from reranking_gateway.components.reranker_engine.errors import RerankerEngineContractViolation
from reranking_gateway.components.reranker_engine.models import RerankerEngineInput


def validate_input(ctx, config: RerankerEngineConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise RerankerEngineContractViolation(
            "too many candidates for reranker_engine",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: RerankerEngineInput, config: RerankerEngineConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise RerankerEngineContractViolation("duplicate candidate ids after reranker_engine")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise RerankerEngineContractViolation(
                "reranker_engine introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise RerankerEngineContractViolation("reranker_engine produced an unsorted ranking")
