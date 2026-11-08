"""Audit role: append an immutable, redacted record of what the run saw and decided."""

from __future__ import annotations

from reranking_gateway.domain.models import PipelineContext
from reranking_gateway.stages.base import Stage


class AuditStage(Stage):
    role = "audit"

    def process(self, ctx: PipelineContext) -> None:
        req = ctx.request
        record = {
            "run_id": ctx.run_id,
            "at": self.services.clock.now_iso(),
            "stage": self.name,
            "tenant": req.tenant,
            "subject": req.principal.subject,
            "roles": list(req.principal.roles),
            "query_chars": len(req.query),
            "candidate_ids": [c.doc_id for c in ctx.candidates],
            "denied": list(ctx.metadata.get("denied", [])),
            "degraded": ctx.degraded,
        }
        self.services.audit.append(record)
        ctx.decide(self.name, "audited", candidates=len(ctx.candidates))
