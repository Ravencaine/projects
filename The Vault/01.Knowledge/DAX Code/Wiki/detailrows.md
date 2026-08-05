---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# DETAILROWS

Evaluates a Detail Rows Expression defined for a measure and returns the data. A Detail Rows Expression is set in model properties and determines what detail data to show when the user double-clicks a measure value.

## Syntax

```dax
DETAILROWS(<Measure>)
```

## Parameters

| Term | Definition |
|------|------------|
| `Measure` | Name of a measure whose Detail Rows Expression will be evaluated. |

## Return Value

A table with the data returned by the Detail Rows Expression. If no Detail Rows Expression is defined, the data for the table containing the measure is returned.