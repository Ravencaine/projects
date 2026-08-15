---
created: 2026-08-11
updated: 2026-08-11
source: "Handling Multiple Fact Tables in Power BI.md"
source_url: "https://databear.com/handling-multiple-fact-tables-power-bi/"
note_type: source
tags: [data-modeling, multi-fact, star-schema, power-bi]
---

# Handling Multiple Fact Tables in Power BI — Source

Article by Boniface Muchendu (DataBear) on managing multiple fact tables in Power BI using star schema and shared dimensions.

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2025-02-16
> **URL:** https://databear.com/handling-multiple-fact-tables-power-bi/
> **Routed to:** Data Modeling

## Summary

Power BI models with multiple fact tables at different granularities (e.g., Internet Sales and Reseller Sales) require shared, conformed dimensions — not duplicated dimensions per fact, and not consolidated fact tables. A clean star schema with one set of shared dimensions connected to each fact table enables accurate cross-fact reporting, faster refresh, and a smaller model.

## Key Claims

- Duplicating dimensions per fact table inflates model size and slows refresh
- Consolidating fact tables via append creates blank values from unmatched keys
- Shared dimensions enable seamless cross-fact aggregation
- Conformed dimensions enforce identical definitions across fact tables
- Table descriptions improve the report author experience in complex multi-fact models

## Notable Details

- Article uses Internet Sales vs Reseller Sales as the canonical multi-fact scenario
- All Power BI examples reference table-level descriptions as a UX tool for model clarity
- Author frames star schema as the solution to both pitfalls simultaneously

## Extracted Notes

Links to notes derived from this source:

- [[shared-dimensions-multi-fact]] — atomic — one set of dimensions shared across all fact tables
- [[conformed-dimensions]] — pattern — identical dimension definitions enabling cross-fact reporting
- [[pitfall-duplicating-dimensions]] — gotcha — model bloat and ambiguous filtering from duplicated dimensions
- [[pitfall-consolidated-fact-tables]] — gotcha — blank values from null keys when stacking facts
- [[implementing-star-schema-multi-fact]] — workflow — step-by-step build of a multi-fact star schema

## Metadata

| Field | Value |
|-------|-------|
| Source file | 99.System/InboxArchive/2026-08/Handling Multiple Fact Tables in Power BI.md |
| Ingestion date | 2026-08-11 |
| Word count | ~500 |
