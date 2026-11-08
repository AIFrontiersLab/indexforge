"""Reranking Gateway: governed reference service.

Reorder candidates using stronger relevance judgments.

Public entry points:

* ``build_container`` - wire the full object graph from settings.
* ``run`` - execute a single request and return the outcome as a dict.
"""

from reranking_gateway.application.pipeline import run
from reranking_gateway.container import build_container
from reranking_gateway.version import __version__

__all__ = ["__version__", "build_container", "run"]
