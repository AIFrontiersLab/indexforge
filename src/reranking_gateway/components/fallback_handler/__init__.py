"""Fallback Handler.

Restores a safe prior-score ordering when an upstream stage degraded.
"""

from reranking_gateway.components.fallback_handler.adapter import ROLE, build
from reranking_gateway.components.fallback_handler.config import CONFIG, FallbackHandlerConfig
from reranking_gateway.components.fallback_handler.errors import FallbackHandlerError
from reranking_gateway.components.fallback_handler.service import FallbackHandlerService

__all__ = ["CONFIG", "ROLE", "build", "FallbackHandlerConfig", "FallbackHandlerError", "FallbackHandlerService"]
