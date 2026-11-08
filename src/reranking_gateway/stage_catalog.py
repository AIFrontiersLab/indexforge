"""Stage catalog for Reranking Gateway.

Declares the default stage order and registers every built-in and component stage
with the plugin registry. Imports of stage classes are deferred so configuration
modules can read ``DEFAULT_STAGE_ORDER`` without import cycles.
"""

from __future__ import annotations

DEFAULT_STAGE_ORDER = [
    "gateway_controller",
    "corpus_retrieval",
    "metrics_collector",
    "ranking_cache",
    "reranker_engine",
    "fallback_handler",
    "access_policy",
    "token_budget_governor",
    "answer_assembly",
]

BUILTINS = {
    "intake": "ingest",
    "corpus_retrieval": "retrieve",
    "relevance_scoring": "score",
    "access_policy": "policy",
    "graceful_fallback": "fallback",
    "answer_assembly": "answer",
}

COMPONENTS = [
    {"name": 'Gateway Controller', "slug": "gateway_controller", "role": "ingest", "origin": "spec"},
    {"name": 'Reranker Engine', "slug": "reranker_engine", "role": "score", "origin": "spec"},
    {"name": 'Fallback Handler', "slug": "fallback_handler", "role": "fallback", "origin": "spec"},
    {"name": 'Metrics Collector', "slug": "metrics_collector", "role": "enrich", "origin": "spec"},
    {"name": 'Ranking Cache', "slug": "ranking_cache", "role": "cache", "origin": "padded"},
    {"name": 'Token Budget Governor', "slug": "token_budget_governor", "role": "budget", "origin": "padded"},
]


def register_all(registry) -> None:
    from reranking_gateway.components import COMPONENT_FACTORIES
    from reranking_gateway.stages import ROLE_CLASSES

    for name, role in BUILTINS.items():
        cls = ROLE_CLASSES[role]
        registry.register(name, role, lambda services, cls=cls, name=name: cls(name, services), source="builtin")
    for name, (role, factory) in COMPONENT_FACTORIES.items():
        registry.register(name, role, factory, source="component")
