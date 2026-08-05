---
created: 2026-07-27
updated: 2026-08-02
source: "The 5 DAX Patterns Senior Analysts Use"
note_type: pattern
tags: [dax, single-source-of-truth, architecture, dry, measure-branching]
---

# Pattern 4: Single Source of Truth

Every business concept has exactly ONE measure that defines it. All other measures, visuals, and calculations reference that single source. No duplication of logic anywhere in the model.

## Purpose

When business logic is duplicated across measures, a change to the business rule requires updating N measures manually — and some will be missed. A single source of truth ensures every calculation reflects the current business rules automatically.

## The Anti-Pattern

```dax
-- Duplication: same revenue logic in 3 different measures
Revenue Summary = SUMX(Sales, Sales[Qty] * Sales[Price]) - SUMX(Sales, Sales[Returns])

Revenue Dashboard = SUMX(Sales, Sales[Qty] * Sales[Price]) - SUMX(Sales, Sales[Returns])

Revenue KPI = SUMX(Sales, Sales[Qty] * Sales[Price]) - SUMX(Sales, Sales[Returns])
```

To change the revenue definition (e.g., exclude intercompany): update all 3.

## The Pattern

```dax
-- Single source of truth
Revenue = SUMX(Sales, Sales[Qty] * Sales[Price]) - SUMX(Sales, Sales[Returns])

-- All other measures reference the single source:
Revenue Summary = [Revenue]
Revenue Dashboard = [Revenue]
Revenue KPI = [Revenue]
```

To change the revenue definition: update one measure.

## Implementation

1. Identify every distinct business concept in the model (Revenue, Profit, Margin, Count, etc.)
2. Create exactly one base measure for each concept
3. Hide base measures from business users (set to hidden)
4. All KPI measures and visuals reference the base measures
5. Never create a second measure that calculates the same concept differently

## Related

- [[5-senior-dax-patterns-source]]
- [[pattern-1-measure-branching]] — the foundational pattern that enables single source of truth
- [[measure-library-architecture-pattern]] — the organizational structure that enforces single source of truth at the model level
