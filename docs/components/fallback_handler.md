# Fallback Handler

Restores a safe prior-score ordering when an upstream stage degraded.

| Property | Value |
|---|---|
| Stage | `fallback_handler` |
| Role | `fallback` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/reranking_gateway/components/fallback_handler/` |
| Tests | `tests/unit/components/test_component_fallback_handler.py` |

## Behaviour

Restores a safe prior-score ordering when an upstream stage degraded.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Ordering is preserved or intentionally changed per role.

## On failure

Run degrades; ordering from the last healthy stage is kept.

## Metrics

- `component_fallback_handler_runs_total`
- `component_fallback_handler_candidates_out` (histogram)
- `component_fallback_handler_removed_total`
