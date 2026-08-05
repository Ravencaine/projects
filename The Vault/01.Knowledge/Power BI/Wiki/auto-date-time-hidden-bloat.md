---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: gotcha
tags: [power-bi, gotcha, auto-date-time, performance, model-size]
---

# Auto Date/Time Creates Hidden Bloat Tables

Power BI's built-in auto date/time feature generates a hidden date table for every date column in the model, inflating memory usage and producing unreliable cross-column time comparisons.

## Expected Behaviour

Power BI automatically creates intelligent date hierarchies on date columns that work with time intelligence functions and allow drill-down by year, quarter, month.

## Actual Behaviour

Auto date/time creates a **separate hidden date table for each date column** in every table in the model. For a fact table with OrderDate, ShipDate, and DueDate, this means three hidden date tables — plus one for every date column in every dimension table. These tables:
- Consume memory proportional to the date range
- Duplicate the functionality of a properly built `DimDate`
- Cause time intelligence functions to behave unpredictably when both hidden and explicit date tables exist
- Cannot be managed, hidden, or removed without disabling the feature

## Why It Happens

Auto date/time is enabled by default in Power BI Desktop as a convenience feature for new users. It is a crutch, not a best practice for production models.

## How to Handle It

1. **Disable globally**: File → Options and Settings → Options → Data Load → uncheck "Auto date/time"
2. **Build one explicit `DimDate`**: use `List.Dates()` in Power Query or `CALENDAR()` in DAX
3. **Mark it as a Date Table**: Table Tools → Mark as Date Table
4. **Build relationships**: connect each fact date column to `DimDate[Date]` (use `USERELATIONSHIP()` for inactive roles)
5. **Rebuild the model**: disabling auto date/time after adding date columns does not remove existing hidden tables — start from a new .pbix or remove and re-add date columns

## Related Gotchas

- [[date-column-type-vs-datetime]] — Mark as Date Table fails when the column is datetime type

## Related

- [[date-table-post-creation-checklist]] — `reference`
- [[power-query-date-table-build]] — `pattern`
- [[dax-date-table-build]] — `pattern`
