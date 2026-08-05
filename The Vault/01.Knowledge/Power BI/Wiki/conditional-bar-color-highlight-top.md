---
created: 2026-08-02
source: Elevate Your Power BI Bar Charts with 6 Simple Improvements.md
note_type: pattern
tags: [powerbi, dax, conditional-formatting, color, bar-chart, top-performer]
---

# Conditional Bar Color — Highlight Top Performer

A DAX measure that compares each bar's value to the overall top value and returns a distinct color for the top bar while applying a default color to all others.

## Purpose

Color-coding the top bar in a distinct shade draws immediate attention to the most important insight — the highest performer — without cluttering the visual with unnecessary formatting. The top value is computed under the full filter context (ignoring category-level filters on the bar axis) so it always reflects the true global maximum.

## Structure

```dax
Color bar chart =
VAR _TopRegion =
    CALCULATE(
        [Top Value],
        ALL('Postes vacants'[Région administrative], 'Postes vacants'[Organisme])
    )
VAR _Color =
    IF(
        [Vacant positions] = _TopRegion,
        "#DA6E76",
        "#04A88D"
    )
RETURN _Color
```

## How It Works

1. `CALCULATE([Top Value], ALL(...))` — removes the visual's own row context (region and institution columns) to compute the true global maximum. The `ALL` ignores both the Y-axis (region) and any sub-category (institution) on the visual.
2. `IF([Vacant positions] = _TopRegion, ...)` — compares the current bar's value to the global maximum. Returns a highlight color for the top bar, default color for all others.
3. Applied via **Conditional formatting → Field value** on the bar chart's Data colors.

## Key Design Decisions

- `ALL(table[Col1], table[Col2])` removes both the row and any drill-down dimensions from context, ensuring the top-value calculation is independent of what's on the visual axis.
- Without `ALL`, the top-value would be computed per bar, always returning the bar's own value — defeating the purpose.
- Use distinct, contrasting colors: one for the top performer, one for all others.

## Variations

- **Multi-tier highlighting:** Use `SWITCH(TRUE(), [value] = top, "#DA6E76", [value] >= median, "#F5B041", "#04A88D")` for three levels (top, above-median, below-median).
- **Second-place highlight:** Compare to the second-highest value using `TOPN(2, ALLSELECTED(...), [value], DESC)` to highlight both top and runner-up.

## Related

- [[insight-driven-dynamic-chart-title]]
- [[6-bar-chart-elevations]]
