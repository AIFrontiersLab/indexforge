"""Fallback Handler service.

Role: ``fallback``. Restores a safe prior-score ordering when an upstream stage degraded.

Responsibility (from the architecture specification):
    Restores a safe prior-score ordering when an upstream stage degraded.

The service specialises :class:`FallbackStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from reranking_gateway.components.fallback_handler.config import CONFIG, FallbackHandlerConfig
from reranking_gateway.components.fallback_handler.models import FallbackHandlerInput, FallbackHandlerReport
from reranking_gateway.components.fallback_handler.validators import validate_input, validate_output
from reranking_gateway.stages.fallback import FallbackStage

METRIC_PREFIX = "component_fallback_handler"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: FallbackHandlerReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class FallbackHandlerService(FallbackStage):
    def __init__(self, services, config: FallbackHandlerConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = FallbackHandlerInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = FallbackHandlerReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = FallbackHandlerReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
