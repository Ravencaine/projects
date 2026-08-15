---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 3
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-3-f152d1b500b5
note_type: function
tags: [dax, date, time-intelligence, anchor]
---

# STARTOFMONTH — Anchor to First Day of Month

`STARTOFMONTH(<date_column>)` returns the first date of the month in the current filter context. Used inside `CALCULATE` to retrieve a value from a row that is keyed to the first-of-month — regardless of which day the user has selected.

## Syntax

```dax
STARTOFMONTH(<date_column>)
```

Returns a scalar date — the earliest date in the current filter context's month.

## Use Case: Monthly Target Lookups

Production targets stored as one row per month (at the first of month). When the user selects any day in January, the target for that month must be retrieved:

```dax
MEASURE [HL_PT_Monthly] =
CALCULATE(
    SUM('ProductionTargets'[MonthlyTarget_HL_Static]),
    STARTOFMONTH(dateTable[Date])
)
```

Without `STARTOFMONTH`, a filter on `dateTable[Date] = DATE(2024, 1, 15)` would fail to find the monthly target row because its date column holds `2024-01-01`.

## vs. Other Date Anchoring Functions

| Function | Returns |
|---------|---------|
| `STARTOFMONTH(col)` | First date of the month |
| `STARTOFYEAR(col)` | First date of the year |
| `STARTOFQUARTER(col)` | First date of the quarter |

## Related

- [[Dynamic-Goal-Selection-via-SELECTEDVALUE]] — uses STARTOFMONTH to anchor monthly targets
- [[Time-Intelligence-Functions-Reference]] — full time intelligence reference
