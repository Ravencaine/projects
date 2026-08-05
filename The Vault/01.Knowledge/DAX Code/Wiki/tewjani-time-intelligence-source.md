---
created: 2026-08-01
updated: 2026-08-02
source: "Time Intelligence in DAX The Secret Behind YTD, QTD, and SamePeriodLastYear.md"
source_url: "https://medium.com/write-your-world/time-intelligence-in-dax-the-secret-behind-ytd-qtd-and-sameperiodlastyear-5a5e05c4311d"
note_type: source
tags: [dax, time-intelligence, ytd, qtd, mtd, sameperiodlastyear, date-table, beginner]
---

# Time Intelligence in DAX — Tejwani

> **Type:** time intelligence guide / beginner
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-10-30
> **Routed to:** DAX Code
> **KB:** DAX Code

## Summary

Time intelligence requires a marked Date table and CALCULATE. Covers: Date table requirements, YTD/QTD/MTD via DATESYTD/DATESQTD/DATESMTD, SAMEPERIODLASTYEAR for YoY comparisons, the single Date table gotcha, and fiscal year customization with DATESYTD end-date parameter.

## Extracted Notes

- [[time-intelligence-date-table-requirements]] — `atomic` — continuous date range, Year/Month/Quarter/Week columns, DateKey; mark as Date Table in Power BI
- [[ytd-qtd-mtd-functions]] — `atomic` — DATESYTD/DATESQTD/DATESMTD inside CALCULATE; expands date range dynamically; custom fiscal year end via second parameter
- [[sameperiodlastyear-yoY]] — `atomic` — SAMEPERIODLASTYEAR: shifts current date range back 1 year; needs continuous date column; YoY = DIVIDE(Current - LY, LY)
- [[time-intelligence-star-schema]] — `atomic` — one central Date table; relate all fact tables to it; single Date dimension; intern gotcha: wrong date table breaks all time measures

## Metadata

| Field | Value |
|-------|-------|
| Source file | Time Intelligence in DAX The Secret Behind YTD, QTD, and SamePeriodLastYear.md |
| Ingestion date | 2026-08-01 |
| Word count | ~1,500 |
| Level | Beginner |
| Category | Time Intelligence |
