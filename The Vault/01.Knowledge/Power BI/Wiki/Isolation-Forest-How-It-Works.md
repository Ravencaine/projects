---
created: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
note_type: atomic
tags: [isolation-forest, anomaly-detection, unsupervised, sklearn, random-split]
---

# Isolation Forest — How It Works

Isolation Forest isolates anomalies by randomly splitting data — anomalies take fewer splits to isolate because they are few and different.

## Definition

Isolation Forest is an unsupervised anomaly detection algorithm from `sklearn.ensemble`. Unlike models that profile "normal" and flag deviations, it explicitly tries to isolate points. Because anomalies are rare and structurally different, they get isolated in fewer random splits than normal points. The number of splits needed to isolate a point is its anomaly score.

## Key Points

- **Random splitting:** The algorithm builds decision trees by randomly selecting a feature and a split value. Anomalies get isolated faster because they lie in sparse regions of the feature space.
- **Fewer splits = more anomalous:** Points that isolate in fewer average splits across all trees are flagged as `-1` (anomaly); others are `1` (normal).
- **Unsupervised:** No labeled training data required. The model learns the structure of "normal" implicitly.
- **Ensemble of trees:** `n_estimators` trees are built; each point's score is averaged across all trees for stability.
- **Tabular and small-data friendly:** Works well on structured tabular data — no need for images, text, or large datasets.
- **Tunable sensitivity:** The `contamination` parameter controls what fraction of the dataset is pre-assumed to be anomalous; affects the decision boundary.

## Example

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
scores = model.fit_predict(X)  # -1 = anomaly, 1 = normal
```

## Related

- [[Isolation-Forest-Parameters-Quick-Reference]]
- [[Isolation-Forest-Parameters-Quick-Reference]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[anomaly-detection-data-requirements]]
- [[python-script-in-power-query]]
- [[Feature-Engineering-for-Anomaly-Detection]]
