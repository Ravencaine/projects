---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.FromList

Converts a list, list into a table by applying the optional splitting function, splitter, to each item in the list. By default, the list is assumed to be a list of text values that is split by commas. Optional columns may be the number of columns, a list of columns or a TableType. Optional default and extraValues may also be specified.

## Signature

```m
Table.FromList(
list as list,
optional splitter as nullable function,
optional columns as any,
optional default as any,
optional extraValues as nullable number
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional splitter | nullable function | |
| optional columns | any | |
| optional default | any | |
| optional extraValues | nullable number | |

## Returns

table

### Example 1

Create a table from a list using the default splitter.

```m
Table.FromList(
{"a,apple", "b,ball", "c,cookie", "d,door"},
null,
{"Letter", "Example Word"}
)
```

// Output
```
Table.FromRecords({
[Letter = "a", #"Example Word" = "apple"],
[Letter = "b", #"Example Word" = "ball"],
[Letter = "c", #"Example Word" = "cookie"],
[Letter = "d", #"Example Word" = "door"]
})
```

### Example 2

Create a table from a list using a custom splitter.

```m
Table.FromList(
{"a,apple", "b,ball", "c,cookie", "d,door"},
Splitter.SplitByNothing(),
{"Letter and Example Word"}
)
```

// Output
```
Table.FromRecords({
[#"Letter and Example Word" = "a,apple"],
[#"Letter and Example Word" = "b,ball"],
[#"Letter and Example Word" = "c,cookie"],
[#"Letter and Example Word" = "d,door"]
})
```

### Example 3

Create a table from the list using the Record.FieldValues splitter.

```m
Table.FromList(
{
[CustomerID = 1, Name = "Bob"],
[CustomerID = 2, Name = "Jim"]
},
Record.FieldValues,
{"CustomerID", "Name"}
)
```

// Output
```
Table.FromRecords({
[CustomerID = 1, Name = "Bob"],
[CustomerID = 2, Name = "Jim"]
})
```

