---
name: render-to-reality
description: Preserve an approved interior design when converting dream renders into dimensioned, costed, product-specific render packages. Use for interior implementation renders, Blender-to-image handoffs and visual/budget audits; not for unconstrained creative concepts.
---

# Render to Reality

Work from the user's latest approved visual intent toward a buildable equivalent. A cheaper, simpler or incomplete model is not automatically the authoritative design. This skill is model-independent: Claude, Astra or another operator must read it and the relevant project evidence. It does not grant access, purchasing, messaging or publishing permission. Explicit user instructions take precedence.

For Kyoto Ink, first read [the project lessons](references/kyoto-ink-lessons.md). Treat its numbers as dated observations, not immutable specifications. Resolve the latest project revision before changing anything. Never roll back newer work to a bundled snapshot.

## 1. Resolve evidence by subject

Do not give one reference blanket priority over every other reference.

| Subject | Primary evidence |
|---|---|
| Existing architecture, opening direction, services | Verified site survey and authoritative plans; record conflicts with photos/model |
| Desired visible composition | Owner-selected target images and explicit decisions |
| Product size and identity | Exact manufacturer variant, dimensional drawing and product photographs |
| Custom furniture | Approved design intent translated into measured drawings, materials and hardware |
| Cost | Current live register and attributable price/quote, including unresolved costs |
| Camera | Actual source camera transform, lens, sensor, shift, aspect and reference image |
| Existing finishes and view | Site photographs; match their role without borrowing their camera |
| Atmosphere | Original creative prompt and target lighting/photographic character |

A render is not dimensional evidence. A Blender proxy is not a validated product or a decision overriding the target. A generated finish is not a selected material sample.

## 2. Resolve differences before polishing

Make a target-to-implementation ledger for every important visible element:
`element ID | target feature | exact SKU/custom structure | dimensions/source | finish/code | drawing revision | model object | cost row/status | visual difference | reason | approval/open item`.

Classify the reason for each difference: demonstrated physical constraint, cost alternative, manufacturer difference, missing model detail, or generation error. Do not turn the last two into accepted design compromises.

Before shortening a media wall, removing a reveal, lowering a curtain or replacing a finish:
- inspect actual geometry, installation and services;
- test whether the intended detail fits;
- develop a buildable proposal retaining the intended silhouette and proportions;
- price any genuine alternative and show the visual consequence.

Do not assert that the target is unbuildable without evidence. Do not approve significant changes or a higher budget for the owner. Continue independent design work while external measurements/samples remain open.

## 3. Complete the visible scene in the model

Before an implementation pilot, inventory the view: furniture, working front joints, art, material texture, lamps, profiles, rails, curtains, rug, cushions, throw, ceramics/books/plants, exterior and existing threshold. Every item must be modelled, explicitly excluded by the user, or visibly tracked as unresolved.

- Keep designed decorative layers. Do not use blanket instructions such as “no curtains or ornaments” to conceal incomplete modelling.
- Model the real fixture at its documented electrical point. A ceiling point and a fixture are different things.
- Trace light to a physical fitting/profile, supply and accessible driver. Do not add luminous seams to make the image attractive.
- Show chairs in a plausible tucked resting position for the hero image, based on seat/arm/table/base interference. Keep a separate withdrawn-use check. An arbitrary translation is not a clearance test.
- Preserve exact product hand, module arrangement and one transform across views. Softness, seams and curved shells need product references; dimensioned cuboids are insufficient for product identity.
- Resolve curtain height against actual service access and fixing conditions. Do not lower the rail by habit or assume ceiling fixing is possible.
- Show print as print and shallow substrate as shallow substrate. Do not let procedural noise imply stone, relief or expensive finish absent from the specification.

Keep technical studio illumination out of the proposed installed-light specification. A native control may use technical light, but label it accordingly.

## 4. Reconcile the cost before making coverage claims

Read the live workbook before editing; preserve manual changes. Bind each visible purchase/custom item to one summable row. Distinguish verified webshop price, written quote and estimate. Include delivery, installation, supports, electrical equipment and unresolved allowances.

Do not assume cushions, a throw, bulbs or mounting parts are included with the main product. Do not double-count package and components. Do not count an alternative in the selected total. Show realistic unknown-cost ranges.

Update and verify the live register when the task includes cost reconciliation. If a separate delta is all that has been prepared, explicitly state it is NOT yet integrated; never advertise that image as fully reconciled. A better render does not prove budget compliance. Keep the owner's reserve separate.

Answer “is everything real and in budget?” with an evidence-based breakdown:
1. exact selected product and verified variant;
2. custom design with cost estimate/quote;
3. provisional design or unselected product;
4. generated embellishment absent from the model/register.
Only claim full coverage if category4 is empty and remaining categories are accurately disclosed. Do not call an estimated custom design a purchased or fixed-price product.

## 5. Establish a comparable rendering setup

Read the actual original full prompt, not just its STYLE section. Record attachment names and their roles. Preserve original composition, photographic quality, mood and material guidance while replacing only reconciled design content.

Compare numeric camera parameters and projected landmarks. Matching names, lens or eye height alone is insufficient. Matching Blender cameras does not prove generated images retained projection. If a later audit disproves a suspected camera mismatch, correct the explanation.

Use the completed native model render as geometry evidence, target image as appearance intent, product photos as form evidence, and site photos as existing-finish evidence. Do not lock a known-incomplete model “pixel-for-pixel” and expect missing design to appear. Do not use the prettier target to override measured architecture.

Record actual generation tool/mode and settings exposed by it. Do not infer model/version/seed from the chat title or “Astra” label. Do not promise an identical backend when unknown.

## 6. Pilot, inspect, correct, then release

Unless the user asks otherwise, make one pilot before expanding the series. Inspect the generated result against the native control, target, product photos and ledger:
- architecture, window divisions, threshold, camera landmarks;
- product silhouette, hand, scale, module count, seams, chair orientation;
- custom front grid, reveal width, artwork continuity and support thickness;
- curtain position, fixtures, light origins, textile/decor completeness;
- invented legs, objects, lighting, panorama or material upgrades;
- all cost references and remaining approval conditions.

Correct geometry/material/staging errors in the model first. Use a narrowly targeted image retry for generation drift; inspect it again. Do not describe an attempted edit as successful without seeing the result. If repeated drift remains, stop batch production and use a deterministic native render or explicitly labelled concept study; continue repairable model work. Do not consume repeated generations to conceal an unresolved source error.

Use explicit release labels:
- `TECHNICAL_CONTROL`: actual model projection, not necessarily photographic finish.
- `CONDITIONAL_DESIGN_RENDER`: useful appearance study with named unresolved items.
- `RECONCILED_IMPLEMENTATION_RENDER`: visible identities, drawings/model and current costs reconciled within stated tolerances; not a substitute for trade/site approval.

No percentage match, full PASS, manufacturing approval or budget guarantee without a defined test and evidence. Unresolved external facts need an owner/next step, not a blanket halt to other work.

## 7. Deliver a reusable evidence package

Save actual images, actual prompts, input roles/hashes, camera provenance, model revision, drawings/material references, ledger and image-specific audit. Include a simple target/native/final comparison. State what was actually changed, verified and left open. Preserve prior versions.

When repository saving is authorized, commit to the approved branch, preserve newer work, and read back the remote head and important files. Otherwise provide a local package. A file being in a repository does not mean another chat automatically loaded or followed it: instruct that chat to read the skill and source evidence explicitly.
