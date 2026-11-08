"""Metrics Collector.

Annotates candidates with structural features and collapses exact duplicates.
"""

from reranking_gateway.components.metrics_collector.adapter import ROLE, build
from reranking_gateway.components.metrics_collector.config import CONFIG, MetricsCollectorConfig
from reranking_gateway.components.metrics_collector.errors import MetricsCollectorError
from reranking_gateway.components.metrics_collector.service import MetricsCollectorService

__all__ = ["CONFIG", "ROLE", "build", "MetricsCollectorConfig", "MetricsCollectorError", "MetricsCollectorService"]
