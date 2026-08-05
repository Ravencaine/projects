---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: atomic
tags: [dax, user-defined-function, data-modeling, semantic-model, anti-pattern]
---

# UDFs Don't Fix the Model

Wrapping broken DAX in a named function does not fix the underlying semantic model. If the grain is wrong, relationships are ambiguous, or the fact table is a flat ERP export, a UDF gives the problem a nicer name.

## Definition

A UDF is a calculation-layer abstraction. It can only compute correctly from a correct semantic model. UDFs are downstream of data modeling decisions — they cannot compensate for errors in grain, relationship cardinality, or fact table structure.

## Key Points

- **Grain errors:** A fact table with mixed-grain rows produces wrong results whether computed via UDF or inline DAX
- **Ambiguous relationships:** Multiple active paths between tables cause DAX to pick one silently — a function cannot override this
- **Missing dimensions:** A UDF that filters on a column not in the model returns blank or unexpected results
- **The pattern repeats:** Fabric, Copilot, calculation groups — every new capability in the Power BI stack has the same prerequisite: a correct semantic model

## Examples

**Poor model + UDF:**
```dax
-- Wrong grain: fact table has both transaction-level and daily-summary rows
FUNCTION Finance.TotalSales = ( amount : CURRENCY EXPR ) =>
    SUM( amount )   -- double-counts summary rows
```

**Correct model + UDF:**
```dax
-- Clean fact table: one grain, one relationship per dimension
FUNCTION Finance.TotalSales = ( amount : CURRENCY EXPR ) =>
    SUM( amount )   -- correct: each row is one transaction
```

## Rule

Spend 60% of model development time on the semantic model before writing any DAX — including UDFs.

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[dax-udf-adoption-workflow]] — workflow
