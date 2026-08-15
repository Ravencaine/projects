---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.SelectRows

Returns a table of rows from the table, that matches the selection condition.

## Signature

```m
Table.SelectRows(table as table, condition as function) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| condition | function | |

## Returns

table

### Example 1

Select the rows in the table where the values in [CustomerID] column are greater than 2.

```m
Table.SelectRows(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
each [CustomerID] > 2
)
```

// Output
```
Table.FromRecords({
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
```

### Example 2

Select the rows in the table where the names do not contain a "B".

```m
Table.SelectRows(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
each not Text.Contains([Name], "B")
)
```

// Output
```
Table.FromRecords({
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
```

