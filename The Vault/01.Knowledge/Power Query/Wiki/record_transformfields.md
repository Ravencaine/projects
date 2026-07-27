---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.TransformFields

Returns a record after applying transformations specified in list transformOperations to record. One or more fields may be transformed at a given time. In the case of a single field being transformed, transformOperations is expected to be a list with two items. The first item in transformOperations specifies a field name, and the second item in transformOperations specifies the function to be used for transformation. For example, {"Quantity", Number.FromText} In the case of a multiple fields being transformed, transformOperations is expected to be a list of lists, where each inner list is a pair of field name and transformation operation. For example, {{"Quantity",Number.FromText},{"UnitPrice", Number.FromText}}

## Signature

```m
Record.TransformFields(
record as record,
transformOperations as list,
optional missingField as nullable number
) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |
| transformOperations | list | |
| optional missingField | nullable number | |

## Returns

record

### Example 1

Convert "Price" field to number.

```m
Record.TransformFields(
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = "100.0"],
{"Price", Number.FromText}
)
```

// Output
```
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100]
```

### Example 2

Convert "OrderID" and "Price" fields to numbers.

```m
Record.TransformFields(
[OrderID = "1", CustomerID = 1, Item = "Fishing rod", Price = "100.0"],
{{"OrderID", Number.FromText}, {"Price", Number.FromText}}
)
```

// Output
```
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100]
Replacer functions
Article • 08/04/2022
These functions are used by other functions in the library to replace a given value.
Name Description
Replacer.ReplaceText This function be provided to List.ReplaceValue or Table.ReplaceValue to
do replace of text values in list and table values respectively.
Replacer.ReplaceValue This function be provided to List.ReplaceValue or Table.ReplaceValue to
do replace values in list and table values respectively.
Feedback
Was this page helpful? ﾂ Yes ﾄ No
Get help at Microsoft Q&A
```

