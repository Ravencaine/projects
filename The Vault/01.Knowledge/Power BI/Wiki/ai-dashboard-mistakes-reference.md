---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: reference
tags: [ai, mistakes, anti-patterns, performance, power-bi]
---

# AI Dashboard Mistakes Reference

Four high-impact mistakes to avoid when building AI-powered Power BI dashboards.

## Quick Reference

| # | Mistake | Symptom | Fix |
|---|---------|---------|-----|
| 1 | Skipping data modeling | Garbage AI outputs | Spend 60% on model, 40% on AI features |
| 2 | Not validating AI outputs | Misleading insights accepted as fact | Always cross-check with domain knowledge |
| 3 | Using AI for everything | Over-engineered dashboards for simple questions | Use native DAX for SUM/AVG; AI for pattern discovery |
| 4 | Ignoring performance | Slow dashboards on large datasets | Use aggregated tables, import mode, query reduction |

## Mistake 1 — Skipping Data Modeling

**What happens:** AI features are added to a messy model with cryptic column names. Copilot generates wrong measures. Key Influencers finds nothing meaningful.

**Fix:** Spend 60% of project time on the data model before adding any AI feature.

## Mistake 2 — Not Validating AI Outputs

**What happens:** Key Influencers surfaces a statistically significant but practically meaningless correlation. Stakeholders act on it. Nothing improves.

**Fix:** Always validate AI outputs against domain knowledge before presenting or acting on them. AI shows correlations; the analyst provides the explanation.

See: [[ai-shows-correlations-not-causations]]

## Mistake 3 — Using AI for Everything

**What happens:** A Python visual runs a linear regression to calculate what a simple DAX `SUM` could compute in milliseconds.

**When NOT to use AI:**
- Simple aggregations (SUM, AVG, COUNT) → use DAX
- Single-table analysis → use basic visuals
- Highly customised visualisations → build manually

**When to use AI:**
- Pattern discovery in large datasets
- Predictive analytics
- Anomaly detection in time series
- User-driven self-service (Q&A)

## Mistake 4 — Ignoring Performance

**What happens:** AI features slow down the report significantly on datasets with millions of rows.

**Fix:**
- Use aggregated tables for AI visuals (pre-aggregate before passing to AI)
- Enable query reduction in Power BI Service
- Prefer Import mode over DirectQuery where possible
- Schedule Python model retraining off-peak

## Related

- [[build-ai-powered-power-bi-dashboard]] — workflow
- [[ai-shows-correlations-not-causations]] — gotcha
- [[power-bi-ai-feature-comparison]] — reference
