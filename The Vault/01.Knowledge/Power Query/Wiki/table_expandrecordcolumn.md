---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ExpandRecordColumn

Given the column of records in the input table, creates a table with a column for each field in the record. Optionally, newColumnNames may be specified to ensure unique names for the columns in the new table. table: The original table with the record column to expand. column: The column to expand. fieldNames: The list of fields to expand into columns in the table. newColumnNames: The list of column names to give the new columns. The new column names cannot duplicate any column in the new table.

## Signature

```m
Table.ExpandRecordColumn(
table as table,
column as text,
fieldNames as list,
optional newColumnNames as nullable list
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| column | text | |
| fieldNames | list | |
| optional newColumnNames | nullable list | |

## Returns

table

### Example 1

Expand column [a] in the table ({[a = [aa = 1, bb = 2, cc = 3], b = 2]}) into 3 columns "aa", "bb" and "cc".

```m
Table.ExpandRecordColumn(
Table.FromRecords({
[
a = [aa = 1, bb = 2, cc = 3],
b = 2
]
}),
"a",
{"aa", "bb", "cc"}
)
```

// Output
```
Table.FromRecords({[aa = 1, bb = 2, cc = 3, b = 2]})
```

