---
created: 2026-07-27
updated: 2026-08-02
source: "AI in Power BI (2025): AI-Powered Dashboard Using Copilot & Python"
note_type: reference
tags: [power-bi, python-visual, pandas, scikit-learn, matplotlib, reference]
---

# Python Visual in Power BI: Reference

Using Python (pandas, scikit-learn, Matplotlib) inside Power BI via the Python Visual.

## Enabling Python Visuals

- Power BI Desktop: enabled by default (File > Options > Preview features > Python visuals)
- Power BI Service: Admin must enable in Tenant settings (Python scripting)
- On-premises gateway: Python runtime must be installed on the gateway machine

## Dataset Input

Power BI passes the selected table to Python as a `pandas.DataFrame` named `dataset`. All column names from the selected fields appear as DataFrame columns.

```python
import pandas as pd
print(dataset.columns)  # verify column names
```

## Common Patterns

### Scatter Plot with sklearn

```python
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = dataset[['Revenue', 'Quantity']].dropna()
kmeans = KMeans(n_clusters=4, random_state=42).fit(df)
df['Cluster'] = kmeans.labels_

plt.figure(figsize=(10, 6))
for i in range(4):
    cluster = df[df['Cluster'] == i]
    plt.scatter(cluster['Revenue'], cluster['Quantity'], label=f'Cluster {i}')
plt.xlabel('Revenue')
plt.ylabel('Quantity')
plt.legend()
plt.show()
```

### Time Series Decomposition

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = dataset[['Date', 'Sales']].copy()
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').set_index('Date')

result = seasonal_decompose(df['Sales'], model='additive', period=12)
result.plot()
plt.show()
```

## Limitations

| Limitation | Detail |
|-----------|--------|
| No interactive Python visuals | Python outputs are static images |
| Gateway required for cloud refresh | Python runtime must be installed on the PBIEG |
| Max rows | ~150,000 rows passed to Python visual |
| No Python packages requiring compilation | Basic pandas, sklearn, matplotlib work; deep learning libraries may not |

## Related

- [[ai-copilot-power-bi-workflow]]
- [[python-in-excel-workflow]]
