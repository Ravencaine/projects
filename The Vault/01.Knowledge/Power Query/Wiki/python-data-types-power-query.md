---
created: 2026-08-01
updated: 2026-08-02
source: "Unlocking Python Inside Power BI How I Solved the Cumulative Value Challenge (and What I Learned Along the Way).md"
note_type: atomic
tags: [power-query, python, pandas, data-types, gotcha, intermediate]
---

# Python Data Types Don't Carry Into Power Query

Setting `astype()` in pandas inside a Python script does **not** preserve data types after expansion in Power Query. All columns come through as text regardless of what Python set.

## The Problem

Inside the Python script, data types are set correctly:

```python
dataset["Cumulative Value"] = dataset["Cumulative Value"].astype(int)
dataset["Year"] = dataset["Year"].astype(int)
dataset["MonthNum"] = dataset["MonthNum"].astype(int)
dataset["Value"] = dataset["Value"].astype(int)
```

After clicking the expand icon in Power Query, every column shows as **text** (the `ABC` icon) — the `astype()` calls were silently discarded during the expansion step.

Power BI converts all Python output to text when expanding — Python data types are not mapped through.

## The Fix: Table.TransformColumnTypes After Expansion

Add a `Changed Type` step in M after expanding the Python output:

```m
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

This sets all integer columns at once. Far more efficient than clicking each column individually and selecting the type in the UI.

## Why Do This in the Advanced Editor?

Setting types one-by-one in the UI is slow. The Advanced Editor approach handles all columns in a single step — especially valuable when the Python script outputs many columns.

## The Pattern

```
Run Python Script → Expand Output → Table.TransformColumnTypes (Advanced Editor)
```

The data type step always comes **after** Python expansion, never inside the Python script.

## Related

- [[python-script-in-power-query]] — the full pipeline including this step
- [[pandas-cumsum-vs-list-firstn]] — the Python script this pattern is used with
