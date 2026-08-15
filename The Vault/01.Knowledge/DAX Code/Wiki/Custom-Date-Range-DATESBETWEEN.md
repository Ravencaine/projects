---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Where Everything You've Learned About Context Finally Pays Off
source_url: https://medium.com/@jeseenaparveenk/dax-time-intelligence-where-everything-youve-learned-about-context-finally-pays-off-8de1bb67adcb
note_type: reference
tags: [dax, time-intelligence, datesbetween, date, custom-range, fixed-range]
---

# Custom Date Range: DATESBETWEEN + DATE

`DATESBETWEEN` returns exactly the dates between two specified endpoints, inclusive. Use it when you need precise, fixed control over the date window — particularly for fiscal periods, ad-hoc ranges, or boundaries that don't align to standard calendar periods.

## DATESBETWEEN — Fixed Start and End

```dax
Sales in Custom Range =
CALCULATE(
    SUM(Sales[Amount]),
    DATESBETWEEN(
        Dates[Date],
        DATE(2024, 1, 1),   -- start
        DATE(2024, 6, 30)   -- end
    )
)
```

`DATE(year, month, day)` constructs a single date value — use it to specify fixed boundaries rather than relying on LASTDATE or FIRSTDATE.

## When to Use DATESBETWEEN

- **Fiscal period calculations** with custom boundaries (e.g., 4-4-5 retail calendars)
- **Ad-hoc reporting ranges** hardcoded into measures
- **Precisely bounded comparisons** where you need Oct 1–Dec 31 regardless of what the user's date slicer says
- **Replacement for TOTALYTD** when the fiscal year end is not a simple string like "06-30"

```dax
-- Equivalent to TOTALYTD with fiscal year end Jun 30
Fiscal YTD Sales =
CALCULATE(
    SUM(Sales[Amount]),
    DATESBETWEEN(
        Dates[Date],
        FIRSTDATE(DATESYTD(Dates[Date], "06-30")),
        LASTDATE(Dates[Date])
    )
)
```

## Caveat

`DATESBETWEEN` with hardcoded dates ignores the user's date slicer context. If the user filters to Feb–Apr 2025, a measure with `DATE(2024, 1, 1)` as the start will still return only Jan–Apr 2024 data. Be intentional about whether you want to respect or override the user's filter context.

## Related

- [[Running-Total-Functions-TOTALMTD-TOTALQTD-TOTALYTD]] — TOTALYTD fiscal year alternative
- [[Time-Intelligence-Is-CALCULATE-With-Date-Table]] — the conceptual model
