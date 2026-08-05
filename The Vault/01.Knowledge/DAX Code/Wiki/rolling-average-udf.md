---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, rolling-window, average, time-intelligence, datesinperiod, power-bi]
---

# RollingAverage — Rolling Window Average

Calculates an average over a trailing N-period window. Uses `DISTINCTCOUNT` on appropriate time grain for the denominator.

## Signature

```c
UDF RollingAverage =
    ( base : AnyRef expr,
      n    : INT64,
      unit : STRING   // "DAY" | "WEEK" | "MONTH" | "QUARTER" | "YEAR"
    ) => ...
```

## Denominator Logic

| Unit | Denominator |
|------|-------------|
| DAY/DAYS/WEEK/WEEKS | `DISTINCTCOUNT('Date'[Date])` |
| MONTH/MONTHS | `DISTINCTCOUNT('Date'[Year] & "-" & 'Date'[MonthNo])` |
| QUARTER/QUARTERS | `DISTINCTCOUNT('Date'[Year] & "-" & 'Date'[Quarter])` |
| YEAR/YEARS | `DISTINCTCOUNT('Date'[Year])` |

Uses grain-aware denominator so monthly avg = sum/months, not sum/days.

## Config

`// 🔧 CONFIG` — change `'Date'[Date]`, `'Date'[Year]`, `'Date'[MonthNo]`, `'Date'[Quarter]`.

## Usage

```c
Total Sales := SUM(Sales[SalesAmount])

Avg Daily Sales (7D)  := RollingAverage([Total Sales], 7,  "DAY")
Avg Monthly Sales (6M) := RollingAverage([Total Sales], 6,  "MONTH")
```

## Related

- [[rolling-total-udf]]
