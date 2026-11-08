"""Reranker Engine.

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from reranking_gateway.components.reranker_engine.adapter import ROLE, build
from reranking_gateway.components.reranker_engine.config import CONFIG, RerankerEngineConfig
from reranking_gateway.components.reranker_engine.errors import RerankerEngineError
from reranking_gateway.components.reranker_engine.service import RerankerEngineService

__all__ = ["CONFIG", "ROLE", "build", "RerankerEngineConfig", "RerankerEngineError", "RerankerEngineService"]
