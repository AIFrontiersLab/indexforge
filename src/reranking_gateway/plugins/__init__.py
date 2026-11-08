"""Extension points: stage factories and lifecycle hooks."""

from reranking_gateway.plugins.hooks import HookManager
from reranking_gateway.plugins.registry import StageRegistry

__all__ = ["HookManager", "StageRegistry"]
