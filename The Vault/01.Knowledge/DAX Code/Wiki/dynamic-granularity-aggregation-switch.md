---
created: 2026-08-02
source: Power BI Time Hacks: Mastering Dynamic Date Views
note_type: pattern
tags: [dax, pattern, switch, selectedvalue, field-parameter, dynamic-aggregation, calendar]
---

# Dynamic Granularity Aggregation: SWITCH on SELECTEDVALUE(field_param)

A measure that aggregates the base metric differently depending on which calendar column the field parameter has selected on the visual axis.

```dax
Trading Volume Display Value =
VAR _MaxDate  = [Maximum Date]
VAR _MaxWeek  = [Maximum Week]
VAR _MaxMonth = [Maximum Month]
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

**Pattern:** `SELECTEDVALUE('Date Granularity'[...])` returns the full column reference string as selected in the field parameter. Match it against the literal string (including single-quote wrapping) and use `FILTER('Calendar', col = _maxValue)` to aggregate only the selected period.

> See `maximum-date-week-month-anti-blank.md` for the `Maximum Date/Week/Month` measures that feed `_MaxDate`, `_MaxWeek`, `_MaxMonth`.
