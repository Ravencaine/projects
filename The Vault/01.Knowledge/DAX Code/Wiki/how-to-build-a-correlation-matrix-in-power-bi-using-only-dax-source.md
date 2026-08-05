---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
source_url: https://medium.com/microsoft-power-bi/how-to-build-a-correlation-matrix-in-power-bi-using-only-dax-ab611a19a194
note_type: source
tags: [dax, power-bi, correlation, matrix, visualization, statistics]
---

# How to Build a Correlation Matrix in Power BI Using Only DAX

Build a fully dynamic, interactive correlation matrix in Power BI using only DAX — no Python, no external tools. Uses a Matrix visual, disconnected selector tables, Pearson correlation measures, DAX-driven conditional formatting, and an interactive scatter chart tooltip.

> **Type:** article
> **Author:** Isabelle Bittar (KI Data Science)
> **Published:** 2025-08-24
> **URL:** https://medium.com/microsoft-power-bi/how-to-build-a-correlation-matrix-in-power-bi-using-only-dax-ab611a19a194
> **Routed to:** DAX Code, Power BI

## Summary

This article walks through building an interactive correlation matrix visual in Power BI entirely with DAX. A pair of disconnected `DATATABLE` tables (`VariablesX`, `VariablesY`) drive the Matrix visual's rows and columns; a single `Correlation` measure computes Pearson r using `SUMMARIZE`, `ADDCOLUMNS`, and `SUMX`. A second measure hides the upper triangle and diagonal. DAX color-bucket measures replace the built-in gradient for consistent conditional formatting across filter contexts. A tooltip page with a scatter chart provides drill-through on hover, with an HTML subtitle that labels the correlation strength and explains it in plain language.

## Key Claims

- DAX alone is sufficient to compute and display a pairwise correlation matrix in Power BI
- Using DAX measures for conditional formatting (rather than the built-in gradient) keeps colors meaningful across filter contexts
- An interactive tooltip with a scatter chart adds context without requiring additional infrastructure
- The approach is fully dynamic: any report filter or slicer re-computes all correlations in real time
- Use case demonstrated on HR data: Overtime Hours negatively correlated with Engagement in IT (-0.62)

## Notable Details

- The `Correlation` measure uses a `VAR Base` shadowing risk — DAX has a `BASE()` function that this variable name would overwrite if referenced later
- The HTML subtitle uses nested `SUBSTITUTE()` calls to bold both "increases" and "decreases" simultaneously before conditionally swapping direction based on the sign of r
- The color palette uses teal (`#008080`, `#00BFB2`) for positive correlations and coral (`#E76F51`, `#F4A896`) for negative — distinct from the typical green/red to avoid colour-blind accessibility issues
- PBIX available for download (Google Drive link in article)
- The scatter chart tooltip page must be set as Page type: Tooltip and assigned in the Matrix visual's General → Tooltip property

## Extracted Notes

Links to notes derived from this source:

- [[correlation-matrix-in-power-bi-dax-only]] — `pattern` — end-to-end correlation matrix pattern
- [[pearson-correlation-coefficient-in-dax]] — `pattern` — Pearson formula walkthrough
- [[correlation-core-pearson-measure]] — `function` — the Correlation measure
- [[variablesx-variablesy-disconnected-selector-tables]] — `function` — selector tables
- [[correlation-lower-triangle-no-diagonal]] — `function` — display modifier
- [[dax-color-bucket-conditional-formatting-matrix]] — `pattern` — color bucket system
- [[color-palette-measures-static-hex-strings]] — `function` — color palette measures
- [[correlation-color-buckets]] — `function` — background color per bucket
- [[correlation-font-color]] — `function` — font color per bucket
- [[interactive-tooltip-scatter-chart-on-matrix]] — `pattern` — tooltip scatter chart
- [[selected-x-name-selected-y-name]] — `function` — variable name capture
- [[x-value-y-value-dynamic-variable-mapping]] — `function` — dynamic numeric mapping
- [[scatter-title]] — `function` — dynamic chart title
- [[scatter-subtitle-html-dynamic-label-badge]] — `function` — HTML subtitle measure
- [[pearson-correlation-coefficient]] — `atomic` — statistical concept
- [[Author-Isabelle-Bittar]] — `author` — author note

## Metadata

| Field | Value |
|-------|-------|
| Source file | How to Build a Correlation Matrix in Power BI Using Only DAX.md |
| Archived at | pending — source remains in Inbox |
| Ingestion date | 2026-08-02 |
| Word count | ~2,100 |
