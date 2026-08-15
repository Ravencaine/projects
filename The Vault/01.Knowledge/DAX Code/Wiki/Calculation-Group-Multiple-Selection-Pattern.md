---
created: 2026-08-06
updated: 2026-08-06
source: Controlling empty or multiple selections in calculation groups
note_type: pattern
tags: [calculation-groups, dax, multiple-selection, tabular, pattern, ERROR, LOOKUPVALUE, SELECTEDMEASURE]
---

# Calculation Group Multiple Selection Pattern

DAX pattern for `multipleOrEmptySelectionExpression` — intercepts when ≥2 calculation items are active and applies a defined fallback behaviour.

<!-- one-line description: multipleOrEmptySelectionExpression — ERROR on invalid combos, or pick highest ordinal item, or combine time intelligence items via INTERSECT/SWITCH -->

## Pattern 1 — Raise an Error (Strict Mode)

Use when multiple selection is semantically invalid. Forces the user to pick exactly one item.

```dax
// In TMDL — add inside calculationGroup block:
multipleOrEmptySelectionExpression = ERROR("Multiple selection of Metric is not allowed")
```

## Pattern 2 — Pick Highest Ordinal (Prioritised Fallback)

Use when one of the selected items should win based on sort order.

```dax
// In TMDL:
multipleOrEmptySelectionExpression = ``
    VAR maxSelection = MAX('Unit measure C'[Ordinal])
    VAR selection =
        LOOKUPVALUE(
            'Unit measure C'[Metric],
            'Unit measure C'[Ordinal], maxSelection
        )
    RETURN
        CALCULATE(
            SELECTEDMEASURE(),
            'Unit measure C'[Metric] = selection
        )
    ``

formatStringDefinition = ``
    VAR maxSelection = MAX('Unit measure C'[Ordinal])
    VAR selection =
        LOOKUPVALUE(
            'Unit measure C'[Metric],
            'Unit measure C'[Ordinal], maxSelection
        )
    RETURN
        CALCULATE(
            SELECTEDMEASUREFORMATSTRING(),
            'Unit measure C'[Metric] = selection
        )
    ``
```

**Why Ordinal over Name?** The Ordinal column respects the explicit sort order defined in the model, not alphabetical order.

## Pattern 3 — Combine Time Intelligence Items (INTERSECT + SWITCH)

Use for Time Intelligence groups where certain combinations should produce a derived item (e.g., YTD + PY → PYTD).

```dax
// In TMDL:
multipleOrEmptySelectionExpression = ``
    VAR sel_YTD_PY   = {"YTD", "PY"}
    VAR sel_YTD_YOY  = {"YTD", "YOY"}
    VAR selection    = VALUES('Time Intelligence'[Name])
    RETURN
        SWITCH(
            TRUE(),
            COUNTROWS(INTERSECT(selection, sel_YTD_PY)) = COUNTROWS(sel_YTD_PY)
                && COUNTROWS(selection) = COUNTROWS(sel_YTD_PY),
                    CALCULATE(SELECTEDMEASURE(), 'Time Intelligence'[Name] = "PYTD"),
            COUNTROWS(INTERSECT(selection, sel_YTD_YOY)) = COUNTROWS(sel_YTD_YOY)
                && COUNTROWS(selection) = COUNTROWS(sel_YTD_YOY),
                    CALCULATE(SELECTEDMEASURE(), 'Time Intelligence'[Name] = "YTDOYTD"),
            ERROR("Invalid Time Intelligence selection")
        )
    ``
```

> ⚠️ DAX has no recursion — cannot chain-calculate across multiple selected items. The INTERSECT approach works only when you know the exact combinations in advance.

## Pattern 4 — Average or Sum Multiple Selected Items

When you want to aggregate across all selected items:

```dax
// Conceptual — DAX has no recursion, so iterate via a table context:
multipleOrEmptySelectionExpression = ``
    VAR allItems = VALUES('Time Intelligence'[Name])
    VAR result =
        SUMX(
            allItems,
            CALCULATE(SELECTEDMEASURE(), 'Time Intelligence'[Name] = SELECTEDVALUE('Time Intelligence'[Name]))
        )
    RETURN
        result
    ``
```

> ⚠️ This applies each calculation item sequentially — no true recursion, results may differ from expected composition.

## Key DAX Functions Used

| Function | Purpose |
|----------|---------|
| `MAX(column)` | Get highest ordinal to select by priority |
| `LOOKUPVALUE()` | Map ordinal value back to item name |
| `VALUES(column)` | Get the set of active values from filter context |
| `CALCULATE(SELECTEDMEASURE(), ...)` | Re-execute the current measure under a modified filter |
| `INTERSECT(set1, set2)` | Check whether selected items exactly match a known combination |
| `COUNTROWS(INTERSECT(...))` | Compare cardinalities to detect exact combo match |
| `SWITCH(TRUE(), ...)` | Route to specific CG item based on detected combination |
| `ERROR()` | Raise a user-defined error for unsupported selections |
| `SELECTEDMEASURE()` | Refer to the measure currently being evaluated |
| `SELECTEDMEASUREFORMATSTRING()` | Return the format string of the current measure |

## Gotchas

- The expression runs inside the current filter context — you can inspect active values via `VALUES('CG'[Name])` and `VALUES('CG'[Ordinal])`
- `multipleOrEmptySelectionExpression` fires for **both zero AND multiple** items — distinguish in code by checking `COUNTROWS(VALUES('CG'[Name]))`
- Set `formatStringDefinition` alongside the value expression to avoid format string mismatches on fallback values
- Requires compatibility level **1605** minimum

## Related

- [[Controlling-Calculation-Group-Selection]] — concept overview and property reference
- [[Calculation-Group-No-Selection-Default-Pattern]] — `noSelectionExpression` pattern (different property)
- [[TMDL-Syntax-Calculation-Group-Properties]] — full TMDL syntax reference
