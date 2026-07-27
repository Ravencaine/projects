---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.IsEmpty

Indicates whether the table contains any rows. Returns true if there are no rows (i.e. the table is empty), false otherwise.

## Signature

```m
Table.IsEmpty(table as table) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

logical

### Example 1

Determine if the table is empty.

```m
Table.IsEmpty(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
)
```

// Output
```
false
```

### Example 2

Determine if the table ({}) is empty.

```m
Table.IsEmpty(Table.FromRecords({}))
```

// Output
```
true
```

