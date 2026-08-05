---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, calculated-column, measure, decision-tree, beginner, row-context, filter-context]
---

# Calculated Column vs Measure: Decision Tree

Four questions that reliably determine whether a given calculation belongs as a calculated column or a measure. Work through them in order.

## The Decision Tree

**Question 1: Do I need to filter or slice by this result?**
- YES → Calculated column
- NO → Go to Question 2

Can you put this result in a slicer? Can you use it as rows or columns in a Matrix? Can you filter a visual by this value? If yes, it needs to exist as a stored value — a column.

**Question 2: Am I aggregating values (SUM, AVERAGE, COUNT, MIN, MAX)?**
- YES → Measure
- NO → Go to Question 3

Any formula that summarises multiple rows into a single number belongs in a measure. These are the most common measure cases.

**Question 3: Does the calculation need to respond to filters and change dynamically?**
- YES → Measure
- NO → Go to Question 4

If you want the result to be different depending on what is filtered in the report (time period, region, product), it needs to be a measure. Calculated columns are static — they don't react to report filters.

**Question 4: Is this a row-level property or categorisation?**
- YES → Calculated column
- NO → Measure (default fallback)

Is this a property of each individual row (e.g., "Is this order large?" / "What is the full name of this customer?")? Or is it an aggregate that should change based on context? Row-level = column. Aggregate = measure.

## Quick Reference Table

| Scenario | Choice |
|----------|--------|
| Customer full name | Column |
| Product price category (Budget/Standard/Premium) | Column |
| Date dimension key for relationship | Column |
| Is this order over $1,000? | Column |
| Total revenue | Measure |
| Profit margin % | Measure |
| Year-over-year growth | Measure |
| Average order value | Measure |
| Customer count | Measure |
| % of total sales | Measure |

## The Mental Model

> **Columns = properties of things. Measures = numbers about things.**

Products have price categories (property → column). Sales have totals (numbers → measure). Customers have names (property → column). Sales have customer counts (numbers → measure).

## Related

- [[calculated-column-row-context]] — what context columns operate in
- [[measure-filter-context]] — what context measures operate in
- [[calculated-column-vs-measure-total-sums]] — common failure when percentages are put in columns
