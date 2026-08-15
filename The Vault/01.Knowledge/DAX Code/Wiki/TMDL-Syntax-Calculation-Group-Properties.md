---
created: 2026-08-06
updated: 2026-08-06
source: Controlling empty or multiple selections in calculation groups
note_type: reference
tags: [calculation-groups, tmdl, syntax, reference, tabular, power-bi, compatibility-level]
---

# TMDL Syntax for Calculation Group Properties

Reference for writing `multipleOrEmptySelectionExpression` and `noSelectionExpression` in TMDL format. Both properties are in preview as of May 2025 and require compatibility level **1605**.

<!-- one-line description: TMDL syntax reference for calculationGroup multipleOrEmptySelectionExpression, noSelectionExpression, and formatStringDefinition properties -->

## Enabling TMDL View in Power BI Desktop

Power BI Desktop → View → **TMDL view** (preview feature as of mid-2025).

## TMDL Scripting Steps

1. Open **TMDL view**
2. Right-click the calculation group in the Model pane
3. **Script TMDL to** → **Script tab**
4. Write the property inside the `calculationGroup` block
5. Click **APPLY:** may prompt to upgrade compatibility level to 1605

## Property Syntax

### multipleOrEmptySelectionExpression

Fires when the CG column has 0 OR ≥2 visible items in the filter context.

```
calculationGroup 'Metric'
    multipleOrEmptySelectionExpression = ```
        <DAX expression>
        ```
```

### noSelectionExpression

Fires when the CG column has **no filters** applied at all.

```
calculationGroup 'Metric'
    precedence: <integer>
    noSelectionExpression = ```
        <DAX expression>
        ```
```

### formatStringDefinition (paired)

Defines the format string alongside either expression. Must mirror the logic of the main expression.

```
formatStringDefinition = ```
    <DAX expression returning a string>
    ```
```

### calculationItem

Creates a named calculation item inside the CG.

```
calculationItem '<Item Name>' = <DAX expression>
```

## TMDL Escaping

Backtick strings (`` ``` ``) in the TMDL representation use escaped backticks (`\`\`\``) to avoid terminating the string literal.

| Literal in TMDL | What you type in TMDL |
|---|---|
| ``` ``` ``` (open/close) | `\`\`\`` |
| Line breaks | Preserved in the string literal |

## Compatibility Level

| Property | Min CL | Notes |
|---|---|---|
| `multipleOrEmptySelectionExpression` | 1605 | Tabular Editor only shows this property when CL ≥ 1605 |
| `noSelectionExpression` | 1605 | Same |
| `formatStringDefinition` | 1605 | Paired with either of the above |
| `precedence` | — | Standard CG property, not new |

## Tabular Editor Path

1. Select the calculation group in the model tree
2. In the **Properties** pane, locate the property
3. Edit the expression directly — no TMDL escaping needed (Tabular Editor handles it)
4. Requires CL ≥ 1605 to be visible in the UI

## Related

- [[Controlling-Calculation-Group-Selection]] — concept overview
- [[Calculation-Group-Multiple-Selection-Pattern]] — example expressions
- [[Calculation-Group-No-Selection-Default-Pattern]] — noSelectionExpression examples
- [[Create-a-Calculation-Group]] — creating a CG in Tabular Editor
- [[CG-Creation-Power-BI-Model-View]] — creating a CG in Power BI Desktop Model View (no external tools)

## Basic CG Creation Syntax (from MS Learn)

The minimum TMDL to create a calculation group with one calculation item and two required columns:

```tmdl
createOrReplace
    table 'Calculation group'
        calculationGroup
            precedence: 1
            calculationItem 'Calculation item' = SELECTEDMEASURE()
        column 'Calculation group column'
            dataType: string
            summarizeBy: none
            sourceColumn: Name
            sortByColumn: Ordinal
            annotation SummarizationSetBy = Automatic
        column Ordinal
            dataType: int64
            formatString: 0
            summarizeBy: sum
            sourceColumn: Ordinal
            annotation SummarizationSetBy = Automatic
```

Required components:
- **`calculationGroup` block:** defines the CG name and precedence
- **`calculationItem`:** the DAX expression (uses `SELECTEDMEASURE()`)
- **Name column:** string, `summarizeBy: none`, `sourceColumn: Name`, sorted by Ordinal
- **Ordinal column:** int64, `summarizeBy: sum`, `formatString: 0`, controls display order

> Source: [[Source-Create-Calculation-Groups-Power-BI]] — Microsoft Learn
