---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [explainability, shah, mimic, feature-permutation, black-box, interpretability]
---

# Explain Black-Box Models — SHAP, Mimic, Feature Permutation

Post-hoc techniques for explaining opaque ML models that don't expose their reasoning directly.

## Purpose

Black-box models (random forests, gradient boosting, neural networks) are more accurate but opaque. Explanation techniques approximate how they make decisions.

## Techniques

### SHAP (SHapley Additive exPlanations)

| Property | Value |
|---------|-------|
| Basis | Game theory — Shapley values from cooperative game theory |
| Output | Per-feature contribution to each prediction |
| Advantage | Additive, consistent, grounded in theory |
| Tool | `shap` Python library |

```python
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

### Mimic Explanations

| Property | Value |
|---------|-------|
| Basis | Train a transparent surrogate model (linear regression / decision tree) on the black-box model's predictions |
| Output | A transparent model that approximates the black-box |
| Advantage | Interpretable output (a tree or linear model) |
| Tool | Azure ML Designer → Explain Model component |

### Feature Permutation Importance

| Property | Value |
|---------|-------|
| Basis | Shuffle each feature's values; measure the drop in model accuracy |
| Output | Per-feature importance ranking |
| Advantage | Model-agnostic; works on any black-box model |
| Tool | Azure ML Designer → Permutation Feature Importance component |

## When to Use Each

| Scenario | Technique |
|---------|----------|
| Explain a specific individual prediction | SHAP |
| Explain a model's overall behaviour | Mimic (decision tree surrogate) |
| Rank features by importance | Feature Permutation |
| Regulatory requirement for explainability | Mimic (transparent output) |

## Related

- [[transparent-by-design-algorithms]]
- [[feature-importance-aggregate-versus-individual]]
- [[responsible-ai-six-principles]]
