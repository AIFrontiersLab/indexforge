# Gateway Controller

Validates, normalises, de-duplicates, and bounds the incoming candidate set.

| Property | Value |
|---|---|
| Stage name | `gateway_controller` |
| Role | `ingest` |
| Interface | `REST API /rerank` |
| Critical | Yes. A failure stops the run. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `GatewayControllerService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Validates, normalises, de-duplicates, and bounds the incoming candidate set.

See also [`docs/components/gateway_controller.md`](../../../../docs/components/gateway_controller.md).
