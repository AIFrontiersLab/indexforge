"""Static configuration for the Metrics Collector component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MetricsCollectorConfig:
    name: str = "metrics_collector"
    display_name: str = 'Metrics Collector'
    role: str = "enrich"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Annotates candidates with structural features and collapses exact duplicates.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = False


CONFIG = MetricsCollectorConfig()
