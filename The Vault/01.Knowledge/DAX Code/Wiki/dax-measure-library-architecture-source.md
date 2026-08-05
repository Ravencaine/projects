---
created: 2026-07-29
updated: 2026-08-02
source: DAX Measure Library Architecture — From Messy to Maintainable (Tejwani, 2026-01-19)
source_url: https://medium.com/towards-artificial-intelligence/dax-measure-library-architecture-from-messy-to-maintainable-97e0aca852a9
note_type: source
tags: [dax, measure-library, architecture, organization, folder-structure, naming, governance, roi]
---

# DAX Measure Library Architecture — From Messy to Maintainable (source note)

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2026-01-19
> **URL:** https://medium.com/towards-artificial-intelligence/dax-measure-library-architecture-from-messy-to-maintainable-97e0aca852a9
> **Routed to:** DAX Code

## Summary

The organizational problem: 147 measures with no organization cost Tejwani's team $93,600/year in search time. The solution: a 4-layer architecture framework (folder structure, naming conventions, documentation standards, governance process) that transformed DAX from a chaotic collection into a maintainable library. ROI of 1,257% in year one. 4-week implementation plan included.

## Key Claims

- 4 hours/week × 6 analysts × $75/hr = $93,600/year wasted on searching for existing measures
- 89% of measures built from scratch before architecture → 67% built from existing components after
- New analyst onboarding: 4–6 weeks before → 1–2 weeks after
- 1,257% ROI in year one (40 hours investment vs $93,600 annual savings)
- The 4 layers: Folder Structure, Naming Conventions, Documentation, Governance Process
- Measure naming formula: `[Business Object] [Metric Name] [Modifier] [Time Period]`
- Folder structure: `_Base Measures`, `Time Intelligence`, `Comparisons & Variance`, `KPIs & Metrics`, `Utilities`, `Formatting`, `_Exploration`
- Documentation levels: Level 1 (base measures), Level 2 (business metrics), Level 3 (complex KPIs with full template)
- Governance cadence: weekly review (15 min), monthly audit (30 min), quarterly cleanup (2 hr)
- Library Champion role: rotating monthly coach, not enforcer
- Exploration exception: `#` prefix + personal `_Exploration` folder for deadline work

## Notable Details

- Special prefixes: `_` (base/internal), `#` (temporary), `!` (needs fix)
- Naming convention test: findability, WHAT-not-HOW, consistency, new-team-member test
- Maximum 3 folder levels — if you need more, refactor categories
- Folder names use business language: `Sales`, not `Fact_Sales`
- The architecture doesn't make DAX faster — it makes teams faster at using DAX

## Extracted Notes

Links to notes derived from this source:

- [[implement-dax-measure-library-architecture]] — `workflow` — 4-week implementation plan
- [[measure-governance-process]] — `workflow` — 3-step process + weekly/monthly/quarterly cadence
- [[dax-measure-naming-convention-framework]] — `reference` — naming formula and rules
- [[dax-measure-folder-structure-template]] — `reference` — canonical folder structure template
- [[dax-measure-documentation-template]] — `snippet` — three-level documentation template with examples
- [[when-measure-library-architecture-is-essential]] — `comparison` — decision framework for when to implement
- [[hidden-cost-of-messy-measures]] — `atomic` — three costs: search time, inconsistency, knowledge loss
- [[measure-library-architecture-roi]] — `comparison` — before/after metrics with 1,257% ROI

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX Measure Library Architecture From Messy to Maintainable.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-29 |
| Word count | ~5,600 |
