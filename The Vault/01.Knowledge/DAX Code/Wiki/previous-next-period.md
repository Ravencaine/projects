---
created: 2026-07-26
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

## Notes

- All return a **table** — must be used inside CALCULATE
- PREVIOUS/NEXT WEEK require a calendar (ISO week dates)
- `PREVIOUSYEAR` and `NEXTYEAR` accept `year_end_date` for fiscal years
- Discouraged in visual calculations — likely returns meaningless results
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[dateadd]], [[sameperiodlastyear]]

## Related

- [[dateadd]]
- [[sameperiodlastyear]]
