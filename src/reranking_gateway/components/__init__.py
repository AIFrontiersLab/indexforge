"""Concept-specific components. Each one specialises a stage role with its own
configuration, validation, metrics, and errors."""

from reranking_gateway.components.fallback_handler import adapter as _fallback_handler
from reranking_gateway.components.gateway_controller import adapter as _gateway_controller
from reranking_gateway.components.metrics_collector import adapter as _metrics_collector
from reranking_gateway.components.ranking_cache import adapter as _ranking_cache
from reranking_gateway.components.reranker_engine import adapter as _reranker_engine
from reranking_gateway.components.token_budget_governor import adapter as _token_budget_governor

COMPONENT_FACTORIES = {
    "gateway_controller": (_gateway_controller.ROLE, _gateway_controller.build),
    "reranker_engine": (_reranker_engine.ROLE, _reranker_engine.build),
    "fallback_handler": (_fallback_handler.ROLE, _fallback_handler.build),
    "metrics_collector": (_metrics_collector.ROLE, _metrics_collector.build),
    "ranking_cache": (_ranking_cache.ROLE, _ranking_cache.build),
    "token_budget_governor": (_token_budget_governor.ROLE, _token_budget_governor.build),
}
