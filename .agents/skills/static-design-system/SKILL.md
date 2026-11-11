---
name: static-design-system
description: Create and resume premium static product-ad batches in the shared design automation workspace, preserving brand briefs, product references, prompts, outputs, and quality reviews across Codex and AntiGravity.
---

Use the workspace root containing `tools/design_system.py`. Read its `AGENTS.md`, `WORKFLOW.md`, `state/workspace.json` and `HANDOFF.md` first. Load only the active brand/product files and relevant video lessons.

When showing the design catalogue, include named carousels from `Design References - Carousels/index.html` alongside static concepts in `Design References - Named Library/index.html`. Resolve Carousel 1/2/3 and CR01–CR11 through the saved lookup. Before recreation inspect every selected slide and its source limitations, then adapt the visual sequence to current brand facts and identity. Partial screenshots remain partial; do not invent missing source artwork.

Read `CREATIVE-STANDARDS.md` for version-2 requirements: authored direct/indirect route, five hook candidates and a named copy preflight, concrete designer-level specification, realistic humans, and explicit reference/copy/route comparisons at final QA. New batches enforce these records and the designer_polish/copy_strength criteria. Do not treat passing technical checks as a taste judgment or auto-fill scores. Preserve legacy finals under their original standard. When the user requests workflow updates only, change the shared instructions/templates/tools without producing images.

For a new brand, collect a landing-page URL and product image. Derive audience, benefits, offer and identity from evidence; ask the user for missing business decisions. Save a structured brief, product originals and user references under the product folder using the helper. Research category references when helpful, with screenshots, source URLs and explicit notes about the visual principles being borrowed.

For existing products, reuse the saved brief and references, including user corrections. Plan the requested number of distinct concepts in a resumable manifest. Begin with buyer desire, product category, awareness and selling idea; choose the scene and format to communicate that idea. Write exact copy and art direction per concept before generation. Identity references establish packaging, not a mandatory pose or action. Use `tools/audit_plan.py` to expose missing strategy fields and repeated scenes, then judge the actual visual set. Follow `WORKFLOW.md` for style selection and the distinction between concept counts and format exports. Generate actual assets using available tools, with identity references attached, then inspect them visually. Strategic clarity and relevance must pass alongside visual quality. Record and fix defects. Never fabricate product evidence or performance data.

Use `tools/design_system.py --help` for helper commands. Claim the batch while working; release it at handoff. Record the next action in `HANDOFF.md`. If tools or quota are unavailable, leave a truthful, resumable queue with the actual blocker.
