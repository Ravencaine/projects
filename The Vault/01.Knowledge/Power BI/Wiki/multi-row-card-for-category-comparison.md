---
created: 2026-08-13
source: Top Use Cases of Multi-Row Cards in Power BI
source_url: https://medium.com/write-a-catalyst/top-use-cases-of-multi-row-cards-in-power-bi-19934e239698
note_type: atomic
tags: [power-bi, multi-row-card, comparison, variance, budget-vs-actual]
---

# Multi-Row Card for Category Comparison

Use Multi-Row Cards with page-level filters to compare metrics across categories: Budget vs. Actual, Current Month vs. Previous Month, Target vs. Achievement.

## Purpose

Delivers a compact comparison view across time periods or categories without needing a chart. More scannable than a small multiple chart for 2–3 comparison pairs.

## When to Use

- Financial performance dashboards (budget vs. actual)
- Time period comparison reports (month-over-month, YoY)
- Target tracking dashboards (target vs. achievement)

## Design Notes

- Add a Variance or Delta row showing the difference (absolute and/or %)
- Use conditional formatting on variance: green (favourable), red (unfavourable)
- Keep comparison pairs to 2–3 metrics per card to avoid cognitive overload

## Related

- [[Multi-Row-Card-as-KPI-Summary]]
- [[Multi-Row-Card-Best-Practices]]
