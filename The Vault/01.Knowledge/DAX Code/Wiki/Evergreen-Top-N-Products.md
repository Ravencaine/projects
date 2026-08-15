---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
note_type: atomic
tags: [dax, top-n, evergreen, sqlbi, pattern]
---

# Evergreen Top-N Products

A product qualifies as "evergreen" when it appears in the top-N list in at least *coverage%* of the reporting periods (years, months, etc.).

## Definition

A product is evergreen if it is among the top-N performers by a given measure in at least a defined threshold proportion of all periods. The threshold prevents single-year flash products from qualifying — only products with sustained high performance across multiple periods are selected.

## Key Points

- **Coverage threshold** is a configurable fraction (e.g. 0.8 = 80%) applied against the total number of periods
- The period list is enumerated with `ALLSELECTED()` so the threshold adapts to the visual's selected years
- Products meeting the threshold are flagged once and then used as a filter on any downstream measure (count, sum, ratio)
- The pattern identifies **stable bestsellers** vs **seasonal winners:** useful for category planning and inventory forecasting
- The same logic applies to customers, stores, channels, or any dimension with a time grain

## How It Works (High Level)

```
1. GENERATE (all years,  TOPN (N per year,  products,  [measure]))
2. GROUPBY (count appearances per product → NumOfYears)
3. FILTER   (keep only products where NumOfYears >= TotalYears × Coverage)
4. Apply as KEEPFILTERS(BestProds) in CALCULATE
```

## Examples

- **Retail KPI scorecards:** find the 10 SKUs that appear in the top-10 revenue list every year — these get permanent shelf space
- **Sales compensation:** only products that were top-10 in ≥80% of the year qualify for accelerator commissions
- **Customer retention:** find the 100 customers appearing in the top-100 by margin in ≥4 of the last 5 years

## Related

- [[query-measure-function-workflow]] — the three-stage workflow used to author this pattern
- [[Local.ComputeForBestProds]] — the reusable UDF implementing this pattern
- [[TopN-ProductKey-Override-Gotcha]] — a filter-context pitfall when using this pattern
- [[Source-SQLBI-Top-10-Every-Year]] — primary source from SQLBI
