---
created: 2026-08-02
updated: 2026-08-02
source: Here’'s a Quick Way to Switch Measures in Power BI.md
source_url: https://medium.com/@BIWave/heres-a-quick-way-to-switch-measures-in-power-bi-6b8212307adc
note_type: source
tags: [power-bi, medium, field-parameters, dynamic-visuals, calculation-groups]
---

# Switch Measures in Power BI

A guide to using Power BI Field Parameters to create dynamic visuals that switch between measures and dimensions via slicer, covering the build workflow, button slicer configuration, hierarchy persistence, SELECTEDVALUE workarounds, and limitations.

> **Type:** tutorial / how-to
> **Author:** Mikhail Mikushin (BIWave)
> **Published:** 2026-07-30
> **URL:** https://medium.com/@BIWave/heres-a-quick-way-to-switch-measures-in-power-bi-6b8212307adc
> **Routed to:** Power BI

## Summary

The article demonstrates how to create a field parameter in Power BI Desktop (Modeling → New Parameter → Fields), bind it to a visual, configure a button slicer with single-select and force selection, enable hierarchy persistence, handle the SELECTEDVALUE incompatibility via three workarounds (MAX, SUMMARIZE+SELECTCOLUMNS, calculated column), and compares field parameters against calculation groups.

## Key Claims

- Field parameters are calculated tables with `ParameterMetadata` and `GroupByColumns` metadata properties
- Creating a parameter generates: a slicer, metadata, and a calculated table with NAMEOF
- Persist hierarchy level keeps matrix row expansions when switching parameters
- SELECTEDVALUE fails on field parameter display columns — use MAX (single-select), SUMMARIZE+SELECTCOLUMNS (multi-select), or a calculated column workaround
- Field parameters stop working in composite models
- Field parameters work at visual level; calculation groups work at visual/page/report level
- Date columns with auto date/time lose their Date Hierarchy inside field parameters

## Notable Details

- NAMEOF should replace hard-coded strings for rename propagation
- Keep parameter lists under 10–15 items; use dropdown slicer style for larger lists
- Field parameters support relationships; calculation groups do not
- Combine with Object-Level Security for role-based measure visibility
- Consolidate multiple static report pages into one dynamic page with field parameters

## Extracted Notes

- [[field-parameters-calculated-tables]] — `atomic` — Field parameters as calculated tables with metadata properties
- [[field-parameter-build-workflow]] — `pattern` — Step-by-step: create parameter, bind to visual, configure slicer
- [[field-parameters-vs-calculation-groups]] — `pattern` — When to use field parameters vs calculation groups
- [[field-parameter-limitations]] — `gotcha` — Composite models, Q&A, live connections, implicit measures, SELECTEDVALUE, drill-through pages, date hierarchies
- [[selectedvalue-workaround-field-parameters]] — `function` — Three workarounds: MAX, SUMMARIZE+SELECTCOLUMNS, calculated column
- [[field-parameter-best-practices]] — `reference` — NAMEOF, list size, slicer types, explicit measures, OLS, consolidation

## Metadata

| Field | Value |
|-------|-------|
| Source file | `Here's a Quick Way to Switch Measures in Power BI.md` |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-02 |
| Word count | ~950 |
| Language | English |
