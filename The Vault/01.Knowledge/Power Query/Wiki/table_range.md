---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.Range

Returns the rows from the table starting at the specified offset. An optional parameter, count, specifies how many rows to return. By default, all the rows after the offset are returned.

## Signature

```m
Table.Range(
table as table,
offset as number,
optional count as nullable number
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| offset | number | |
| optional count | nullable number | |

## Returns

table

### Example 1

Return all the rows starting at offset 1 in the table.

```m
Table.Range(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
1
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

### Example 2

Return one row starting at offset 1 in the table.

```m
Table.Range(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
1,
1
)
```

// Output
```
Table.FromRecords({[CustomerID = 2, Name = "Jim", Phone = "987-6543"]})
```

