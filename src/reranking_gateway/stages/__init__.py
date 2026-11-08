"""Role implementations. Components specialise one of these strategies."""

from reranking_gateway.stages.answer import AnswerStage
from reranking_gateway.stages.approval import ApprovalStage
from reranking_gateway.stages.audit import AuditStage
from reranking_gateway.stages.base import Stage, StageServices
from reranking_gateway.stages.budget import BudgetStage
from reranking_gateway.stages.cache import CacheStage
from reranking_gateway.stages.enrich import EnrichStage
from reranking_gateway.stages.fallback import FallbackStage
from reranking_gateway.stages.ingest import IngestStage
from reranking_gateway.stages.policy import PolicyStage
from reranking_gateway.stages.retrieve import RetrieveStage
from reranking_gateway.stages.score import ScoreStage

ROLE_CLASSES: dict[str, type[Stage]] = {
    "ingest": IngestStage,
    "retrieve": RetrieveStage,
    "enrich": EnrichStage,
    "score": ScoreStage,
    "cache": CacheStage,
    "policy": PolicyStage,
    "budget": BudgetStage,
    "approval": ApprovalStage,
    "fallback": FallbackStage,
    "audit": AuditStage,
    "answer": AnswerStage,
}

__all__ = ["ROLE_CLASSES", "Stage", "StageServices", *[cls.__name__ for cls in ROLE_CLASSES.values()]]
