---
created: 2026-08-09
updated: 2026-08-09
source: "DAX Calendar-Based Time Intelligence What You Must Know Before Editing Your Model.md"
note_type: gotcha
tags: [power-bi, dax, time-intelligence, calendar-based, column, delete, lineage, TMDL, processing-error]
---

# Deleting Calendar Columns Breaks Calendar-Based Time Intelligence

In calendar-based time intelligence (preview), **never delete a column that is part of a calendar definition:** only rename it. Deletion causes a processing failure that leaves the model in a broken state with no visible recovery path from the UI.

## The Error

```
CalendarColumnReference object refers to a column that has been deleted
```

This appears during the processing phase (Close & Apply in Power Query) after a column used in the calendar definition has been deleted and replaced.

## Why Rename Works But Delete Does Not

Power BI tracks columns by **lineage tag:** an internal identifier that survives renames:

```tomd
column 'Month of Year'
    lineageTag: d32df0ee-107e-4e5d-abda-69cb4ead6d6c
    sourceColumn: Month of Year

column 'Month of Years'
    lineageTag: d32df0ee-107e-4e5d-abda-69cb4ead6d6c   ← same tag after rename
    sourceColumn: Month of Years
```

When you rename a column, the lineage tag is preserved and calendar references remain valid. When you delete and recreate a column, a new lineage tag is assigned and the calendar definition still points to the old (now-deleted) column.

## The Stuck State

After a failed processing:
1. The new column does not exist (processing was interrupted)
2. The calendar UI does not surface the broken reference
3. No error is shown in the calendar definition UI
4. Every subsequent processing attempt fails

## Recovery Steps

1. Open **TMDL View** in Power BI Desktop
2. Locate the broken calendar definition
3. Delete the mapping to the missing column manually
4. Run processing to succeed
5. Recreate the column
6. Remap it in the calendar definition

This requires TMDL knowledge — not accessible to business users.

## Prevention

- **Always rename** columns in the calendar definition rather than deleting them
- Use **Bravo for Power BI** to modify date tables safely
- Avoid structural changes to columns used in calendar definitions in production models
- Document which columns are part of calendar definitions before making changes

## Related

- [[Source-DAX-Calendar-Based-Time-Intelligence]] — source note
- [[value-lineage]] — Power Query lineage concept (different domain but related idea)
