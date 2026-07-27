---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# CEILING

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number up, to the nearest integer or to the nearest multiple of significance.

## Syntax

```dax
CEILING(<number>, <significance>)
```

## Remarks

There are two CEILING functions in DAX, with the following differences: The CEILING function emulates the behavior of the CEILING function in Excel. The ISO.CEILING function follows the ISO-defined behavior for determining the ceiling value. The two functions return the same value for positive numbers, but different values for negative numbers. When using a positive multiple of significance, both CEILING and ISO.CEILING round negative numbers upward (toward positive infinity). When using a negative multiple of significance, CEILING rounds negative numbers