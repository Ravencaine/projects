---
created: 2026-07-29
updated: 2026-08-02
source: DAX Measure Library Architecture — From Messy to Maintainable (Tejwani, 2026-01-19)
note_type: atomic
tags: [dax, measure-library, technical-debt, waste, cost, search-time, knowledge-loss]
---

# The Hidden Cost of Messy Measures

The three costs of a disorganized DAX measure library: wasted search time, formula inconsistency, and knowledge loss when analysts leave.

## Cost 1: Search Time

A team of 6 analysts spending 4 hours/week searching for, recreating, or debugging existing measures:

```
4 hours/week × 6 analysts × 52 weeks = 1,248 hours/year
At $75/hour = $93,600/year in wasted salary
```

This is not an exaggeration — it's a conservative estimate from a real team. The measure existed. Nobody could find it. Rebuilding was faster than searching.

## Cost 2: Inconsistency

The same business metric, calculated three different ways:

```
Finance: Customer Lifetime Value (completed orders only)
Sales: Customer Lifetime Value (all orders)
Marketing: Customer Lifetime Value (website-engaged customers only)
```

Three correct answers. Three different numbers. The CFO asks "What is our customer lifetime value?" and gets three answers.

No amount of DAX sophistication fixes inconsistent definitions.

## Cost 3: Knowledge Loss

When an analyst leaves, they take their understanding of the model with them.

Measures found after a departure:

```
[Calc_Adjusted_Rev_Final]    — what's "adjusted"?
[Test_Metric_2]              — is this still a test?
[DO_NOT_USE_OLD]             — then why is it in the model?
```

The measures are still there. The context isn't.

## The Breaking Point

When `[DO_NOT_USE_OLD]` appears in a shared model, it's the signal: either build a system for organizing DAX, or drown in technical debt forever.

The cost of building the system is less than the cost of living with the chaos.

## The Starting Point

Before implementing any architecture, answer this question honestly:

> "Can you find [specific measure] in under 1 minute?"

If the answer is no for commonly-requested measures, the hidden cost is already accruing.

## Related

- [[implement-dax-measure-library-architecture]] — the solution
- [[when-measure-library-architecture-is-essential]] — scope decision
- [[measure-library-architecture-roi]] — quantified before/after
