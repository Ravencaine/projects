---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
source_url: https://www.sqlbi.com/articles/find-the-products-in-the-top-10-every-year-with-dax/
note_type: source
tags: [source, dax, sqlbi, marco-russo, alberto-ferrari, top-n, evergreen, udf, query-measure-function]
---

# Find the products in the top 10 every year with DAX (Russo & Ferrari / SQLBI)

A worked walkthrough of finding "evergreen" products — items that consistently appear in the top 10 by year — via a three-stage authoring protocol (query → measure → function).

> **Type:** article
> **Author:** Marco Russo & Alberto Ferrari
> **Published:** 2025-11-03
> **URL:** https://www.sqlbi.com/articles/find-the-products-in-the-top-10-every-year-with-dax/
> **Routed to:** DAX Code

## Summary

The article frames a specific business question — given top-N rankings by year, which products appear in the top N *most* years? — and walks through the full authoring process for the answer. The algorithm uses `GENERATE(Years, TOPN(...))` to build a `(Year, ProductKey)` table, `GROUPBY` + `SUMX(CURRENTGROUP(), 1)` to count appearances, and a `Coverage` threshold to filter to "evergreen" products. The article is as much about *process* as content: it demonstrates the SQLBI-preferred workflow of prototyping in a DAX query, porting to a measure (fixing filter-context issues with `CALCULATETABLE(... ALLSELECTED())` and `KEEPFILTERS`), then extracting to a `Local.*` UDF when the logic is reused across measures.

## Key Claims

- Evergreen products — items consistently in the top N across years — can be found by combining `GENERATE` + `TOPN` (top N per period) with `GROUPBY` + `SUMX(CURRENTGROUP(), 1)` (frequency count per product), filtered by a coverage threshold (`>= 80% of periods`).
- `CALCULATETABLE(... ALLSELECTED())` is essential for the top-N computation to see the user's slicer selection, not the matrix cell's deeply-filtered context.
- `KEEPFILTERS(BestProds)` is essential when applying the resulting product list via `CALCULATE` — without it, the measure's product filter overrides any matrix column on the same column.
- `COUNTROWS` cannot be used as a `GROUPBY` aggregation — must use `SUMX(CURRENTGROUP(), 1)` (or other iterators from the supported set) to count rows per group.
- When the same logic is reused across multiple measures (e.g., `Num Best Prods` and `Sales Best Prods`), extract to a `Local.*` UDF with `EXPR`-typed parameters; wrap UDF arguments inside `TOPN` with `CALCULATE(sortExpr)` to ensure correct evaluation regardless of argument form.

## Notable Details

- The article explicitly references two prior SQLBI articles on top-N filtering (alongside "other products", "Top 3 per category") as context for this variation — evergreen is framed as the third natural extension.
- The final design is a measure whose result is *dynamic*: it responds to slicer selections on year range (via `ALLSELECTED`) and product category (via `KEEPFILTERS` preserving the matrix row filter).
- The article concludes with the explicit authoring philosophy: "writing non-trivial DAX code requires an approach that minimizes the possible problems" — start as a query (no filter context), promote to a measure (fix context), promote to a UDF (share logic).
- The `Coverage` variable is parameterised (default `0.8`); the article frames this as more robust than a fixed integer threshold because it scales with the number of periods in the data.
- The UDF parameter `sortExpr` is wrapped in `CALCULATE(sortExpr)` inside `TOPN` — this is the EXPR-parameter evaluation idiom that ensures the sort criterion evaluates correctly when called with a measure, a column, or a complex expression.

## Extracted Notes

- [[evergreen-top-n-products-pattern]] — `pattern` — top-N-by-group + frequency threshold + coverage filter
- [[query-measure-function-workflow]] — `workflow` — SQLBI three-stage authoring protocol
- [[topn-filter-context-leak-matrix-gotcha]] — `gotcha` — TOPN/CALCULATE returning 1 in every matrix cell
- [[generate-inside-calculatetable-allselected-atomic]] — `atomic` — decouple GENERATE+TOPN from matrix filter context
- [[groupby-sumx-currentgroup-constant-count-pattern]] — `pattern` — counting rows per group over a VAR table
- [[topn]] — `function` (extended) — added GENERATE+TOPN-per-group idiom
- [[generate]] — `function` (extended) — added CALCULATETABLE+ALLSELECTED wrapping idiom
- [[currentgroup]] — `function` (extended) — added SUMX(CURRENTGROUP(), 1) count-via-constant
- [[Author-Marco-Russo-Alberto-Ferrari]] — `author` (extended) — added 5th source

## Metadata

| Field | Value |
|-------|-------|
| Source file | Find the products in the top 10 every year with DAX.md |
| Archived at | (in Inbox; archive pending) |
| Ingestion date | 2026-08-09 |
| Word count | ~1,600 |