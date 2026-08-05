---
created: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
note_type: snippet
tags: [python, pandas, sklearn, isolation-forest, anomaly-detection, one-hot, snippet]
---

# Isolation Forest + Pandas One-Hot Encoding Boilerplate

Drop-in Python snippet for running Isolation Forest inside Power Query — with null handling, HourGroup bucketing, one-hot encoding, and merge-back to full dataset.

## Code

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

# Drop rows with nulls in key fields
df = dataset.dropna(subset=['Amount', 'Category', 'Department', 'PaymentType', 'Time'])

# Convert Time to hour group
def group_hour(time_str):
    try:
        hour = int(time_str.split(':')[0])
    except:
        hour = 0
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

# Add results to modelling dataframe
df['AnomalyScore'] = anomaly_scores

# Merge results back into full original dataset
df_full = dataset.copy()
df_full['HourGroup'] = df['HourGroup']
df_full['AnomalyScore'] = df['AnomalyScore']

result = df_full
```

## When to Use

Use this pattern when embedding a Python ML model inside Power Query to add a scored column (e.g., anomaly flag, risk score) back onto the full input dataset.

## Variations

| Variation | Change |
|-----------|--------|
| Different contamination | `contamination=0.01` for fewer flags, `0.05` for more |
| More features | Add columns to `features` list before `pd.get_dummies()` |
| Custom time buckets | Adjust `group_hour()` hour ranges |
| Reproducible across refreshes | Ensure `random_state=42` is always present |
| Skip HourGroup | Remove `group_hour()` and the `HourGroup` column from features |

## Related

- [[Isolation-Forest-Power-Query-Pattern]]
- [[Python-Data-Preparation-for-ML-Power-Query]]
- [[HourGroup-Feature-Engineering]]
- [[Isolation-Forest-How-It-Works]]
