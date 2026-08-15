---
created: 2026-08-09
updated: 2026-08-09
source: "Enhance Data Modelling in Power BI.md"
note_type: atomic
tags: [power-bi, data-modeling, measures, repository, table, atomic]
---

# Measures Repository Underscore Table Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-enhance-data-modelling-power-bi]]

Create a `_Measures` table (underscore prefix forces sort to top) with a `Hide Me` column via Enter Data. This table holds all measures as a centralized repository — cleaner than scattering measures across data tables.

## Steps

1. **Home ribbon → Enter Data:** creates a new table
2. **Name the table `_Measures`:** leading underscore sorts it first in the field list
3. **Create one column named `Hide Me`:** content irrelevant (e.g., value "1")
4. **Create measures in this table:** or move existing measures via Home Table property

## Why underscore prefix

`_Measures` sorts alphabetically before any letter-prefixed table names, so it always appears at the top of the field list.

## Hide Me column

The column exists purely to create the table — set its visibility off (right-click → Hide in report view) or ignore it. Its content is never used.

## Measure storage vs. data tables

Measures in a `_Measures` table are semantically separate from data tables — avoids mixing business logic (measures) with data storage (tables). Improves model clarity and discoverability.

## Related

- [[home-table-property-move-measures]] — move existing measures into repository
- [[display-folder-organization-workflow]] — organize measures within the repository
- [[measures-repository-setup-workflow]] — full setup procedure
