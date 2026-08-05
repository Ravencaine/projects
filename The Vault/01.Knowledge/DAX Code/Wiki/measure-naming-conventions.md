---
created: 2026-07-27
updated: 2026-08-02
source: "DAX Measure Library Architecture: From Messy to Maintainable"
note_type: atomic
tags: [dax, naming-conventions, measure-library, architecture]
---

# Measure Naming Conventions (DAX)

Consistent naming conventions for DAX measures that separate internal/base measures from business-facing KPIs and enable safe branching.

## Prefix Convention

| Prefix | Meaning | Example |
|--------|---------|---------|
| `_` (underscore) | Internal/base measure — not shown to business users | `_GrossProfit`, `_RowCount` |
| (no prefix) | Business-facing KPI | `Revenue`, `Gross Margin %` |
| `TEST` | Validation/test measure | `TEST Revenue = SUM(Sales[Revenue])` |
| `[Old]` | Deprecated — kept for history | `[Old] Revenue v1` |

## Underscore Rule

**Internal measures** (prefixed with `_`) are implementation details. They should:

- Be hidden from end users (set to "hidden" in the field list)
- Never be dragged directly onto visuals by business users
- Only be referenced by KPI measures (via measure branching)
- Be named after what they calculate, not how they calculate it

**Business KPI measures** (no prefix) are:

- Safe for business users to use directly on visuals
- Self-documenting without needing explanation
- Named after the business concept they represent

## Suffix Convention

| Suffix | Meaning |
|--------|---------|
| ` LY` | Same period last year |
| `vs Budget` | Variance to budget amount |
| `vs Budget %` | Percentage variance to budget |
| ` MTD / QTD / YTD` | Period-to-date variants |
| ` %` | Percentage (always as suffix, not prefix) |

## Examples

| Internal (Base) | Business KPI |
|----------------|-------------|
| `_GrossProfitAmount` | `Gross Profit` |
| `_GrossProfit LY` | `Gross Profit LY` |
| `_GrossProfit vs Budget` | `Gross Profit vs Budget %` |
| `_RowCount` | `Total Transactions` |

## Anti-Patterns

| Bad | Good |
|-----|------|
| `GrossProfitCalculation` | `_GrossProfit` |
| `SumOfRevenue` | `Revenue` |
| `RevenueLYCalculation` | `Revenue LY` |
| `MyCustomMeasure` | `<Business Concept>` |

## Related

- [[measure-library-architecture-pattern]]
- [[measure-branching-pattern]]
