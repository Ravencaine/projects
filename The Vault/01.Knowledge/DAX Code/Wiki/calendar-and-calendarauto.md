---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# CALENDAR and CALENDARAUTO

Creates a single-column table of dates between a start and end date.

## CALENDAR

```dax
CALENDAR(<start_date>, <end_date>)
```

| Term | Definition |
|------|------------|
| `start_date` | Any DAX expression returning a datetime value |
| `end_date` | Any DAX expression returning a datetime value |

## CALENDARAUTO

```dax
CALENDARAUTO([fiscal_year_end_month])
```

| Term | Definition |
|------|------------|
| `fiscal_year_end_month` | (Optional) Month number (1–12) that the fiscal year ends on |

## Returns

A single-column table with one column named **Date** containing all dates from start to end, inclusive.

## Examples

```dax
-- Fixed date range
DateTable = CALENDAR(DATE(2020, 1, 1), DATE(2025, 12, 31))

-- Auto-detect range from model data
DateTable = CALENDARAUTO()

-- Auto with fiscal year ending March
FiscalCalendar = CALENDARAUTO(3)
```

## Notes

- CALENDAR: error if `start_date > end_date`
- CALENDARAUTO: automatically detects the earliest and latest date in the model — no arguments needed
- CALENDARAUTO is the preferred method for building date tables from model data
- The output column is named "Date" (capital D)
- Not supported in DirectQuery mode for calculated tables or RLS rules
- Always mark the output as a **date table** in the model properties after creation

## Related

- [[date]] — date construction
- [[today]] — current date
- [[datevalue]] — text to date conversion
