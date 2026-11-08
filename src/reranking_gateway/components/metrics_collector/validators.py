"""Pre- and post-conditions for Metrics Collector.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from reranking_gateway.components.metrics_collector.config import MetricsCollectorConfig
from reranking_gateway.components.metrics_collector.errors import MetricsCollectorContractViolation
from reranking_gateway.components.metrics_collector.models import MetricsCollectorInput


def validate_input(ctx, config: MetricsCollectorConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise MetricsCollectorContractViolation(
            "too many candidates for metrics_collector",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: MetricsCollectorInput, config: MetricsCollectorConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise MetricsCollectorContractViolation("duplicate candidate ids after metrics_collector")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise MetricsCollectorContractViolation(
                "metrics_collector introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise MetricsCollectorContractViolation("metrics_collector produced an unsorted ranking")
