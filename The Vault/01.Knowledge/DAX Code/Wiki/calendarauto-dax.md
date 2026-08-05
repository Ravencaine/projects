---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: function
tags: [dax, date-table, calendarauto, time-intelligence]
---

# CALENDARAUTO — DAX Auto Date Table Generator

Automatically generates a date table covering all dates present in the entire data model. The quickest way to create a Date Table with no manual range specification.

## Signature

```
CALENDARAUTO([fiscal_year_month_end])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `fiscal_year_month_end` | Integer | Optional — last month of fiscal year (1–12). Defaults to December if omitted. |

## Returns

A single-column table of all dates found in the model, expanded to cover full calendar years.

## Examples

```dax
-- Default: auto-detect from model, calendar year
DateTable = CALENDARAUTO()

-- Fiscal year ending in June:
DateTable = CALENDARAUTO(6)
```

## Notes

- `CALENDARAUTO` scans all columns in the model that contain date values and derives the range automatically.
- The output always expands to full calendar years — if your data spans March 2023 to August 2024, the table runs from January 1, 2023 to December 31, 2024.
- Best suited for quick prototyping or models with simple calendar requirements.
- For production models, `CALENDAR` with explicit MIN/MAX is preferred — it is more transparent and performs better.
- Requires `ADDCOLUMNS` to add Year, Month, Quarter, and other calendar columns.

## Related

- [[calendar-dax]] — `function`
- [[dax-date-table-build]] — `pattern`
- [[dax-vs-m-date-table-quick-reference]] — `reference`
