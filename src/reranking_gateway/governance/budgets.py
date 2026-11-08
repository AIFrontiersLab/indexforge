"""Token budget resolution: request budget, bounded by the configured hard limit."""

from __future__ import annotations

from reranking_gateway.domain.models import Request
from reranking_gateway.domain.value_objects import TokenBudget


class BudgetGuard:
    def __init__(self, default_tokens: int, hard_limit_tokens: int) -> None:
        self.default_tokens = default_tokens
        self.hard_limit_tokens = hard_limit_tokens

    def for_request(self, request: Request) -> TokenBudget:
        requested = self.default_tokens if request.budget_tokens is None else request.budget_tokens
        return TokenBudget(limit=min(requested, self.hard_limit_tokens))
