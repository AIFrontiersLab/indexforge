"""Pre- and post-conditions for Gateway Controller.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from reranking_gateway.components.gateway_controller.config import GatewayControllerConfig
from reranking_gateway.components.gateway_controller.errors import GatewayControllerContractViolation
from reranking_gateway.components.gateway_controller.models import GatewayControllerInput


def validate_input(ctx, config: GatewayControllerConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise GatewayControllerContractViolation(
            "too many candidates for gateway_controller",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: GatewayControllerInput, config: GatewayControllerConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise GatewayControllerContractViolation("duplicate candidate ids after gateway_controller")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise GatewayControllerContractViolation(
                "gateway_controller introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise GatewayControllerContractViolation("gateway_controller produced an unsorted ranking")
