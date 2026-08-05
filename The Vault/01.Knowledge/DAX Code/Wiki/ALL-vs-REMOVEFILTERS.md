---
created: 2026-08-05
updated: 2026-08-05
source: ALL and REMOVEFILTERS in Power BI (Boniface Muchendu)
note_type: comparison
tags: [dax, all, removefilters, comparison, sumx, calculate]
---

# ALL vs REMOVEFILTERS

Side-by-side comparison of ALL() and REMOVEFILTERS() — the two DAX functions that both remove filter context but differ in one critical way: ALL returns a table/column value; REMOVEFILTERS returns nothing.

## At a Glance

| Feature | ALL | REMOVEFILTERS |
|---------|-----|--------------|
| Introduced | Pre-2019 | 2019 |
| Removes filters | ✓ | ✓ |
| Return value | Table or column | Nothing |
| Use in SUMX | ✓ | ✗ |
| Use in FILTER | ✓ | ✗ |
| Use in CALCULATE | ✓ | ✓ |
| Multiple arguments | ✓ | ✓ |
| No-argument form | ALL() = all rows | N/A |
| Readability | Functional | Intent-expressive |

## The Single Critical Difference

ALL returns a value. REMOVEFILTERS does not. This means:

```dax
-- ALL can stand alone as a table expression
VAR _AllRows = ALL(Sales)       -- returns a table
VAR _Result = COUNTROWS(_AllRows) -- works

-- REMOVEFILTERS cannot
VAR _Nothing = REMOVEFILTERS(Sales) -- returns nothing; any further use errors
```

## When to Use Which

| Situation | Use |
|-----------|-----|
| Only removing filters inside CALCULATE | REMOVEFILTERS (clearer intent) |
| Need the unfiltered table for SUMX | ALL |
| Need the unfiltered column for FILTER | ALL |
| Writing a modern measure for readability | REMOVEFILTERS |
| Supporting older models | ALL |

## Equivalence in CALCULATE

Inside CALCULATE, the following are functionally equivalent:

```dax
-- ALL form
CALCULATE([Total Sales], ALL(DimProduct))

-- REMOVEFILTERS form
CALCULATE([Total Sales], REMOVEFILTERS(DimProduct))
```

Both remove all filters on DimProduct. REMOVEFILTERS is preferred for readability.

## Modern DAX Idiom

For filter removal only, prefer REMOVEFILTERS — it makes the intent explicit and avoids the ambiguity of ALL which does different things depending on context.

## Related

- [[ALL-Function-DAX]]
- [[REMOVEFILTERS-Function-DAX]]
- [[Removing-Slicer-Filters-ALL]]
