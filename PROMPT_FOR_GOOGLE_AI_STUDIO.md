# Copy-paste prompt for Google AI Studio Build mode

You are building the public, read-only technical companion for Momentum, an AI Builder Cup 2026 industrial AI hackathon submission. The complete **approved factual content** is in the attached file `CONTENT.md`, and the authentic screenshots and chart references are in `images/`. You may also inspect `index.html`, which is an existing no-backend static reference site in this bundle.

## Objective

Create a polished, usable, accessible, public-facing website named **Momentum | Behind the Build**, using the provided source content instead of inventing any new history, technology, outcome, or customer claim. The result must work without login. It is documentation, **not an AI chatbot** and **not an extension to the production Momentum app**.

## Mandatory source priority

1. `CONTENT.md` is your immediate, comprehensive content specification. Include **every major section, reference table, explicit limitation, FAQ and exact metric**. Do not silently abbreviate or omit inconvenient evidence.
2. `images/` contains authentic screenshots and the selected visual evidence. Reuse the original bytes; do not redraw or regenerate product screenshots.
3. The public project repository and linked guides are secondary verification sources:
   - https://github.com/SiddhantOswal/Momentum
   - https://github.com/SiddhantOswal/Momentum/blob/main/README.md
   - https://github.com/SiddhantOswal/Momentum/blob/main/docs/README.md
   - https://github.com/SiddhantOswal/Momentum/blob/main/config/model-acceptance.json
4. If a source is inaccessible, do not claim to have inspected it. Preserve the documented claim, mark the source URL, and flag the access limitation for maintainer review.
5. Distinguish clearly: **implemented**, **demonstrated**, **modeled**, **validated**, and **planned**. The record contains important limits: factory cost savings are not measured; four model holdout R² results fall below thresholds; the CRACK holdout is negative; physical control and sensors are not implemented; identity is a hackathon demo session.

## Experience and design

- Recreate the polished visual family of the submitted Momentum deck: off-white page; dark navy/charcoal text; restrained forest-teal accents; muted brass/gold for small visual highlights; fine separators; modern typography; generous whitespace.
- Responsive desktop/mobile layouts, clear visible focus indicators, large hit areas and accessible color contrast.
- Desktop: sticky top navigation and an organized documentation sidebar.
- Easy entry: two-minute executive overview, illustrated one-journey product flow, links to product and public repository.
- Deep reading: clearly organized sections, original screenshots, data tables, citations and citations/links to source evidence.
- Interactions: instant local search across headings and body; anchored sections; optional FAQ accordions; copyable links; optional image enlargement; clear breadcrumbs or progress state. Use lightweight functionality only; no runtime Gemini calls.
- Maintain readability at standard laptop PDF/web viewing sizes. Do not include irrelevant animations, generic AI art, fabricated UI images, gratuitous icons or dense futuristic visual effects.
- Honor prefers-reduced-motion and keyboard navigation.

## Content architecture

Preserve these source sections in the order given or a carefully justified navigation grouping:

1. Start here: two-minute overview and evidence status.
2. The real manufacturing problem, including cost erosion on **sellable** boxes, not scrap alone.
3. Origin of the idea through actual corrugated-factory context and Team Nucleas founders.
4. Implemented product: New Lot, Defect Check, Impact and the full PO → approval → stored card workflow.
5. Reference result PKBX0041 with exact material, quantity, modeled kg/₹ comparison and three specific setting changes.
6. Five BigQuery ML defect models, numeric candidate search, constraint bounds, trade-offs and evidence explanations.
7. Google Cloud architecture and measured demonstration activity.
8. Responsible use, authorization boundaries, data access, uncertainty, quotas, privacy and failure conditions.
9. Tests, approval/PDF retrieval, retained failures and model-validation results including the complete September holdout table.
10. Workflow USP without fabricated competitor benchmarks.
11. Sustainability as a proposed measurable outcome, without claimed field reductions.
12. Validation-first rollout and realistic plant-to-plant scaling.
13. Authentic screenshots, diagrams and captions.
14. All original FAQs, glossary and source register.

Every technical chart or numerical outcome must be accompanied by a short human-readable takeaway and a qualifier where appropriate.

## Prohibited claims

Do not assert that Momentum is autonomous; controls machines; uses continuous live telemetry; has achieved real scrap, carbon or profit reduction; is independently certified; uses unbounded PO uploads; identifies operators via production identity; or meets model performance thresholds on the September holdout other than PRINT. Do not replace the currently documented BigQuery SQL candidate search with OR-Tools unless verifiable current implementation evidence is supplied.

Do not turn the reference `₹925` simulated scrap-cost reduction into annual profit, guaranteed savings, customer ROI or measured economic impact. Do not treat 43 passing software checks as predictive-model accuracy. Do not hide the two recorded failures or the model holdout results.

## Publication and isolation

- This must be a static, read-only site with **no backend requirement, no API key and no pay-per-view LLM calls**.
- The user should be able to export the result as HTML/CSS/JS, or a Vite/React build that produces static deployable files.
- The site must be hosted separately from the application and must not push changes into `SiddhantOswal/Momentum` or alter its `main` branch.
- Prefer creating a new GitHub repository named `momentum-behind-the-build` and publishing with GitHub Pages, or use a standard public deployment through Google AI Studio if that results in a no-login read-only URL.
- Ensure resources are relative-path-safe for a project subpath under GitHub Pages (`/momentum-behind-the-build/`).
- Include a discrete optional feedback link to https://forms.gle/4NWFdb8USJopqPwV7 and prominent product/repository links.
- Leave the demo-video link out until a real public URL is supplied. Never invent a demo video address.

## Validation before finalizing

1. All content sections and FAQs have been preserved, and screenshot asset paths resolve.
2. Numeric facts match the exact `CONTENT.md` values and their evidence qualifications.
3. Open all navigation, search, image viewer, tables, FAQ interactions and responsive layouts on desktop and mobile.
4. Confirm anonymous view works without authentication and without user-edit controls.
5. Check external URLs: Momentum application, GitHub repository, model evidence and feedback form.
6. No content overflow, clipped captions, broken links or missing images.
7. No user credentials, API keys, project secrets or private factory records in generated files.
8. Provide a downloadable ZIP of the final site and give exact independent hosting instructions.

**Deliver a finished public documentation website; do not return only wireframes or instructions.** When information is missing, keep the documented facts and label what must be verified rather than hallucinating a resolution.
