---
created: 2026-08-05
updated: 2026-08-05
source: 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)
source_url: https://medium.com/@digitalbykewat/5-data-cleaning-mistakes-that-ruin-your-dashboard-and-how-to-avoid-them-4aa7373d9e62
note_type: source
tags: [data-cleaning, data-quality, duplicate, date-format, missing-values, outlier, power-query]
---

# 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)

Five common data cleaning mistakes that silently break dashboards: duplicate records, inconsistent date formats, missing values, inconsistent categories, and ignoring outliers — plus a pre-publish health checklist and data cleaning pipeline flow.

> **Type:** article
> **Author:** DigitalBYKewat (@digitalbykewat on Medium)
> **Published:** 2026-07-15
> **URL:** https://medium.com/@digitalbykewat/5-data-cleaning-mistakes-that-ruin-your-dashboard-and-how-to-avoid-them-4aa7373d9e62
> **Routed to:** Data Modeling

## Summary

DigitalBYKewat makes the case that dashboards fail not because of poor visualisation but because of dirty data. Five specific mistakes are covered with real-world examples, SQL/Power Query fixes, and a five-point pre-publish health checklist. A recommended data cleaning pipeline is also provided.

## Key Claims

- Duplicate records distort Revenue, Profit, Customer Count, and Inventory metrics
- Inconsistent date formats cause wrong month and year grouping — one retailer had April transactions interpreted as January
- Blank cells silently break average calculations, slicers, and forecasting models
- Inconsistent text categories (Mumbai/MUMBAI/Bombay) split bar charts into many small bars instead of one large one
- Outliers (e.g., ₹20,00,000 for a keychain) warp averages and trend lines

## Notable Details

- Remove Duplicates early in the Power Query pipeline — not after aggregations
- ISO format `YYYY-MM-DD` is the safest universal date standard
- `Text.Trim` and `Text.Clean` in Power Query remove ghost/invisible characters
- COUNT vs DISTINCTCOUNT QA check: if they differ significantly, duplicates likely exist
- Dimension/lookup tables map legacy names (Bombay → Mumbai) for canonical categories
- Outlier investigation: check min/max before publishing — if it looks like a phone number, investigate

## Data Cleaning Pipeline

```
Raw Data → Duplicate Check → Missing Value Check → Standardize Formats → Validate Categories → Review Outliers → Clean Dataset → Power BI Dashboard → Reliable Business Decisions
```

## Extracted Notes

Links to notes derived from this source:

- [[Duplicate-Records-Detection-Removal]] — `atomic` — Remove Duplicates, primary keys, COUNT vs DISTINCTCOUNT QA
- [[Inconsistent-Date-Formats-ISO]] — `atomic` — ISO YYYY-MM-DD standard, locale settings in Power Query
- [[Missing-Values-Handling-Strategy]] — `atomic` — why blanks break averages/slicers/models, default vs drop strategy
- [[Inconsistent-Categories-Normalisation]] — `atomic` — Text.Trim/Clean, casing normalisation, dimension lookup tables
- [[Ignoring-Outliers-Detection-Action]] — `atomic` — min/max QA, investigation before publishing
- [[Dashboard-Health-Checklist]] — `workflow` — 5-point pre-publish checklist
- [[Data-Cleaning-Pipeline-Flow]] — `workflow` — 8-step data cleaning pipeline
- [[Author-DigitalBYKewat]] — `author` — DigitalBYKewat

## Metadata

| Field | Value |
|-------|-------|
| Source file | 5 Data Cleaning Mistakes That Ruin Your Dashboard (And How to Avoid Them).md |
| Archived at | — |
| Ingestion date | 2026-08-05 |
| Word count | ~1,100 |
