---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# NONVISUAL

## Syntax

```dax
NONVISUAL(<expression>)
```

## Remarks

Marks a value filter in SUMMARIZECOLUMNS as not affecting measure values, but only applying to group-by columns. This function can only be used within a SUMMARIZECOLUMNS expression. It's used as either a filterTable argument of the SUMMARIZECOLUMNS function or a groupLevelFilter argument of the ROLLUPADDISSUBTOTAL or ROLLUPISSUBTOTAL function.
