#!/usr/bin/env bash
set -euo pipefail
export RERANKING_GATEWAY_CONFIG=${RERANKING_GATEWAY_CONFIG:-config/development.toml}
PYTHONPATH=src exec python -m reranking_gateway serve "$@"
