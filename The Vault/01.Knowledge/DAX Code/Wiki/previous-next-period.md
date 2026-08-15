---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, time-intelligence]
---

# PREVIOUS / NEXT: Day, Week, Month, Quarter, Year

Move the date filter backward or forward by one standard period.

## PREVIOUS Functions

| Function | Returns | Works with |
|----------|---------|------------|
| `PREVIOUSDAY(<dates>)` | Table — all dates representing the day before the first date in context | Date column, calendar |
| `PREVIOUSWEEK(<calendar>)` | Table — all dates of the previous week | Calendar only |
| `PREVIOUSMONTH(<dates>)` | Table — all dates of the previous month | Date column, calendar |
| `PREVIOUSQUARTER(<dates>)` | Table — all dates of the previous quarter | Date column, calendar |
| `PREVIOUSYEAR(<dates>[, <year_end_date>])` | Table — all dates of the previous year | Date column, calendar |

## NEXT Functions

| Function | Returns | Works with |
|----------|---------|------------|
| `NEXTDAY(<dates>)` | Table — all dates of the next day | Date column, calendar |
| `NEXTWEEK(<calendar>)` | Table — all dates of the next week | Calendar only |
| `NEXTMONTH(<dates>)` | Table — all dates of the next month | Date column, calendar |
| `NEXTQUARTER(<dates>)` | Table — all dates of the next quarter | Date column, calendar |
| `NEXTYEAR(<dates>[, <year_end_date>])` | Table — all dates of the next year | Date column, calendar |

## Examples

```dax
-- Previous day sales
Sales Yesterday = CALCULATE([Sales], PREVIOUSDAY('Date'[Date]))

-- Previous month sales
Sales Prev Month = CALCULATE([Sales], PREVIOUSMONTH('Date'[Date]))

-- Year-over-year comparison
YoY Growth = DIVIDE([Sales] - CALCULATE([Sales], PREVIOUSYEAR('Date'[Date])), CALCULATE([Sales], PREVIOUSYEAR('Date'[Date])))
```

## PREVIOUS — Visual Calculation Variant

`PREVIOUS()` in a visual calculation is a **different function** from the PREVIOUSDAY/PREVIOUSMONTH/PREVIOUSYEAR time-intelligence family. It retrieves the value of a measure from the previous row or column in the **visual calculation data grid**, without needing to recalculate via the storage engine.

```dax
PREVIOUS( <Measure> [, <Steps>] [, <Axis>] [, <OrderBy>] [, <Blanks>] [, <Reset>] )
```

| Parameter | Description |
|-----------|-------------|
| `<Measure>` | The measure to retrieve (e.g., `[Sales Amount]`) |
| `<Steps>` | Number of steps back (default 1) |
| `<Axis>` | `ROWS`, `COLUMNS`, or `ROWS COLUMNS` — which axis to navigate |
| `<OrderBy>` | Optional ordering for the axis |
| `<Blanks>` | How to handle blanks |
| `<Reset>` | Reset navigation at certain boundaries |

### Example — YoY% in a Visual Calculation

```dax
YOY % =
VAR CY = [# Customers]
VAR PY = PREVIOUS([# Customers], COLUMNS)
RETURN DIVIDE(CY - PY, PY)
```

### Performance Characteristics

`PREVIOUS()` in a visual calculation reads from the **precomputed virtual table:** no new storage engine query is fired for each cell. This makes it significantly faster than `SAMEPERIODLASTYEAR` when the virtual table is small (~110 rows). However, for large virtual tables (~1.7M rows), the densification overhead makes it 4× slower than the measure-based equivalent.

See [[VC-vs-Measure-Performance-Decision]] for the full decision framework.

## Notes

- All time-intelligence PREVIOUS/NEXT return a **table**: must be used inside CALCULATE
- PREVIOUS/NEXT WEEK require a calendar (ISO week dates)
- `PREVIOUSYEAR` and `NEXTYEAR` accept `year_end_date` for fiscal years
- Not supported in DirectQuery mode for calculated columns or RLS rules
- The visual calculation `PREVIOUS()` is a separate function — see [[PREVIOUS-YoY-VC-Pattern]] for the VC variant

## Related

- [[PREVIOUS-YoY-VC-Pattern]] — ready-to-use VC pattern using `PREVIOUS(COLUMNS)`
- [[VC-vs-Measure-Performance-Decision]] — when to use VC PREVIOUS vs measure with SAMEPERIODLASTYEAR
- [[dateadd]]
- [[sameperiodlastyear]]
