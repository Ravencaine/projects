---
created: 2026-08-01
updated: 2026-08-02
source: "The DAX concepts that actually save you time in Power BI.md"
note_type: atomic
tags: [dax, row-context, filter-context, fundamentals, beginner]
---

# Row Context vs Filter Context: The Core Distinction

The concept that separates analysts who fight DAX from those who write it. These two contexts don't automatically talk to each other.

## Row Context

Row context shows up when a formula **walks through a table one row at a time**.

- Happens inside **calculated columns**
- Happens inside **iterator functions** (`SUMX`, `AVERAGEX`, etc.)
- Picture walking down a spreadsheet, row by row, doing the same calculation on each
- **No filtering happens**: just the current row

```c
// Inside a calculated column — row context for Sales
Extended Price = Sales[Quantity] * Sales[Unit Price]
// Evaluated row by row; result stored per row
```

## Filter Context

Filter context is the **set of filters currently applied** to a calculation.

- Comes from: slicers, rows/columns in a table/matrix visual, page-level filters, `CALCULATE` statements
- When viewing a total in a visual, that number reflects only the rows that **survive the current filter context**

```c
// A measure evaluated in current filter context
Total Sales = SUM(Sales[Amount])
// Changes when slicers, filters, or visual context changes
```

## The Disconnect

These two contexts **don't automatically talk to each other**.

A row context, on its own, **does not filter anything**.

This is why a calculated column referencing another table's aggregated value behaves strangely without `CALCULATE` bridging the gap — row context exists but filter context doesn't.

## Bridging: CALCULATE

`CALCULATE` converts row context into filter context — see [[calculate-context-transition-core]].

```c
// Inside an iterator — row context for each Customer row
Customer Total =
SUMX(
    Sales,
    CALCULATE(SUM(Sales[Amount]))
    -- CALCULATE converts row context (current Customer)
    -- into filter context, so SUM sees only that customer's rows
)
```

## Mental Model

| Context | Analogy |
|---------|---------|
| Row context | Walking down a spreadsheet one row at a time |
| Filter context | Looking through a set of sunglasses that hides some rows |

## Related

- [[measures-vs-calculated-columns]] — calculated columns use row context
- [[calculate-context-transition-core]] — CALCULATE bridges and transitions between contexts
- [[var-dax-reading-complexity]] — VAR captures values in current context
