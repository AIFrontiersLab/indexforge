"""Gateway Controller service.

Role: ``ingest``. Validates, normalises, de-duplicates, and bounds the incoming candidate set.

Responsibility (from the architecture specification):
    Validates, normalises, de-duplicates, and bounds the incoming candidate set.

The service specialises :class:`IngestStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from reranking_gateway.components.gateway_controller.config import CONFIG, GatewayControllerConfig
from reranking_gateway.components.gateway_controller.models import GatewayControllerInput, GatewayControllerReport
from reranking_gateway.components.gateway_controller.validators import validate_input, validate_output
from reranking_gateway.stages.ingest import IngestStage

METRIC_PREFIX = "component_gateway_controller"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: GatewayControllerReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class GatewayControllerService(IngestStage):
    def __init__(self, services, config: GatewayControllerConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = GatewayControllerInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = GatewayControllerReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = GatewayControllerReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
