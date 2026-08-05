---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: comparison
tags: [dax, user-defined-function, calculation-groups, comparison, reuse]
---

# UDFs vs Calculation Groups

When to use DAX user-defined functions and when to use calculation groups — the two reuse mechanisms in DAX.

## Summary

UDFs solve the **business logic reuse** problem: parameterized rules with inputs. Calculation groups solve the **time intelligence variation** problem: applying the same calculation across different filter contexts. Most serious models use both.

## UDFs

### What They Do

Named, parameterized functions living in the semantic model. Each call evaluates the function body in the caller's context.

### Best For

- Parameterized business rules: `Finance.NetRevenue(amount, taxRate)`
- Tiered margin logic
- Currency normalization
- Safe divide with business-specific default
- Text cleanup rules for data matching

### Limitation

A function receives its arguments and evaluates. It does not automatically apply itself across a set of dimension members the way calculation groups do.

## Calculation Groups

### What They Do

A dimension-like object in the model that applies a set of calculation expressions across all measures in scope simultaneously. A single calculation group item (e.g., "Year-to-Date") rewrites every measure's expression.

### Best For

- Time intelligence: YTD, QTD, MTD, PY, YoY%
- Scenario analysis: Actual, Budget, Forecast
- Any context transformation that should apply uniformly to every measure

### Limitation

Calculation groups transform the filter context. They are not designed for parameterized business logic with typed inputs.

## Comparison Table

| Criteria | UDFs | Calculation Groups |
|----------|------|-------------------|
| Primary use | Business logic with parameters | Context transformation |
| Input mechanism | Function arguments | Active calculation group item |
| Scope | Per-call | Per-measure (applied to all) |
| Time intelligence | Can express any individual pattern | Purpose-built (YTD, PY, YoY%) |
| Parameterized | Yes | Limited |
| Model Explorer visibility | Yes | Yes |
| TMDL file | `functions.tmdl` | `calculationGroups.tmdl` |
| Performance impact | Per-function evaluation | Single context scan per measure |

## When to Use Both

A model with serious DAX typically has:
- **Calculation groups** for all time intelligence variations (YTD, QTD, PY, YoY%)
- **UDFs** for business logic: `Finance.NetRevenue`, `Sales.SafeDivide`, `Ops.WorkingDaysAdjusted`

Do not replace calculation groups with UDFs for time intelligence — calculation groups handle context rewriting more efficiently and with cleaner syntax.

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[dax-udf-adoption-workflow]] — workflow
