---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ToColumns

Creates a list of nested lists from the table, table. Each list item is an inner list that contains the column values.

## Signature

```m
Table.ToColumns(table as table) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

list

### Example 1

Create a list of the column values from the table.

```m
Table.ToColumns(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"]
})
)
```

// Output
```
{{1, 2}, {"Bob", "Jim"}, {"123-4567", "987-6543"}}
```

