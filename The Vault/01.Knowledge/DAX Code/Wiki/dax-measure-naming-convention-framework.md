---
created: 2026-07-29
updated: 2026-08-02
source: DAX Measure Library Architecture — From Messy to Maintainable (Tejwani, 2026-01-19)
note_type: reference
tags: [dax, measure-library, naming-convention, findability, naming, pattern]
---

# DAX Measure Naming Convention Framework

The naming convention formula and rules that make DAX measures findable through search. Based on Tejwani's framework.

## The Formula

```
[Business Object] [Metric Name] [Modifier] [Time Period]
```

## Examples

```
✅ Customer Lifetime Value
✅ Sales vs Target %
✅ Revenue per Customer
✅ Profit Margin %
✅ Inventory Turnover Ratio
```

## Components

### Business Object (optional)

- **When to use:** The metric applies to a specific domain
- **Values:** Customer, Sales, Product, Inventory, Finance, Operations
- **Example:** `Customer Lifetime Value` — business object is Customer

### Metric Name (required)

- **What it is:** The actual thing being measured
- **Examples:** Lifetime Value, Conversion Rate, Margin, Revenue, Churn Rate

### Modifier (optional)

- **What it shows:** What kind of comparison or calculation
- **Examples:** vs Target, vs LY, per Customer, Growth Rate, % Change

### Time Period (optional — only when baked in)

- **When to use:** The time period is fixed inside the measure definition
- **Values:** YTD, MTD, QTD, LY, YoY
- **Example:** `Sales YTD` — time period is fixed in the measure

## Special Prefixes

| Prefix | Meaning | Example |
|--------|---------|---------|
| `_` (underscore) | Base measure — internal use only | `_Sales Amount` |
| `#` (hash) | Temporary / test measure | `#Test Revenue Metric` |
| `!` (exclamation) | Needs review / fix | `!Revenue Calc Error` |

## Naming Convention Test

For every measure, ask:

**Q1: Findability**
If someone searches the most obvious term, will they find it?
- ✅ "lifetime value" → finds `Customer Lifetime Value`
- ❌ "CLV" → misses `Customer Lifetime Value`

**Q2: Describes WHAT, not HOW**
- ✅ `Customer Lifetime Value` — what it measures
- ❌ `Sum_of_Revenue_by_Customer_with_SUMX` — how it's calculated

**Q3: Consistent with similar measures**
- If you have `Sales vs Target`, don't also have `Target Variance — Revenue`
- Pick one pattern and stick to it

**Q4: New team member test**
- Show the name to someone not on your team
- If they ask "what does that mean?", the name fails

## What to Avoid

```
❌ Calc_Rev_v2_final
❌ SALES_AMOUNT_2024
❌ my_test_measure
❌ DO_NOT_USE
❌ temp123
```

If something is temporary, use the `#` prefix and delete it within the sprint.

## Name Collisions: The Before State

Same measure, five different names — the problem this solves:

```
Customer Lifetime Value
CLV
LTV_Customer
Customer_LTV_Total
Lifetime Value (Customers)
```

When someone searches "lifetime value," they find three. Missed two. All three are different calculations.

## Rule: Stick to One Pattern Per Category

If your model has `Sales vs Target`, do not introduce `Target Variance — Revenue` as a separate pattern for the same category. Pick the pattern, document it, enforce it.

## Related

- [[implement-dax-measure-library-architecture]] — implementation workflow
- [[measure-governance-process]] — governance
- [[dax-measure-documentation-template]] — documentation template
