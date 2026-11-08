"""Ranking Cache.

Short-circuits repeated identical requests with a TTL-bounded ranking cache keyed by principal.
"""

from reranking_gateway.components.ranking_cache.adapter import ROLE, build
from reranking_gateway.components.ranking_cache.config import CONFIG, RankingCacheConfig
from reranking_gateway.components.ranking_cache.errors import RankingCacheError
from reranking_gateway.components.ranking_cache.service import RankingCacheService

__all__ = ["CONFIG", "ROLE", "build", "RankingCacheConfig", "RankingCacheError", "RankingCacheService"]
