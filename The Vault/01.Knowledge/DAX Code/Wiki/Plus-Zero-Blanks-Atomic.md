---
created: 2026-08-05
updated: 2026-08-05
source: Blank Values in Power BI Reports (Boniface Muchendu)
note_type: atomic
tags: [dax, blank, isblank, measure, zero, quick-fix]
---

# `+ 0` Fix for Blank Values

Appending `+ 0` to any DAX measure forces it to return a numeric value instead of blank when the underlying data is empty — the fastest way to eliminate blank card values.

## Definition

Adding `+ 0` at the end of a measure expression. The addition operation converts a blank result to zero instead of propagating the blank.

## Code

```dax
// Before: returns blank when no matching rows
Sales = SUMX('SalesTable', 'SalesTable'[SalesAmount])

// After: returns 0 instead of blank
Sales = SUMX('SalesTable', 'SalesTable'[SalesAmount]) + 0
```

## How It Works

DAX blank values propagate through arithmetic: `BLANK + 0 = 0`. By appending `+ 0`, the blank result from the aggregation is coerced to zero before being returned from the measure.

## When to Use

- Card visuals that show a single KPI value
- Quick fix with no need for custom display text
- When blank and zero are semantically equivalent in the visual

## Warning: Chart Behaviour

In charts, `+ 0` converts blanks to zeros — meaning the chart will plot zero values for periods with no data instead of omitting the point. For charts, prefer `IF`-based solutions that keep the value blank.

## Related

- [[IF-Implicit-Blank-Check-Pattern]]
- [[Choosing-Blank-Value-Strategy]]
- [[New-Card-Visual-Blank-Setting]]
