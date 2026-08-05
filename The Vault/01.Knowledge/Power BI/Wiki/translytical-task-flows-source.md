---
created: 2026-07-27
updated: 2026-08-02
source: "Translytical Task Flows Just Hit GA. They Quietly Change What a Power BI Report Actually Is"
source_url: "https://medium.com/power-bi-made-easy/translytical-task-flows-just-hit-ga-9f4a6b8c0d1l"
note_type: source
tags: [power-bi, translytical-task-flows, fabric, direct-lake, directquery, new-feature]
---

# Translytical Task Flows (GA)

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-11-24
> **URL:** https://medium.com/power-bi-made-easy/translytical-task-flows-just-hit-ga-9f4a6b8c0d1l
> **Routed to:** Power BI

## Summary

Translytical Task Flows is a new Microsoft Fabric/Power BI feature that enables write-back scenarios (data entry, scenario modeling, what-if analysis) directly within a Power BI report — without requiring Excel or a separate planning application. It represents a fundamental shift in what a Power BI report can do.

## Key Claims

- Translytical Task Flows allow users to input data directly into a Power BI report, which writes back to a semantic model
- Use cases: budget entry, sales forecasting input, scenario modeling, approval workflows
- Previously required: separate Excel file, manual upload, or a custom application
- Task Flows are configured in Microsoft Fabric (Mirrored Database or Lakehouse) and embedded in Power BI reports
- Data entered via Task Flows can immediately affect displayed KPIs (unlike traditional write-back that requires refresh)

## Notable Details

- Translytical Task Flows require Microsoft Fabric capacity (not standard Power BI Pro)
- Data written via Task Flows persists in the Fabric Lakehouse, not the PBIX file
- Real-time updates: changes made by one user are immediately visible to others viewing the same report

## Extracted Notes

- [[translytical-task-flows-overview]] — pattern

## Metadata

| Field | Value |
|-------|-------|
| Source file | Translytical Task Flows Just Hit GA. They Quietly Change What a Power BI Report Actually Is.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~3,685 |
