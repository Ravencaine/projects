---
created: 2026-08-02
updated: 2026-08-02
source: Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included).md
note_type: function
tags: [dax, function, visual-calculation, movingaverage, rolling-average, time-series]
---

# MOVINGAVERAGE (Visual Calculation)

A visual-level DAX function that calculates a rolling window average directly within a Power BI visual, without needing a separate DAX measure in the model.

## Syntax

```dax
MOVINGAVERAGE(column, rows)
```

- `column` — the measure or column to average
- `rows` — number of rows in the moving window (including the current row)

## How It Works

`MOVINGAVERAGE([Total Sales], 3)` calculates the average of the current row and the previous 2 rows — a 3-row moving window. It operates within the visual's row context, not the model.

## Use Case

Rolling 3-month sales average in a table visual:

```dax
Avg Past 3 Months =
IF(
    ISATLEVEL([Month]),
    FORMAT(MOVINGAVERAGE([Total Sales], 3), "#,#.0")
)
```

## Key Properties

| Property | Value |
|---|---|
| Scope | Visual-level only — not a model measure |
| Context | Operates within the visual's row context |
| Row window | Current row + (N-1) preceding rows |
| Prerequisites | Right-click visual → New visual calculation |

## Visual Calculation vs Model Measures

| | Visual Calculation | Model Measure |
|---|---|---|
| Location | Inside a specific visual | In the model (reusable) |
| Row context | Respects visual's row ordering | Requires explicit context handling |
| Use when | Calculation is unique to one visual | Calculation is reused across visuals |

## Related

- [[visual-calculations-what-they-are]] — `atomic`
- [[isatlevel-guard-pattern]] — `pattern`
- [[format-visual-calc-returns-text]] — `gotcha`
