---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [feature-importance, aggregate, individual, global, local]
---

# Feature Importance — Aggregate vs Individual

Two perspectives on which features matter: aggregate (overall model) vs individual (single prediction).

## Definition

| View | What it measures | Use case |
|------|------------------|---------|
| **Aggregate (global)** | Which features matter overall | Model auditing, feature selection |
| **Individual (local)** | Why this specific prediction was made | Per-case explanation, debugging |

## Aggregate Feature Importance

- "Across all predictions, which features contributed most?"
- SHAP: `shap.summary_plot(shap_values, X)` — shows global importance
- Azure ML: Permutation Feature Importance component
- Use for: identifying which features to engineer, detecting leakage, model comparison

## Individual Feature Importance

- "For this specific customer/transaction, why did the model predict X?"
- SHAP: `shap.force_plot(explainer.expected_value, shap_values[i], X_test[i])`
- Azure ML: Explain Model with individual explanations
- Use for: debugging specific predictions, investigating anomalies, regulatory explanation

## Key Points

- Aggregate importance can mask conflicting individual effects (a feature helps for some cases, hurts for others)
- Always check both aggregate and individual explanations for a complete picture
- Azure ML Designer has both views: the "Global explanations" tab vs per-row explanations

## Related

- [[explain-black-box-models]]
- [[feature-engineering-versus-selection-versus-importance]]
