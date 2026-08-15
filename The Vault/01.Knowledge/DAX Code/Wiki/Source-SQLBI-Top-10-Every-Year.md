---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
source_url: "https://www.sqlbi.com/articles/find-the-products-in-the-top-10-every-year-with-dax/"
note_type: source
tags: [dax, sqlbi, top-n, evergreen, measure, udf, pattern]
---

# SQLBI — Find the Products in the Top 10 Every Year with DAX

> **Type:** article
> **Author:** Marco Russo & Alberto Ferrari (SQLBI)
> **Published:** 2025-11-03
> **URL:** https://www.sqlbi.com/articles/find-the-products-in-the-top-10-every-year-with-dax/
> **Routed to:** DAX Code

## Summary

Identifies products that appear in the top-N list across the majority of years (evergreen products) using GENERATE + TOPN to enumerate top-N per year, GROUPBY to count appearances, then a coverage-threshold filter. Demonstrates the full SQLBI authoring protocol: query-first (no filter context), promote to measure (fix ALLSELECTED + KEEPFILTERS), then extract to a UDF.

## Key Claims

- `GENERATE` + `TOPN` produces a year-by-top-N table for further aggregation
- `GROUPBY` is required when aggregating over a variable table (not a model table)
- `ALLSELECTED()` must wrap both the year list and the TOPN step to ignore matrix filters during enumeration
- `KEEPFILTERS(BestProds)` is required to avoid the BestProds filter overwriting the outer filter context's `Product[ProductKey]` filter
- Coverage threshold (e.g. 80%) filters for products that are evergreen rather than flash-in-the-pan
- UDF extraction (`Local.ComputeForBestProds`) enables reuse across `COUNTROWS` and `SUMX` measures

## Notable Details

- The `sortExpr` argument passed to TOPN is wrapped in `CALCULATE()` to ensure correct evaluation regardless of context
- The final measure returns correct counts only when `KEEPFILTERS` is present — without it, the count is wrong by a factor
- `SUMX(CURRENTGROUP(), 1)` replaces `COUNTROWS(CURRENTGROUP())` inside GROUPBY

## Extracted Notes

Links to notes derived from this source:

- [[Evergreen-Top-N-Products]] — `atomic` — evergreen products: top-N appearing in ≥coverage% of years
- [[TopN-ProductKey-Override-Gotcha]] — `gotcha` — BestProds filter overrides outer ProductKey filter without KEEPFILTERS
- [[Local.ComputeForBestProds]] — `function` — UDF that computes any expression only for evergreen top-N products
- [[Source-SQLBI-Top-10-Every-Year]] — `source` — this source note
- [[query-measure-function-workflow]] — `workflow` — extended with coverage-threshold variation
- [[Evergreen-Top-N-Products]] — `atomic` — evergreen products: top-N appearing in ≥coverage% of years
- [[TopN-ProductKey-Override-Gotcha]] — `gotcha` — BestProds filter overrides outer ProductKey filter without KEEPFILTERS
- [[Local.ComputeForBestProds]] — `function` — UDF that computes any expression only for evergreen top-N products
- [[generate]] — GENERATE function used to crossjoin years with their top-N products
- [[topn]] — TOPN function used to rank products per year
- [[groupby]] — GROUPBY used with SUMX(CURRENTGROUP(),1) to count appearances
- [[allselected]] — ALLSELECTED wraps year enumeration and TOPN to decouple from matrix filter context
- [[keepfilters]] — KEEPFILTERS intersects BestProds with outer filter context instead of replacing it
- [[calculate]] — CALCULATE applies the BestProds filter to any downstream expression

## Metadata

| Field | Value |
|-------|-------|
| Source file | Find the products in the top 10 every year with DAX.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~800 |
