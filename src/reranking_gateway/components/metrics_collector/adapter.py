"""Port and registry adapter for Metrics Collector.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from reranking_gateway.components.metrics_collector.config import CONFIG
from reranking_gateway.components.metrics_collector.service import MetricsCollectorService
from reranking_gateway.domain.models import PipelineContext

ROLE = CONFIG.role


class MetricsCollectorPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> MetricsCollectorService:
    return MetricsCollectorService(services)
