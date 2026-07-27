---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.FromValue

Creates a table with a column containing the provided value or list of values, value. An optional record parameter, options, may be specified to control the following options: DefaultColumnName: The column name used when constructing a table from a list or scalar value.

## Signature

```m
Table.FromValue(value as any, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional options | nullable record | |

## Returns

table

### Example 1

Create a table from the value 1.

```m
Table.FromValue(1)
```

// Output
```
Table.FromRecords({[Value = 1]})
```

### Example 2

Create a table from the list.

```m
Table.FromValue({1, "Bob", "123-4567"})
```

// Output
```
Table.FromRecords({
[Value = 1],
[Value = "Bob"],
[Value = "123-4567"]
})
```

### Example 3

Create a table from the value 1, with a custom column name.

```m
Table.FromValue(1, [DefaultColumnName = "MyValue"])
```

// Output
```
Table.FromRecords({[MyValue = 1]})
```

