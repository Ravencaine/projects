---
created: 2026-08-02
updated: 2026-08-05
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, rolling-window, time-intelligence, datesinperiod, power-bi]
---

# RollingTotal — Rolling Window Total

Calculates a measure total over a trailing N-period window anchored on the latest visible date.

## Signature

```c
UDF RollingTotal =
    ( base : AnyRef expr,
      n    : INT64,
      unit : STRING   // "DAY" | "WEEK" | "MONTH" | "QUARTER" | "YEAR"
    ) => ...
```

## Implementation Notes

- Window **ends at `MAX('Date'[Date])`:** adapts to filter context
- Weeks implemented as `7 * n` days (DAX has no week unit for `DATESINPERIOD`)
- Returns `BLANK()` when the date window is empty

## Config

`// 🔧 CONFIG` — change `'Date'[Date]` to your date column.

## Usage

```c
Total Sales := SUM(Sales[SalesAmount])

Sales (30D) := RollingTotal([Total Sales], 30, "DAY")
Sales (12M) := RollingTotal([Total Sales], 12, "MONTH")
Sales (4Q)  := RollingTotal([Total Sales], 4,  "QUARTER")
```

## Combining with CompareOverPeriodRange

```c
// Compare 30D rolling vs. prior 30D
Sales (30D Prior) :=
    CompareOverPeriodRange([Sales (30D)], "DoD", "VALUE")
```

## Related

- [[rolling-average-udf]]
- [[compareoverperiodrange-udf-whole-period-time-comparisons]]
