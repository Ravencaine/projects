---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.SelectColumns

Returns the table with only the specified columns. table: The provided table. columns: The list of columns from the table table to return. Columns in the returned table are in the order listed in columns. missingField: (Optional) What to do if the column does not exist. Example: MissingField.UseNull or MissingField.Ignore.

## Signature

```m
Table.SelectColumns(
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

Only include column [Name].

```m
Table.SelectColumns(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
"Name"
)
```

// Output
```
Power Query M
Table.FromRecords({
[Name = "Bob"],
[Name = "Jim"],
[Name = "Paul"],
[Name = "Ringo"]
})
```

### Example 2

Only include columns [CustomerID] and [Name].

```m
Table.SelectColumns(
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
{"CustomerID", "Name"}
)
```

// Output
```
Table.FromRecords({[CustomerID = 1, Name = "Bob"]})
```

### Example 3

If the included column does not exist, the default result is an error.

```m
Table.SelectColumns(
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
"NewColumn"
)
```

// Output
```
[Expression.Error] The field 'NewColumn' of the record wasn't found.
```

### Example 4

```m
Table.SelectColumns(
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
{"CustomerID", "NewColumn"},
MissingField.UseNull
)
```

// Output
```
Table.FromRecords({[CustomerID = 1, NewColumn = null]})
```

