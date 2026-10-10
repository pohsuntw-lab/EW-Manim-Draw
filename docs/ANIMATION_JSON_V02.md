# Animation JSON v0.2

JSON is the authoritative interchange format for mobile and desktop. The validated example is `examples/simple_flow.json`.

Required: `schema_version: "0.2"`, `nodes`, `timeline`. Optional: `title`, `locale`, `edges`, `layout`, `output` (defaults supplied by validator but should be explicit in exports).

Timeline kinds: `appear` (node), `draw_edge` (edge ID), `highlight` (node), `wait` (no target). Durations in seconds; events play sequentially.

Current renderer supports up to 8 nodes, forward left-to-right edges, and horizontal layout. Each output requests only a preference, not a guarantee of successful rendering.

Security: validated declarative inputs only, no Python execution from JSON. Keep original source files and report actual artifact creation truthfully.

Next: add actual PNG/GIF export pipeline, environment diagnostics, brand asset upload and end-to-end rendering tests.
