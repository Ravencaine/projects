---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "finance", "gross-margin", "profitability"]
note_type: pattern

---

# Gross Margin Calculation in DAX

Measuring the percentage of revenue retained after subtracting direct costs.

## Formula

```
Gross Margin % = ( Revenue - Cost ) / Revenue * 100
```

## DAX Pattern

```dax
Gross Revenue := SUM( 'Sales'[Revenue] )
Cost of Goods Sold := SUM( 'Sales'[COGS] )

Gross Profit :=
[Gross Revenue] - [COGS]

Gross Margin % :=
DIVIDE( [Gross Profit], [Gross Revenue] )
```

## Notes

- COGS should include only direct costs (materials, direct labor)
- Exclude overhead, marketing, and R&D from COGS
- Gross Margin % varies by industry: software companies often see 70-90%, manufacturing 20-40%

## Related

- [[mrr-and-arr-metrics-in-dax]]
- [[current-ratio-and-quick-ratio-in-dax]]
