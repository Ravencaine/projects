---
created: 2026-08-02
updated: 2026-08-02
source: Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included).md
source_url: https://medium.com/microsoft-power-bi/easily-create-multiple-calculations-using-a-single-formula-in-power-query-pbix-included-e4c71b1e6835
note_type: source
tags: [power-query, medium, power-bi, custom-column, record-syntax]
---

# Multiple Calculations Using a Single Formula in Power Query

A beginner-level tutorial demonstrating how to use Power Query's record literal syntax in a Custom Column to define multiple derived columns from a single formula, then expand the record into separate columns and load them as an Invoked Function table in the Power BI data model.

> **Type:** tutorial
> **Author:** Shashanka Shekhar
> **Published:** 2026-07-30
> **URL:** https://medium.com/microsoft-power-bi/easily-create-multiple-calculations-using-a-single-formula-in-power-query-pbix-included-e4c71b1e6835
> **Routed to:** Power Query

## Summary

The article demonstrates a Power Query technique for generating multiple calculated columns from a single Custom Column formula. By returning a record literal, one formula step produces Cost, ProfitPct, and Commission sub-columns. After expansion, Power BI creates an Invoked Function table in the model. The approach is presented as an efficiency and consistency pattern for data transformation workflows.

## Key Claims

- A single record literal formula replaces multiple separate Custom Column steps
- The five benefits of this approach are: efficiency, consistency, scalability, flexibility, and optimization
- The formula `[\n    Cost = [Sales] - [Profit],\n    ProfitPct = [Profit] / [Sales],\n    Comm = 0.1 * [Profit]\n]` generates three output columns
- After expansion, the columns appear in a separate Invoked Function table in the Power BI model
- The PBIX file and sample data are available for download via Google Drive links

## Notable Details

- Source table: `Multiple_Columns` with columns Sales Rep, Sales (10,400–14,200), Profit (3,040–5,720)
- Three derived columns created: Cost (Sales − Profit), ProfitPct (Profit/Sales), Comm (10% of Profit)
- The record column is expanded via the expand icon in the column header
- The resulting Invoked Function table is visible in the Data pane and can be used in visuals
- Article is classified as Beginner level, DAX category, tagged Tutorial

## Extracted Notes

- [[single-formula-multiple-columns-power-query]] — `pattern` — Record literal syntax for multi-column output in one step
- [[power-query-custom-column-workflow]] — `pattern` — Step-by-step Custom Column workflow
- [[five-benefits-single-formula-design]] — `atomic` — Five compounding benefits of single-formula design
- [[invoked-function-table-power-bi]] — `pattern` — Invoked Function table created after record expansion
- [[power-query-pbix-demo-download]] — `reference` — PBIX and sample data download links

## Metadata

| Field | Value |
|-------|-------|
| Source file | `Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included).md` |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-02 |
| Word count | ~550 |
| Language | English |
