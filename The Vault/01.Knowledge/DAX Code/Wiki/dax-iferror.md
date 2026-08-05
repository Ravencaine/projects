---


title: "IFERROR"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, error-handling]
note_type: function
description: "IFERROR — wraps an expression and returns a fallback value if the expression returns an error. Used to prevent division-by-zero and other runtime errors. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# IFERROR

Returns a specified value if an expression evaluates to an error; otherwise, returns the expression's result.

## Syntax

```
IFERROR( <value>, <value_if_error> )
```

## Arguments

| Argument | Description |
|----------|-------------|
| `value` | The expression to evaluate |
| `value_if_error` | The value to return if `value` results in an error |

## Common Use Cases

### Division by zero

```dax
Profit Ratio :=
IFERROR(
    DIVIDE( [Total Profit], [Total Sales] ),
    BLANK()
)
```

### Invalid lookups

```dax
Safe Lookup :=
IFERROR(
    LOOKUPVALUE( Products[Name], Products[ID], Sales[ProductID] ),
    "Unknown"
)
```

## IFERROR vs. DIVIDE

`DIVIDE` already handles division by zero internally (returning BLANK), so wrapping `DIVIDE` with `IFERROR` is redundant unless you want a specific non-BLANK fallback.

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
