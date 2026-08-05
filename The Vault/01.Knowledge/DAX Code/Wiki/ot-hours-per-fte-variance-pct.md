---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, variance, week-over-week, percentage]
---

# OT Hours per FTE Variance %

Percentage change in OT Hours per FTE week-over-week.

## Signature

```dax
OT Hours per FTE Variance % =
    DIVIDE(
        [OT Hours per FTE Variance],
        [OT Hours per FTE Last Week]
    )
```

## Parameters

None — references two other measures.

## Returns

A decimal number expressed as a percentage. Positive = increase in OT. Negative = decrease.

## Examples

```dax
-- Used as Column Value in Dynamic Chart SWITCH (highlight order = 2)
OT Hours per FTE Variance %
```

## Notes

`DIVIDE` is used to handle the case where `[OT Hours per FTE Last Week]` is zero or blank. For OT hours specifically, a negative variance % is the desired outcome — lower overtime is better. Conditional formatting should display green for negative values and red for positive ones.

## Related

- [[OT-Hours-per-FTE-Variance]]
- [[OT-Hours-per-FTE-This-Week]]
- [[OT-Hours-per-FTE-Last-Week]]
