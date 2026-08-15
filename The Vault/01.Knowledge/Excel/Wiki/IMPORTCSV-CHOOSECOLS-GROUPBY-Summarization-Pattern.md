---
created: 2026-08-10
updated: 2026-08-10
source: Excel IMPORTCSV and IMPORTTEXT Functions Explained
source_url: https://www.myonlinetraininghub.com/excel-importcsv-and-importtext-functions-explained
note_type: pattern
tags: [excel, let, choosecols, groupby, importtext, dynamic-array, summarization, pipe]
---

# LET + CHOOSECOLS + GROUPBY on Imported Text File

IMPORTCSV and IMPORTTEXT return dynamic arrays, so their output can be piped directly into LET, CHOOSECOLS, and GROUPBY for on-the-fly summarization — all in one formula, no intermediate tables.

## The Pattern

```
=LET(
    data,  IMPORTTEXT("C:\Data\sales.txt"),
    GROUPBY(
        CHOOSECOLS(data, 2),       -- Category column
        CHOOSECOLS(data, 4),       -- Sales column
        SUM,
        3,                         -- include headers
        1                          -- include grand total
    )
)
```

## How Each Function Contributes

| Function | Role |
|----------|------|
| `LET` | Stores the imported array in `data` — evaluates IMPORTTEXT once, makes the formula readable |
| `CHOOSECOLS` | Extracts specific columns from the spilled array (column 2 = Category, column 4 = Sales) |
| `GROUPBY` | Groups by Category, sums Sales, adds headers and grand total |

## Why This Is Powerful

1. **No intermediate tables:** data is imported and summarised in one formula
2. **No Power Query:** works entirely in the grid for clean, simple files
3. **Entirely formula-driven:** the workflow is transparent and auditable
4. **Refreshes with the import:** GROUPBY recalculates when IMPORTTEXT refreshes

## Common Variants

### Group by two columns, average instead of sum

```
=LET(
    data,  IMPORTCSV("C:\Data\sales.csv"),
    GROUPBY(
        CHOOSECOLS(data, 2, 3),     -- two grouping columns
        CHOOSECOLS(data, 4),
        AVERAGE,
        3,
        1
    )
)
```

### Filter before grouping

```
=LET(
    data,  IMPORTCSV("C:\Data\sales.csv"),
    filtered,  FILTER(data, CHOOSECOLS(data, 3) > 1000),
    GROUPBY(
        CHOOSECOLS(filtered, 2),
        CHOOSECOLS(filtered, 4),
        SUM,
        3, 1
    )
)
```

## Related

- [[IMPORTCSV-IMPORTTEXT-Reference]] — IMPORTCSV and IMPORTTEXT function signatures and parameters
- [[Source-Treacy-IMPORTCSV-IMPORTTEXT]] — source note
