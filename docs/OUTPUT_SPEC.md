# EW Manim Draw v0.1.0 — Output Contract

## Product
Skill-only, no MCP requirement for v0.1.0. Deliver GIF animation and PNG static diagram. MP4 is excluded from user-facing deliverables and claims.

## Defaults
- 16:9, 1920 × 1080 for PNG; GIF may be scaled down to manage size.
- GIF target 12–15 FPS, optimized palette and reasonable duration/size.
- Languages: English, Traditional Chinese, Simplified Chinese with licensed fonts.
- Flow JSON remains the semantic source of truth.
- Preserve owner-approved original logo, with no regeneration or modification.

## Implementation requirements
- Validate all nodes, edges, ordering and labels before rendering.
- Generate deterministic scene frames using Manim, then encode animated GIF with Pillow (or another separately licensed encoder).
- Export a static PNG independently from the validated scene.
- Do not require an MP4 intermediate for the final workflow.
- Never claim rendering succeeded without inspecting actual output files.
- If the host lacks Manim and required system dependencies, return the validated project and explain that GIF/PNG rendering was not executed.

## Release gate
- Replace or revise the prototype CLI's MP4-only output before declaring GIF/PNG support implemented.
- Add deterministic GIF/PNG export tests, Unicode tests and visual acceptance.
- Audit licenses of Manim, Pillow, fonts and system libraries.
- No MCP deployment or cloud renderer is part of v0.1.0.
