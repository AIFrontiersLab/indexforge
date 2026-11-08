"""Errors raised by Reranker Engine. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from reranking_gateway.kernel.errors import StageError


class RerankerEngineError(StageError):
    code = "reranker_engine_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("reranker_engine", message, retryable=retryable, details=details)


class RerankerEngineContractViolation(RerankerEngineError):
    code = "reranker_engine_contract_violation"
