---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: gotcha
tags: [power-bi, gotcha, date-column, data-type, time-intelligence]
---

# DateTime vs Date Column Type — Mark as Date Table Fails

Power BI's "Mark as Date Table" validation rejects columns that are `DateTime` instead of `Date`. This silently breaks all time intelligence functions.

## Expected Behaviour

After building a Date Table, you mark the `Date` column as a Date Table using Table Tools → Mark as Date Table. Power BI activates time intelligence for that column.

## Actual Behaviour

Power BI displays an error: "This column does not contain unique values" or "This column contains duplicate or incomplete date values." The Mark as Date Table option remains unavailable, and DAX time intelligence functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`, etc.) fail silently or return incorrect results.

## Why It Happens

- The column was loaded as `DateTime` instead of `Date` — datetime columns include a time component (e.g., `2024-03-15 08:30:00`)
- A `DateTime` column has multiple rows with the same date but different times — not unique dates from Power BI's perspective
- `DateTime` columns can never pass the "unique date values" validation required for Mark as Date Table

## How to Handle It

1. **In Power Query**: change the column type from `Date/Time` to `Date` before loading:
   ```
   Table.TransformColumnTypes(Source, {{"Date", type date}})
   ```
2. **Strip the time component in M** if the source returns datetime:
   ```m
   Table.AddColumn(Source, "DateOnly",
       each Date.From([OrderDate]), type date)
   ```
3. **In DAX**: wrap in `DATE()`:
   ```dax
   DateTable = CALENDAR(DATE(2018,1,1), DATE(2026,12,31))
   ```
   `CALENDAR` always returns pure dates — never datetime.
4. After fixing the type, verify in Data view that the column shows dates only (no time component)

## Related Gotchas

- [[auto-date-time-hidden-bloat]] — related: auto date/time uses hidden datetime columns

## Related

- [[date-table-post-creation-checklist]] — `reference`
- [[power-query-date-table-build]] — `pattern`
