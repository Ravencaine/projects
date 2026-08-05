---
created: 2026-08-05
updated: 2026-08-05
source: ALL and REMOVEFILTERS in Power BI (Boniface Muchendu)
note_type: function
tags: [dax, removefilters, filter-context, calculate, introduced-2019]
---

# `REMOVEFILTERS()` DAX

Clears filter context from specified tables or columns — but returns nothing. Use only inside CALCULATE to remove filters; cannot be used as a table expression in SUMX, FILTER, or other functions.

## Definition

> REMOVEFILTERS clears filters from specified tables or columns. It does not return a value — it only modifies filter context.

Introduced in **2019** as a more readable alternative to ALL when only filter removal is needed.

## Syntax

```dax
REMOVEFILTERS(<TableName>)
REMOVEFILTERS(<ColumnName>[, <ColumnName>[, …]])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `TableName` | table | Clear all filters on the specified table |
| `ColumnName` | column | Clear filters on one or more columns |

## Return Value

**Nothing** — REMOVEFILTERS does not return a table or column. It only has a side effect: it clears filter context. This is why it cannot be used as a table expression.

## Common Pattern

```dax
Total Sales REMOVEFILTERS =
CALCULATE(
    [Total Sales],
    REMOVEFILTERS(DimProduct),
    REMOVEFILTERS(DimSalesTerritory)
)
```

Equivalent result to `CALCULATE([Total Sales], ALL(DimProduct), ALL(DimSalesTerritory))` — but using REMOVEFILTERS makes the intent clearer.

## When REMOVEFILTERS Cannot Be Used

```dax
-- WRONG: REMOVEFILTERS does not return a table — SUMX will error
Total Sales SUMX =
SUMX(
    REMOVEFILTERS(Sales),   -- ERROR: REMOVEFILTERS returns nothing
    Sales[Quantity] * Sales[Price]
)

-- CORRECT: use ALL instead
Total Sales SUMX =
SUMX(
    ALL(Sales),
    Sales[Quantity] * Sales[Price]
)
```

## Related

- [[ALL-Function-DAX]]
- [[ALL-vs-REMOVEFILTERS]]
- [[Removing-Slicer-Filters-ALL]]
