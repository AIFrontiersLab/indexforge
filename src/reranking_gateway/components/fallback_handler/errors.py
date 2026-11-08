"""Errors raised by Fallback Handler. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from reranking_gateway.kernel.errors import StageError


class FallbackHandlerError(StageError):
    code = "fallback_handler_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("fallback_handler", message, retryable=retryable, details=details)


class FallbackHandlerContractViolation(FallbackHandlerError):
    code = "fallback_handler_contract_violation"
