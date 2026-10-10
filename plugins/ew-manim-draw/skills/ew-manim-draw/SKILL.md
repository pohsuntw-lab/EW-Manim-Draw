---
name: ew-manim-draw
description: Convert natural-language processes and architecture descriptions into validated, deterministic Manim-ready animated flowchart specifications, with bilingual support and strict execution evidence.
---

# EW Manim Draw

## Scope
Help users turn process descriptions, SOPs, architecture notes and flow diagrams into deterministic animated-flow specifications. Never invent missing equipment, functions, transitions, or implementation status.

## Workflow
1. Extract the exact nodes, edges, labels, conditions, and intended sequence.
2. Clarify only essential ambiguity; distinguish factual flow from optional visual suggestions.
3. Produce structured JSON compatible with the repository validator; respect the renderer's current node and layout limits.
4. Validate endpoints, duplicate IDs, layout constraints and Unicode labels.
5. Prepare Manim scenes only through controlled templates; never execute untrusted generated Python.
6. When a Manim runtime is available, render a low-resolution preview, inspect it, then render the approved output.
7. When a runtime is not available, provide the validated source and explicit rendering instructions; never claim an MP4 was rendered.
8. Preserve JSON and source as editable project assets. Clearly distinguish proposed, implemented, tested and deployed capabilities.

## Defaults
Traditional Chinese or English matching user language; 16:9 landscape; light background; navy and blue; large readable typography; avoid dense layouts. Use the approved Embodied Worker logo without modification only when the original asset is present.

## Safety
No shell commands embedded in labels, no arbitrary code execution, no unapproved external uploads, no exposure of private business data. Public rendering requires an isolated runtime, timeouts and resource limits.
