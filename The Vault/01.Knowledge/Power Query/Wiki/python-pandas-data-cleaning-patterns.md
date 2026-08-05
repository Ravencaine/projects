---
created: 2026-08-01
updated: 2026-08-02
source: "Supercharge Your Power BI with Python Cleaning Magic - Janvi Gupta.md"
note_type: atomic
tags: [power-query, python, pandas, data-cleaning, beginner]
---

# Python Pandas Data Cleaning Patterns in Power Query

Common pandas operations for cleaning data inside Power Query's Python script step.

## Removing Duplicates

`drop_duplicates()` removes duplicate rows from the dataset — equivalent to Power Query's Remove Duplicates.

```python
import pandas as pd

# Remove exact duplicate rows
dataset = dataset.drop_duplicates()
```

Also supports subset-based deduplication:

```python
# Keep first row per key column
dataset = dataset.drop_duplicates(subset=["CustomerID", "OrderDate"])
```

## Handling Missing Values

See [[python-null-nan-handling-power-query]].

## Removing Unnecessary Columns

`drop()` removes specified columns by name.

```python
# Remove single column
dataset = dataset.drop(columns=["Notes"])

# Remove multiple columns
dataset = dataset.drop(columns=["Notes", "InternalFlag", "TempColumn"])
```

## Renaming Columns

`rename()` with a dictionary maps old names to new names.

```python
dataset = dataset.rename(columns={
    "CustID": "CustomerID",
    "SaleAmt": "SaleAmount",
    "SaleDt": "SaleDate"
})
```

## Splitting Columns

`str.split()` with `expand=True` splits a string column into multiple columns.

```python
# Split "City, Country" into two columns
dataset[["City", "Country"]] = dataset["Location"].str.split(", ", expand=True)
```

## Filtering Rows

Boolean masking filters rows by condition.

```python
# Keep only rows where Amount > 0
dataset = dataset[dataset["Amount"] > 0]

# Keep only active customers
dataset = dataset[dataset["Status"] == "Active"]
```

## Related

- [[python-script-in-power-query]] — step-by-step for running Python in PQ
- [[python-null-nan-handling-power-query]] — missing value patterns
- [[python-text-cleaning-power-query]] — whitespace and text cleaning
- [[formula-firewall-python-blocked]] — Formula Firewall limitation (Python only on direct queries)
