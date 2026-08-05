---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: gotcha
tags: [power-bi, gotcha, profit, revenue, retail]
---

# High Sales Does Not Mean High Profit

A product or category can rank at the top of a revenue leaderboard while generating zero or negative profit. Relying on sales alone to drive inventory and promotional decisions leads to wasted resources on unprofitable activity.

## Expected Behaviour

Products with the highest sales revenue are the most valuable to the business. Prioritizing them in inventory and promotions is the right strategy.

## Actual Behaviour

Deep discounting, high cost of goods sold, or shipping costs on certain product types can push total sales upward while profit collapses. Furniture is a common example — high revenue but negative profit due to heavy discounting and logistics costs. A product can be the #1 revenue driver and the #1 profit drain simultaneously.

## Why It Happens

- Discounts applied at checkout reduce margin without necessarily reducing the "sales price" shown in the dataset
- COGS may be disproportionately high for large/bulky items (furniture, electronics)
- Shipping costs on heavy items eat into margins
- Some categories are priced for market penetration (low margin, high volume strategy)
- The profit column already reflects these deductions — so a low profit is the correct signal that the category needs review

## How to Handle It

1. Always display Total Profit and Profit Margin alongside Total Sales in category and product views
2. Sort by Profit Margin, not just Sales, to surface the truly valuable products
3. Build a matrix visual with Sales on one axis and Profit on another — products in the upper-right quadrant are the true performers
4. Investigate categories where Sales rank and Profit rank differ significantly
5. Use a waterfall chart to break down profit by category — shows exactly where margin is being lost

## Related Gotchas

- Related to [[revenue-vs-profit-distinction]] — same root cause, dashboard-level symptom

## Related

- [[category-comparison-sales-vs-profit]] — `pattern`
- [[total-profit-dax-measure]] — `function`
