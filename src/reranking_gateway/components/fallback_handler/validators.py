"""Pre- and post-conditions for Fallback Handler.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from reranking_gateway.components.fallback_handler.config import FallbackHandlerConfig
from reranking_gateway.components.fallback_handler.errors import FallbackHandlerContractViolation
from reranking_gateway.components.fallback_handler.models import FallbackHandlerInput


def validate_input(ctx, config: FallbackHandlerConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise FallbackHandlerContractViolation(
            "too many candidates for fallback_handler",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: FallbackHandlerInput, config: FallbackHandlerConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise FallbackHandlerContractViolation("duplicate candidate ids after fallback_handler")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise FallbackHandlerContractViolation(
                "fallback_handler introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise FallbackHandlerContractViolation("fallback_handler produced an unsorted ranking")
