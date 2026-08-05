---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
source_url: https://medium.com/@simon.harrison_Select_Distinct/how-to-build-a-clean-p-l-in-power-bi-select-distinct-86c34d2197dd
note_type: source
tags: [power-bi, medium, pl, financial-reporting, xero, dax, matrix-visual, kpi]
---

# Clean P&L in Power BI

A step-by-step guide to building an executive-ready Profit & Loss statement in Power BI from raw Xero accounting data — covering Xero data extraction, Excel preparation, mapping table design, dynamic DAX measure, Matrix visual configuration, conditional formatting, and an executive KPI sidebar.

> **Type:** tutorial / end-to-end walkthrough
> **Author:** Simon Harrison (Analytics / Power BI / SQL)
> **Published:** 2026-07-30
> **URL:** https://medium.com/@simon.harrison_Select_Distinct/how-to-build-a-clean-p-l-in-power-bi-select-distinct-86c34d2197dd
> **Routed to:** Power BI

## Summary

The article walks through a complete P&L build: export Chart of Accounts and Account Transactions from Xero as .xlsx files → clean in Excel (delete metadata rows, filter to Revenue/Expense only, ensure Date is formatted) → load into Power BI → create two mapping tables (Section Mapping with Custom sort order, Structure mapping accounts to sections) → build 1-to-Many relationships → sort Section Mapping → write a Dynamic P&L measure → configure Matrix visual (Section + P&L Line on Rows, Year/Month on Columns, Dynamic P&L as Values) → style (horizontal gridlines on, vertical off, black borders) → apply conditional formatting (sage green for Gross Profit and Operating Profit) → add KPI cards and trend chart sidebar.

## Key Claims

- Xero exports must be saved as Excel Workbook (.xlsx), not CSV — preserves data types
- P&L structure is controlled by two manually created mapping tables, not by the raw data
- The Section Mapping table's Custom Sort Order column is what sequences the P&L correctly
- The Dynamic P&L measure handles both detail accounts and calculated subtotals in one formula
- Null Date values break relationship validation — filter them out in Power Query before loading
- Gross Profit and Operating Profit rows highlighted with sage green (#E3E8E1) via conditional formatting

## Notable Details

- 13 core columns selected when exporting Account Transactions from Xero
- Four tables total in the final model: Transactions, Chart of Accounts, Section Mapping, P&L Structure
- Matrix Date column must use Year or Month/Year hierarchy — day-level causes horizontal overflow
- "Show items with no data" enabled on Section row field to display subtotal rows
- YTD KPI measures use TOTALYTD time intelligence with a 6/30 fiscal year-end

## Extracted Notes

- [[xero-power-bi-pl-pipeline]] — `pattern` — Full Xero → Excel → Power BI pipeline
- [[pl-data-model-relationships]] — `pattern` — 4-table model + 1:Many relationships + sort-by
- [[pl-mapping-table-pattern]] — `pattern` — Section Mapping + Structure table design
- [[pl-dynamic-matrix-visual]] — `pattern` — Matrix config: rows (Section + Line), columns (Date hierarchy), values (Dynamic P&L)
- [[pl-styling]] — `pattern` — Gridlines, borders, title, hierarchy cleanup
- [[pl-conditional-formatting]] — `pattern` — Sage green (#E3E8E1) on Gross Profit and Operating Profit rows
- [[pl-executive-sidebar]] — `pattern` — KPI cards + monthly trend chart
- [[executive-pl-statement-structure]] — `atomic` — Standard P&L hierarchy: Revenue → Gross Profit → Operating Profit → Net Profit
- [[pl-null-date-break-relationships]] — `gotcha` — Null Date values prevent relationship validation; filter out in Power Query
- [[dynamic-pl-measure]] — `function` — Single measure handling detail rows and calculated subtotals in Matrix
- [[ytd-kpi-measures-pl]] — `function` — TOTALYTD measures for Revenue, Gross Profit, Operating Profit, Net Profit
- [[pl-line-structure-reference]] — `reference` — Standard account code ranges and P&L section structure

## Metadata

| Field | Value |
|-------|-------|
| Source file | `How to Build a Clean P&L in Power BI — Select Distinct.md` |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-02 |
| Word count | ~1,100 |
| Language | English |
