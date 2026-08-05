---
created: 2026-08-05
updated: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
note_type: atomic
tags: [feature-engineering, anomaly-detection, one-hot-encoding, isolation-forest, tabular-data]
---

# Feature Engineering for Anomaly Detection

The quality of an anomaly detection model is directly determined by the features it receives. Isolation Forest does not know what an "expense" or a "transaction" is — it only sees numeric patterns, so features must encode domain context.

## Definition

Selecting and transforming raw columns into model-ready features. For tabular anomaly detection, this typically means: numeric columns as-is, categorical columns one-hot encoded, and derived features that encode business context (like HourGroup for time-of-day).

## Key Points

- **Isolation Forest needs numeric input:** All features must be numeric. Categorical columns (vendor, department, category) must be one-hot encoded via `pd.get_dummies()` or equivalent.
- **Drop rows with nulls in key fields:** Nulls in critical features (Amount, Category, Time) break both encoding and model fitting — drop or impute before modelling.
- **Domain features carry signal:** Adding `HourGroup` (time-of-day bucket) or `Department` (team context) gives the model business-level context it cannot derive from Amount alone.
- **Feature selection is a design choice:** Including too many features dilutes the signal; too few misses context. Isabelle used Amount, Category, Department, PaymentType, HourGroup.
- **One-hot encoding creates sparse columns:** One column per unique category value. For high-cardinality columns (e.g., vendor with 500 values), consider frequency encoding or grouping rare vendors first.
- **Merge results back to full dataset:** Rows excluded during modelling (due to nulls) still need AnomalyScore — merge model output back onto the full DataFrame.

## Related

- [[Isolation-Forest-How-It-Works]]
- [[HourGroup-Feature-Engineering]]
- [[Isolation-Forest-Power-Query-Pattern]]
- [[Python-Data-Preparation-for-ML-Power-Query]]
- [[high-cardinality-features-antipattern]]
- [[python-script-in-power-query]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[anomaly-detection-data-requirements]]
