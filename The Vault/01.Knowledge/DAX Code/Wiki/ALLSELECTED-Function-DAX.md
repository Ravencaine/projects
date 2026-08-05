---
created: 2026-08-05
updated: 2026-08-05
source: ALL, ALLSELECTED and ALLEXCEPT DAX Filter Function (Boniface Muchendu)
note_type: function
tags: [dax, allselected, filter-context, calculate, query-level, external-slicer]
---

# `ALLSELECTED()` DAX

Removes filters that were applied inside the current query — but preserves all filters that originated outside the query (external slicer selections, report-level filters). Unlike ALL which removes all filters, ALLSELECTED respects what the user selected outside the visual.

## Definition

> ALLSELECTED removes context filters from columns and rows in the current query while retaining all other context filters or explicit filters.

## Syntax

```dax
ALLSELECTED([<tableName> | <columnName>[, <columnName>[, …]]])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `tableName` | Removes query-level filters on all columns in the specified table |
| `columnName` | Removes query-level filters on the specified column(s) |
| No arguments | Removes all query-level filters from the entire model |

## The Key Distinction: Query-Level vs External Filters

| Filter source | ALLSELECTED behaviour |
|-------------|----------------------|
| Slicer on the same visual | **Removed** (query-level) |
| Slicer on a different visual | **Preserved** (external) |
| Report-level filter | **Preserved** (external) |
| Cross-filter from another visual | **Preserved** (external) |

## Example

```dax
Total Sales = SUM(Sales[Amount])

-- Shows sales ignoring this visual's internal Category filter
-- but respecting external Region slicer selection
Sales ALLSELECTED =
CALCULATE(
    [Total Sales],
    ALLSELECTED(DimProduct[Category])
)
```

When the Category slicer on the same visual is set to "Electronics":
- `Total Sales` = Electronics only
- `Sales ALLSELECTED` = Total across all categories (ignores internal filter)
- But if a Region slicer (external) is set to "North": `Sales ALLSELECTED` = All categories × North region

## ALLSELECTED vs ALL

| Scenario | ALL result | ALLSELECTED result |
|---------|-----------|-------------------|
| No internal query filters (select all) | Grand total | Grand total (same) |
| Category filter active on same visual | Grand total | Grand total |
| Category filter + external Region filter | Grand total (ignores both) | Total across categories × selected Region |

## Common Use Cases

| Use case | Why ALLSELECTED |
|---------|---------------|
| % of page total | Show each category's share of the overall total respecting external filters |
| Ranking within a filtered context | Rank products within the currently selected region |
| Totals row in a matrix | Show correct totals that respect the page-level filters |

## Related

- [[ALL-Function-DAX]]
- [[ALLEXCEPT-Function-DAX]]
- [[ALL-ALLSELECTED-ALLEXCEPT-Comparison]]
