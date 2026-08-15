---
created: 2026-08-14
source: 4 ways to use error bars in Power BI - small feature, big impact.md
note_type: atomic
tags: [error-bars, power-bi, pattern]
---

# Dummy0 Lower-Bound Anchor

A measure that always returns 0, used as the lower bound in an error bar configuration so the error bar draws from the chart baseline to the upper bound value.

## Definition

```dax
Dummy0 = 0
```

When set as the lower bound of an error bar whose upper bound is a non-zero value, the error bar draws a vertical line from the chart's zero baseline to the upper bound position. This is the foundational building block for data flags in column charts.

## Key Points

- **Baseline anchor** — the error bar starts exactly at y = 0 (the chart's value-axis origin), regardless of the data range
- **Always returns 0** — no filter context dependencies, no CALCULATE needed
- **Enables vertical flag lines** — paired with a conditional upper bound (returning BLANK() for non-target categories), the error bar appears only at specified positions as a vertical flag
- **Alternative: match upper bound** — for symmetrical decorations (e.g., centered rounded bars), set both upper and lower bounds to the same value or use `Upper = 0%`, `Lower = 100%` with By Percentage type

## Related

- [[Error-Bar-Data-Flags]]
- [[Error-Bars-as-Invisible-Anchors]]
