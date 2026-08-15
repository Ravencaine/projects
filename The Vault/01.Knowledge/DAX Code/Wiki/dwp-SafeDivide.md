---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: function
tags: [dax, udf, safe-divide, divide, blank, zero, parameter]
---

# dwp.SafeDivide — Parameterized Safe Division UDF

Replaces all ad-hoc `IF(Denominator=0, BLANK(), DIVIDE(...))` patterns across a model with a single, typed, reusable function.

## Signature

```
dwp.SafeDivide(Numerator: NUMERIC, Denominator: NUMERIC): NUMERIC
```

## Definition

```dax
DEFINE
    /// Returns Numerator safely divided by Denominator.
    /// @param {NUMERIC} Numerator — value to divide
    /// @param {NUMERIC} Denominator — value to divide by
    /// @returns division result, or BLANK if denominator is zero
    FUNCTION dwp.SafeDivide = (
        Numerator: NUMERIC,
        Denominator: NUMERIC
    ) =>
        IF ( Denominator = 0, BLANK(), DIVIDE ( Numerator, Denominator ) )

EVALUATE
{ dwp.SafeDivide ( [Total Sales], [Total Cost] ) }
```

## Usage

```dax
// Simple call
[Safe Margin] := dwp.SafeDivide ( [Total Profit], [Total Revenue] )

// Inside a measure
Gross Margin % :=
VAR _margin = dwp.SafeDivide ( [Gross Sales], [Total Revenue] )
RETURN
    IF ( HASONEVALUE ( Calendar[Year] ), _margin, BLANK() )
```

## Key Design Points

- `BLANK()` on zero denominator — returns empty in visuals rather than `INFINITY` or an error
- Both parameters are `NUMERIC` (value type) — they evaluate eagerly when called
- No context transition needed — pure arithmetic, not measure-dependent

## UDF Candidates It Consolidates

Before UDFs: 6 near-identical measures, each containing `IF(x=0, BLANK(), DIVIDE(...))` written slightly differently. After: 1 function. Every measure that called one of the 6 now calls `dwp.SafeDivide`.

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[Value-vs-Expression-Parameter-Types]] — parameter type explanation (both NUMERIC here — no expression needed)
