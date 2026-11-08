# Reranker Engine

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage | `reranker_engine` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/reranking_gateway/components/reranker_engine/` |
| Tests | `tests/unit/components/test_component_reranker_engine.py` |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Output is sorted by descending score.

## On failure

Run degrades; fallback restores upstream prior order.

## Metrics

- `component_reranker_engine_runs_total`
- `component_reranker_engine_candidates_out` (histogram)
- `component_reranker_engine_removed_total`
