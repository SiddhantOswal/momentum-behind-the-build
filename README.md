# Momentum | Behind the Build

**The problem, engineering, evidence, and decisions behind Momentum.**

*A public technical companion to Team Nucleas's AI Builder Cup 2026 submission.*

[**Explore the Knowledge Bank**](https://siddhantoswal.github.io/momentum-behind-the-build/) · [Live Application](https://momentum-ai.cloud.run/) · [Source Code](https://github.com/SiddhantOswal/Momentum) · [Share Feedback](https://forms.gle/4NWFdb8USJopqPwV7)

---

## What is Momentum?

Momentum is a **supervised, AI-assisted production intelligence platform** focused initially on corrugated packaging manufacturing.

It helps production teams review purchase orders, evaluate defect risks, compare machine-setting alternatives, and prepare recommendations for supervisor approval before production begins.

The idea emerged from real corrugation operations, where production inefficiencies can increase manufacturing costs and reduce profit margins even when finished products remain sellable.

**Problem Statement:** Manufacturing: Intelligent Operations & Industrial Efficiency  
**Submission Category:** Sustainability  
**Team:** Nucleas - 
**Leader:** Siddhant Oswal & 
**Teammate:** Om Jain

## How Momentum Works

1. **Review:** Gemini extracts order information from an approved purchase order.
2. **Confirm:** The application validates catalog details and operators confirm production conditions.
3. **Evaluate:** Five BigQuery ML models estimate warp, delamination, strength, print, and crack risks.
4. **Optimize:** A bounded numerical search compares permitted machine-setting alternatives and modeled cost and quality trade-offs.
5. **Explain:** Gemini provides evidence-based explanations for the recommendation.
6. **Approve:** The recommendation remains a draft until supervisor approval, after which the PDF job card is stored and retrievable.

Momentum supports industrial decision-making. It does not autonomously control production machinery.

## Explore the Knowledge Bank

The public documentation provides a detailed technical reference covering:

- **The Manufacturing Problem:** Production complexity, operating costs, resource inefficiencies, and the impact on margins.
- **Our Journey:** How real factory experience informed the problem and solution.
- **Product Walkthrough:** New Lot, Defect Check, and Impact workspaces.
- **Technical Architecture:** Vertex AI Gemini, BigQuery, BigQuery ML, Cloud Run, Cloud Storage, and Firestore.
- **AI and Optimization:** Defect-risk estimation, permitted setting comparisons, explanations, and approval controls.
- **Implementation Evidence:** Prototype screenshots, documented tests, stored records, and reference results.
- **Responsible Use:** Human supervision, known limitations, operational safeguards, and validation requirements.
- **Future Development:** Plant validation, configurable deployment, and opportunities for industrial expansion.
- **Technical FAQs:** Detailed answers about system architecture, AI models, reliability, manufacturing economics, and product decisions.

Read the complete documentation on the [**Momentum Knowledge Bank**](https://siddhantoswal.github.io/momentum-behind-the-build/).

## Reference Result

For the documented PKBX0041 production reference case, Momentum compared:

| Metric | Entered Setup | Recommended Setup |
|---|---:|---:|
| Predicted scrap quantity | 100.4 kg | 83.0 kg |
| Predicted scrap cost | ₹5,351 | ₹4,426 |

**Estimated difference: 17.4 kg and ₹925 for the reference lot.**

These figures are model-based estimates, not measured factory savings or guaranteed production outcomes.

## Technology and Validation

The Momentum application combines Gemini's language capabilities with BigQuery ML predictions, bounded numerical comparisons, persistent storage, and supervisor approval.

The prototype has demonstrated a working production-preparation and approval workflow. However, predictive-model reliability across real factory conditions and realized financial impact require further validation.

The documented training history is modeled using a real 117-item plant catalog. The independent September holdout did not meet the recorded thresholds for four of the five defect models. Recommendations therefore remain supervised estimates.

See the [application's repository guide](https://github.com/SiddhantOswal/Momentum/blob/main/docs/README.md) for implementation details and operating limitations.

## About This Repository

This repository hosts the public, read-only technical knowledge bank. It is separate from the main Momentum application.

| File or Directory | Purpose |
|---|---|
| `index.html` | Responsive public website |
| `CONTENT.md` | Complete technical documentation and FAQs |
| `images/` | Screenshots, architecture diagrams, and evidence |
| `build_static.py` | Optional static-site generation utility |
| `PROMPT_FOR_GOOGLE_AI_STUDIO.md` | Optional AI-assisted design instructions |
| `README_PUBLISH.md` | Publishing and maintenance instructions |

The site is deployed using GitHub Pages. It does not require user registration, paid AI calls, or a backend service.

Updates to the published website can be committed to the `main` branch. When editing `CONTENT.md`, regenerate or update `index.html` as well.

## Feedback

We welcome technical feedback, suggestions, and constructive criticism.

[**Share feedback on Momentum**](https://forms.gle/4NWFdb8USJopqPwV7)

---

**Team Nucleas | AI Builder Cup 2026 — JAPAC**

*Building practical AI-assisted intelligence for better industrial decisions.*

This documentation describes a supervised prototype and its recorded evidence, not certified autonomous manufacturing performance.
