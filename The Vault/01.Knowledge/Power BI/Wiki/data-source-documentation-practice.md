---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, documentation, data-governance, data-sources, best-practices]
---

# Data Source Documentation Practice

Every Power BI solution depends on one or more data sources. Documenting them at build time prevents deployment failures, refresh errors, and lost institutional knowledge.

## What to Document

For each data source in a report:

| Field | Why it matters |
|-------|----------------|
| **Source type** | File, database, cloud service, API — determines refresh method |
| **Server name / file path** | Needed to recreate connection on another machine or in another environment |
| **Authentication method** | How credentials are provided; needed when credentials expire or are rotated |
| **Refresh schedule** | How often the source data changes; determines whether Import or scheduled refresh is appropriate |
| **Owner / IT contact** | Who manages access changes, schema updates, and data quality issues |
| **Gateway required** | Whether the report needs an on-premises gateway when published to Power BI Service |
| **Last refresh / data as-of** | When the data was last successfully updated — critical for interpreting reports |

## Where to Store Documentation

The best location is alongside the report itself — a cover page or description field in Power BI Desktop that survives publishing. For enterprise solutions, a companion document or wiki entry linked from the report description is the standard approach.

## Common Omission

The detail most frequently missing from documentation: **what happens when the source changes schema**: a column is renamed, a table is split, or a database is migrated. Documenting who to contact and what the escalation path looks like is as important as the connection details themselves.

## The Refresh Planning Checklist

Before finalising any data source documentation:
- [ ] Local file or cloud? (determines manual vs automatic refresh)
- [ ] On-premises database? (gateway required)
- [ ] Credentials managed by IT or self-service?
- [ ] Refresh schedule agreed with source owner?
- [ ] Owner confirmed read-only access is sufficient?

## Related

- [[import-vs-directquery-connection]] — the design decision that drives refresh planning
- [[on-premises-gateway-requirement]] — gateway documentation field
- [[cloud-data-sources-onedrive-sharepoint]] — refresh behaviour by cloud source type
