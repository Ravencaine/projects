---
created: 2026-08-09
updated: 2026-08-09
source: "Build a Dynamic Excel Report with Just 4 Formulas • My Online Training Hub"
note_type: pattern
tags: [excel, dynamic-arrays, filter, boolean-logic, and, or, multiply, add, conditions]
see_also: [FILTER-Boolean-AND-OR-Logic]
---

# FILTER Boolean AND/OR Logic

Inside FILTER's include argument, boolean multiplication (`*`) implements AND logic and boolean addition (`+`) implements OR logic. Each condition returns TRUE (1) or FALSE (0); combining them with * or + creates compound conditions without IF.

## AND Logic (Multiplication)

```
=FILTER(SalesData,
  (SalesData[Country]=D4) *
  (SalesData[Category]=D5),
  "No results found"
)
```

| Condition A | Condition B | A × B | Row included? |
|-------------|-------------|-------|---------------|
| TRUE (1) | TRUE (1) | 1 | ✓ |
| TRUE (1) | FALSE (0) | 0 | ✗ |
| FALSE (0) | TRUE (1) | 0 | ✗ |
| FALSE (0) | FALSE (0) | 0 | ✗ |

Multiplication by 0 (FALSE) zeroes out the row — standard AND logic.

## OR Logic (Addition)

```
=FILTER(SalesData,
  (SalesData[Country]="Japan") +
  (SalesData[Country]="Germany"),
  "No results found"
)
```

| Condition A | Condition B | A + B | Row included? |
|------------|-------------|-------|---------------|
| 1 | 0 | 1 | ✓ |
| 0 | 1 | 1 | ✓ |
| 1 | 1 | 2 | ✓ |
| 0 | 0 | 0 | ✗ |

Non-zero = TRUE, zero = FALSE. Any non-zero sum = row included.

## Why No IF Needed

FILTER's include argument is already a boolean expression. Returning TRUE = include, FALSE = exclude. `*` and `+` let you build compound booleans without nested IF.

## Related

- [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy]] — source
- [[SUMIFS-COUNTIFS-Replace-IF-Helper-Columns]] — SUMIFS replaces IF helper columns for aggregation; FILTER replaces IF for row-level filtering
