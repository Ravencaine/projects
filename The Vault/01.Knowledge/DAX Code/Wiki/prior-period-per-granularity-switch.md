---
created: 2026-08-02
source: Power BI Time Hacks: Mastering Dynamic Date Views
note_type: pattern
tags: [dax, pattern, prior-period, date, dateadd, edate, switch, field-parameter]
---

# Prior-Period Calculation Per Granularity (Date−1, Week−7, EDATE)

Derives the prior period date for each granularity so the same measure can compute DoD/ WoW/MoM variation without duplicating logic.

```dax
Trading Volume Display Value Date Before =
VAR _MaxDate  = [Maximum Date] - 1      -- prior day
VAR _MaxWeek  = [Maximum Week] - 7       -- prior week
VAR _MaxMonth = EDATE([Maximum Month],-1) -- prior month
VAR _Volume   =
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields])
            = "'Calendar'[Daily]",
            CALCULATE(
                [Trading Volume],
                FILTER('Calendar', 'Calendar'[Daily] = _MaxDate)
            ),

        SELECTEDVALUE('Date Granularity'[Data Granularity Fields])
            = "'Calendar'[Weekly]",
            CALCULATE(
                [Trading Volume],
                FILTER('Calendar', 'Calendar'[Weekly] = _MaxWeek)
            ),

        SELECTEDVALUE('Date Granularity'[Data Granularity Fields])
            = "'Calendar'[Monthly]",
            CALCULATE(
                [Trading Volume],
                FILTER('Calendar', 'Calendar'[Monthly] = _MaxMonth)
            )
    )
RETURN _Volume
```

**Prior period offsets:**

- `Daily` → `_maxDate - 1`
- `Weekly` → `_maxWeek - 7` (7 days)
- `Monthly` → `EDATE(_maxMonth, -1)` (same day-of-month, prior month)

> Combine with `dynamic-granularity-aggregation-switch.md` for the full variation pattern.
