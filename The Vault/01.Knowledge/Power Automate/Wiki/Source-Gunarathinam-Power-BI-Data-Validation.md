---
created: 2026-08-10
updated: 2026-08-10
source: Automate Data Validation in Power BI Reports using Power Automate
source_url: https://medium.com/@guna24x7/automate-data-validation-in-power-bi-reports-using-power-automate-6deea7b04dbb
note_type: source
tags: [power-automate, power-bi, data-quality, validation, dax-query, automation]
---

# Source: Gunarathinam — Power BI Data Validation via Power Automate

> **Type:** article
> **Author:** Gunarathinam M
> **Published:** 2024-09-18
> **URL:** https://medium.com/@guna24x7/automate-data-validation-in-power-bi-reports-using-power-automate-6deea7b04dbb
> **Routed to:** Power Automate
> **Category:** Power Automate, Power BI, Data Quality, Automation

## Summary

Captures DAX queries from Power BI report visuals via Performance Analyzer, then runs them on a schedule in Power Automate using the "Run a Query against Dataset" action. Compose actions define validation rules against the tabular output; conditions route outcomes; email/Teams alerts fire on validation failure. Also covers DAX Query View for testing captured queries before deployment. Mentions Microsoft Fabric + Semantic Link + Great Expectations as a deeper alternative.

## Key Claims

1. **Problem:** Bad data in reports erodes trust and causes poor decisions
2. **Solution:** Scheduled Power Automate flow runs the visual's DAX query before business hours and validates output
3. **Query capture:** Performance Analyzer → Refresh Visuals → Copy query — gives the exact DAX EVALUATE query
4. **Flow steps:** Recurrence → Run a Query against Dataset → Compose (validation rules) → Condition → Email/Teams notification
5. **Parameterization:** Queries can include dynamic parameters for reuse across different filter contexts
6. **DAX Query View:** The captured query can be tested in DAX Query View to confirm expected output before automating
7. **Advanced alternative:** Microsoft Fabric + Semantic Link + Great Expectations for code-rich, deeper data validation (future article)

## Limitations Noted

- Validates report-level data, not raw source data
- Manual process to capture queries from Performance Analyzer
- No automated discovery of which visuals to validate

## Code Patterns Extracted

| Pattern | Description |
|---------|-------------|
| DAX EVALUATE query | Captured from Performance Analyzer; DEFINE + SUMMARIZECOLUMNS + TREATAS |
| Flow condition | Compose outputs → Condition → alert on failure |
| Parameterized DAX | `@{variables('FilterValue')}` injected into TREATAS |

## External Resources

- Performance Analyzer docs: learn.microsoft.com/power-bi/create-reports/desktop-performance-analyzer
- DAX Query View: learn.microsoft.com/power-bi/transform-model/dax-query-view
- Power BI connector for Power Automate: learn.microsoft.com/connectors/powerbi/

## Extracted Notes

- [[Power-BI-DAX-Query-Data-Validation-Flow]] — `workflow` — scheduled flow: Recurrence → Run query → Compose rules → Condition → alert
- [[Performance-Analyzer-Visual-Query-Capture]] — `reference` — Performance Analyzer copy query → DAX Query View test → Power Automate

## Metadata

| Field | Value |
|-------|-------|
| Source file | Automate Data Validation in Power BI Reports using Power Automate.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~132 |
