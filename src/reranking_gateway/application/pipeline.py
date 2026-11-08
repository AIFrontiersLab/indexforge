"""Convenience entry points for embedding the pipeline in another program.

    >>> from reranking_gateway.application.pipeline import run
    >>> result = run({"query": "example", "evidence_ids": ["doc-1"]})
    >>> result["abstain"]
    False
"""

from __future__ import annotations

from reranking_gateway.application.commands import RunPipeline


def run(request: dict, *, container=None) -> dict:
    """Execute one request against a fresh (or supplied) container and return the outcome dict."""
    if container is None:
        from reranking_gateway.container import build_container

        container = build_container()
    return container.bus.handle(RunPipeline(request=request))
