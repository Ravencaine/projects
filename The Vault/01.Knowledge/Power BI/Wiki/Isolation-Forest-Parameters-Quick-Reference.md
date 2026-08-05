---
created: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
note_type: reference
tags: [isolation-forest, sklearn, parameters, reference, anomaly-detection]
---

# Isolation Forest Parameters — Quick Reference

Key parameters for `sklearn.ensemble.IsolationForest` used inside Power Query.

## Quick Reference

| Parameter | Default | Description |
|-----------|---------|-------------|
| `n_estimators` | 100 | Number of isolation trees in the ensemble. Higher = more stable scores. |
| `contamination` | `auto` | Fraction of data expected to be anomalous. `0.02` = 2%. Lower = fewer anomalies flagged. Higher = more sensitive. |
| `random_state` | `None` | Seed for reproducibility. Set to an integer (e.g., `42`) for consistent results across runs. |
| `max_samples` | `'auto'` | Number of samples to draw to build each tree. `'auto'` = `min(256, n_samples)`. |
| `max_features` | `1.0` | Fraction of features to draw per tree. Default uses all features. |
| `bootstrap` | `False` | Whether to sample with replacement. Default (`False`) is usually correct. |

## Notes

- **Output values:** `fit_predict(X)` returns `-1` for anomalies and `1` for normal points.
- **`contamination` drives recall vs precision:** Isabelle used `contamination=0.02` (~2% of rows flagged). Lower values reduce false positives; higher values catch more anomalies but increase noise.
- **`random_state` is essential in Power Query:** Python re-runs on every data refresh. Without a seed, anomaly flags shift between refreshes even with the same data.
- **`n_estimators=100` is sufficient** for most tabular datasets under 10k rows. Increasing beyond 200 yields diminishing returns.

## Related

- [[Isolation-Forest-How-It-Works]]
- [[Isolation-Forest-Power-Query-Pattern]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[python-script-in-power-query]]
