---
created: 2026-07-27
updated: 2026-08-02
source: "Integrating Python into Excel: A New Era of Data Analysis"
note_type: workflow
tags: [excel, python, workflow, pandas, xl-function, py-function]
---

# Python in Excel Workflow

Step-by-step workflow for using Python (pandas, Matplotlib, scikit-learn) inside Excel via the =PY() function.

## Prerequisites

- Microsoft 365 Business or Enterprise subscription
- Windows (macOS support rolling out)
- Excel updated to latest version

## Steps

### 1. Activate Python

Navigate to **Formulas > Insert Python** (or type `=PY(` in a cell).

### 2. Reference Excel Data as DataFrame

Use the `xl()` function to convert Excel ranges or tables to pandas DataFrames:

```python
=PY("
import pandas as pd
df = xl('Sheet1!A1:C10', headers=True)
")
```

### 3. Run Python Analysis

```python
=PY("
import pandas as pd
df = xl('SalesData!A1:D1000', headers=True)

# Data transformation with pandas
df_clean = df.dropna()
df_grouped = df_clean.groupby('Product')['Revenue'].sum()
")

# Machine learning with scikit-learn
=PY("
from sklearn.linear_model import LinearRegression
df = xl('HistoricalSales', headers=True)
model = LinearRegression()
model.fit(df[['Month', 'Week']], df['Sales'])
")
```

### 4. Display Results in Excel

Return a DataFrame to display as an Excel table, or a scalar to display in a single cell.

## Related

- [[excel-as-bi-tool]]
- [[integrating-python-excel]]
