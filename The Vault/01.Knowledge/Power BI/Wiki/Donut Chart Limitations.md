---
created: 2026-08-11
source: 📊 Use Cases of Donut Charts in Power BI.md
author:
  - Anurodh Kumar
note_type: atomic
tags: [visual-type, chart, anti-pattern]
---

# Donut Chart Limitations

<!-- conditions under which donut charts are the wrong visual choice in Power BI -->

## Definition

Donut charts are contraindicated when the data has more than 5–6 categories, when exact values are more important than proportions, or when the insight involves change over time.

## Key Points

- **Too many categories:** Arc segments become indistinguishable beyond ~6 categories — use a bar chart instead
- **Precise values required:** Donut arcs communicate rough proportions; if readers need exact figures, a table or horizontal bar chart is more accurate
- **Time-series data:** Donut charts are static snapshots — they cannot show trends, changes, or comparisons across time periods; use line charts or clustered bar charts
- **Negative or zero values:** Donut charts cannot represent negative values or zero — filter these out or switch visual type
- **Near-equal values:** When all segments are similar in size, the donut provides no visual discrimination — a table may serve better

## Related

- [[Donut Chart Use Cases]] (companion atomic — when to use)
- Source: [Anurodh Kumar — Use Cases of Donut Charts in Power BI](https://medium.com/write-a-catalyst/use-cases-of-donut-charts-in-power-bi-e2555ec0d901)
