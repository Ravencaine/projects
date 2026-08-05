---
created: 2026-08-02
updated: 2026-08-02
source: Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included).md
note_type: pattern
tags: [dax, pattern, visual-calculation, isatlevel, guard, hierarchy]
---

# ISATLEVEL Guard Pattern

`ISATLEVEL()` is a visual calculation function that returns `TRUE` when the current evaluation context is at a specific field level in the visual's row hierarchy. It is used as a guard to prevent misleading values from appearing at rollup levels.

## Syntax

```dax
ISATLEVEL([FieldName])
```

Returns `TRUE` if the current row in the visual is at the `[FieldName]` level. Returns `FALSE` when the visual has rolled up to a higher aggregation level.

## Use Case

Prevent a 3-month rolling average from displaying on a Year total row:

```dax
Avg Past 3 Months =
IF(
    ISATLEVEL([Month]),
    FORMAT(MOVINGAVERAGE([Total Sales], 3), "#,#.0")
)
```

Without the `ISATLEVEL` guard, the `MOVINGAVERAGE` would show a misleading average on the Year total row — aggregating beyond its intended window.

## What ISATLEVEL Returns By Context

| Visual Row Context | `ISATLEVEL([Month])` |
|---|---|
| January (Month level) | `TRUE` |
| February (Month level) | `TRUE` |
| 2007 Total (Year level) | `FALSE` |

## Common Use Cases for ISATLEVEL

| Scenario | Pattern |
|---|---|
| Rolling average on detail rows only | Wrap MOVINGAVERAGE with `IF(ISATLEVEL([Date]), ...)` |
| Running total on detail rows | Guard RUNNINGSUM or OFFSET with ISATLEVEL |
| % of row total (not column total) | Guard denominator to ensure row-level context |

## Related

- [[movingaverage-visual-calc]] — `function`
- [[visual-calculations-what-they-are]] — `atomic`
