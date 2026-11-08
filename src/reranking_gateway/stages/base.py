"""Stage contract and the service bundle injected into every stage.

A stage is a strategy object with a single ``process(ctx)`` method that mutates
the run context. Stages are created by factories in the plugin registry so new
behaviour can be added without editing the orchestrator.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from reranking_gateway.config.settings import Settings
from reranking_gateway.domain.models import PipelineContext
from reranking_gateway.kernel.clock import Clock


@dataclass
class StageServices:
    settings: Settings
    clock: Clock
    scorer: Any
    corpus: Any
    cache: Any
    audit: Any
    metrics: Any
    policy_engine: Any
    redactor: Any
    approvals: Any
    budget_guard: Any
    extras: dict = field(default_factory=dict)


class Stage(ABC):
    role: str = "generic"
    critical: bool = False

    def __init__(self, name: str, services: StageServices, *, description: str = "") -> None:
        self.name = name
        self.services = services
        self.description = description

    @abstractmethod
    def process(self, ctx: PipelineContext) -> None:
        """Mutate ``ctx`` in place. Raise ``StageError`` for recoverable faults."""

    def describe(self) -> dict:
        return {
            "name": self.name,
            "role": self.role,
            "critical": self.critical,
            "description": self.description,
        }

    def __repr__(self) -> str:
        return f"<{type(self).__name__} name={self.name!r} role={self.role!r}>"
