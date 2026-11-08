"""Errors raised by Metrics Collector. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from reranking_gateway.kernel.errors import StageError


class MetricsCollectorError(StageError):
    code = "metrics_collector_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("metrics_collector", message, retryable=retryable, details=details)


class MetricsCollectorContractViolation(MetricsCollectorError):
    code = "metrics_collector_contract_violation"
