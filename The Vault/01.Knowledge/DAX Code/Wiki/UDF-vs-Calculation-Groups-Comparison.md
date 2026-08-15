---
created: 2026-08-09
updated: 2026-08-09
source: "DAX user-defined functions (UDF) vs. calculation groups.md"
note_type: comparison
tags: [dax, user-defined-function, calculation-groups, udf, comparison, code-reuse]
---

# UDF vs Calculation Groups

UDFs and calculation groups serve fundamentally different purposes. Confusing them leads to poor model design, maintenance problems, and performance degradation.

## At a Glance

| Aspect | User-Defined Function | Calculation Group |
|--------|----------------------|-------------------|
| Target audience | Developer | Report user |
| Visibility | Invisible to users | Visible in reports |
| Purpose | Code reuse | User-facing selection |
| Parameters | Explicit (typed) | Via filter context |
| Query plan | Macro-expanded | Filter context manipulation |
| Reuse scope | Measures, calc items, security roles | Visual-level selection |

## UDF — Developer Tool for Code Reuse

A UDF is a named DAX expression with typed parameters. It is expanded in the query plan before execution:

```dax
DaxPatterns.NewReturning.Absolutes.NewCustomers =(
    TxCustomerKeyColumn: COLUMNREF,
    CustomerTable: TABLEREF,
    TxDateColumn: COLUMNREF,
    DateColumn: COLUMNREF
)=>
    FILTER(
        DaxPatterns.NewReturning.Absolutes.CustomersWithNewDate(...),
        [@NewCustomerDate] IN VALUES(DateColumn)
    )
```

Parameters are resolved at plan-construction time. Multiple calls to the same UDF within one query do not compound filter-context overhead — each call is independently expanded.

## Calculation Group — User-Facing Selector

A calculation group exposes calculation items as a slicer. Every measure in the visual responds to the selected item:

```
[Current Month] → applied to all measures
[Last Quarter]  → applied to all measures
```

The same filter transformation applies to every measure simultaneously. This is the value proposition: one slicer, whole visual responds.

## When UDFs Are Better

- Business logic is complex or shared across multiple measures
- The same rule must appear in both a measure and a calculation item
- Side-by-side visuals: one measure uses the logic, another does not
- Parameters vary per context (different date columns, different key columns)
- Performance: logic invoked multiple times per query (filter-context overhead accumulates)

## When Calculation Groups Are Better

- User needs to choose which calculation applies to all measures in a visual
- The transformation is simple and uniform (period selection, scale factor)
- No parameters needed — the same result applies to every measure

## The Hybrid Pattern

The strongest models combine both:

1. Define business logic in **model-independent UDFs** (DaxPatterns.*)
2. Wrap in **model-dependent UDFs** (Local.*)
3. Call from both **standalone measures** and **calculation items**

```dax
-- UDF defines the business rule
Local.NewCustomers = () =>
    DaxPatterns.NewReturning.Absolutes.NewCustomers(
        Sales[CustomerKey], Customer, Sales[Order Date], 'Date'[Date]
    )

-- Used in a measure
Sales New Customers =
CALCULATE([Sales Amount], Local.NewCustomers())

-- Used in a calculation item
New customers =
CALCULATE(SELECTEDMEASURE(), Local.NewCustomers())
```

Business rule defined once. Every consumer calls the same function.

## Decision Tree

```
Does the user need to choose which calculation applies to ALL measures in this visual?
│ YES → Calculation Group
│ NO  ↓
Is the logic complex, shared across multiple places, or does it need parameters?
│ YES → UDF (in measures, calc items, or both)
│ NO  → Simple measure expression
```

## Related

- [[Source-DAX-User-Defined-Functions-vs-Calculation-Groups]] — source note
- [[dax-udf-define-function-pattern]] — UDF syntax pattern
- [[calculation-groups]] — calculation groups reference
