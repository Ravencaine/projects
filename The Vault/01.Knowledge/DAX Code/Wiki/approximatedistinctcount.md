---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# APPROXIMATEDISTINCTCOUNT

Applies to: Calculated column Calculated table Measure Visual calculation Returns an estimated count of unique values in a column. This function invokes a

## Syntax

```dax
APPROXIMATEDISTINCTCOUNT(<columnName>)
```

## Remarks

The only argument to this function is a column. You can use columns containing any type of data. When the function finds no rows to count, it returns a BLANK, otherwise it returns the count of distinct values.