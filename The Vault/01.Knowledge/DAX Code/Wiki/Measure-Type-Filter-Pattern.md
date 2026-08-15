---
created: 2026-08-09
updated: 2026-08-09
source: "⚡How I Built a Modern Oblique Area Chart in Power BI (Using Only Native Visuals)"
note_type: pattern
tags: [dax, calculate, filter, measure-type, row-context, average, max, min, vital-stats, healthcare]
---

# Measure Type Filter Pattern (Average/Max/Min)

When a single column stores multiple metric types as text values (e.g. "Average", "Max", "Min"), use CALCULATE + FILTER to isolate each one. FILTER iterates the table and applies the text filter in row context.

## Formula

```dax
Average Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER(
            'Vital Stats',
            'Vital Stats'[Measure Type] = "Average"
        )
    )

Max Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER(
            'Vital Stats',
            'Vital Stats'[Measure Type] = "Max"
        )
    )

Min Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER(
            'Vital Stats',
            'Vital Stats'[Measure Type] = "Min"
        )
    )
```

## How It Works

| Step | Expression | Role |
|------|-----------|------|
| 1 | `SUM('Vital Stats'[Value])` | Aggregation to apply |
| 2 | `CALCULATE(..., ...)` | Context transition: row context → filter context |
| 3 | `FILTER('Vital Stats', condition)` | Iterates table; keeps rows where condition = TRUE |
| 4 | `'[Measure Type] = "Average"'` | Text equality filter on the metric type column |

## Why FILTER Inside CALCULATE

FILTER iterates the table in **row context**. CALCULATE transitions that row context into a **filter context**. Without CALCULATE, the filter would apply at the existing context level rather than as an independent filter.

## Use Cases

- Vital signs: Average/Max/Min of Heart Rate, BP, SpO2 stored in one column
- Financial: Actual/Budget/Forecast stored as rows
- Performance: Best/Worst/Average in one column

## Related

- [[Source-Oblique-Area-Chart-Native-Visuals-Isabelle-Bittar]] — source
- [[MAXX-MINX-ALL-Date-Dynamic-Range]] — builds on these measures; MAXX/MINX over ALL(Date) removes context
- [[VAR-for-Intermediate-Measure-Calculation]] — intermediate variable pattern for cleaner multi-step measures
