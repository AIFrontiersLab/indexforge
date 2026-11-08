# Fallback Handler

Restores a safe prior-score ordering when an upstream stage degraded.

| Property | Value |
|---|---|
| Stage name | `fallback_handler` |
| Role | `fallback` |
| Interface | `process(ctx) -> None` |
| Critical | No. A failure degrades the run and downstream fallback restores a safe ordering. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `FallbackHandlerService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Restores a safe prior-score ordering when an upstream stage degraded.

See also [`docs/components/fallback_handler.md`](../../../../docs/components/fallback_handler.md).
