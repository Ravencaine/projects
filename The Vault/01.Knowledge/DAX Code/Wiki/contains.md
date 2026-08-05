---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# CONTAINS

Applies to: Calculated column Calculated table Measure Visual calculation Returns true if values for all referred columns exist, or are contained, in those columns;

## Syntax

```dax
CONTAINS(<table>, <columnName>, <value>[, <columnName>, <value>]…)
```

## Remarks

The arguments columnName and value must come in pairs; otherwise an error is returned.