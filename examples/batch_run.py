"""Run every example request and print a summary table."""

import json
from pathlib import Path

from reranking_gateway import build_container
from reranking_gateway.application.commands import RunPipeline

container = build_container()
for path in sorted((Path(__file__).parent / "requests").glob("*.json")):
    result = container.bus.handle(RunPipeline(request=json.loads(path.read_text())))
    cited = (result["answer"] or {}).get("evidence_ids", [])
    print(f"{path.stem:<22} {result['status']:<18} degraded={result['degraded']!s:<5} cited={cited}")
