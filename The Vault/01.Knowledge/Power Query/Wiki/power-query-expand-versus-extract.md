---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [power-query, expand, extract, record, list, nested-data]
---

# Table.ExpandRecordColumn and Table.ExpandListColumn

Two Power Query transforms for flattening nested data structures in semi-structured sources.

## Table.ExpandRecordColumn

Extracts individual fields from a **record** (single object) nested inside a column.

## Signature

```
Table.ExpandRecordColumn(
  table as table,
  columnName as text,
  fieldNames as list,
  newColumnNames as list
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | Source table |
| columnName | text | Name of the column containing the record |
| fieldNames | list | List of field names to extract (e.g., `{"Year", "Score"}`) |
| newColumnNames | list | Names for the new columns (e.g., `{"Year_Extracted", "Score_Extracted"}`) |

## Table.ExpandListColumn

Extracts a **list** (array) nested inside a column, creating one row per list item.

## Signature

```
Table.ExpandListColumn(
  table as table,
  columnName as text
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | Source table |
| columnName | text | Name of the column containing the list |

## Example

Expand a record field called `Metrics` containing `{Year: 2019, LifeLadder: 7.8}`:

```
Table.ExpandRecordColumn(
  Source,
  "Metrics",
  {"Year", "LifeLadder"},
  {"Year", "LifeLadder"}
)
```

## When to Use Each

| Data type | Transform |
|-----------|----------|
| Record (single nested object) | `Table.ExpandRecordColumn` |
| List (array of values) | `Table.ExpandListColumn` |

## Related

- [[fixing-data-structure-pq]]
- [[power-query-unpivot-columns]]
- [[table_expandrecordcolumn]]
- [[table_expandlistcolumn]]
