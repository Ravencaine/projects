---
created: 2026-08-05
updated: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
note_type: pattern
tags: [power-query, python, isolation-forest, anomaly-detection, sklearn, pandas, pattern]
---

# Isolation Forest Anomaly Detection in Power Query (Python)

Run an sklearn `IsolationForest` unsupervised anomaly detection model entirely inside Power Query — no Premium, no external tools, no labeled data needed.

## Purpose

Flag suspicious transactions (expenses, timesheets, inventory) by scoring each row with `-1` (anomaly) or `1` (normal) using an Isolation Forest model embedded in Power Query's Python step.

## Components

1. `dataset` — Power Query table as pandas DataFrame
2. Null-drop on key fields (Amount, Category, Department, PaymentType, Time)
3. `group_hour()` — time bucketing function
4. `pd.get_dummies()` — one-hot encoding of categorical features
5. `IsolationForest.fit_predict()` — scoring
6. Merge results back to full dataset

## Structure

```python
# 'dataset' holds the input data for this script
import pandas as pd
from sklearn.ensemble import IsolationForest

# Drop rows with nulls in key fields
df = dataset.dropna(subset=['Amount', 'Category', 'Department', 'PaymentType', 'Time'])

# Convert Time to hour group
def group_hour(time_str):
    try:
        hour = int(time_str.split(':')[0])
    except:
        hour = 0  # Fallback for invalid formats
    if 6 <= hour <= 9:
        return 'Morning'
    elif 10 <= hour <= 13:
        return 'Midday'
    elif 14 <= hour <= 17:
        return 'Afternoon'
    elif 18 <= hour <= 21:
        return 'Evening'
    else:
        return 'Night'

df['HourGroup'] = df['Time'].apply(group_hour)

# Select and one-hot encode relevant features
features = df[['Amount', 'Category', 'Department', 'PaymentType', 'HourGroup']]
X = pd.get_dummies(features)

# Fit Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
anomaly_scores = model.fit_predict(X)

# Add results to original data
df['AnomalyScore'] = anomaly_scores

# Merge results back into full original dataset
df_full = dataset.copy()
df_full['HourGroup'] = df['HourGroup']
df_full['AnomalyScore'] = df['AnomalyScore']
df_full['CardNumber'] = df['CardNumber']

# Output
result = df_full
```

## Key Steps

| Step | What it does |
|------|-------------|
| `dropna()` | Removes rows where key feature columns are null — required before one-hot encoding |
| `group_hour()` | Maps raw time string to one of 5 time-period buckets |
| `pd.get_dummies()` | One-hot encodes all categorical features — sklearn requires numeric input |
| `fit_predict()` | Trains and scores in one call; returns array of `-1` / `1` |
| Merge back | Applies scores to the full dataset (including null-excluded rows) |

## Variations

- **Adjust sensitivity:** Change `contamination` — lower (e.g., `0.01`) = fewer anomalies; higher (e.g., `0.05`) = more flags
- **Add features:** Bring in project codes, travel destinations, user roles for richer context
- **Different hour buckets:** Hospitality and shift-based teams may need custom time ranges
- **Frequency encoding:** For high-cardinality categoricals (e.g., vendor with hundreds of values), use frequency encoding instead of one-hot

## Related

- [[python-script-in-power-query]]
- [[HourGroup-Feature-Engineering]]
- [[Isolation-Forest-How-It-Works]]
- [[Isolation-Forest-Parameters-Quick-Reference]]
- [[Feature-Engineering-for-Anomaly-Detection]]
- [[Python-Data-Preparation-for-ML-Power-Query]]
- [[formula-firewall-python-blocked]]
