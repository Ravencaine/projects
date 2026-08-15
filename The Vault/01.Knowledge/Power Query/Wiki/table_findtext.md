---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.FindText

Returns the rows in the table table that contain the text text. If the text is not found, an empty table is returned.

## Signature

```m
Table.FindText(table as table, text as text) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| text | text | |

## Returns

table

### Example 1

Find the rows in the table that contain "Bob".

```m
Table.FindText(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
"Bob"
)
```

// Output
```
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})
```

