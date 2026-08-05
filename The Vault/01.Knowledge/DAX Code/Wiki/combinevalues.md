---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# COMBINEVALUES

Applies to: Calculated column Calculated table Measure Visual calculation Joins two or more text strings into one text string. The primary purpose of this function

## Syntax

```dax
COMBINEVALUES(<delimiter>, <expression>, <expression>[, <expression>]…)
```

## Remarks

The COMBINEVALUES function assumes, but does not validate, that when the input values are different, the output strings are also different. Based on this assumption, when COMBINEVALUES is used to create calculated columns in order to build a relationship that joins multiple columns from two DirectQuery tables, an optimized join condition is generated at query time. For