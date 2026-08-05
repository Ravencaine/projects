---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [responsible-ai, principles, fairness, transparency, privacy, accountability]
---

# Responsible AI — Six Principles

Microsoft's six principles for building and deploying AI systems ethically.

## The Six Principles

| Principle | What it means |
|-----------|---------------|
| **Fairness** | AI should treat all groups equitably — not systematically disadvantage any group |
| **Reliability & Safety** | AI should perform reliably and safely under adversarial conditions |
| **Privacy & Security** | AI should respect data privacy and protect against unauthorised access |
| **Inclusiveness** | AI should serve all people — accessible design for disability, diverse cultures |
| **Transparency** | AI decisions should be explainable — users should understand why an outcome occurred |
| **Accountability** | Humans should be accountable for AI outcomes — clear ownership of decisions |

## Key Points

- These principles are not optional — they are prerequisites for trustworthy AI
- Each principle has practical techniques: Fairlearn for fairness, SHAP for transparency, PII detection for privacy
- The analyst's role is to apply these principles at every stage: data collection, model building, deployment, monitoring
- Responsible AI is not a post-processing step — it must be built in from the start

## Application in Power BI / Azure ML

- **Fairness**: Fairlearn (fairness assessment), balanced datasets
- **Transparency**: SHAP, Feature Importance, explainable algorithms
- **Privacy**: PII Detection, Differential Privacy, remove PII before processing
- **Accountability**: Document model lineage, evaluation metrics, and known limitations

## Related

- [[remove-pii-from-datasets]]
- [[fair-models-identify-mitigate-unfairness]]
- [[explain-black-box-models]]
