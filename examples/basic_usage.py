"""Run one governed request in-process."""

import json
from pathlib import Path

from reranking_gateway import build_container
from reranking_gateway.application.commands import RunPipeline

request = json.loads((Path(__file__).parent / "requests" / "governed_query.json").read_text())
outcome = build_container().bus.handle(RunPipeline(request=request))
print(json.dumps({k: outcome[k] for k in ("status", "abstain_reason", "answer", "degraded")}, indent=2))
