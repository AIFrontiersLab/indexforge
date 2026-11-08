"""Static configuration for the Gateway Controller component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GatewayControllerConfig:
    name: str = "gateway_controller"
    display_name: str = 'Gateway Controller'
    role: str = "ingest"
    interface: str = 'REST API /rerank'
    responsibility: str = 'Validates, normalises, de-duplicates, and bounds the incoming candidate set.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = True
    enforce_sorted_output: bool = False


CONFIG = GatewayControllerConfig()
