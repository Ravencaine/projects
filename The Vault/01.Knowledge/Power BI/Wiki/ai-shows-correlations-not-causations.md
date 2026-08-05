---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: gotcha
tags: [ai, correlation, causation, key-influencers, misleading]
---

# AI Shows Correlations, Not Causations

Power BI AI features — especially Key Influencers and anomaly detection — surface statistical correlations in your data. It is easy to mistake these for causal explanations.

## Expected Behaviour

Key Influencers shows: *"Sales at Store 12 drop 23% during weeks when Employee X is on vacation."*

An analyst might conclude: "Employee X causes sales to drop when they take vacation."

## Actual Behaviour

Employee X works the busiest shifts. When Employee X is absent, the store is simply understaffed during peak hours. The AI correctly identified a correlation — but the cause is staffing levels, not Employee X specifically.

Similarly, Key Influencers may surface *"Sales are 47% higher in stores with 5+ employees"* — this reflects a staffing correlation, not an inherent sales driver.

## Why It Happens

Key Influencers uses regression analysis to rank factors associated with variance in the target metric. It measures *association*, not *mechanism*. The relationship could be:

- A causes B
- B causes A
- A and B are both caused by a third factor (confounding variable)
- Coincidence (especially in small datasets)

Anomaly Detection attributes flagged points to the dimension values present at that moment — again, correlation, not causation.

## How to Handle It

1. **Always validate AI attributions with domain knowledge** before acting on them
2. **Ask "what else could explain this?"** before accepting a Key Influencer result
3. **Check for confounding variables**: e.g., staffing → sales correlation is confounded by store foot traffic
4. **Design controlled experiments** when causation matters (e.g., A/B tests on promotions)
5. **Report AI outputs as "AI-detected correlations"** not causal findings when presenting to stakeholders

## Related

- [[correlation-does-not-imply-causation]] — extended note (Diepeveen 2022)
- [[scatter-plot-trend-line-correlation]] — Diepeveen 2022
- [[anomaly-correlations-require-domain-expertise]] — Diepeveen 2022 gotcha
- [[build-ai-powered-power-bi-dashboard]] — workflow
- [[power-bi-ai-feature-comparison]] — reference
