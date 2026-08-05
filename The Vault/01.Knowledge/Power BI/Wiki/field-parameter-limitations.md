---
created: 2026-08-02
updated: 2026-08-02
source: Here's a Quick Way to Switch Measures in Power BI.md
note_type: gotcha
tags: [power-bi, gotcha, field-parameters, limitations, composite-models]
---

# Field Parameter Limitations

Field parameters have specific constraints that make them unsuitable in certain Power BI scenarios. Understanding these limitations prevents unexpected behavior at design time.

## Composite Models

Field parameters **stop working** in composite models (models that mix import and DirectQuery connections, or multiple DirectQuery sources). If your semantic model uses composite mode, field parameters will be disabled.

**Workaround**: Avoid composite models if field parameters are required, or use calculation groups instead.

## Q&A Visual and AI Visuals

AI-powered visuals and the Q&A visual **cannot interpret field parameters**. The AI engine does not understand the parameter substitution mechanism.

**Workaround**: Use standard visuals when field parameters are in use. Do not mix Q&A or AI visuals on the same report page with field parameter-driven visuals.

## Live Connections

Pure live connections to Power BI semantic models or Analysis Services **do not support field parameters:** the parameter table must exist in the local model.

**Workaround**: Use a local model (composite model) for DirectQuery with Power BI semantic models. Pure live connections cannot use field parameters.

## Implicit Measures

Dragging a column with automatic `SUM` aggregation into a field parameter **does not work**. Field parameters require **explicit DAX measures**.

**Workaround**: Create explicit DAX measures for all numeric columns you want to reference in field parameters:

```dax
Total Revenue = SUM(Sales[Revenue])
```

Then reference the explicit measure in the parameter.

## SELECTEDVALUE Incompatibility

The `GroupByColumns` metadata property on field parameter tables **prevents standard `SELECTEDVALUE`** from detecting a single selected value.

**Workaround**: See [[selectedvalue-workaround-field-parameters]] — use `MAX`, `SUMMARIZE + SELECTCOLUMNS`, or a calculated column workaround.

## Drill-Through and Tooltip Pages

Field parameters **cannot be used as linked fields** on drill-through or tooltip pages.

**Workaround**: Link the individual columns referenced within the parameter directly, rather than the parameter field itself.

## Date Columns with Auto Date/Time

When `Auto date/time` is enabled, a date column used in a field parameter **loses its Date Hierarchy** (Year, Quarter, Month drill-down).

**Workaround**: Create the parameter with explicit hierarchy levels (Year, Quarter, Month, Day) instead of relying on the auto date/time hierarchy.

## Persist Hierarchy Level Behavior

The **Persist hierarchy level** option remembers row expansions across parameter changes — but some report designs benefit from the default collapsed-on-change behavior.

**Workaround**: Test both settings per report. Enable it for matrix drill-down scenarios; leave it off for card/KPI layouts.

## Related

- [[field-parameters-calculated-tables]] — `atomic`
- [[field-parameter-build-workflow]] — `pattern`
- [[selectedvalue-workaround-field-parameters]] — `function`
- [[field-parameter-best-practices]] — `reference`
