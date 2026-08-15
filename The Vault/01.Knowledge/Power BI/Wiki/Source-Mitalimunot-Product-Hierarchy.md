---
created: 2026-08-10
updated: 2026-08-10
source: Building a Product Hierarchy Analytics Dashboard in Power BI: A Beginner's Journey
source_url: https://medium.com/@mitalimunot64/building-a-product-hierarchy-analytics-dashboard-in-power-bi-a-beginners-journey-6b3c72375d41
note_type: source
tags: [power-bi, dashboard-design, product-hierarchy, beginner, treemap, slicer, visual-design]
---

# Source: Mitalimunot — Product Hierarchy Analytics Dashboard

> **Type:** beginner case study / project walkthrough
> **Author:** Mitalimunot
> **Published:** 2026-08-09
> **URL:** https://medium.com/@mitalimunot64/building-a-product-hierarchy-analytics-dashboard-in-power-bi-a-beginners-journey-6b3c72375d41
> **Routed to:** Power BI
> **Category:** Power BI, Dashboard Design, Product Hierarchy, Beginner Project

## Summary

Beginner's account of building a Product Hierarchy Analytics Dashboard in Power BI from a flat product catalog. The dataset: 74 products, 3-level hierarchy (Primary → Secondary → Tertiary category). Two dashboard pages: Executive Summary (KPI cards + 4 summary visuals + filter panels) and Drill-Down Analysis (3 cascading slicers + detailed visuals + data table). Key design lessons: treemap beats bar chart at ~15+ categories; separate cascaded slicers outperform a single dropdown for hierarchy navigation; two pages reflect two mental modes ("orient me" vs "let me investigate"); KPI cards do disproportionate communication work relative to build effort.

## Key Claims / Components

1. **Dataset:** 74 products, 3-level hierarchy, plus product type, price range, purchase frequency, seasonal relevance, target demographic
2. **Page 1 (Executive Summary):** 4 KPI cards (total products, primary/secondary/tertiary counts), horizontal bar chart (Primary Category), donut chart (proportion), treemap (Secondary Category), bar chart (Product Type), 4 filter panels
3. **Page 2 (Drill-Down):** 3 stacked cascading slicers (Primary → Secondary → Tertiary), bar chart (Purchase Frequency), donut (Seasonal Relevance), treemap (Tertiary Category), detailed data table
4. **Design lessons:** Treemap > bar chart at ~15+ categories; separate cascaded slicers beat single dropdown for hierarchy; two pages reflect "orient me" vs "let me investigate" mental modes; KPI cards do ~30% of communication work; sketch questions before picking chart types
5. **Tools:** Power BI only; no DAX, no complex data model

## Limitations

- Beginner project — no DAX, no advanced data modeling
- No actual PBIX or dataset shared
- No semantic model design discussion
- No RLS, no performance considerations

## Value: Power BI KB

The Power BI contributions are the UX patterns: treemap threshold, cascading slicer layout, two-page overview-first structure, and KPI card first-impression value. These are actionable design heuristics, not just narrative.

## Extracted Notes

- [[Treemap-Beats-Bar-Chart-15-Plus-Categories]] — `atomic` — treemap outperforms bar chart when category count exceeds ~15; area comparison is more intuitive than bar-length at high counts
- [[Cascading-Slicers-Mirror-Hierarchical-Data]] — `pattern` — three stacked slicers (Primary → Secondary → Tertiary) make hierarchy navigation explicit; one dropdown cannot do this
- [[Two-Page-Dashboard-UX-Pattern]] — `pattern` — executive summary page + drill-down analysis page; "orient me" vs "let me investigate"; overview first, details second
- [[Source-Mitalimunot-Product-Hierarchy]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | Building a Product Hierarchy Analytics Dashboard in Power BI A Beginner's Journey.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~153 |
