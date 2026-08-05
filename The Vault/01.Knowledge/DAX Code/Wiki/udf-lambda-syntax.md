---
created: 2026-07-27
updated: 2026-08-02
source: "DAX Finally Got User-Defined Functions"
note_type: atomic
tags: [dax, udf, lambda, user-defined-functions, new-feature]
---

# DAX UDF / Lambda Syntax

DAX User-Defined Functions (UDFs) allow parameterized reusable expressions within DEFINE FUNCTION blocks, using Lambda-style anonymous function syntax.

## Syntax

```dax
DEFINE
    FUNCTION FunctionName (param1, param2)
    RETURNS <scalar type>
    AS
        VAR Result = <expression using param1, param2>
        RETURN Result

MEASURE Sales[My Measure] =
    FunctionName( [Revenue], [Cost] )
```

## Examples

**SafeMargin UDF — replaces repeated DIVIDE-with-BLANK patterns:**

```dax
DEFINE
    FUNCTION SafeMargin (Revenue, Cost)
    RETURNS NUMBER
    AS
        VAR Profit = Revenue - Cost
        RETURN DIVIDE(Profit, Revenue, BLANK())

MEASURE Sales[Gross Margin %] = SafeMargin([Revenue], [Cost])
MEASURE Sales[Net Margin %] = SafeMargin([Revenue], [Cost] - [Overhead])
```

**Lambda inline syntax (anonymous):**

```dax
MEASURE Sales[Inline Test] =
    (x, y) => DIVIDE(x - y, x, 0)  -- anonymous Lambda
```

## What UDFs Can Do

- Encapsulate repeated calculation logic across measures
- Replace repeated DIVIDE-with-BLANK patterns with a single function
- Make complex expressions more readable by naming sub-expressions

## What UDFs Cannot Do

- Replace standalone measures (they are defined inside DEFINE FUNCTION, used inside measures)
- Have side effects (cannot write to model, cannot call external APIs)
- Be shared across PBIX files (scoped to the DEFINE block)
- Provide performance optimization (calling a UDF does not cache or pre-compute)

## Related

- [[var-in-dax]] — VAR used inside UDFs for intermediate calculations
- [[pattern-2-defensive-dax]] — UDFs can implement defensive DAX patterns
