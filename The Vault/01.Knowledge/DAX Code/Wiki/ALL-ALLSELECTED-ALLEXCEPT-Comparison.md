---
created: 2026-08-05
updated: 2026-08-05
source: ALL, ALLSELECTED and ALLEXCEPT DAX Filter Function (Boniface Muchendu)
note_type: comparison
tags: [dax, all, allselected, allexcept, comparison, filter-context]
---

# ALL vs ALLSELECTED vs ALLEXCEPT

Side-by-side comparison of the three DAX filter-removal functions: ALL, ALLSELECTED, and ALLEXCEPT — covering what each removes, what each keeps, parameter order, and when to use each.

## At a Glance

| Feature | ALL | ALLSELECTED | ALLEXCEPT |
|---------|-----|------------|----------|
| Removes | All filters | Query-level filters only | All filters on table |
| Keeps | Nothing | External filters (outside query) | Explicitly listed columns |
| Return value | Table or column | Table or column | Table |
| Parameter order | Table or column first | Table or column first | **Table first, then columns** |
| No-arg form | ALL() = all rows | ALLSELECTED() = all rows | Not applicable |

## Filter Behaviour Matrix

| Filter source | ALL | ALLSELECTED | ALLEXCEPT(table, col) |
|-------------|-----|------------|----------------------|
| Same visual slicer | Removed | Removed | Removed |
| External slicer | Removed | **Preserved** | Removed |
| Report-level filter | Removed | **Preserved** | Removed |
| Specified column filter | Removed | Removed | **Preserved** |
| Other visual cross-filter | Removed | **Preserved** | Removed |

## Decision Guide

### Use ALL when:
- You want the absolute grand total — ignore all slicers, filters, and external selections
- Building a denominator for a "% of grand total" measure

### Use ALLSELECTED when:
- You want the total for the current page or visual context — respect external slicers, ignore internal ones
- Building "% of page total" or "ranking within a filtered set"

### Use ALLEXCEPT when:
- You want to remove filters on most columns but keep one or two specific slicers active
- "Ignore everything except X" is clearer than "remove filter X, remove filter Y, remove filter Z, keep filter A"

## Syntax Comparison

```dax
-- ALL: table or column first, multiple allowed
ALL(DimProduct)
ALL(DimProduct[Category])
ALL(DimProduct[Category], DimProduct[Color])

-- ALLSELECTED: same as ALL
ALLSELECTED(DimProduct)
ALLSELECTED(DimProduct[Category])

-- ALLEXCEPT: table FIRST, then columns to KEEP
ALLEXCEPT(Sales, DimDate[Year])
ALLEXCEPT(Sales, DimDate[Year], DimDate[Month])
```

## Example: "% of What" Measures

| Measure | Formula | Denominator |
|---------|---------|------------|
| % of Grand Total | `CALCULATE([Sales], ALL())` | Absolute grand total |
| % of Page Total | `CALCULATE([Sales], ALLSELECTED())` | Total respecting external filters |
| % of Year Total | `CALCULATE([Sales], ALLEXCEPT(Sales, DimDate[Year]))` | Total for selected year across all other dims |

## The Hierarchy

```
ALL          → removes EVERYTHING
ALLEXCEPT    → removes almost everything, keeps select columns
ALLSELECTED  → removes only query-level, keeps everything external
```

ALL is the most aggressive. ALLSELECTED is the most conservative.

## Related

- [[ALL-Function-DAX]]
- [[ALLSELECTED-Function-DAX]]
- [[ALLEXCEPT-Function-DAX]]
