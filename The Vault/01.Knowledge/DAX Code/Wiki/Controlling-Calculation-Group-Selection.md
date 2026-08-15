---
created: 2026-08-06
updated: 2026-08-06
source: Controlling empty or multiple selections in calculation groups
note_type: atomic
tags: [calculation-groups, dax, tabular, selection-context, multiple-selection, empty-selection]
---

# Controlling Calculation Group Selection

Two new calculation group properties — `multipleOrEmptySelectionExpression` and `noSelectionExpression` — intercept DAX execution when a calculation group has multiple active items, zero active items, or no active filters at all. These properties close a gap where Power BI visuals with a calculation group column show correct results, but cells outside that visual (or when the CG is not in the visual) silently ignore all calculation item logic and return raw measure values.

<!-- one-line description: two CG properties — multipleOrEmptySelectionExpression and noSelectionExpression — that intercept DAX execution when CG has ≠1 active items or no filters -->

## Why These Properties Exist

In a Power BI visual that includes the calculation group column (e.g., a Matrix with Metric as a row), each cell has exactly one calculation item in its filter context — no issue. The problem arises when the calculation group column is NOT in the visual:

- **Multiple selection in slicer:** all selected items are active simultaneously; the engine ignores them all → original measure value returned
- **Empty selection:** filter produces zero visible items (e.g., item renamed in the model after report was saved) → same silent fallback
- **No selection:** no filters active on the CG column at all → also returns original measure value

Before these properties, developers had no programmatic hook into these three conditions.

## Property Reference

| Property | Triggers when | In preview? | Min compatibility level |
|---|---|---|---|
| `multipleOrEmptySelectionExpression` | 0 OR ≥2 CG items visible in filter context | Yes (May 2025) | 1605 |
| `noSelectionExpression` | No filters at all on the CG column | Yes (May 2025) | 1605 |

> ⚠️ "Empty selection" ≠ "No selection". Empty = filter active but produces zero rows. No selection = no filter at all. The names are counterintuitive — see [[Controlling-Calculation-Group-Selection]] for the distinction.

## Key Behaviours

- `multipleOrEmptySelectionExpression` intercepts **both** zero and multiple items — they share the same event
- `noSelectionExpression` fires only when the CG column has zero filters applied, including indirect cross-filters
- Both require compatibility level **1605** minimum — Tabular Editor hides these properties if CL < 1605
- Both support a paired `formatStringDefinition` to set the format string alongside the value expression
- Performance note: these properties add execution overhead on every measure reference — test thoroughly before releasing (SQLBI recommends the Optimizing DAX video course)

## Setting via TMDL (Power BI Desktop)

1. Switch to **TMDL view**
2. Right-click the calculation group → Script TMDL → Script tab
3. Add the expression inside the `calculationGroup` block
4. Click **APPLY:** may prompt for compatibility level upgrade to 1605

## Setting via Tabular Editor

1. Select the calculation group in the model tree
2. Set `precedence` if needed (default 0)
3. Edit `multipleOrEmptySelectionExpression` and `noSelectionExpression` in the Properties pane (requires CL ≥ 1605)

## Relationship to Existing Notes

- [[Calculation-Groups]] — conceptual overview of calculation groups
- [[Create-a-Calculation-Group]] — workflow for creating a CG in Tabular Editor
- [[Calculation-Group-Multiple-Selection-Pattern]] — pattern for handling multi-item selection
- [[Calculation-Group-No-Selection-Default-Pattern]] — pattern for applying a default when no CG items are active
- [[TMDL-Syntax-Calculation-Group-Properties]] — syntax reference for both properties

## Related

- [[avoiding-pitfalls-calculation-groups-precedence-source]] — precedence and context in CGs (Ferrari / SQLBI)
- [[Calculation-Group-External-Tools]] — Tabular Editor and DAX Studio for CG management
