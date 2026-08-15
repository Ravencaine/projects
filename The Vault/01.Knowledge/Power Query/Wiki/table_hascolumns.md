---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.HasColumns

Indicates whether the table contains the specified column(s), columns. Returns true if the table contains the column(s), false otherwise.

## Signature

```m
Table.HasColumns(table as table, columns as any) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| columns | any | |

## Returns

logical

### Example 1

Determine if the table has the column [Name].

```m
Table.HasColumns(
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
true
```

### Example 2

Find if the table has the column [Name] and [PhoneNumber].

```m
Table.HasColumns(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
{"Name", "PhoneNumber"}
)
```

// Output
```
false
```

