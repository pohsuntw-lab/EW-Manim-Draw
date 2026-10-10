# EW Manim Draw — Runtime Capability Policy

## Product decision (2026-10-10)
Skill-only. No MCP dependency. Never require an iPhone or Android user to install Manim.

## Delivery matrix
- Any supported chat environment: validated flow/animation JSON is the minimum deliverable.
- Runtime with static drawing support: JSON + PNG where actually rendered.
- Runtime with frame animation support: JSON + GIF where actually rendered.
- Desktop/runtime with Manim installed: JSON + supported PNG/GIF/MP4 outputs after actual rendering.
- Runtime without Manim: JSON plus optional desktop installation instructions.

## Required animation JSON fields (future schema version)
- schema_version
- project metadata and locale
- nodes and edges with stable IDs
- layout constraints and reading order
- timeline with target IDs, animation kinds, durations and ordering
- output preferences, aspect ratio and background
- branding asset references (never embed fabricated logos)

The current v0.1.0 example/validator covers only basic nodes and edges. Timeline, layout and export settings are **not implemented yet**. Do not claim complete animation interchange until schema and renderer are upgraded together.

## User-facing rule
No renderer available → return validated JSON. Never claim an MP4/GIF/PNG was generated without an actual artifact. Avoid promises of identical rendering across different Manim versions or fonts.
