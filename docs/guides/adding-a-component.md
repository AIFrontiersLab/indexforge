# Adding a concept component

Copy any folder under `src/reranking_gateway/components/`, rename the classes, choose a role, and
add it to `components/__init__.py` and `stage_catalog.COMPONENTS`. The component test
template in `tests/unit/components/` shows the minimum contract coverage.
