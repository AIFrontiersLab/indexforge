# Components (C4 level 3)

| # | Stage | Role | Critical | Source |
|---|---|---|---|---|
| 1 | `gateway_controller` (Gateway Controller) | `ingest` | yes | [component](../components/gateway_controller.md) |
| 2 | `corpus_retrieval` (Corpus Retrieval) | `retrieve` | no | built-in |
| 3 | `metrics_collector` (Metrics Collector) | `enrich` | no | [component](../components/metrics_collector.md) |
| 4 | `ranking_cache` (Ranking Cache) | `cache` | no | [component](../components/ranking_cache.md) |
| 5 | `reranker_engine` (Reranker Engine) | `score` | no | [component](../components/reranker_engine.md) |
| 6 | `fallback_handler` (Fallback Handler) | `fallback` | no | [component](../components/fallback_handler.md) |
| 7 | `access_policy` (Access Policy) | `policy` | yes | built-in |
| 8 | `token_budget_governor` (Token Budget Governor) | `budget` | no | [component](../components/token_budget_governor.md) |
| 9 | `answer_assembly` (Answer Assembly) | `answer` | yes | built-in |

Each concept component follows the same internal layout so reviewers can navigate
any of them blind: `config.py`, `port.py`, `service.py`, `validators.py`, `models.py`,
`metrics.py`, `errors.py`, `adapter.py`.
