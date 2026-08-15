---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Power BI Reports Using Parameters in Power BI.md"
source_url: https://databear.com/master-dynamic-reporting-in-power-bi/
note_type: source
tags: [power-bi, parameters, power-query, stored-procedure, excel, gateway, dynamic-report, databear, boniface-muchendu]
---

# Dynamic Power BI Reports Using Parameters (Data Bear)

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2025-02-16
> **URL:** https://databear.com/master-dynamic-reporting-in-power-bi/
> **Routed to:** Power BI

## Summary

Power Query parameters drive dynamic filtering from external Excel workbooks. Pattern: SQL stored procedure → Power Query with parameter → convert to function → invoke with Excel column values → refresh in Power BI Service (via gateway). End users update Excel, refresh report, data auto-filters.

## Key Claims

### Parameter Setup
- Create parameter: Manage Parameters → New Parameter → name + type + sample value
- Integrate into query: Advanced Editor → replace hardcoded value with parameter name
- Stored procedure execution: Get Data → SQL Server → paste EXEC statement in query editor

### Multi-Value Pattern (Excel-Driven)
1. Create single-column Excel table of filter values (e.g., Student IDs)
2. Import into Power Query
3. On the main query: Create Function (right-click) — wraps SP call with parameter input
4. Invoke Custom Function on the Excel table → returns one row per value
5. Refreshing pulls new values from Excel automatically

### Gateway for Power BI Service
- Personal or enterprise gateway on the machine
- Configure in Manage Gateways: Excel workbook data source + SQL Server data source
- After gateway setup: Power BI Service refresh picks up Excel changes

### Use Case
- End users manage filter values in Excel (no Power BI access needed)
- Report refresh pulls latest values automatically
- Eliminates need to edit Power BI file for filter changes

## Metadata

| Field | Value |
|-------|-------|
| Source file | Dynamic Power BI Reports Using Parameters in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
