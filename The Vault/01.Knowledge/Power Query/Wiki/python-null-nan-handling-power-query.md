---
created: 2026-08-01
updated: 2026-08-02
source: "Supercharge Your Power BI with Python Cleaning Magic - Janvi Gupta.md"
note_type: atomic
tags: [power-query, python, pandas, null, nan, missing-values, beginner]
---

# Handling Null/NaN Values in Power Query with Python

Pandas uses `NaN` (Not a Number) for missing values. Python scripts inside Power Query can handle these systematically.

## Identifying Missing Values

```python
import pandas as pd

# Count NaN per column
print(dataset.isnull().sum())

# Boolean mask of missing values
dataset[dataset.isnull()]
```

## Filling Missing Values

`fillna()` replaces NaN with a specified value.

```python
# Replace NaN with a string placeholder
dataset["Region"] = dataset["Region"].fillna("Unknown")

# Replace NaN with 0 (numeric columns)
dataset["Quantity"] = dataset["Quantity"].fillna(0)

# Forward-fill (carry previous value down)
dataset["Price"] = dataset["Price"].fillna(method="ffill")

# Backward-fill (carry next value up)
dataset["Price"] = dataset["Price"].fillna(method="bfill")
```

## Dropping Rows with Missing Values

`dropna()` removes rows containing NaN.

```python
# Drop rows with any NaN
dataset = dataset.dropna()

# Drop rows where specific column has NaN
dataset = dataset.dropna(subset=["CustomerID"])

# Drop rows where ALL columns are NaN
dataset = dataset.dropna(how="all")
```

## Replacing NaN in Multiple Columns

```python
# Different fill values per column
dataset = dataset.fillna({
    "CustomerName": "Unknown",
    "OrderDate": dataset["OrderDate"].mode()[0],  # fill with most common date
    "Amount": 0
})
```

## Note on Power Query Integration

After running Python, data types are not preserved — see [[python-data-types-power-query]] and always add a `Table.TransformColumnTypes` M step after expanding Python output.

## Related

- [[python-pandas-data-cleaning-patterns]] — broader cleaning patterns
- [[python-script-in-power-query]] — Python step in PQ
- [[python-data-types-power-query]] — always add Changed Type after Python
