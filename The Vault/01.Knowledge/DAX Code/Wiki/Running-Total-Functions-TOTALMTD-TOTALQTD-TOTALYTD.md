---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Where Everything You've Learned About Context Finally Pays Off
source_url: https://medium.com/@jeseenaparveenk/dax-time-intelligence-where-everything-youve-learned-about-context-finally-pays-off-8de1bb67adcb
note_type: reference
tags: [dax, time-intelligence, totalmtd, totalqtd, totalytd, datesmtd, datesytd, running-total]
---

# Running Total Functions: TOTALMTD / TOTALQTD / TOTALYTD vs DATESMTD / DATESYTD

TOTAL* and DATES* versions do the same thing — cumulative totals from period start to current date. The TOTAL shortcuts wrap CALCULATE + DATES internally; the DATES versions give you the raw date table for custom combinations.

## TOTAL* — Shortcut for Simple Cumulative Totals

```dax
MTD Sales   = TOTALMTD(SUM(Sales[Amount]), Dates[Date])
QTD Sales   = TOTALQTD(SUM(Sales[Amount]), Dates[Date])
YTD Sales   = TOTALYTD(SUM(Sales[Amount]), Dates[Date])
```

Each accumulates from the start of its period to the last date in the current filter context.

### TOTALYTD — Optional Fiscal Year Parameter

```dax
Fiscal YTD Sales =
TOTALYTD(
    SUM(Sales[Amount]),
    Dates[Date],
    "06-30"   -- fiscal year ends June 30
)
```

Pass the fiscal year-end date string to override the default December 31 reset. Supports fiscal quarters and years with non-calendar boundaries.

## DATES* — Raw Date Table for Custom CALCULATE Combinations

```dax
YTD Sales =
CALCULATE(
    SUM(Sales[Amount]),
    DATESYTD(Dates[Date])
)
```

`DATESYTD` returns the same date table as `TOTALYTD` uses internally. Use the DATES versions when you need to combine the running total logic with other filters inside CALCULATE:

```dax
-- YTD sales for a specific region
YTD North Sales =
CALCULATE(
    SUM(Sales[Amount]),
    DATESYTD(Dates[Date]),
    Sales[Region] = "North"
)
```

## When to Use Which

| Situation | Use |
|-----------|-----|
| YTD/MTD/QTD is the only filter logic | `TOTALYTD` / `TOTALMTD` / `TOTALQTD` (cleaner) |
| Need to combine with other CALCULATE filters | `DATESYTD` / `DATESMTD` / `DATESQTD` |
| Fiscal year non-calendar | `TOTALYTD` with fiscal end parameter |

## Related

- [[Time-Intelligence-Is-CALCULATE-With-Date-Table]] — conceptual foundation: these are all CALCULATE with date table filters
- [[Date-Table-Must-Be-Marked-Requirement]] — prerequisite
