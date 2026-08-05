---
created: 2026-08-01
updated: 2026-08-04
source: "Unlocking Python Inside Power BI How I Solved the Cumulative Value Challenge (and What I Learned Along the Way).md"
note_type: atomic
tags: [power-query, python, pandas, step-by-step, intermediate, forecasting, statsmodels, holt-winters, time-series]
---

# Running Python Scripts Inside Power Query

Power BI allows Python scripts to run directly inside Power Query — the table is passed as a pandas DataFrame called `dataset`. No external scripts, no file imports.

## Steps

1. **Open Power Query Editor**: Transform Data
2. **Select the source query**: the table you want to process (not a referenced query — see [[formula-firewall-python-blocked]])
3. **Run Python Script**: Transform → Run Python Script
4. **Paste script**: Power BI automatically passes the table as `dataset` (a pandas DataFrame)
5. **Click OK**: Python executes; output appears as an embedded table
6. **Expand output**: click the expand icon to flatten table columns back into individual columns
7. **Close & Apply**

## The dataset Variable

`dataset` is the Power Query table at that point in the pipeline, converted to a pandas DataFrame. Everything you do in Python works on that DataFrame.

```python
# dataset = your Power Query table as a pandas DataFrame
# Write your Python here
```

## Example: Full Python Script

```python
import pandas as pd

dataset = dataset.sort_values(["Version", "EU#", "MonthNum"])

dataset["Cumulative Value"] = (
    dataset.groupby(["Version", "EU#"])["Value"]
    .cumsum()
)
```

## After Expansion: M Code Result

Power BI generates M code that wraps the Python execution:

```m
#"Run Python script" = Python.Execute(
    "import pandas as pd
    dataset = dataset.sort_values([...])
    ...",
    [dataset=Result]
),
#"Removed Columns" = Table.RemoveColumns(#"Run Python script", {"Name"}),
#"Expanded Value" = Table.ExpandTableColumn(
    #"Removed Columns",
    "Value",
    {"EU#", "Enterprise Unit", "Period", "Value",
     "Year", "MonthNum", "Month", "Version", "Cumulative Value"},
    {"EU#", "Enterprise Unit", "Period", "Value",
     "Year", "MonthNum", "Month", "Version", "Cumulative Value"}
),
#"Changed Type" = Table.TransformColumnTypes(
    #"Expanded Value",
    {
        {"Value", Int64.Type},
        {"Year", Int64.Type},
        {"MonthNum", Int64.Type},
        {"Cumulative Value", Int64.Type}
    }
)
```

## Limitation: Output Is One Table

Python can only return a single DataFrame. Multiple outputs require splitting the script into separate Python Script steps or post-processing in M.

## Notable Variation: Forecasting with statsmodels

Python in Power Query is not just for cleaning — it's also a viable surface for **statistical modelling** that produces data Power BI can visualise natively. The [[Holt-Winters-Forecasting-in-Power-Query]] pattern fits one `ExponentialSmoothing` model per group, tags forecast rows with a `Forecast=True` boolean, and returns a combined historical+forecast table:

```python
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = dataset.copy()
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

frames = []
for grp in df['Group'].unique():
    temp = df[df['Group'] == grp].sort_values('Date')
    if len(temp) >= 12:                                         # ≥ 1 seasonal cycle
        model = ExponentialSmoothing(temp['Metric'], trend='add', seasonal='add', seasonal_periods=12)
        fit = model.fit()
        future = pd.date_range(temp['Date'].max() + pd.DateOffset(months=1), periods=12, freq='M')
        frames.append(pd.DataFrame({
            'Date': future, 'Metric': fit.forecast(12).values,
            'Group': grp, 'Forecast': True
        }))
result = pd.concat([df.assign(Forecast=False), *frames])
```

The `Forecast` flag is what lets downstream DAX distinguish actuals from predictions (e.g., `[Type] = IF(MAX(Metric[Forecast]), "Forecast", "Actual")`).

This contrasts with the Python *Visual* approach ([[python-forecasting-in-power-bi-sklearn]]) — Python-in-Power-Query pre-computes the forecast as data; Python-in-Visual renders the model inside the chart. Choose Power Query when you want the underlying values; choose Python Visual when you want a one-shot prediction visual.

## Related

- [[formula-firewall-python-blocked]] — critical: Python only works on direct source queries, not references
- [[python-data-types-power-query]] — always add Changed Type step after expanding Python output
- [[pandas-cumsum-vs-list-firstn]] — the actual script used in the source article
- [[Holt-Winters-Forecasting-in-Power-Query]] — the canonical forecasting pattern (Power Query + Python)
