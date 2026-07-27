---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# EVALUATEANDLOG

Returns the value of the first argument and logs it in a DAX Evaluation Log profiler event. Fully functional in Power BI Desktop only — acts as a simple passthrough in other environments.

## Syntax

```dax
EVALUATEANDLOG(<Value>[, <Label>][, <MaxRows>])
```

## Parameters

| Term | Definition |
|------|------------|
| `Value` | Any scalar or table expression to be evaluated and logged. |
| `Label` | (Optional) A constant string included in the JSON text and Label column of the DAX Evaluation Log event for easy identification. |
| `MaxRows` | (Optional) Maximum number of rows in the JSON text when the first argument is a table expression. Default is 10. |

## Return Value

The value of the first argument. JSON logged includes: expression (text of first argument), label, and inputs (columns in the evaluation context that affect the result).