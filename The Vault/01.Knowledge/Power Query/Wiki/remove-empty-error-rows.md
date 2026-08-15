---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, remove-blank-rows, remove-errors]
---

# Remove Empty / Error Rows

Delete rows that are entirely blank or contain error values.

## Purpose

Error rows propagate failures through the pipeline and break visuals. Blank rows inflate row counts and distort aggregations.

## Components

- `Table.SelectRows`
- `Table.RemoveRowsWithErrors`

## Structure

```m
// Remove rows where all specified columns are null/blank
Table.SelectRows(Source, each List.RemoveNulls(Record.FieldValues(_)) <> {})

// Remove rows with errors in any column
Table.RemoveRowsWithErrors(Source, {"Column1", "Column2"})
```

## Example

```m
// Remove completely blank rows (all columns null)
Table.SelectRows(
    Source,
    each List.RemoveNulls(Record.FieldValues(_)) <> {}
)

// Remove rows where specific columns contain errors
Table.RemoveRowsWithErrors(Source, {"Revenue", "Quantity"})
```

## Variations

| Scenario | M approach | UI equivalent |
|----------|-----------|---------------|
| Entire row blank | `Table.SelectRows` with null check | Home → Remove Rows → Remove Blank Rows |
| Row has errors | `Table.RemoveRowsWithErrors` | Home → Remove Rows → Remove Errors |
| Column-specific nulls | `Table.SelectRows` per column | Filter dropdown → Remove Blank |

## Related

- [[Replace-Values]] — convert sentinel values to null before removing
- [[Remove-Duplicates]] — often paired after blank removal
