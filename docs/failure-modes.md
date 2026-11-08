# Failure modes

## From the design specification

- None listed.

## Per stage

| Stage | Role | Behaviour on failure |
|---|---|---|
| `gateway_controller` | `ingest` | Run fails; the request never reaches retrieval. |
| `corpus_retrieval` | `retrieve` | Run degrades; supplied candidates (if any) continue. |
| `metrics_collector` | `enrich` | Run degrades; candidates continue without annotations. |
| `ranking_cache` | `cache` | Run degrades; the request is treated as a cache miss. |
| `reranker_engine` | `score` | Run degrades; fallback restores upstream prior order. |
| `fallback_handler` | `fallback` | Run degrades; ordering from the last healthy stage is kept. |
| `access_policy` | `policy` | Run fails closed: no candidates survive, the run abstains with `policy_unavailable`. |
| `token_budget_governor` | `budget` | Run degrades; the answer stage still applies `top_k`. |
| `answer_assembly` | `answer` | Run fails with `stage_failure:<name>`. |

## Platform

| Condition | Behaviour |
|---|---|
| Bulkhead full | 503 `stage_error` |
| Rate limited | 429 `budget_exceeded` |
| Breaker open | stage reported `degraded` with `circuit_open`; `/readyz` fails |
| Hook raises | captured in `hooks.failures`; run continues |
| Event handler raises | captured in `dead_letters`; run continues |
