---
created: 2026-08-13
source: How to Build a Clean P&L in Power BI
source_url: https://www.selectdistinct.co.uk/2026/07/30/clean-pl-formatting-power-bi/
note_type: source
tags: [power-bi, financial-reporting, p&l, xero, matrix-visual, executive-report]
---

# Source: How to Build a Clean P&L in Power BI

> **Type:** tutorial
> **Author:** Elle Harrison
> **Published:** 2026-07-30
> **URL:** https://www.selectdistinct.co.uk/2026/07/30/clean-pl-formatting-power-bi/
> **Routed to:** Power BI

## Summary

Step-by-step tutorial for building an executive-grade Profit & Loss dashboard in Power BI. Three-stage pipeline: export raw data from Xero → clean/prepare in Excel → model and visualise in Power BI. Covers mapping tables, dynamic DAX, matrix formatting, conditional formatting, and KPI sidebar.

## Key Claims

1. P&L data should flow Xero → Excel (clean) → Power BI, not directly into Power BI from raw exports
2. Chart of Accounts + Transaction Data are the two core data extracts from Xero
3. Mapping tables with custom sort order control P&L section sequence in the matrix
4. A single SWITCH-based Dynamic P&L measure handles both account-level detail and subtotals
5. Sage green conditional formatting on Gross Profit and Operating Profit rows adds executive polish

## Notable Details

- Source: selectdistinct.co.uk (Elle Harrison — new author for this vault)
- Article includes embedded YouTube video (watched, no extraction needed)
- Multiple embedded images showing Xero screenshots, Excel steps, and Power BI UI — no text alternative
- DAX formula shown as screenshot image (not extractable) — formula reconstructed from prose description
- Step-by-step detail is high enough to create a genuine reusable workflow pattern
- Related to: [[matrix-cash-flow-pl-report-workflow]] (similar matrix-for-financial-reporting concept, different source)

## Extracted Notes

- [[Power-BI-PL-Dashboard-Xero-to-Power-BI]] — pattern — full Xero → Excel → Power BI pipeline with data extraction steps, mapping tables, and relationship model
- [[Power-BI-PL-Matrix-Formatting]] — pattern — P&L matrix formatting: section mapping, spacing, conditional formatting, KPI sidebar

## Metadata

| Field | Value |
|-------|-------|
| Source file | How to Build a Clean P&L in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-13 |
| Word count | ~1,200 |
