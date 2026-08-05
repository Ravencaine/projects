---
created: 2026-07-29
updated: 2026-08-02
source: DAX Measure Library Architecture — From Messy to Maintainable (Tejwani, 2026-01-19)
note_type: snippet
tags: [dax, measure-library, documentation, template, purpose, dependencies, business-rules]
---

# DAX Measure Documentation Template

The standard documentation template for DAX measures, with three documentation levels based on measure complexity.

## The Full Template

Place this as a comment block at the top of the measure expression or in the measure description field:

```dax
/*
DOCUMENTATION
PURPOSE: What business question does this answer?
USAGE: When should this be used (and when NOT)?
DEPENDENCIES: What measures/tables does it rely on?
BUSINESS RULES: What filters or logic are applied?
FORMULA: The underlying calculation logic
OWNER: Who built it / who maintains it?
LAST MODIFIED: When was it last changed?
*/
```

## Real Example

```dax
Customer Lifetime Value =
VAR AvgOrderValue = [Average Order Value]
VAR AvgFrequency = [Average Purchase Frequency]
VAR AvgLifespan = [Average Customer Lifespan]
VAR LTV = AvgOrderValue * AvgFrequency * AvgLifespan
RETURN LTV
```

Documentation:

```
PURPOSE: Estimates total revenue a customer will generate over their relationship with the company
USAGE: Use for customer segmentation and acquisition cost decisions. NOT for actual revenue reporting.
DEPENDENCIES: [Average Order Value], [Average Purchase Frequency], [Average Customer Lifespan]
BUSINESS RULES: Only includes completed orders. Excludes returns and internal transactions.
FORMULA: AOV × Purchase Frequency × Customer Lifespan
OWNER: Sarah Chen (sarah.chen@company.com)
LAST MODIFIED: 2024-12-15
```

## Three Documentation Levels

Not every measure needs the full template.

### Level 1: Base Measures (Minimal)

Purpose is obvious from the name.

```dax
_Sales Amount = SUM(Sales[Amount])
// Base measure for all sales calculations
```

### Level 2: Business Metrics (Medium)

Explain any business rules that aren't obvious.

```dax
Active Customers =
CALCULATE(
    DISTINCTCOUNT(Sales[CustomerID]),
    Sales[OrderDate] >= TODAY() - 365
)
/*
Active = purchased within last 365 days
Used for retention analysis
See Customer Analytics dashboard
*/
```

### Level 3: Complex KPIs (Full Template)

Everything someone needs to understand and maintain it.

Use the full PURPOSE / USAGE / DEPENDENCIES / BUSINESS RULES / OWNER / MODIFIED template.

## Documentation Without Context Is Bad Documentation

**Bad:**
```dax
// Calculates customer lifetime value
```

**Good:**
```dax
/*
PURPOSE: Estimates total revenue per customer over their lifespan
USAGE: Marketing budget decisions, NOT financial reporting
DIFFERS FROM: [Actual Customer Revenue] — this is predictive
*/
```

## Documentation as a Conversation

Write documentation to answer the questions a confused analyst (or future you) will have:
- What does this measure?
- When should I use it?
- When should I NOT use it?
- Why does it exclude X?
- Who do I ask if something looks wrong?

## The Test

Show the documentation to someone not on your team. If they still have questions, the documentation is incomplete.

## Related

- [[dax-measure-naming-convention-framework]] — naming conventions
- [[measure-governance-process]] — governance
- [[implement-dax-measure-library-architecture]] — implementation
