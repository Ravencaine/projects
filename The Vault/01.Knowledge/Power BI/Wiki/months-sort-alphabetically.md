---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: gotcha
tags: [power-bi, gotcha, sort-by-column, month-name, alphabetical]
---

# Months Sort Alphabetically Without Sort Column

Power BI sorts text month names alphabetically by default (April, August, December...) rather than chronologically. Every report with a MonthName column exhibits this unless Sort by Column is configured.

## Expected Behaviour

When MonthName is placed on an axis or in a slicer, months appear in chronological order: January, February, March...

## Actual Behaviour

Months appear in alphabetical order: April, August, December, February, January, July, June, March, May, November, October, September. This makes trend charts unreadable and slicers confusing.

## Why It Happens

Power BI treats the MonthName column as plain text. Text columns sort alphabetically unless explicitly told to sort by a numeric column. The MonthName column has no intrinsic numeric meaning to Power BI without a Sort Column setting.

## How to Handle It

1. **Create a MonthNumber sort column** in the Date Table:
   ```m
   Table.AddColumn(Source, "MonthNum",
       each Date.Month([Date]), Int64.Type)
   ```
2. **Set Sort by Column** in Power BI Desktop:
   - Go to Data view
   - Select the `DimDate` table
   - Click the `MonthName` column
   - Go to Column Tools → Sort by Column → select `MonthNum`
   - Repeat for `MonthShort` → `MonthNum`, `DayName` → `DayOfWeekNum`
3. Do this **before publishing** the report — changing it in the service breaks existing visual configurations

## Related Gotchas

- [[date-column-type-vs-datetime]] — date type is a prerequisite for a valid Date Table

## Related

- [[date-table-post-creation-checklist]] — `reference`
- [[power-query-date-table-build]] — `pattern`
- [[dax-date-table-build]] — `pattern`
