---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.IsDistinct

Indicates whether the table contains only distinct rows (no duplicates). Returns true if the rows are distinct, false otherwise. An optional parameter, comparisonCriteria, specifies which columns of the table are tested for duplication. If comparisonCriteria is not specified, all columns are tested.

## Signature

```m
Table.IsDistinct(table as table, optional comparisonCriteria as any) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| optional comparisonCriteria | any | |

## Returns

logical

### Example 1

Determine if the table is distinct.

```m
Table.IsDistinct(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
)
```

// Output
```
true
```

### Example 2

Determine if the table is distinct in column.

```m
Power Query M
Table.IsDistinct(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 5, Name = "Bob", Phone = "232-1550"]
}),
"Name"
)
```

// Output
```
false
```

## Related

[[comparison_criteria]]

