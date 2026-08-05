---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ExpandListColumn

Given a table where column contains a list of values, splits the list into a row for each value. Values in the other columns are duplicated in each new row created. This function can also expand nested tables by treating them as lists of records.

## Signature

```m
Table.ExpandListColumn(table as table, column as text) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| column | text | |

## Returns

table

### Example 1

Split the list column [Name].

```m
Table.ExpandListColumn(
Table.FromRecords({[Name = {"Bob", "Jim", "Paul"}, Discount = .15]}),
"Name"
)
```

// Output
```
Table.FromRecords({
[Name = "Bob", Discount = 0.15],
[Name = "Jim", Discount = 0.15],
[Name = "Paul", Discount = 0.15]
})
```

### Example 2

Split the nested table column [Components].

```m
Table.ExpandListColumn(
#table(
{"Part", "Components"},
{
{"Tool", #table({"Name", "Quantity"}, {{"Thingamajig", 2}, {"Widget",
3}})}
}
),
"Components"
)
```

// Output
```
Table.FromRecords({
[Part = "Tool", Components = [Name = "Thingamajig", Quantity = 2]],
[Part = "Tool", Components = [Name = "Widget", Quantity = 3]]
})
```

