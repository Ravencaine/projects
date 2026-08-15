---
created: 2026-08-10
updated: 2026-08-10
source: BI Case Study: Automating Quarterly Financial Reporting for Contoso Ltd using Power BI and Power Automate
source_url: https://medium.com/@benjohnokezie/automating-quarterly-financial-reporting-for-using-power-bi-and-power-automate-22b07300a706
note_type: source
tags: [power-bi, power-automate, financial-reporting, case-study, automation, documentation]
---

# Source: Okezie — Quarterly Financial Reporting Case Study

> **Type:** case study (simulated)
> **Author:** Ben-John Okezie
> **Published:** 2025-08-07
> **URL:** https://medium.com/@benjohnokezie/automating-quarterly-financial-reporting-for-using-power-bi-and-power-automate-22b07300a706
> **Routed to:** Power BI
> **Category:** Power BI, Power Automate, Financial Reporting, Automation, Case Study

## Summary

Simulated BI case study for Contoso Ltd (outdoor equipment manufacturer). Power BI replaces manual Excel P&L and balance sheet preparation. Power Automate exports reports as PDFs on a quarterly schedule and emails them to executives. Key results: 7-day → 2-day turnaround; Excel formula errors eliminated via DAX; consistent logic across 4 business units through shared semantic model. Also covers neutral/low-saturation color design principles and a 3-part documentation structure (Data Source + Metadata, Business Logic/Calculations, Report Pages + KPIs).

## Key Claims

1. **Problem:** Finance analysts manually build quarterly Excel reports; formula errors, conflicting numbers, 7-day turnaround
2. **Solution:** Power BI semantic model (Azure SQL + Dynamics 365) + Power Automate PDF export
3. **Data sources:** Azure SQL Database (`contoso-sql.database.windows.net`, `FinancialDB`, `dbo.FactFinancials`); Dynamics 365 via built-in connector
4. **Power Automate flow:** Scheduled cloud flow → export Power BI report as PDF → send email with attachment + plain-text template
5. **Email template:** `Hello,\n\nPlease find attached the quarterly Power BI report.\n\nRegards,\nPower BI Automation System`
6. **Other outputs:** SharePoint, OneDrive, Excel template population
7. **Design principle:** Neutral tones, low saturation; chart colors must stand out from nav bar and background
8. **Documentation:** 3-part Excel doc — Data Source/Metadata, Business Logic/Calculations, Report Pages/KPIs
9. **Results:** 7 days → 2 days; formula errors eliminated; business unit logic standardised
10. **Premium note:** PDF export and some Power Automate features require Pro or Premium license

## Limitations

- Simulated (no live Azure SQL or Dynamics 365)
- No actual DAX formulas shown — references "consistent DAX formulas" but doesn't show them
- Power Automate flow is thin: 3 steps, no error handling, no conditional routing
- No security model documented (RLS, workspace roles)

## Value: Power BI KB

The Power BI contributions are the neutral-tones/low-saturation design principle and the case study structure (objectives → data source → report design → refresh → automation → documentation → results). Most Power Automate content is already covered by Gunarathinam's DAX query validation flow.

## Extracted Notes

- [[Dashboard-Design-Neutral-Tones-Low-Saturation]] — `atomic` — low saturation colors reduce cognitive load; chart colors must stand out from chrome
- [[Source-Okezie-Quarterly-Financial-Case-Study]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | BI Case Study Automating Quarterly Financial Reporting for Contoso Ltd using Power BI and Power Automate.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~163 |
