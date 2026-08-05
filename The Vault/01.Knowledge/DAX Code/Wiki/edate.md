---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: function
tags: [date-arithmetic, time-intelligence, period-slicer]
related: [SELECTEDVALUE, SWITCH, TOTALYTD, SAMEPERIODLASTYEAR]
---

# EDATE

Returns the date that is the specified number of months before or after a start date.

## Signature

```dax
EDATE(<startDate>, <months>)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `startDate` | Date | The start date |
| `months` | Integer | Number of months to add (positive) or subtract (negative) |

## Returns

A single date value, the result of shifting `startDate` by `months` months.

## Examples

**Time period slicer — dynamic minimum date (Bittar technique):**
```dax
Maximum Date = MAX('Stock Data'[Date])

Minimum Date =
VAR _MaxDate = [Maximum Date]
VAR _SelectedPeriod = SELECTEDVALUE(Period[Period])
VAR _MinimumDate =
    SWITCH(
        TRUE(),
        _SelectedPeriod = "1W", _MaxDate - 7,
        _SelectedPeriod = "1M", EDATE(_MaxDate, -1),
        _SelectedPeriod = "6M", EDATE(_MaxDate, -6),
        _SelectedPeriod = "1Y", EDATE(_MaxDate, -12)
    )
RETURN _MinimumDate
```

**Previous period comparison:**
```dax
Sales Prior Period =
    VAR _CurrentDate = MAX('Sales'[Date])
    VAR _PriorDate = EDATE(_CurrentDate, -1)
    RETURN
        CALCULATE(
            [Total Sales],
            'Sales'[Date] <= _PriorDate,
            'Sales'[Date] >= EDATE(_PriorDate, -1)
        )
```

**Month-over-month flag:**
```dax
Is Current Month =
    VAR _Today = TODAY()
    VAR _MonthStart = DATE(YEAR(_Today), MONTH(_Today), 1)
    RETURN
        IF(MAX('Sales'[Date]) >= _MonthStart, TRUE(), FALSE())
```

## Notes

- `EDATE` shifts by whole months — it preserves the day-of-month when possible. If the result month has fewer days than the start day, the last day of the result month is used.
- Often used inside `SWITCH(TRUE(), ...)` with `SELECTEDVALUE(Period[Period])` to implement user-selectable date ranges for stock/financial dashboards.
- In Bittar's Market Watch article, `EDATE` is the core of the time period slicer pattern — the user's period selection determines how many months to subtract from the maximum date.
- Combine with `MAX(<date column>)` or `LASTDATE()` to anchor to the most recent data point, then subtract months dynamically.
- `EOMONTH` (end-of-month) is the sibling function — use it when you need the last day of the shifted month.

## Related

- [[SELECTEDVALUE]] — read the user's period selection
- [[SWITCH]] — branch on period type
- [[SAMEPERIODLASTYEAR]] — equivalent for year-over-year comparisons
- [[TOTALYTD]] / [[TOTALQTD]] / [[TOTALMTD]] — built-in period aggregations
