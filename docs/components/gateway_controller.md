# Gateway Controller

Validates, normalises, de-duplicates, and bounds the incoming candidate set.

| Property | Value |
|---|---|
| Stage | `gateway_controller` |
| Role | `ingest` |
| Interface | `REST API /rerank` |
| Critical | yes |
| Source | `src/reranking_gateway/components/gateway_controller/` |
| Tests | `tests/unit/components/test_component_gateway_controller.py` |

## Behaviour

Validates, normalises, de-duplicates, and bounds the incoming candidate set.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- May introduce new candidate ids.
- Ordering is preserved or intentionally changed per role.

## On failure

Run fails; the request never reaches retrieval.

## Metrics

- `component_gateway_controller_runs_total`
- `component_gateway_controller_candidates_out` (histogram)
- `component_gateway_controller_removed_total`
