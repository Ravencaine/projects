---
created: 2026-08-02
updated: 2026-08-02
source: Here's a Quick Way to Switch Measures in Power BI.md
note_type: function
tags: [dax, function, selectedvalue, field-parameters, workaround]
---

# SELECTEDVALUE Workarounds for Field Parameters

`SELECTEDVALUE` cannot detect single-value selections directly on a field parameter's display column because the `GroupByColumns` metadata property overrides standard filter context behavior. Three workarounds resolve this.

## Why SELECTEDVALUE Fails

Field parameter tables carry `GroupByColumns` metadata, which changes how filter context propagates. `SELECTEDVALUE` relies on standard filter context, so it returns `BLANK` instead of the selected display value when used against the parameter's display column.

## Workaround 1: MAX (Single-Select Slicers)

When the parameter slicer is configured for single-select, `MAX` returns the selected value without needing to clear the filter context:

```dax
Selected Measure Name = MAX('KPI Selector'[KPI Selector])
```

**Requirements**: Button slicer + Single select + Force selection must be enabled.

**Limitation**: Only works for single-select scenarios.

## Workaround 2: SUMMARIZE + SELECTCOLUMNS (Multi-Select)

For multi-select parameter slicers, reconstruct the value set via SUMMARIZE, then use SELECTCOLUMNS:

```dax
VAR SelectedValue =
    SELECTCOLUMNS(
        SUMMARIZE(
            'KPI Selector',
            'KPI Selector'[KPI Selector],
            'KPI Selector'[KPI Selector Fields]
        ),
        'KPI Selector'[KPI Selector]
    )
RETURN
    IF(
        COUNTROWS(SelectedValue) = 1,
        SELECTEDVALUE('KPI Selector'[KPI Selector])
    )
```

This works by re-aggregating the parameter table context back to a single-row representation before testing with SELECTEDVALUE.

## Workaround 3: Calculated Column (No Composite Key)

Add a calculated column that copies the display column. The new column will not inherit the composite key metadata:

```dax
KPI Name = 'KPI Selector'[KPI Selector]
```

Then use `SELECTEDVALUE('KPI Selector'[KPI Name])` in measures — the calculated column does not have the GroupByColumns override, so SELECTEDVALUE works normally.

**Limitation**: The calculated column is static and won't update if the parameter structure changes.

## Summary

| Workaround | Use Case | Limitation |
|---|---|---|
| `MAX` | Single-select slicers | Only works with single select |
| `SUMMARIZE + SELECTCOLUMNS` | Multi-select slicers | Complex DAX |
| Calculated column | Any SELECTEDVALUE need | Static; doesn't react to parameter structure changes |

## Related

- [[field-parameters-calculated-tables]] — `atomic`
- [[field-parameter-limitations]] — `gotcha`
