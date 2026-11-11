# Creative standard · version 2

User direction, October 8, 2026: the current Rockettes collection is acceptable as an automation baseline. Future work must look more polished and deliberately designed, with excellent writing and a considered mix of direct and indirect marketing. This update authorizes system changes only; do not generate or revise images until a new creative request arrives.

## One buyer, one selling idea

Choose the buyer's situation, desire, belief and objection before the layout. A demographic label alone is not an insight. State what the product is and the one relevant, supportable reason to care. A format fact can support a benefit; it should not replace the selling idea in every ad. A beautiful product image with interchangeable motivational copy is insufficient.

## Two marketing routes

| Route | Primary job | Structure | Next step | Reject |
|---|---|---|---|---|
| Direct | Help a ready buyer decide | Specific desire or problem → relevant product/benefit → supported proof or practical reason → real offer/value → clear action | Purchase, compare packages, explore the trial, or another exact destination | Vague slogans; unexplained price; badges instead of proof; invented urgency |
| Indirect | Earn attention, trust or consideration | Recognizable situation, useful question or story → genuine insight/payoff → relevant product bridge | Read, save, swipe, learn more, or a restrained product invitation | Clickbait with no payoff; disguised testimonials; a hard sell on every frame; education unrelated to the product |

Choose route from awareness and purpose, not appearance. A clean poster can be indirect; a native photo can sell directly. For an unspecified multi-concept batch, start with roughly half of each and record that as an adjustable assumption. Intentional exceptions need a reason; do not force an equal split within one carousel. Education, story and tips usually start indirectly and may close directly. Reviews/objections can support either route. Save the route, payoff and transition explicitly in each concept.

## Copy standard

Use original writing guided by offer clarity, buyer relevance, specificity and economical persuasion. The user's Alex Hormozi reference means apply these principles, not copy his catchphrases, pretend he wrote the ads, or promise his results.

Use the [Acquisition.com value checklist](https://www.acquisition.com/hubfs/Offer%20Checklists%20-%20PDF%20Downloads/Pricing-Value-Checklist.pdf?hsLang=en) as a planning lens: clarify the desired outcome, strengthen confidence with legitimate evidence, and identify actual reductions in waiting, effort or sacrifice. The checklist is source material, not permission to change prices or make health claims.

1. Research the actual offer and customer language. Separate quoted customer text from original brand copy; keep provenance with every quote.
2. Draft at least five meaningfully different hooks per concept: for example desire, practical problem, objection, useful insight and value. Select for relevance and proof, not the loudest wording. Record why the winner beats the alternatives.
3. Give the reader a concrete reason to care. Replace empty adjectives and generic phrases such as 'unlock confidence', 'elevate your routine' or repeated 'small packet/simple routine' with the buyer's real situation and specific support. Brevity is not a substitute for a selling idea.
4. One main promise, supported by facts. Use outcome wording only to the extent evidence supports it; otherwise sell documented format, discretion, convenience, trial choice or value convincingly. Never imply a performance mechanism through imagery that copy cannot substantiate.
5. Address one real objection. Explain the relevant fact or tradeoff instead of asserting 'no-brainer', 'risk-free', 'works instantly' or 'clinically proven' without evidence.
6. Frame offers clearly: what is included, total price, useful unit economics, applicable shipping and actual guarantee conditions. Proposals for bundles/bonuses/guarantees belong in a separate labeled offer-proposal document; ads use only approved terms. Do not manufacture urgency.
7. Write on-image text and caption together. On-image hierarchy delivers the hook and key support; caption supplies needed context and objections without simply repeating the artwork. Keep language natural, concrete and easy to scan. Do not impose one headline length on every format.
8. For a carousel, map each slide's job and write the whole narrative first. The first frame earns the swipe; each middle frame adds information; the last provides a fitting action. Avoid five unrelated posters, repeated points and premature hard selling.
9. Edit aloud: remove filler, stiff phrasing, empty comparisons, unexplained jargon and duplicated claims. Verify each number and quote. Review emotional relevance as well as grammar.

Before generation, record a named copy review with actual reasons and 0–5 scores for hook strength, buyer relevance, specificity, proof match and route fit. All must reach 4; scoring is editorial judgment, not performance prediction. Rewrite weak copy first.

## Designer-level finish

Before generation author a real design specification. 'High-end', 'premium' and 'like the reference' alone are not specifications.

- Analyze the chosen reference: grid, reading order, type character, spacing, image scale, crop, copy density and why they serve its idea. State the brand adaptation and what must not transfer. Do not inherit source-brand claims or faces.
- Use a deliberate grid, alignment anchors, margins and repeatable spacing rhythm. Resolve optical alignment, line lengths, awkward wraps, widows and kerning. Usually use one or two type families with controlled weights; distinguish headline, support and utility text without indiscriminate bolding.
- Integrate text and image into one composition: intentional crop, natural negative space, believable depth/overlap and controlled contrast. Avoid the default giant headline + hand-held packet + generic pill button in every output. CTA treatment depends on the concept; a text action can be better than a button.
- Keep palette and brand cues coherent. Use accent color selectively; remove decoration, badges, icons and borders that add no meaning. Every icon must match its label. Never leave blank comparison columns or unfinished layout regions.
- Match light, shadows, perspective, foil/fabric texture and physical product scale. Preserve the actual package print. Inspect realistic people at full size: pores, hair, teeth, eyes, nails, fingers, grip and garment texture; avoid waxy faces, repetitive stock-model poses and artificial expressions.
- For polished photographic work, require convincing art direction and retouching restraint. For native work, preserve credible casualness while making framing and reading order intentional. Polish does not mean making every image look like a luxury campaign.
- Establish continuity within a carousel: recurring type scale, margins, palette, navigation and photographic language. Vary slide composition to match its job while maintaining one visual family. A story may change context without changing character identity accidentally.
- Compare the final against the actual reference and the supplied product, not against a vague mental benchmark. At 100% check rendering/text; at phone size check hook, category, support and next action. Inspect the whole sequence and batch for repeated composition and repeated copy.

A technically valid image can still fail. Version-2 QA adds designer_polish and copy_strength to the existing eleven criteria. Require explicit reference comparison, copy review and route review; every criterion must reach 4 with no hard failures. A 4 means deliberately finished and suitable to show the user, not merely 'usable for automation'. Do not auto-fill passing scores. Fix typography/layout/photography or rewrite the concept when needed, then re-inspect the actual output. Preserve rejected versions.

## Shared implementation

New batches record production_standard=2. templates/concept.json records route, copy candidates/review and design specification. templates/qa.json records the stronger review. The queue validates these records before preparation and acceptance; it cannot determine taste or sales performance automatically. Agents remain responsible for honest inspection and editorial judgment.

Existing outputs are preserved with their original review standard. The 35 Rockettes images are an automation baseline, not evidence that the new polish/copy standard has been met. Use a new batch for future creative work. Read this file in Codex and AntiGravity before planning or generation.
