---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: comparison
tags: [dax, user-defined-function, copy-paste, maintainability, governance, organization]
---

# UDFs vs Copy-Paste Pattern

UDFs eliminate the primary failure mode of copy-paste: silent, independent drift of duplicated business logic across a model over time.

## Summary

Copy-paste is how one business rule becomes twelve slightly different business rules. UDFs make the rule a single named object — updated once, correct everywhere.

## Copy-Paste Pattern (Before)

```dax
-- Measure 1: copied from screenshot, lightly modified
MEASURE Sales[Net Revenue] =
    CALCULATE(
        SUM(Sales[Amount]),
        Sales[Type] = "Revenue",
        Sales[ExcludeDiscount] = TRUE()
    )

-- Measure 2: same rule, different author, no way to find Measure 1
MEASURE Sales[Net Revenue Final] =
    CALCULATE(
        SUM(Sales[Amount]),
        Sales[Type] = "Revenue",
        Sales[ExcludeDiscount] = TRUE(),
        Sales[Region] = "EMEA"   -- silently different
    )

-- Measure 3: third copy, different still
MEASURE Sales[NetRev_Corp] =
    CALCULATE(
        SUM(Sales[Amount]),
        Sales[ExcludeDiscount] = TRUE()
        -- forgot Sales[Type] = "Revenue" entirely
    )
```

**Problem:** Three measures. Three subtly different implementations of the same business rule. Finance changes the rule: update all three. Nobody knows how many copies exist.

## UDF Pattern (After)

```dax
DEFINE
/// Net revenue: sum of sales amount excluding discounts
FUNCTION Finance.NetRevenue = (
    amount : CURRENCY EXPR
) =>
    CALCULATE(
        amount,
        Sales[Type] = "Revenue",
        Sales[ExcludeDiscount] = TRUE()
    )

MEASURE Sales[Net Revenue]         = Finance.NetRevenue( SUM(Sales[Amount]) )
MEASURE Sales[Net Revenue Final]   = Finance.NetRevenue( SUM(Sales[Amount]) )
MEASURE Sales[NetRev_Corp]         = Finance.NetRevenue( SUM(Sales[Amount]) )
```

**Result:** One definition. Finance updates the rule once. All three measures inherit the fix. The new analyst reads the function name and knows what it does.

## When Copy-Paste Still Makes Sense

Do not write UDFs for:
- One-off measures with no reuse potential
- Grain-dependent calculations where the model assumption is part of the logic
- Experimental or exploratory measures that may be deleted
- Measures where the expression itself is the documentation (the logic is visible and changing it would be noticed)

## Key Insight

The organizational value of UDFs exceeds their computational value. Nothing previously impossible becomes possible. What changes is whether a team's DAX can be maintained by people who didn't write it.

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[dax-udf-adoption-workflow]] — workflow
- [[val-vs-expr-parameter-evaluation]] — gotcha
