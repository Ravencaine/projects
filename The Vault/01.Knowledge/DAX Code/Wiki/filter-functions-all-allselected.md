---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, filter-functions, beginner, all, allselected, removefilters, percent-of-total]
---

# Filter Functions: ALL and ALLSELECTED

Removing filters is as important as applying them. ALL and ALLSELECTED are the primary tools.

## ALL — Remove All Filters

ALL removes filters from a table or column. Used inside CALCULATE to get a denominator for % of total calculations.

```dax
Revenue % of Total =
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(Products))
)
```

For each category row:
- Numerator: revenue for that category (filtered by the table visual)
- Denominator: ALL revenue across all categories (ALL removed the Product filter)

Result: each category as a percentage of the grand total.

## ALLSELECTED — Respect Visual Filters

**ALL:** Ignores everything, including what's selected in the visual.

**ALLSELECTED:** Ignores row context from the table/Matrix but respects page/report-level slicers.

```dax
Revenue % of Filtered Total =
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALLSELECTED(Products))
)
```

If a Year slicer is set to 2024:
- ALLSELECTED denominator = 2024 total (respects the Year slicer)
- ALL denominator = all-time total (ignores the Year slicer)

Use ALLSELECTED when "total" should mean "what the user is currently looking at."

## REMOVEFILTERS — Modern ALL

REMOVEFILTERS does the same thing as ALL but is more explicit:

```dax
// These are identical:
CALCULATE([Total Revenue], ALL(Products))
CALCULATE([Total Revenue], REMOVEFILTERS(Products))
```

REMOVEFILTERS reads more naturally: "remove filters from Products."

```dax
// Remove filters from specific columns:
CALCULATE(
    [Total Revenue],
    REMOVEFILTERS(Date[Month]),
    REMOVEFILTERS(Date[Quarter])
)
```

## Real Example: Grand Total in a Matrix

```dax
Company Total Revenue =
CALCULATE(
    [Total Revenue],
    ALL()   // Removes ALL filters from the entire model
)
```

When placed in a Matrix visual, this shows the grand total on every row — useful for "% of Total" comparisons at a glance.

## ALL on a Single Column

```dax
// Remove filter from one column only (keeps others)
Revenue All Categories =
CALCULATE(
    [Total Revenue],
    ALL(Products[ProductCategory])
)
```

The category filter is removed but other filters (Year, CustomerSegment) are preserved.

## Related

- [[calculate-context-modifier]] — CALCULATE is where ALL and ALLSELECTED are used
- [[filter-functions-allexcept-keepfilters]] — ALLEXCEPT and KEEPFILTERS for more targeted control
- [[advanced-patterns-ranking-abc-pareto]] — ALLSELECTED used in ranking and Pareto patterns
