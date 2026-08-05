---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.AddIndexColumn

Appends a column named newColumnName to the table with explicit position values. An optional value, initialValue, the initial index value. An optional value, increment, specifies how much to increment each index value.

## Signature

```m
Table.AddIndexColumn(
table as table,
newColumnName as text,
optional initialValue as nullable number,
optional increment as nullable number,
optional columnType as nullable type
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| newColumnName | text | |
| optional initialValue | nullable number | |
| optional increment | nullable number | |
| optional columnType | nullable type | |

## Returns

table

### Example 1

Add an index column named "Index" to the table.

```m
Table.AddIndexColumn(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
"Index"
)
```

// Output
```
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567", Index = 0],
[CustomerID = 2, Name = "Jim", Phone = "987-6543", Index = 1],
[CustomerID = 3, Name = "Paul", Phone = "543-7890", Index = 2],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550", Index = 3]
})
```

### Example 2

Add an index column named "index", starting at value 10 and incrementing by 5, to the table.

```m
Table.AddIndexColumn(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
"Index",
10,
5
)
```

// Output
```
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567", Index = 10],
[CustomerID = 2, Name = "Jim", Phone = "987-6543", Index = 15],
[CustomerID = 3, Name = "Paul", Phone = "543-7890", Index = 20],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550", Index = 25]
})
```

## Related

[[type_functions]]

