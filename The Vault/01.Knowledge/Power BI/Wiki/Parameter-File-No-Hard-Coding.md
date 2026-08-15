---
created: 2026-08-05
updated: 2026-08-05
source: 4 Tips Work Efficiently Power BI (Isabelle Bittar)
note_type: atomic
tags: [power-bi, dax, parameter-file, excel, hard-coding, best-practice]
---

# Parameter File: No Hard-Coding in DAX

Storing business logic values (benchmarks, targets, ratios) in an Excel parameter file, loading it as a disconnected table in Power Query, and retrieving values via DAX — enabling updates without republishing the PBIX.

## Definition

Hard-coding values in DAX means that when a business user changes a threshold or ratio, the PBIX must be reopened, edited, and republished. A parameter file decouples the value from the formula — users update the Excel file and refresh the data source.

## The Pattern

### Step 1 — Create the Excel parameter file

| Group | ValueName | Value |
|-------|-----------|-------|
| Tier 2 | Students per teacher | 10 |
| Tier 3 | Students per teacher | 5 |

Save as `.xlsx` and place in a shared or OneDrive location.

### Step 2 — Load in Power Query

1. **Get Data → Excel** → select the parameter file
2. Load the sheet as a table (do not create any relationships)
3. The table is **disconnected:** no active relationships to the data model

### Step 3 — Retrieve values in DAX

```dax
Tier 2 Teaching Requirements =
CALCULATE(
    MAX('Teaching Requirements'[Value]),
    FILTER(
        'Teaching Requirements',
        'Teaching Requirements'[Group] = "Tier 2"
    )
)

Tier 3 Teaching Requirements =
CALCULATE(
    MAX('Teaching Requirements'[Value]),
    FILTER(
        'Teaching Requirements',
        'Teaching Requirements'[Group] = "Tier 3"
    )
)
```

`CALCULATE(MAX(...), FILTER(...))` is used to return a single scalar value from the disconnected table.

## Why Not LOOKUPVALUE?

`LOOKUPVALUE` works too, but `CALCULATE(MAX(...), FILTER(...))` is Isabelle's preferred pattern — it avoids the duplicate column requirement that `LOOKUPVALUE` sometimes imposes.

## When to Use

| Use case | Why parameter file helps |
|---------|------------------------|
| Business thresholds that change | Users update the Excel, not the PBIX |
| Targets and benchmarks | Centralise in one file for multiple reports |
| Regulatory ratios | Ensures all reports use the same value |
| Colour values | See [[Color-Measures-Consistent-Theme]] |

## Limitations

- Requires Power BI Service refresh after Excel update — not real-time
- Users need access to the parameter file location
- The table is disconnected — no relationships to join on

## Related

- [[Color-Measures-Consistent-Theme]]
- [[Organizing-Measures-Display-Folders]]
