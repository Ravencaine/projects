---
created: 2026-08-11
updated: 2026-08-11
source: "11-Power-BI-Tips-Guy-in-a-Cube-Transcript.md"
note_type: workflow
tags: [power-bi, measure-table, model-organization, workflow]
---

# Measure Table — Dedicated Table for Measure Organization

Create a single hidden integer column table named "Measures" to hold all model measures in one place.

## Steps

1. Modeling → New Table
2. `Measures = DATATABLE("N", INTEGER, {{1}})`
3. Move all measures to this table (drag in Model view)
4. Hide the `N` column
5. Use Display Folders for further organization (Revenue, KPIs, Ratios, etc.)

## Purpose

- One location for all measures — no hunting across fact/dimension tables
- Cleaner Model view
- Does NOT improve performance — only organization
- Compatible with both approach: some devs prefer measures in related fact table (also valid)

## Related

- [[model-organization-display-folders]] — display folder patterns
