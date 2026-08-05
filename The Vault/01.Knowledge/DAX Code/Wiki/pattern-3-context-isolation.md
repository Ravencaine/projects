---
created: 2026-07-27
updated: 2026-08-02
source: "The 5 DAX Patterns Senior Analysts Use"
note_type: pattern
tags: [dax, context-isolation, calculate, filter-context, all, allselected]
---

# Pattern 3: Context Isolation

Measures are wrapped in CALCULATE with explicit ALL() or ALLSELECTED() to prevent unintended filter bleed from slicers, visuals, or other measures.

## Purpose

A measure should only react to the filters the analyst intends. Without explicit context isolation, a measure's denominator (for example) may inherit unexpected filters from the visual context.

## Components

- CALCULATE() — modifies filter context
- ALL() — removes a specific filter entirely
- ALLSELECTED() — removes visual/page-level filters but preserves report-level slicer selections
- REMOVEFILTERS() — equivalent to ALL() in newer DAX

## Structure

```dax
-- Without context isolation: denominator inherits visual filters
Bad Margin % := [Profit] / SUM(Products[Cost])  -- Cost sum may be filtered unexpectedly

-- With context isolation: denominator ignores product filter
Good Margin % :=
CALCULATE (
    DIVIDE ( [Profit], SUM ( Products[Cost] ), 0 ),
    ALL ( Products )  -- ignores any Product slicer/visual filter
)
```

## Common Use Cases

| Scenario | Function | Example |
|---------|---------|---------|
| Grand total as denominator | ALL() | `CALCULATE(..., ALL())` |
| Denominator ignores visual filter | ALL() | `CALCULATE(..., ALL(Products))` |
| Denominator ignores page filters but keeps slicers | ALLSELECTED() | `CALCULATE(..., ALLSELECTED())` |
| Remove all filters for grand total | ALL() | `CALCULATE(..., ALL(Date))` |

## Related

- [[calculate]]
- 
- [[filter]] — FILTER is often used inside CALCULATE as the first argument for explicit context modification
- [[calculate]] — context isolation is achieved by wrapping CALCULATE with ALL() or REMOVEFILTERS()
