---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, time-intelligence]
---

# SAMEPERIODLASTYEAR and PARALLELPERIOD

Shift a date period one year back, or by a parallel period of any interval.

## SAMEPERIODLASTYEAR

```dax
SAMEPERIODLASTYEAR(<dates>)
```

Returns the same period shifted exactly one year back. Only shifts by year — no other interval.

```dax
Sales Last Year = CALCULATE([Sales], SAMEPERIODLASTYEAR('Date'[Date]))
```

**Note:** When used with a calendar table that includes a lunar year, SAMEPERIODLASTYEAR can produce different results than DATEADD — Feb 29 shifted back may become Mar 1 (since the target year has no Feb 29). For lunar calendars, prefer `DATEADD(Calendar, -13, MONTH)` instead.

## PARALLELPERIOD

```dax
PARALLELPERIOD(<dates>, <number_of_intervals>, <interval>)
```

Returns a table of dates shifted by N intervals, but preserves the full parallel period rather than just shifting individual dates.

| Parameter | Values |
|-----------|--------|
| `interval` | YEAR, QUARTER, MONTH, WEEK (calendar only) |
| `number_of_intervals` | Integer (positive = forward, negative = backward) |

```dax
-- Same quarter last year
Sales Same Qtr Last Year = CALCULATE([Sales], PARALLELPERIOD('Date'[Date], -1, QUARTER))
```

## SAMEPERIODLASTYEAR vs DATEADD vs PARALLELPERIOD

| Scenario | Function |
|----------|----------|
| Standard YTD comparison | SAMEPERIODLASTYEAR |
| Flexible interval shift | DATEADD |
| Full period comparison | PARALLELPERIOD |
| Lunar calendars | DATEADD(Calendar, -13, MONTH) |

## Notes

- All return a **table**: use inside CALCULATE
- SAMEPERIODLASTYEAR does not support fiscal year offsets
- PARALLELPERIOD fills gaps (if context has Mar 1–10, shifting back by YEAR gives Mar 1–10 of prior year even if those days don't exist)
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[dateadd]]

## Related

- [[dateadd]]
- [[dateadd-datesbetween-datesinperiod]]
