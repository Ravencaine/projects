---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# CONVERT

Applies to: Calculated column Calculated table Measure Visual calculation Converts an expression of one data type to another.

## Syntax

```dax
CONVERT(<Expression>, <Datatype>)
```

## Remarks

The function returns an error when a value cannot be converted to the specified data type. DAX calculated columns must be of a single data type. Since MEDIAN and MEDIANX functions over an integer column return mixed data types, either integer or double, the following calculated column expression will return an error as a result: DAX MedianOrderQuantity = MEDIAN ( [Order Quantity] )