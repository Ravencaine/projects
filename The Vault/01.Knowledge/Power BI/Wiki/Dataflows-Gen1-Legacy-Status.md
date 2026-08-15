---
created: 2026-08-09
updated: 2026-08-09
source: "Document Power BI Dataflows Gen1 with Copilot Cowork (Before You Migrate).md"
note_type: atomic
tags: [power-bi, dataflows-gen1, dataflows-gen2, legacy, migration, microsoft-fabric, atomic]
---

# Dataflows Gen1 Legacy Status

**Type:** Atomic · **KB:** Power BI · **Source:** [[Source-Document-Dataflows-Gen1-CoWork]]

**Power BI Dataflows Generation One is legacy but not deprecated.** Microsoft has not announced an end-of-support date. Organizations should document Gen1 dataflows now — before migrating to Gen2 or another platform — so they have a complete technical record of what needs to be moved.

## What "legacy" means

- No new features are being developed for Dataflows Gen1
- Existing Gen1 dataflows continue to work and receive security updates
- No forced migration timeline has been announced
- This is the right time to document and plan, not panic

## Why document before migrating

Gen1 dataflows store their complete definition in the export.json file:
- All table definitions
- All column names and data types
- All Power Query M code (transformations)
- Source system connections
- Primary/foreign key relationships
- Refresh schedules and metadata

This information is required to recreate the dataflow in Gen2 or an alternative platform. Without documentation, migration becomes reverse-engineering.

## Gen1 vs Gen2 at a glance

| | Gen1 | Gen2 |
|--|------|------|
| Status | Legacy | Current |
| New features | No | Yes |
| Compute isolation | No | Yes |
| Workspace-level reuse | Limited | Enhanced |
| Export.json | Available | Different export format |
| Migration path | Document first | Current target |

## Recommendation

Document Gen1 dataflows while they are still running. Use export.json + CoWork to generate the documentation automatically.

## Related

- [[Document-Dataflows-Gen1-with-CoWork-Workflow]] — the workflow for this
- [[CoWork-Skill-from-Input-Output-Samples]] — the pattern that powers it
