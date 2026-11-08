"""Port and registry adapter for Fallback Handler.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from reranking_gateway.components.fallback_handler.config import CONFIG
from reranking_gateway.components.fallback_handler.service import FallbackHandlerService
from reranking_gateway.domain.models import PipelineContext

ROLE = CONFIG.role


class FallbackHandlerPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> FallbackHandlerService:
    return FallbackHandlerService(services)
