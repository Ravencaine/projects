---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [feature-engineering, feature-selection, feature-importance, ml-concepts]
---

# Feature Engineering vs Feature Selection vs Feature Importance

Three distinct stages of working with features in an ML pipeline.

## Definitions

| Concept | Stage | Question it answers |
|---------|-------|-------------------|
| **Feature Engineering** | Pre-processing | How do I create new useful features from raw data? |
| **Feature Selection** | Training | Which features should I include in my model? |
| **Feature Importance** | Post-training | Which features contributed most to the model's predictions? |

## Feature Engineering

Creating new features from raw data that improve model performance:

- **Derive**: extract year, month, day from a date column
- **Combine**: create ratio features (revenue / employees = revenue-per-employee)
- **Encode**: one-hot encode categorical variables
- **Binning**: convert continuous age to age groups
- **Interaction**: create product of two features (age × income)

## Feature Selection

Choosing which features to include — removing noise and redundant features:

- **Filter methods**: correlation, chi-squared, mutual information
- **Wrapper methods**: recursive feature elimination (RFE)
- **Embedded methods**: L1 regularisation (Lasso) — sets irrelevant feature coefficients to zero
- **Why**: reduces overfitting, improves interpretability, reduces training time

## Feature Importance

Quantifying each feature's contribution after model training:

- **Tree-based models**: built-in importance (Gini importance)
- **Linear models**: coefficient magnitude
- **SHAP**: game-theoretic per-feature contribution
- **Permutation importance**: accuracy drop when feature is shuffled

## Pipeline Order

```
Raw Data → Feature Engineering → Feature Selection → Train Model → Feature Importance
```

## Related

- [[data-science-process-five-phases]]
- [[feature-importance-aggregate-versus-individual]]
- [[explain-black-box-models]]
