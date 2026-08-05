---
created: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
note_type: reference
tags: [power-query, python, pandas, sklearn, data-preparation, anomaly-detection, reference]
---

# Python Data Preparation for ML in Power Query — Checklist

Key data preparation steps when embedding Python ML models inside Power Query's Run Python Script step.

## Quick Reference

| Step | Command | Why |
|------|---------|-----|
| Drop nulls in key features | `df.dropna(subset=[cols])` | Nulls break one-hot encoding and model fitting |
| Create derived features | `df['new'] = df['col'].apply(fn)` | Add domain context (e.g., HourGroup) |
| Select feature columns | `df[feature_list]` | Scope modelling to relevant columns |
| One-hot encode categoricals | `pd.get_dummies(df)` | sklearn requires numeric input |
| Fit and score | `model.fit_predict(X)` | Returns -1 (anomaly) / 1 (normal) |
| Merge back to full dataset | `df_full['Score'] = df['Score']` | Score applies only to non-null rows — merge restores full row count |

## Notes

- **Order matters:** Drop nulls → engineer features → select features → one-hot → fit → merge back
- **Drop nulls BEFORE one-hot:** If a row has a null in a categorical column, `pd.get_dummies()` silently drops that column's indicator — silently corrupting the feature matrix
- **Merge back is mandatory:** Rows dropped during null removal still need an AnomalyScore — use `dataset.copy()` as the base and assign computed columns back to it
- **Power Query only accepts one output DataFrame:** Return `result = df_full` with all columns needed downstream
- **Expand Python output after running:** Power Query nests the output as a table column — click the expand icon to flatten it into individual columns
- **Add Changed Type step after expanding:** Python output columns inherit type `Any` — explicitly cast Amount to Decimal, AnomalyScore to Text/Int

## Related

- [[Isolation-Forest-Power-Query-Pattern]]
- [[python-script-in-power-query]]
- [[formula-firewall-python-blocked]]
- [[python-data-types-power-query]]
- [[Feature-Engineering-for-Anomaly-Detection]]
