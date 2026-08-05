---
created: 2026-07-27
updated: 2026-08-02
source: "AI in Power BI (2025): AI-Powered Dashboard Using Copilot & Python"
note_type: workflow
tags: [power-bi, ai, copilot, python, workflow, forecasting, anomaly-detection]
---

# AI Copilot + Python Power BI Workflow

Step-by-step workflow for building an AI-augmented Power BI dashboard using Copilot for rapid prototyping and Python for advanced analytics.

## Prerequisites

- Power BI Pro or Premium workspace
- Python for Windows installed (python.org, add to PATH)
- Power BI Desktop (latest version with Copilot enabled)
- Edit permissions on the target workspace

## Step 1: Data Preparation

1. Connect data sources (SQL, Excel, SharePoint, etc.)
2. Load into Power Query for cleaning and transformation
3. Create data model: define relationships, date table, hierarchies
4. Publish to Power BI Service (required for Copilot)

## Step 2: Copilot-Assisted Report Building

### Generate DAX Measures

```
Prompt: "Create a measure for year-to-date revenue using the Date table"
```
Copilot generates the measure — review and edit before applying.

### Generate Visuals

```
Prompt: "Create a bar chart showing total sales by product category for the current year"
```
Copilot creates the visual — adjust formatting and filters.

### Generate Entire Pages

```
Prompt: "Build an executive summary page with KPI cards for Revenue, Profit, and Customer Count"
```

## Step 3: Python Visual for Advanced Analytics

### 1. Insert Python Visual

Insert > Python Visual. Select a dataset (table from model).

### 2. Forecasting with scikit-learn

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = dataset.copy()  # dataset is the selected Power BI table

# Prepare features (e.g., month as integer)
X = df[['Month']]  # transform date column to month integer
y = df['Sales']

# Fit model
model = LinearRegression()
model.fit(X, y)

# Predict next 3 months
future_months = pd.DataFrame({'Month': [13, 14, 15]})
predictions = model.predict(future_months)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], label='Actual')
plt.plot(future_months['Month'], predictions, label='Forecast', linestyle='--')
plt.legend()
plt.show()
```

### 3. Anomaly Detection

```python
from sklearn.ensemble import IsolationForest
import numpy as np

df['Anomaly'] = IsolationForest(contamination=0.05).fit_predict(df[['Sales']])
anomalies = df[df['Anomaly'] == -1]
print(anomalies)
```

## Step 4: Publish and Share

1. Publish to Power BI Service
2. Enable Python scripting in the workspace (Admin portal > Tenant settings > Python)
3. Schedule refresh (Python visuals require the Python runtime on the gateway)
4. Share via workspace or direct link

## Limitations of Copilot in Power BI

- Copilot requires semantic model to be published (not local PBIX)
- Generated DAX must be reviewed — occasionally uses incorrect table/column names
- Python visuals require Python runtime on the Power BI gateway for cloud refresh
- Copilot availability depends on tenant settings (admin must enable it)

## Related

- [[python-in-excel-workflow]] — Python in Excel vs. Python in Power BI
- 
- [[reports-semantic-models-power-bi-service]] — the semantic model is what Copilot analyzes and what Python visuals connect to
