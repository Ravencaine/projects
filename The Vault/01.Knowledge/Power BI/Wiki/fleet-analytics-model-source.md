---
created: 2026-07-31
updated: 2026-08-02
source: From Messy Power BI Relationships to a Clean Fleet Analytics Model.md
source_url: https://medium.com/microsoft-power-bi/from-messy-power-bi-relationships-to-a-clean-fleet-analytics-model-d9ae82bb323c
note_type: source
tags: [power-bi, data-modeling, fleet-analytics, hub-and-spoke, star-schema]
---

# From Messy Power BI Relationships to a Clean Fleet Analytics Model

> **Type:** article
> **Author:** Mark Chen
> **Published:** 2026-03-17
> **URL:** https://medium.com/microsoft-power-bi/from-messy-power-bi-relationships-to-a-clean-fleet-analytics-model-d9ae82bb323c
> **Routed to:** Power BI, Data Modeling

## Summary

Fleet analytics datasets (~1,000 equipment, 2–3 years of daily data) are prone to relationship ambiguity when dimensions are overloaded. The solution: hub-and-spoke star schema with Equipment as the central hub, treat operator assignments as a fact table (not a dimension), and push complex allocations into DAX measures rather than columns.

## Key Claims

- Overloaded dimensions (Operator = attributes + assignments + region) cause ambiguous filter propagation and circular dependencies
- Treating assignment tables as fact tables (bridge-as-fact) eliminates relationship ambiguity
- Equipment naturally serves as the hub in fleet analytics — nearly every operational signal connects to machines
- Many-to-many payroll allocation should be done via DAX measures, not columns
- Power BI handles ~1M fact rows / 50–150 MB easily; performance problems come from complex relationship paths, not data volume
- The Operational Triangle (Operator + Equipment + Project) is the core entity structure for equipment-heavy industries
- Optional: consolidate separate fact tables into a single unified Activity Fact at consistent grain

## Extracted Notes

- [[hub-and-spoke-equipment-as-hub]] — pattern — Equipment as the central hub in fleet analytics
- [[assignment-table-as-fact-pattern]] — pattern — Treating operator assignment tables as fact tables
- [[operational-triangle-model]] — pattern — The Operator + Equipment + Project triangle
- [[consolidated-activity-fact-pattern]] — pattern — Merging multiple same-grain facts into one table
- [[mark-chen]] — author — Mark Chen's author note (4th source)

## Metadata

| Field | Value |
|-------|-------|
| Source file | From Messy Power BI Relationships to a Clean Fleet Analytics Model.md |
| Ingestion date | 2026-07-31 |
| Word count | ~1,000 |
| Level | Beginner |
| Category | Data Model |
