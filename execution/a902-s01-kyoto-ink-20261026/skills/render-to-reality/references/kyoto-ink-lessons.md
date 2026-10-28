# Kyoto Ink A-902: observed failures and corrective rules

Evidence date: 2026-10-28. Repository: peterkapusi88-hub/wsg-berendezes.
Authorized execution branch: execution/a902-s01-kyoto-ink-design-to-budget-20261026.
Project folder: execution/a902-s01-kyoto-ink-20261026/.
R09 saved checkpoint: c7dcfdef40f6eb98d010839eed20c93745bfe7bd. Always check for newer work.

This is a failure record, not approval of R09 or a frozen design specification.

| Observed issue | Actual lesson / required next verification |
|---|---|
| Sparse R08 despite rich original prompt | Curtains, cushions, throw, ceramics/books and ML05 were omitted or suppressed. Build the complete designed scene; precision does not require an empty image. |
| Media-wall composition changed | Original text specified3600mm,720mm tower,120mm recessed separating reveal,2400mm four-front low cabinet. R06–R09 used3300mm composition,700mm tower and3300mm five-front low cabinet. These are material design differences, not a validated equivalence. The owner prefers the visible dream wall: reconcile the images, original text and actual wall/installation before finalising any dimensions. |
| Missing intermediate media-wall element | The separating reveal and depth hierarchy must be drawn and modelled as physical details; a generated vertical glow is not a substitute. |
| Suspected camera mismatch | Original correction log was recovered from commit ad291be88b288a4ae78a27cd29b0a85f9aa860dd, file04_renderek/ai_chatgpt/OPUS55_V3_1_60_TESZT/_cam02_korrekcio/vegleges/cam02_korr_log.json. Numeric parameters MATCH R08: location[8.3,4.4,1.55], rotation radians[1.4791,0,0.8577],20mm, sensor36mm AUTO, shift0/0,1600x1000. Do not repeat the disproven camera-mismatch explanation. Generated composition is still unverified. |
| Threshold | Site photo confirms a step. R08–R09 represented100mm provisionally; original creative lock says about150mm. Neither is a verified site measurement. Preserve its presence and resolve height, rather than erase or call either measured. |
| Eamy chairs look wrong | Initial reconstruction used segmented bands. R09 rounded the shell, but generated orientation/form still diverges. Obtain correct front/back reference and manufacturer dimensions; check tucked position against table/base. Moving120mm inward was staging, not a complete fit test. |
| Lennon differs from dream | Both original prompt and register name2380x1800x680mm right-hand Lennon. Do not invent a product substitution explanation. Audit reconstruction, hand, assembly, upholstery/seams, placement and generated drift. Dream is not a certified catalogue rendering either. |
| Curtain low | R09 rail z2.60 under2.90m ceiling was not justified by a completed detail. Determine highest feasible wall/reveal mounting with shutter access and heating/cooling constraints. Do not encode2.60m as a design requirement. |
| Missing/wrong lamp | ML05 in register KI-113:381x84mm, electrical plan x5.619/y6.274. ML04 x8.549/y6.274; old model put Somar at8.25/6.2. R09 corrected the latter. Verify current plan and visible projection, not assumed appearance. |
| TV background texture wrong | Procedural/generated texture was not an approved finish. Develop actual matte paper/textile carrier and print/sample process. Original look has not been proven unbuildable. |
| Coffee tables differ | KI-037 CF-01 and KI-038 ST-01 were custom estimated proposals, not identified ready-made SKUs. R06 sizes700x450x350 and300x300x450mm; original prose dimension ordering is ambiguous. Label axes, match silhouette and detail the substrate/edge. R09 generator invented legs before correction. |
| Terrace boxes | R09 detailed them inside existing envelopes, but no exact outdoor product identity was thereby verified. Jacuzzi remains2200x2200x900mm provisional; its location blocks the view. Do not move/delete it silently, or claim the covered visual proves a selected1.7M product. |
| Budget completeness overstated | R06 total24482890Ft was an estimate, not18M feasibility. R09 added a separate45000Ft cushion/throw allowance (30000–60000 range), yielding24527890Ft forecast, NOT integrated into the live Excel. Do not repeat the old total as complete or add the delta again if subsequently integrated.2M reserve separate. |
| Styling cost | KI-135 included50000Ft for ceramics/books/small plants, not proven free accessories. Audit scope across rooms. Curtain rows KI-040/041/042 and ML05 already existed; don't add them again simply because newly visible in the model. |
| Final generated image | Still includes non-camera-matched skyline, unverified plant illumination and texture/form drift. R09 is CONDITIONAL, not final purchasable truth. |

## Inputs to resolve in this project

- Owner-selected latest target images: R06/targets/ and manifest, plus any subsequently approved replacements.
- Full original prompt supplied by owner; preserve camera/geometry, material, detail/access and photographic sections, not just style DNA.
- R09_living/audit/original_camera_log.json and model_changes.json.
- R09_living/prompts/ACTUAL_IMAGEGEN_PROMPT.txt and TARGETED_CORRECTION.txt; these are diagnostic evidence, not templates to copy unquestioningly.
- outputs/A902_Kyoto_Ink_elo_regiszter.xlsx and latest actual cost/drawing/model revisions.
- R09_living/00_OLVASD_EL.txt: unresolved issues and unintegrated45k cost delta.

Desired next outcome: a measured, costed reconstruction of the owner's media-wall composition and complete furnished scene. Do not automatically polish R09 unchanged and call that the desired design.
