---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.RemoveColumns

Removes the specified columns from the table provided. If the specified column doesn't exist, an error is raised unless the optional parameter missingField specifies an alternative behavior (for example, MissingField.UseNull or MissingField.Ignore).

## Signature

```m
Table.RemoveColumns(
table as table,
columns as any,
optional missingField as nullable number
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| columns | any | |
| optional missingField | nullable number | |

## Returns

table

### Example 1

Remove column [Phone] from the table.

```m
Table.RemoveColumns(
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
"Phone"
)
```

// Output
```
Table.FromRecords({[CustomerID = 1, Name = "Bob"]})
```

### Example 2

Try to remove a non-existent column from the table.

```m
Table.RemoveColumns(
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
"Address"
)
```

// Output
```
[Expression.Error] The column 'Address' of the table wasn't found.
```

