---
created: 2026-08-09
updated: 2026-08-09
source: "Fix Incorrect Totals in Power BI Tables.md"
note_type: atomic
tags: [dax, totals, row-context, filter-context, context-transition, power-bi]
---

# Why Totals Are Wrong: Row Context Missing at Total Level

The total row in a table or matrix visual operates under a fundamentally different evaluation context than the detail rows. This mismatch is the root cause of the "incorrect totals" problem.

## Definition

In DAX, a measure is **re-evaluated** for each cell in a visual — including the total row. At the detail row level, the filter context contains the grouping columns (Category, Month, etc.). At the total row level, those grouping filters are absent — the context is broader or empty. This means the aggregation (`MAX`, `MIN`, `AVERAGE`) operates on the entire filtered dataset, not on the per-group result.

## Key Points

- **Row context exists at detail level** through the visual's grouping — each row has filters for its category/month/etc.
- **Row context is absent at total level:** the total row has no single-category filter; it sees all data
- **`MAX`, `MIN`, `AVERAGE` don't sum:** `SUM(myTable[Value])` happens to give correct totals by coincidence (sum of all rows = total of row-level sums); MAX/MIN/AVERAGE give a single aggregate value, not a sum of per-group aggregates
- **The total row is a separate evaluation:** DAX doesn't "add up the visible rows"; it runs the same formula in a different context
- **`CALCULATE` triggers context transition:** wrapping an aggregation in `CALCULATE` inside `SUMX(SUMMARIZE(...))` converts row context into filter context for each group

## Mental Model

```
Detail rows:   MAX(Orders[Price])  → evaluated with Category="X" filter  → 50
Total row:    MAX(Orders[Price])  → evaluated with NO category filter    → 120  ← wrong

Corrected:    SUMX(SUMMARIZE(Categories, Categories[Cat], "m", CALCULATE(MAX(Orders[Price]))), [m])
              → iterates each category, MAX in category context, SUMX sums the results  → 170  ← right
```

## The Fix Is Always the Same Pattern

1. `SUMMARIZE` to define the groups (re-creates the grouping columns from the visual)
2. `CALCULATE` inside to get per-group aggregation via context transition
3. `SUMX` to sum across groups into the total

## Related

- [[Fix-Incorrect-Totals-SUMX-SUMMARIZE-Pattern]] — the pattern implementing this fix
- [[measure-totals-problem-dax]] — HASONEVALUE/ISINSCOPE guards for related total scenarios
- [[context-transition-with-calculate]] — how CALCULATE converts row context to filter context
- [[Why Totals Look Wrong in DAX (and How to Fix Them)]] — source note with full explanation
