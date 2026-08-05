---
created: 2026-08-01
updated: 2026-08-02
source: "Stop Copy-Pasting DAX The Power of Measure Branching in Power BI.md"
note_type: atomic
tags: [dax, measure-branching, base-measure, design, best-practices, beginner]
---

# Base Measure Design

The quality of a measure branching model depends on the base measures. Well-designed base measures are simple, stable, and contain no business logic.

## Principles for Base Measures

### Principle 1: One Column, One Aggregation

Each base measure wraps a single aggregation on a single fact table column:

```dax
Base Sales      = SUM ( Sales[Revenue] )
Base Cost       = SUM ( Sales[Cost] )
Base Quantity   = SUM ( Sales[Qty] )
Base Returns    = SUM ( Sales[ReturnAmount] )
```

Do not combine columns in a base measure — that is the job of derived measures.

### Principle 2: No Business Logic in Base Measures

Base measures should be raw. Business logic (what counts as a sale, how to handle returns) belongs in Layer 2 derived measures:

```dax
-- Base: raw aggregation only
Base Sales = SUM ( Sales[Revenue] )
Base Returns = SUM ( Sales[ReturnAmount] )

-- Derived: business logic applied here
Net Sales = [Base Sales] - [Base Returns]
```

This way, "what is a return" is defined once, in one place.

### Principle 3: Fact Table Columns Only

Base measures reference fact table columns — never dimension table columns. Dimensions are handled by filters and CALCULATE at the derived layer.

```dax
-- Correct: fact table column
Base Sales = SUM ( Sales[Revenue] )

-- Incorrect: dimension column in base measure
Base Sales = SUM ( Sales[Region] )  -- Region is a dimension, not a fact
```

### Principle 4: Avoid FILTER, CALCULATE, and Time Intelligence in Base Measures

Base measures should be pure aggregations. All filtering, context modification, and time intelligence belongs in derived/advanced measures:

```dax
-- Correct: pure aggregation
Base Sales = SUM ( Sales[Revenue] )

-- Incorrect: filtered base measure (move the filter to a derived measure)
Base Sales (Electronics) = SUM ( FILTER ( Sales, Sales[Category] = "Electronics" ) )
```

## Naming Convention

Prefix base measures with `Base` or `Core` to make the hierarchy obvious:

```
Base Sales
Base Cost
Base Quantity
Base Returns
```

This makes it immediately clear these are the foundation of the model.

## How Many Base Measures?

Typically one per fact table column that is directly aggregated. For a Sales fact table:

| Column | Base Measure |
|--------|-------------|
| Revenue | Base Sales |
| Cost | Base Cost |
| Qty | Base Quantity |
| ReturnAmount | Base Returns |
| DiscountAmount | Base Discount |

Do not create base measures for every column — only those that are genuinely aggregated in KPIs.

## Related

- [[measure-branching-pattern]] — the full three-layer branching structure
- [[measure-branching-calculate-composition]] — extending base measures with CALCULATE
- [[measure-branching-naming-conventions]] — organizing the measure hierarchy
