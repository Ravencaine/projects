---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: pattern
tags: [dax, udf, time-intelligence, yoy, qoq, mom, wow, dod, rolling-window, power-bi]
---

# CompareOverPeriodRange UDF — Whole-Period Time Comparisons

Anchors on the latest visible date and calculates the **entire prior period** (not just the parallel day). Returns prior value, delta, or percent change on demand.

## Signature

```c
UDF CompareOverPeriodRange =
    ( base : AnyRef expr,
      shift : STRING,    // "YOY" | "QoQ" | "MoM" | "WoW" | "DoD"
      mode : STRING      // "VALUE" | "DELTA" | "PCT"
    ) => ...
```

## Core Logic

```
today = MAX('Date'[Date])

current_period = shift_range(today, shift)
prior_period   = shift_range(today, shift) - 1

currVal  = CALCULATE(base, current_period)
priorVal = CALCULATE(base, prior_period)
delta    = currVal - priorVal
pct      = DIVIDE(delta, priorVal)

RETURN SWITCH(mode, "VALUE", priorVal, "DELTA", delta, "PCT", pct, pct)
```

## Period Definitions

| Shift | Current Period | Prior Period |
|-------|---------------|-------------|
| YOY | Jan 1 → today | Jan 1 (prev year) → Dec 31 (prev year) |
| QoQ | Quarter start → today | Quarter start (−3 months) → end of that quarter |
| MoM | 1st of month → today | 1st of month (−1) → end of that month |
| WoW | today−6 → today | today−13 → today−7 |
| DoD | today | today−1 |

## Usage

```c
Total Sales := SUM(Sales[SalesAmount])

YoY Sales % (period) := CompareOverPeriodRange([Total Sales], "YOY", "PCT")
QoQ Sales Δ (period)  := CompareOverPeriodRange([Total Sales], "QoQ", "DELTA")
MoM Sales (prior)     := CompareOverPeriodRange([Total Sales], "MoM", "VALUE")
```

## Key Design Points

- Anchors to `MAX('Date'[Date])` — adapts to any slicer/filter context
- Whole-period not parallel: QoQ compares full quarter-to-date vs. full prior quarter, not day-to-day
- `mode` parameter avoids duplicating the logic per output type
- Returns `BLANK()` when prior period is zero or blank

## Config

`// 🔧 CONFIG` — change `'Date'[Date]` to your Date table column if different.

## Related

- [[rolling-total-udf]] — rolling window KPIs
- [[rolling-average-udf]] — rolling window averages
- [[compareoverperiodrange-udf-whole-period-time-comparisons]] (function note)
