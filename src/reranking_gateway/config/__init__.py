"""Typed configuration: defaults in code, profiles in TOML, overrides from the environment."""

from reranking_gateway.config.loader import load_settings
from reranking_gateway.config.settings import Settings

__all__ = ["Settings", "load_settings"]
