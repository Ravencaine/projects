---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: gotcha
tags: [anomaly, correlation, causation, domain-expertise, false-positive]
---

# Anomaly Correlations Require Domain Expertise to Validate

The Anomalies pane's attribution of anomalies to specific dimensions is a statistical correlation — not a causal explanation. Always validate with domain knowledge.

## Expected Behaviour

The Anomalies pane shows "Product Category X contributed most to this spike" — implying Product Category X *caused* the spike.

## Actual Behaviour

The attribution is a statistical correlation. The model found that the spike co-occurred with high values in Product Category X — but this could be coincidence, a shared cause (e.g., summer holiday drove both), or a genuine cause.

## Why It Happens

Anomaly detection models find statistical deviations, not causal mechanisms. The "Explain by" feature shows which dimensions co-occurred with the anomaly, not what *caused* it.

## How to Handle It

- Always validate Anomalies Pane explanations with a domain expert
- Cross-check against known events (holidays, marketing campaigns, outages) before accepting the attribution
- Treat the attribution as a hypothesis for investigation, not a confirmed explanation

## Related

- [[anomalies-pane-explain-with-attributes]]
- [[correlation-does-not-imply-causation]]
- [[anomaly-detection-visual]]
