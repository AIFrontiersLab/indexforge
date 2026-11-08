"""Static configuration for the Fallback Handler component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FallbackHandlerConfig:
    name: str = "fallback_handler"
    display_name: str = 'Fallback Handler'
    role: str = "fallback"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Restores a safe prior-score ordering when an upstream stage degraded.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = False


CONFIG = FallbackHandlerConfig()
