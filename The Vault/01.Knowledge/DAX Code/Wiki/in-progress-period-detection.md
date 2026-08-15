---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Time Hacks: Mastering Dynamic Date Views
note_type: pattern
tags: [dax, pattern, time-frame, date, in-progress, switch, selectedvalue]
---

# "In Progress" Period Detection (Weekly+6 > MaxDate, EOMONTH > MaxDate)

Appends "(In Progress)" to the time frame label when the selected period is ongoing and not yet complete.

```dax
Time frame =
VAR _IsInProgress =
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields])
            = "'Calendar'[Weekly]"
            && [Maximum Week] + 6 > [Maximum Date],
            " (In Progress)",

        SELECTEDVALUE('Date Granularity'[Data Granularity Fields])
            = "'Calendar'[Monthly]"
            && EOMONTH([Maximum Month], 0) > [Maximum Date],
            " (In Progress)"
    )
VAR _TimeFrame =
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields])
            = "'Calendar'[Daily]",
            "As of " & FORMAT([Maximum Date], "mmm d yyyy"),

        SELECTEDVALUE('Date Granularity'[Data Granularity Fields])
            = "'Calendar'[Weekly]",
            "For the week of " & FORMAT([Maximum Week], "mmm d yyyy"),

        SELECTEDVALUE('Date Granularity'[Data Granularity Fields])
            = "'Calendar'[Monthly]",
            "For the month of " & FORMAT([Maximum Month], "mmm yyyy")
    )
RETURN _TimeFrame & _IsInProgress
```

**Logic:**

- `Weekly` → if the Saturday of the week (`Maximum Week + 6`) is after the last data date, the week is still in progress
- `Monthly` → if the end-of-month (`EOMONTH(Maximum Month, 0)`) is after the last data date, the month is still in progress
- `Daily` → never "in progress" (the day either has data or doesn't)

> Combine with `dynamic-granularity-aggregation-switch.md` for the full KPI card label.
