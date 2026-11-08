"""Port and registry adapter for Reranker Engine.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from reranking_gateway.components.reranker_engine.config import CONFIG
from reranking_gateway.components.reranker_engine.service import RerankerEngineService
from reranking_gateway.domain.models import PipelineContext

ROLE = CONFIG.role


class RerankerEnginePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> RerankerEngineService:
    return RerankerEngineService(services)
