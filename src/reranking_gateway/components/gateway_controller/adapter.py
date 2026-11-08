"""Port and registry adapter for Gateway Controller.

Interface from the architecture specification: ``REST API /rerank``
"""

from __future__ import annotations

from typing import Protocol

from reranking_gateway.components.gateway_controller.config import CONFIG
from reranking_gateway.components.gateway_controller.service import GatewayControllerService
from reranking_gateway.domain.models import PipelineContext

ROLE = CONFIG.role


class GatewayControllerPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> GatewayControllerService:
    return GatewayControllerService(services)
