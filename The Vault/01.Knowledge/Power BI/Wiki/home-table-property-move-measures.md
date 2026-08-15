---
created: 2026-08-09
updated: 2026-08-09
source: "Enhance Data Modelling in Power BI.md"
note_type: atomic
tags: [power-bi, data-modeling, measures, home-table, model-view, atomic]
---

# Home Table Property Move Measures Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-enhance-data-modelling-power-bi]]

In Power BI model view, a measure's `Home Table` property determines which table the measure belongs to. Changing this property consolidates existing measures into a centralized `_Measures` repository without re-creating them.

## Steps

1. Open **Model View** in Power BI Desktop
2. Select the measure you want to move
3. In the **Properties pane**, find **Home Table**
4. Change Home Table to `_Measures`

The measure moves to the `_Measures` table. Its definition is unchanged — only the owning table reference changes.

## Effect on DAX

DAX references to the measure remain unchanged — `[{MeasureName}]` still works regardless of which table owns it.

## Why move measures

- Centralized repository: all measures in one logical location
- Cleaner field list: measures don't pollute data table groupings
- Easier discovery: `_Measures` table at top of field list

## Related

- [[measures-repository-underscore-table]] — creating the repository
- [[display-folder-organization-workflow]] — organize after moving
- [[measures-repository-setup-workflow]] — full workflow
