---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: pattern
tags: [python, power-bi, forecasting, scikit-learn, linear-regression, predictive-analytics]
---

# Python Forecasting in Power BI (sklearn LinearRegression)

Using a Python Visual with scikit-learn LinearRegression to predict next-period values from Power BI data.

## Purpose

Plug a trained regression model into Power BI to forecast future sales, demand, or any numeric metric — without leaving the Power BI canvas. The model reads from the live dataset and outputs a prediction visual.

## Components

- Power BI Python Visual
- pandas — data manipulation
- scikit-learn `LinearRegression` — model training
- numpy — array operations

## Structure

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Get data from Power BI dataset
df = dataset

# Prepare date-based features
df['Month_Num'] = pd.to_datetime(df['Date']).dt.month
df['Week_of_Year'] = pd.to_datetime(df['Date']).dt.isocalendar().week

# Define features (X) and target (y)
X = df[['Month_Num', 'Week_of_Year', 'Promotion_Active']]
y = df['Sales']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Generate future predictions
# (future_X should be prepared from the next N periods)
future_predictions = model.predict(future_X)
```

## Example

Given a `Sales` table with columns `Date`, `Month_Num`, `Week_of_Year`, and `Promotion_Active`:

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

df = dataset

# Engineer features from the date column
df['Month_Num'] = pd.to_datetime(df['Date']).dt.month
df['Week_of_Year'] = pd.to_datetime(df['Date']).dt.isocalendar().week

X = df[['Month_Num', 'Week_of_Year', 'Promotion_Active']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

# Predict next 4 weeks
# future_X should contain 4 rows: (month, week, promotion_flag)
future_X = pd.DataFrame({
    'Month_Num': [7, 7, 8, 8],
    'Week_of_Year': [27, 28, 29, 30],
    'Promotion_Active': [1, 0, 0, 1]
})

predictions = model.predict(future_X)
output = pd.DataFrame({'Week': [27, 28, 29, 30], 'Predicted_Sales': predictions})
```

## Variations

**Adding more features:**
```python
X = df[[employee-count]]
```

**Using RandomForest for non-linear patterns:**
```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)
predictions = model.predict(future_X)
```

**Replacing LinearRegression with XGBoost or LightGBM** for larger datasets with complex interactions.

## Prerequisites

1. Enable Python scripting: File → Options → Preview Features → Enable Python scripting
2. Install Python runtime (Python 3.8+) with `pandas`, `scikit-learn`, `numpy`
3. Ensure the dataset passed to the Python visual contains all required columns

## Notes

- The `dataset` variable is automatically populated by Power BI with the data from the visual's fields
- Accuracy in the 80–85% range is realistic for simple linear models on retail sales data
- Always validate against held-out data (Ignore Last N periods) before presenting predictions
- Forecasts degrade for periods with no historical precedent (genuine disruptions, new products)

## Related

- [[build-ai-powered-power-bi-dashboard]] — workflow
- [[ai-shows-correlations-not-causations]] — gotcha
- [[validate-forecast-with-ignore-last]] — Diepeveen 2022 pattern
