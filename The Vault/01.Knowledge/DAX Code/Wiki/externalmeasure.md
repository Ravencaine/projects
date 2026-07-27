---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# EXTERNALMEASURE

Applies to: Calculated column Calculated table Measure Visual calculation Invokes a measure defined in a remote model and returns its result with the specified datatype.

## Syntax

```dax
EXTERNALMEASURE(<measurename>, <datatype>, <connection>)
```

## Remarks

This function can only be used in composite models that have a remote model connection.