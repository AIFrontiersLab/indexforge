"""Token Budget Governor.

Enforces per-request and global token ceilings before evidence reaches the answer stage.
"""

from reranking_gateway.components.token_budget_governor.adapter import ROLE, build
from reranking_gateway.components.token_budget_governor.config import CONFIG, TokenBudgetGovernorConfig
from reranking_gateway.components.token_budget_governor.errors import TokenBudgetGovernorError
from reranking_gateway.components.token_budget_governor.service import TokenBudgetGovernorService

__all__ = ["CONFIG", "ROLE", "build", "TokenBudgetGovernorConfig", "TokenBudgetGovernorError", "TokenBudgetGovernorService"]
