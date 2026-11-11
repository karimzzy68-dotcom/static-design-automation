# Static design production

`CREATIVE-STANDARDS.md` is the governing finish and copy standard for future work. New batches use production_standard=2. Existing outputs retain their original review status; the latest Rockettes collection is an automation baseline, not an example certified to the raised standard.

## Intake and evidence

One compact intake: brand and URL, product image(s), audience/use case, offer/CTA, number of designs, language and placements. Defaults: English, 4:5 feed, distinct concepts rather than resizes. Confirm these as assumptions in the brief; user corrections override them. Product photos and URL are required for the requested brand workflow, unless the user explicitly wants a concept without a live product page.

Inspect the page and supplied photos. Save a dated page screenshot and notes in `research/landing-page/`. Record facts separately from interpretations. Price, ingredient, mechanism, shipping, guarantee and testimonial claims need a source. Use real customer quotes only with their provenance. Do not invent discounts, endorsements, competitor numbers or results. Mark uncertain claims and omit them from copy until resolved.

## Visual research

Search the product category on Pinterest, public ad libraries, brand sites or editorial/product photography sources when it improves the brief. Pinterest login/access failure is a recoverable research limitation; use accessible sources and record the limitation. Save useful screenshots locally under the product's `references/research/`, with URL, date, category, source owner if known, and why it is useful. Do not report a URL-only reference as a screenshot. Do not reuse third-party images as production assets without rights. Study composition, lighting, hierarchy, palette, whitespace and copy density; create original executions rather than cloning another brand's finished ad.

For each direction, write what works, what clashes with this brand, and what to borrow. Select a coherent brand treatment, with controlled variation across the batch. Avoid default generic gradients, excessive badges, tiny text and repeated product-on-pedestal layouts unless the concept calls for them.

## Concept planning

Before preparing any version-2 concept, choose direct or indirect marketing, author the buyer insight, promise, objection, proof/reason, offer framing and curiosity payoff. Draft five distinct hooks; select one with a reason and complete the named copy preflight. Write the image copy and caption as one argument or narrative. Inspect the actual reference and author the grid, typography, spacing, photography, product integration and carousel continuity in design_spec. Use templates/concept.json. Copy review scores must reach 4 before generation; weak writing is rewritten first. For unspecified multi-concept requests, plan roughly half of each marketing route as an adjustable assumption, not an inflexible rule for every carousel.

Start with 5–10 strong concepts, review actual outputs, then expand the directions that suit the product. Pilot review is an agent quality decision and does not require a new user approval unless the user requested one. A 100–150-design request can proceed in waves of 10–15 to preserve quality and recover from quota interruptions. Never promise that provider quota allows 150 generations in a single session.

Useful concept families: single-benefit hero, problem/solution, mechanism explanation, use occasion, ingredient/material story, verified objection answer, authentic review, documented comparison, real offer and editorial product detail. These are options, not a mandatory list. Omit evidence-dependent formats when proof is absent. Use multiple audiences and awareness levels only where they fit the brief.

Choose a production treatment appropriate to the idea: graphic layout, polished photography, or believable native/creator-style imagery. A request for excellent design should not force every ad into a luxury product poster. Buyer relevance, clear communication and deliberate craft apply to all three treatments.

For 100 concepts, a starting plan could be 10 relevant message angles × 5 composition treatments × 2 art directions. For 150, 10 × 5 × 3. This is capacity planning, not permission to fill a grid mechanically. Every selected combination needs a specific reason to exist. A variation should meaningfully change message or visual narrative. Palette swaps and crops are exports, not new concepts.

Each concept record needs: audience, awareness, angle, evidence IDs, exact headline/body/CTA, composition, product scale/position, palette, typography, lighting, background, reference roles and target dimensions. Set one focal point and clear reading order. Keep headlines brief enough for mobile viewing, but let product evidence dictate copy length. Use whitespace deliberately and maintain recognizable brand identity.

Also author one primary creative goal, product category, buyer desire, concept family, independent scene, primary/caption copy and a creative hypothesis. One ad should do one main job, chosen for one buyer at a particular awareness level. Product identity references do not lock the hands, action, background or composition. Check the set for narrative/scene repetition before generating. If reusing a scene for a deliberate messaging test, record the variation rationale and treat it as a test variation rather than claiming broad visual diversity.

## Generation

Capability-check the current agent's image generator and reference attachment mechanism. Preserve the real packaging, logo, shape, colors and product proportions. Attach actual originals and any relevant style references with distinct roles. Write one finished ad prompt per concept and format. Prompts must specify exact copy, composition and identity requirements, not merely 'make a high-end ad'. Save the prompt before starting the job and save its returned job ID immediately.

For predictable typography or a provider that mangles text, generate the scene and use an editable local layout for exact text. Use an image-editing tool for raster changes; preserve original outputs. Export requested dimensions and retain editable sources when produced. Do not silently switch tools that require a new account or paid service. Record costs only when known, never guessed.

## Quality review and delivery

Version-2 acceptance additionally requires designer_polish and copy_strength >=4, plus concrete reference_comparison, copy_review and marketing_route_review notes. Review optical typography, spacing rhythm, cohesive series, meaningful icons, believable physical imagery and a persuasive purpose beyond formatting. Do not infer polished finish from readable text or correct dimensions. Compare actual source references and actual outputs; never auto-fill passing scores. Direct and indirect creatives are assessed against their own jobs. The queue validates records; the agent must make the actual taste and copy decisions.

Inspect every final at full size and at roughly phone-feed size. Review product/brand fidelity, copy spelling and exactness, supported claims, hierarchy/readability, deliberate art direction, artifacts, contrast and placement fit. Reject distorted packaging, wrong logos, invented proof, unreadable text or clipping regardless of overall beauty. Store a QA record with criterion scores and concrete fixes. A useful internal target is at least 4/5 for every criterion; this is an editorial standard, not a prediction of conversions.

Before visual acceptance, evaluate category clarity, buyer motivation, distinction from other concepts, and message match to the landing page. Purposeful curiosity may use the image and primary text together to establish the category, but a vague format statement is not enough. A technically polished image that fails these strategy criteria must be revised.

Repair failed work with targeted changes. After two unsuccessful fixes on the same concept, try a different composition or record it as blocked; do not loop indefinitely. Inspect the repaired image again. Preserve rejected files for diagnosis outside the final folder.

Build a local gallery/contact sheet of passed designs with IDs and links to full-size files. Deliver actual finals, manifest, prompts and any editable sources. Report finished, failed and pending counts separately. Performance can be learned only from real testing; save future CTR/CPC/CPA/ROAS evidence separately and use it to inform new batches.

## Handoff

Before switching agents, save all in-flight job IDs and statuses, brief decisions, assets, references and QA notes. Update `state/workspace.json` and `HANDOFF.md`; release the batch lock. The next agent checks the provider's existing jobs before retrying pending submissions. A stale lock is investigated rather than automatically deleted.
