---
created: 2026-08-11
source: 📊 Use Cases of Donut Charts in Power BI.md
author:
  - Anurodh Kumar
note_type: atomic
tags: [visual-type, chart, part-to-whole]
---

# Donut Chart Use Cases

<!-- part-to-whole data with fewer than 5–6 categories, where proportional share is the primary insight -->

## Definition

Donut charts display part-to-whole relationships in a circular layout with a hollow center. Each arc represents a category's proportion of the total. Suitable when the number of categories is small and the visual goal is communicating relative contribution, not precise values.

## Key Points

- **Category count limit:** 5–6 categories maximum — beyond this the arcs become unreadable
- **Center use:** Power BI allows placing a KPI, total, or label in the donut hole to add context without a separate card
- **Better for proportions:** When exact values matter, a table or bar chart outperforms a donut
- **Not for trends:** Time-series data requires line or bar charts — donut charts show a single snapshot
- **Readability:** Power BI sorts segments by value descending by default; preserve this order

## Examples

| Use Case | Example Measure |
|---|---|
| Category-wise contribution | Sales by Product Category |
| Market share | Brand share vs. competitors |
| Budget breakdown | Budget vs. actual by department |
| Customer segmentation | Gold / Silver / Bronze tiers |
| Survey / sentiment results | Satisfied / Neutral / Unsatisfied |
| Regional distribution | Sales contribution by region |
| Employee distribution | Headcount by department or role |

## Related

- [[Donut Chart Limitations]] (companion atomic — when not to use)
- Source: [Anurodh Kumar — Use Cases of Donut Charts in Power BI](https://medium.com/write-a-catalyst/use-cases-of-donut-charts-in-power-bi-e2555ec0d901)
