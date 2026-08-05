---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: reference
tags: [power-bi, reference, date-table, checklist, best-practices]
---

# Date Table Post-Creation Checklist

A definitive checklist to run after building any Date Table in Power BI — DAX or Power Query — to ensure it is correctly configured before publishing.

## Pre-Publish Verification

### Column Requirements

- [ ] `Date` column is `type date` (not `DateTime`)
- [ ] No null values in the `Date` column
- [ ] No duplicate dates in the `Date` column
- [ ] No gaps in the date sequence (consecutive daily rows)
- [ ] `YearMonthKey` column present (e.g., `202403` for March 2024)

### Sort by Column Settings

- [ ] `MonthName` sorted by `MonthNum`
- [ ] `MonthShort` sorted by `MonthNum`
- [ ] `DayName` sorted by `DayOfWeekNum`

### Date Table Configuration

- [ ] Table marked as Date Table (Table Tools → Mark as Date Table → select `Date` column)
- [ ] `Date` column set as the Key column
- [ ] Unnecessary helper columns hidden from Report view

### Model Relationships

- [ ] Relationship built from fact table date column → `DimDate[Date]` (many-to-one)
- [ ] Multiple date columns handled via inactive relationships + `USERELATIONSHIP()` in DAX
- [ ] Auto date/time disabled (File → Options → Data Load → uncheck Auto date/time)

### Date Range Quality

- [ ] Table starts on January 1 (use `Date.StartOfYear()`)
- [ ] Table ends on December 31 (use `Date.EndOfYear()`)
- [ ] Future dates added (EndDate = December 31 of year after max data year) for forecast visuals

## Related

- [[date-table-as-backbone]] — `atomic`
- [[power-query-date-table-build]] — `pattern`
- [[dax-date-table-build]] — `pattern`
- [[months-sort-alphabetically]] — `gotcha`
- [[date-column-type-vs-datetime]] — `gotcha`
