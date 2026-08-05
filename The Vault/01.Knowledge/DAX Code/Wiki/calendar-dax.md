---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: function
tags: [dax, date-table, calendar, time-intelligence]
---

# CALENDAR — DAX Date Table Generator

Returns a single-column table of dates between a start and end date. The standard DAX approach for creating a Date Table when you want explicit control over the range.

## Signature

```
CALENDAR(<start_date>, <end_date>)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<start_date>` | Date/Datetime | First date in the returned table |
| `<end_date>` | Date/Datetime | Last date in the returned table |

## Returns

A single-column table with one row per date, column named `Date`.

## Examples

```dax
-- Static date range:
DateTable =
CALENDAR (
    DATE ( 2018, 1, 1 ),
    DATE ( 2026, 12, 31 )
)

-- Dynamic range from fact table:
DateTable =
VAR MinDate = MIN ( FactSales[OrderDate] )
VAR MaxDate = MAX ( FactSales[OrderDate] )
RETURN
    CALENDAR ( MinDate, MaxDate )
```

## Notes

- Both arguments must resolve to dates — use `DATE()` for static values, `MIN()`/`MAX()` for dynamic ranges.
- `CALENDAR` returns a table; it must be used inside `ADDCOLUMNS` or similar to add Year, Month, Quarter, etc. columns.
- `CALENDAR` is faster than `CALENDARAUTO` when you know the range upfront.
- For fiscal year calendars, add a calculated column with the fiscal year logic after generating the table.

## Related

- [[calendarauto-dax]] — `function`
- [[power-query-date-table-build]] — `pattern`
- [[dax-date-table-build]] — `pattern`
- [[dax-vs-m-date-table-quick-reference]] — `reference`
