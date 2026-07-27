---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# CONTAINSSTRING

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE or FALSE indicating whether one string contains another string.

## Syntax

```dax
CONTAINSSTRING(<within_text>, <find_text>)
```

## Remarks

CONTAINSSTRING is case-insensitive, kanatype-insensitive, width-insensitive and accent sensitive. You can use ? and * wildcard characters. Use ~ to escape wildcard characters.