# Metrics Collector

Annotates candidates with structural features and collapses exact duplicates.

| Property | Value |
|---|---|
| Stage name | `metrics_collector` |
| Role | `enrich` |
| Interface | `process(ctx) -> None` |
| Critical | No. A failure degrades the run and downstream fallback restores a safe ordering. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `MetricsCollectorService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Annotates candidates with structural features and collapses exact duplicates.

See also [`docs/components/metrics_collector.md`](../../../../docs/components/metrics_collector.md).
