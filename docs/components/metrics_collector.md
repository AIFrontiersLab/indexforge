# Metrics Collector

Annotates candidates with structural features and collapses exact duplicates.

| Property | Value |
|---|---|
| Stage | `metrics_collector` |
| Role | `enrich` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/reranking_gateway/components/metrics_collector/` |
| Tests | `tests/unit/components/test_component_metrics_collector.py` |

## Behaviour

Annotates candidates with structural features and collapses exact duplicates.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Ordering is preserved or intentionally changed per role.

## On failure

Run degrades; candidates continue without annotations.

## Metrics

- `component_metrics_collector_runs_total`
- `component_metrics_collector_candidates_out` (histogram)
- `component_metrics_collector_removed_total`
