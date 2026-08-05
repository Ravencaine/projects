---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, variance, week-over-week]
---

# OT Hours per FTE Variance

Absolute difference between this week's and last week's OT Hours per FTE.

## Signature

```dax
OT Hours per FTE Variance = [OT Hours per FTE This Week] - [OT Hours per FTE Last Week]
```

## Parameters

None — references two other measures.

## Returns

A decimal number. Positive = increase in OT. Negative = decrease.

## Examples

```dax
-- Show in chart (positive = bad for OT hours)
[OT Hours per FTE Variance]
```

## Notes

This is a simple subtraction between two branching measures. For conditional formatting in a chart, green = decrease (good) and red = increase (bad) — the logic is inverted compared to a sales growth metric. See `OT Hours per FTE Variance %` for the percentage form.

## Related

- [[OT-Hours-per-FTE-This-Week]]
- [[OT-Hours-per-FTE-Last-Week]]
- [[OT-Hours-per-FTE-Variance-Pct]]
