# Momentum | Behind the Build — Static Knowledge Bank

This package is a complete public, read-only technical reference for Momentum, including 6,000+ words of source-grounded documentation, a FAQ, a source register, authentic product screenshots and a ready-to-host static HTML site.

## Files

- `index.html`: finished responsive website; no hosting backend or runtime AI API required.
- `CONTENT.md`: complete plain-English technical knowledge bank. Editable source for Gemini/Claude or any documentation site generator.
- `images/`: actual application images extracted from the approved 25-slide Momentum deck and visual evidence slides.
- `PROMPT_FOR_GOOGLE_AI_STUDIO.md`: copy/paste instructions to regenerate or refine the site from this content in AI Studio Build mode.
- `README_PUBLISH.md`: these instructions.
- `build_static.py`: small optional utility to rebuild `index.html` from `CONTENT.md` (requires Python + mistune). Do not upload API keys or production credentials.

## Recommended: GitHub Pages (no viewer login)

1. Create a **new, separate public repository** called `momentum-behind-the-build`. Do not publish inside or push changes to the existing Momentum application repository.
2. Upload `index.html`, `CONTENT.md` and `images/` to the **root of that new repository**. The build script and AI Studio prompt are optional to publish.
3. Go to `Settings → Pages → Build and deployment`, select `Deploy from a branch`, choose `main` and `/ (root)`.
4. Wait for GitHub Pages to publish the site. A typical URL format is `https://siddhantoswal.github.io/momentum-behind-the-build/`. This is an **example format**, not a verified live URL.
5. Open in a signed-out browser and test navigation, screenshots, citations, source links and mobile layout. Add the final public URL to Slide 24 only when you intentionally decide to change the deck again.

## Optional: refine with Google AI Studio

Open Build mode at https://aistudio.google.com/ and supply `CONTENT.md`, `PROMPT_FOR_GOOGLE_AI_STUDIO.md` and image assets. Ask the model to preserve source claims and create a static site, then download the resulting website ZIP. AI Studio can also publish apps directly to Cloud Run, subject to account eligibility, billing and quota. A pure static GitHub Pages deployment is simpler for this knowledge bank and avoids runtime LLM costs and login friction.

## Before publishing

- Review all factory-origin details for confidential or proprietary information.
- Check the public README and model-acceptance file for current accuracy before sharing.
- The public repo reports a controlled reference journey and modeled history. Do not treat modeled plant data as field measurements.
- Do not publish access credentials or customer POs.
- Feedback form URL: https://forms.gle/4NWFdb8USJopqPwV7.

Content reviewed 17 October 2026. Prepared as an explanation of a supervised prototype, not an independently audited manufacturing case study.
