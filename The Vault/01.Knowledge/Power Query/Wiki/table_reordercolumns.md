---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ReorderColumns

Returns a table from the input table, with the columns in the order specified by columnOrder. Columns that are not specified in the list will not be reordered. If the column doesn't exist, an error is raised unless the optional parameter missingField specifies an alternative (eg. MissingField.UseNull or MissingField.Ignore).

## Signature

```m
Table.ReorderColumns(
table as table,
columnOrder as list,
optional missingField as nullable number
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| columnOrder | list | |
| optional missingField | nullable number | |

## Returns

table

### Example 1

Switch the order of the columns [Phone] and [Name] in the table.

```m
Table.ReorderColumns(
Table.FromRecords({[CustomerID = 1, Phone = "123-4567", Name = "Bob"]}),
{"Name", "Phone"}
)
```

// Output
```
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})
```

### Example 2

Switch the order of the columns [Phone] and [Address] or use "MissingField.Ignore" in the table. It doesn't change the table because column [Address] doesn't exist.

```m
Power Query M
Table.ReorderColumns(
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
{"Phone", "Address"},
MissingField.Ignore
)
```

// Output
```
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})
Last updated on 01/22/2026
```

