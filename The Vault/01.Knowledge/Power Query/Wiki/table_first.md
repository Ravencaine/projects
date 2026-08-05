---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.First

Returns the first row of the table or an optional default value, default, if the table is empty.

## Signature

```m
Table.First(table as table, optional default as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| optional default | any | |

## Returns

any

### Example 1

Find the first row of the table.

```m
Table.First(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
)
```

// Output
```
[CustomerID = 1, Name = "Bob", Phone = "123-4567"]
```

### Example 2

Find the first row of the table ({}) or return [a = 0, b = 0] if empty.

```m
Table.First(Table.FromRecords({}), [a = 0, b = 0])
```

// Output
```
[a = 0, b = 0]
```

