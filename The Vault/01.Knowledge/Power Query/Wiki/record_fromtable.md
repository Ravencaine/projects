---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [record, m-function]
---


# Record.FromTable

Returns a record from a table of records table containing field names and value names {[Name = name, Value = value]}. An error is raised if the field names are not unique.

## Signature

```m
Record.FromTable(table as table) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

record

### Example 1

Create a record from the table of the form Table.FromRecords({[Name = "CustomerID", Value = 1], [Name = "Name", Value = "Bob"], [Name = "Phone", Value = "123-4567"]}).

```m
Record.FromTable(
Table.FromRecords({
[Name = "CustomerID", Value = 1],
[Name = "Name", Value = "Bob"],
[Name = "Phone", Value = "123-4567"]
})
)
```

// Output
```
[CustomerID = 1, Name = "Bob", Phone = "123-4567"]
Last updated on 01/22/2026
```

