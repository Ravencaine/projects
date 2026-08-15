---
created: 2026-08-08
updated: 2026-08-08
source: "Create calculation groups in Power BI"
source_url: https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups
note_type: source
tags: [power-bi, calculation-groups, dax, tabular, model-view, tmdl]
---

# Create Calculation Groups in Power BI (MS Learn)

> **Type:** documentation
> **Author:** Microsoft Learn (kgremban)
> **Published:** unknown
> **URL:** https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups
> **Routed to:** DAX Code

## Summary

Step-by-step Microsoft documentation for creating calculation groups in Power BI via Model View and TMDL view. Covers implicit vs explicit measures, `SELECTEDMEASURE()`, calculation item creation, time intelligence example, precedence, selection expressions, and two key gotchas: variant data types and non-numeric measure errors.

## Key Claims

1. **Calculation groups reduce redundant measures:** one CG replaces N separate time-intelligence measures by wrapping each with `SELECTEDMEASURE()`
2. **Discourage implicit measures is required:** CG requires this property because calculation items only apply to explicit (user-created) measures
3. **Two creation paths:** Model View (ribbon button) and TMDL view (direct script)
4. **TMDL syntax:** CG defined as `table > calculationGroup` with precedence, calculationItem, and column blocks
5. **Dynamic format strings:** calculation items can override measure formatting with a DAX format string expression
6. **Variant data type side effect:** adding a CG promotes all measures to variant type, breaking dynamic format string reuse
7. **ISNUMERIC guard:** CG expressions should check `ISNUMERIC(SELECTEDMEASURE())` before applying math to non-numeric measures

## Notable Details

- Screenshots referenced as `99.System/Attachments/Screenshot_*.png` — likely extracted from the article, not ingested as separate image notes
- Adventure Works DW 2020 PBIX sample model referenced — downloadable from MS Learn DAX sample model page
- The article cross-references `SELECTEDMEASURE()` DAX function docs, Analysis Services CG docs, and FORMAT function docs
- Selection expressions (multi/invalid/no-selection) are mentioned but not demonstrated — see the Analysis Services article

## Extracted Notes

Links to notes derived from this source:

- [[Source-Create-Calculation-Groups-Power-BI]] — this source note
- [[CG-Creation-Power-BI-Model-View]] — `workflow` — creating a CG via Power BI Model View ribbon
- [[CG-Dynamic-Format-String]] — `pattern` — dynamic format string on calculation items
- [[CG-Variant-Data-Type-Gotcha]] — `gotcha` — adding a CG promotes all measures to variant data type
- [[ISNUMERIC-Guard-Pattern-for-CG]] — `pattern` — ISNUMERIC check before applying math in CG expressions
- [[selectedmeasure]] — `function` — the DAX placeholder used inside every calculation item (merged with existing stub)
- [[Create-a-Calculation-Group]] — extended — added Power BI Desktop Model View as an alternative to Tabular Editor
- [[Calculation-Groups]] — extended — variant data type and ISNUMERIC guard added to key points
- [[TMDL-Syntax-Calculation-Group-Properties]] — extended — added full TMDL CG syntax from this source

## Metadata

| Field | Value |
|-------|-------|
| Source file | Create calculation groups in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-08 |
| Word count | ~2,500 |
