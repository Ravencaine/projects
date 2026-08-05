---
created: 2026-08-02
updated: 2026-08-02
source: Here's a Quick Way to Switch Measures in Power BI.md
note_type: atomic
tags: [power-bi, atomic, field-parameters, calculated-table, dynamic-visuals]
---

# Field Parameters as Calculated Tables

Field parameters are calculated tables that reference columns or measures, enabling dynamic visual behavior where user selection from a slicer substitutes fields into a visual. They are the standard Power BI mechanism for toggling between measures and dimensions without duplicating visuals.

## Definition

A field parameter is a calculated table with three key components per row:
- **Field reference**: the actual column or measure being substituted
- **Display name**: the label shown in the slicer
- **Sort order**: controls the slicer order

Power BI also attaches two metadata properties:
- `ParameterMetadata`: marks the table as a field parameter
- `GroupByColumns`: enables grouping behavior

## Key Points

- Created via Modeling → New Parameter → Fields in Power BI Desktop
- Power BI generates the `NAMEOF()` calculated table automatically
- Connecting a slicer to the parameter field enables field substitution in visuals
- Field parameters work at the visual level (unlike calculation groups which work at page/report level)
- Parameter tables can have relationships with other tables (calculation groups cannot)
- Composite models disable field parameter functionality

## Relationship to Calculation Groups

| Feature | Field Parameters | Calculation Groups |
|---|---|---|
| Scope | Visual level | Visual, page, or report level |
| Relationships | Supported | Not supported |
| Performance overhead | Minimal | Can slow queries when filters are modified |
| Creation method | UI or DAX | Tabular Editor / DAX |

## Related

- [[field-parameter-build-workflow]] — `pattern`
- [[field-parameters-vs-calculation-groups]] — `pattern`
- [[selectedvalue-workaround-field-parameters]] — `function`
- [[field-parameter-limitations]] — `gotcha`
- [[field-parameter-best-practices]] — `reference`
