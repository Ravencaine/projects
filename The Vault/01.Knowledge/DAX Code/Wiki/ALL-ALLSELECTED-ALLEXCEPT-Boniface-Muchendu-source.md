---
created: 2026-08-05
updated: 2026-08-05
source: ALL, ALLSELECTED and ALLEXCEPT DAX Filter Function (Boniface Muchendu)
source_url: https://databear.com/all-allselected-and-allexcept-dax-filter-function/
note_type: source
tags: [dax, all, allselected, allexcept, filter-context, calculate, power-bi]
---

# ALL, ALLSELECTED and ALLEXCEPT DAX Filter Function (Boniface Muchendu)

Extends the ALL() function with ALLSELECTED() and ALLEXCEPT() — covering definitions, syntax, and the three filter-removal strategies: ALL (remove all), ALLSELECTED (remove query-level, keep external), ALLEXCEPT (remove all except specified columns).

> **Type:** article
> **Author:** Boniface Muchendu (DataBear)
> **Published:** 2022-11-19
> **URL:** https://databear.com/all-allselected-and-allexcept-dax-filter-function/
> **Routed to:** DAX Code

## Summary

Boniface Muchendu builds on the ALL() function by introducing ALLSELECTED() and ALLEXCEPT(). Each removes filter context in a different way: ALL removes all filters; ALLSELECTED removes only the filters within the current query while preserving external slicer selections; ALLEXCEPT removes all filters except those on specified columns.

## Key Claims

- ALL() on a column removes filters only on that column — other columns' filters remain active
- ALL() on a table removes filters on every column in that table
- ALLSELECTED() removes query-level (internal) filters but keeps filters from outside the query — useful for "% of page total" calculations
- ALLEXCEPT(table, col) removes all filters on the table except filters on the specified column(s)
- ALLSELECTED and ALL return the same value when no internal query filters exist (i.e., "select all" is active)

## The Three Functions

| Function | Removes | Keeps |
|---------|---------|-------|
| ALL | All filters on the table/column | Nothing |
| ALLSELECTED | Filters inside the query | Filters outside the query (external slicers) |
| ALLEXCEPT | All filters except on specified columns | Filters on specified columns only |

## Notable Details

- ALLSELECTED respects external slicer selections but ignores internal visual-level filters
- ALLEXCEPT is useful for "all dimensions except one" scenarios — e.g., calculate across all regions but respect the category slicer
- ALLSELECTED syntax is identical to ALL: `ALLSELECTED(table or column, ...)`
- ALLEXCEPT syntax differs: `ALLEXCEPT(table, column[, column...])` — table first, then columns to keep

## Extracted Notes

Links to notes derived from this source:

- [[ALLSELECTED-Function-DAX]] — `function` — definition, syntax, query-level vs external filters
- [[ALLEXCEPT-Function-DAX]] — `function` — definition, syntax, table-first parameter order
- [[ALL-ALLSELECTED-ALLEXCEPT-Comparison]] — `comparison` — side-by-side: what each removes/keeps, use cases
- [[ALL-Function-DAX]] — `function` — pre-existing ALL() note (from ALL/REMOVEFILTERS source)
- [[Author-Boniface-Muchendu]] — `author` — Boniface Muchendu, DataBear (7 sources)

## Metadata

| Field | Value |
|-------|-------|
| Source file | ALL, ALLSELECTED and ALLEXCEPT DAX Filter Function.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-05 |
| Word count | ~550 |
