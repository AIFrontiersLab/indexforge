"""Errors raised by Gateway Controller. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from reranking_gateway.kernel.errors import StageError


class GatewayControllerError(StageError):
    code = "gateway_controller_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("gateway_controller", message, retryable=retryable, details=details)


class GatewayControllerContractViolation(GatewayControllerError):
    code = "gateway_controller_contract_violation"
