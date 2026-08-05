---
created: 2026-08-05
updated: 2026-08-05
source: ALL and REMOVEFILTERS in Power BI (Boniface Muchendu)
source_url: https://databear.com/all-and-removefilters-in-power-bi/
note_type: source
tags: [dax, all, removefilters, calculate, filter-context, power-bi]
---

# ALL and REMOVEFILTERS in Power BI (Boniface Muchendu)

Explains ALL() and REMOVEFILTERS() DAX functions — their definitions, syntax, return values, and the critical difference: ALL removes filters AND returns a table/column for use in other functions; REMOVEFILTERS removes filters but returns nothing and cannot be used outside CALCULATE.

> **Type:** article
> **Author:** Boniface Muchendu (DataBear)
> **Published:** 2023-04-15
> **URL:** https://databear.com/all-and-removefilters-in-power-bi/
> **Routed to:** DAX Code

## Summary

Boniface Muchendu introduces ALL() and REMOVEFILTERS() as companion filter-removal functions. Both clear filter context from a table or column, but ALL is more versatile — it returns a table or column value that can be fed into SUMX, FILTER, or other DAX functions. REMOVEFILTERS was introduced in 2019 as a more readable shorthand for removing filters alone.

## Key Claims

- ALL() removes all filters from a table or column and returns the result as a table or column value
- REMOVEFILTERS() removes filters but returns nothing — it only modifies filter context inside CALCULATE
- ALL() can be used with SUMX (as a table expression) — REMOVEFILTERS cannot
- REMOVEFILTERS is purely syntactic sugar for the filter-removal use of ALL
- Syntax is identical: `ALL(TableName or ColumnName, …)` vs `REMOVEFILTERS(TableName or ColumnName, …)`

## Notable Details

- Both functions accept multiple table/column arguments
- ALL() on its own (no arguments) returns all rows of all tables — rarely used directly
- ALL() is more commonly used with CALCULATE to create measures like "Total Sales ignoring all slicers"
- REMOVEFILTERS is the preferred modern DAX idiom for readability when only filter removal is needed

## Extracted Notes

Links to notes derived from this source:

- [[ALL-Function-DAX]] — `function` — definition, syntax, parameters, return value (table/column)
- [[REMOVEFILTERS-Function-DAX]] — `function` — definition, syntax, no return value
- [[ALL-vs-REMOVEFILTERS]] — `comparison` — side-by-side: return value, SUMX compatibility, use cases
- [[Removing-Slicer-Filters-ALL]] — `pattern` — CALCULATE + ALL pattern, example with DimProduct and DimSalesTerritory
- [[Author-Boniface-Muchendu]] — `author` — Boniface Muchendu, DataBear (6 sources)

## Metadata

| Field | Value |
|-------|-------|
| Source file | ALL and REMOVEFILTERS in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-05 |
| Word count | ~450 |
