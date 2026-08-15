---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.DemoteHeaders

Demotes the column headers (i.e. column names) to the first row of values. The default column names are "Column1", "Column2" and so on.

## Signature

```m
Table.DemoteHeaders(table as table) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

table

### Example 1

Demote the first row of values in the table.

```m
Table.DemoteHeaders(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"]
})
)
```

// Output
```
Table.FromRecords({
[Column1 = "CustomerID", Column2 = "Name", Column3 = "Phone"],
[Column1 = 1, Column2 = "Bob", Column3 = "123-4567"],
[Column1 = 2, Column2 = "Jim", Column3 = "987-6543"]
})
```

