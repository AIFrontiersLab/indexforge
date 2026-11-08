"""Ports: the interfaces the application core requires from the outside world.

Adapters under ``reranking_gateway.adapters`` implement these protocols. The core never
imports an adapter directly; the composition root (``container.py``) wires them.
"""

from reranking_gateway.ports.audit import AuditSink
from reranking_gateway.ports.cache import RankingCache
from reranking_gateway.ports.corpus import CorpusRepository
from reranking_gateway.ports.event_bus import EventBus
from reranking_gateway.ports.repository import RunRepository
from reranking_gateway.ports.scorer import RelevanceScorer

__all__ = ["AuditSink", "CorpusRepository", "EventBus", "RankingCache", "RelevanceScorer", "RunRepository"]
