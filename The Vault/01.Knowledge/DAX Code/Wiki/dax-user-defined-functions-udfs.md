---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: function
tags: [dax, user-defined-function, uda, functions, model-explorer, tmdl, library]
---

# DAX User-Defined Functions (UDFs)

DAX UDFs are named, parameterized, first-class function objects defined in the semantic model — available in measures, calculated columns, visual calculations, and other functions.

> **GA:** June 2026 Power BI release. Requires database compatibility level 1702 or higher.
> **Preview:** September 2025.

## Signature

```dax
DEFINE
/// <description appears in Model Explorer>
FUNCTION <Name>.<Namespace> = (
    <param1> : <Type>,
    <param2> : <Type> [VAL | EXPR]    -- optional evaluation mode
) =>
    <expression>

-- Call the function
<Name>.<Namespace> ( <arg1>, <arg2> )
```

## Parameters

| Element | Description |
|---------|-------------|
| `Name.Namespace` | Full function name; dot is the namespace separator (e.g., `Sales.NetRevenue`) |
| `///` | Triple-slash comment becomes the Model Explorer description |
| `Type` | Type hint: `NUMERIC`, `INT64`, `DECIMAL`, `STRING`, `DATETIME`, `BOOLEAN` |
| `VAL` (default) | Argument evaluated immediately before the function runs; value is passed in |
| `EXPR` | Unevaluated expression is passed in; the function decides when to evaluate |
| `=>` | Arrow introduces the function body |

## Where to Define

- **Power BI Desktop:** DAX query view or TMDL view → Model Explorer → Functions node
- **PBIP format:** `functions.tmdl` file (version-controllable)

## Calling Contexts

Functions can be called from:

- Measures
- Calculated columns
- Visual calculations
- Other functions (nesting supported)

## Example

```dax
DEFINE
/// Returns amount including tax at the specified rate
FUNCTION Finance.AddTax = (
    amount : NUMERIC,
    taxRate : NUMERIC
) =>
    amount * (1 + taxRate)

EVALUATE { Finance.AddTax ( 1000, 0.1 ) }   // Returns 1100
```

## Naming Convention

Community settled on **PascalCase** with dots for namespacing:

```
Sales.NetRevenue
Finance.AddTax
Operations.SafeDivide
```

## Notes

- Triple-slash `///` doc comment is mandatory — it is the only user-facing documentation for the function in Model Explorer
- Type hints are optional but recommended; they enable tooling support and catch type mismatches
- VAL is the default evaluation mode — explicitly choosing VAL or EXPR for every parameter is the single most important discipline in UDF writing (see [[val-vs-expr-parameter-evaluation]])

## Related

- [[val-vs-expr-parameter-evaluation]] — gotcha: the evaluation mode trap
- [[dax-udf-adoption-workflow]] — workflow: how to adopt UDFs in a production model
- [[dax-udf-define-function-pattern]] — pattern: DEFINE FUNCTION boilerplate
- [[daxlib-sqlbi-open-source-dax-library]] — pattern: SQLBI's community DAX function library
- [[udfs-vs-calculation-groups]] — comparison: when to use each
- [[udfs-vs-copy-paste-pattern]] — comparison: the organizational value of UDFs
