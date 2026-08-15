---
created: 2026-08-10
updated: 2026-08-10
source: Calculation Groups for YoY, MoM & QoQ in Power BI — Powerful, but Maybe Not Worth It?
source_url: https://medium.com/microsoft-power-bi/calculation-groups-for-yoy-mom-qoq-in-power-bi-powerful-but-maybe-not-worth-it-86d996dbd471
note_type: pattern
tags: [dax, calculation-groups, selectedmeasure, guard, defensive-dax, time-intelligence]
---

# ISNUMBER Guard for Calculation Items

Every calculation item that performs numeric operations must guard against non-numeric measures. Without this guard, text measures, SVG measures, color measures, and formatting labels break the visual when the calculation group applies to them.

## The Pattern

```dax
MoM =
IF(
    NOT ISNUMBER( SELECTEDMEASURE() ),
    SELECTEDMEASURE(),
    VAR Prev =
        CALCULATE(
            SELECTEDMEASURE(),
            DATEADD('Dates'[Date], -1, MONTH)
        )
    RETURN
        SELECTEDMEASURE() - Prev
)
```

## Why the Guard Is Required

Calculation groups apply globally — they have no concept of "this measure should be skipped." When the calculation group slicer or context is active:
- `SELECTEDMEASURE()` returns whatever measure the visual is currently rendering
- If that measure is a text label, SVG string, or color hex code, arithmetic on it causes an error
- The guard short-circuits: return the raw value instead of applying the transformation

## When to Apply This Guard

Wrap any calculation item that does arithmetic in `IF(NOT ISNUMBER(...))`:
- YoY, QoQ, MoM delta (subtraction)
- % change (division)
- Running totals
- Any ratio or percentage calculation

Items that simply return `SELECTEDMEASURE()` without arithmetic (e.g., "Current") do not need the guard.

## Variations

For percentage calculations, guard against division by zero as well:

```dax
YoY% =
IF(
    NOT ISNUMBER( SELECTEDMEASURE() ),
    SELECTEDMEASURE(),
    VAR Prev = CALCULATE( SELECTEDMEASURE(), SAMEPERIODLASTYEAR('Dates'[Date]) )
    VAR Result = DIVIDE( SELECTEDMEASURE() - Prev, Prev )
    RETURN
        IF( ISBLANK(Result) || Prev = 0, BLANK(), Result )
)
```

## Related

- [[Calculation-Group-Time-Intelligence-Reference]] — full Current/MoM/QoQ/YoY implementation
- [[Five-DAX-Pitfalls-and-Fixes]] — other common DAX pitfalls
