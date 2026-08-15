---
created: 2026-08-08
updated: 2026-08-08
source: "Create calculation groups in Power BI"
source_url: https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups
note_type: workflow
tags: [calculation-groups, power-bi, model-view, dax]
---

# CG Creation — Power BI Desktop Model View

Create a calculation group directly in Power BI Desktop using Model View — no external tools required.

## Prerequisites

- Power BI Desktop
- A Date table in the model

## Steps

### 1 — Enable Discourage Implicit Measures

In Power BI Desktop, edit the semantic model and switch to **Model View**. Select the **Calculation group** button in the ribbon. If **Discourage implicit measures** is off, a dialog prompts you to enable it. Select **Yes:** this is required because calculation items only apply to explicit (user-created) measures.

> An *implicit measure* is created when you drag a numeric column directly into a visual and Power BI applies a default aggregation (SUM, AVERAGE, MIN, MAX). These implicit measures are invisible in the model and are not affected by calculation groups.

### 2 — Name the Calculation Group

Once enabled, a calculation group is added with a default name. Rename it by double-clicking in the **Data** pane or via the **Properties** pane. This name becomes the table name in the model.

### 3 — Write the First Calculation Item

The DAX formula bar opens for the first calculation item. Use `SELECTEDMEASURE()` as the placeholder for whichever measure the visual is currently computing:

```dax
SELECTEDMEASURE()
```

Rename the calculation item to a meaningful name (e.g., `MTD`, `QTD`, `YTD`).

### 4 — Add More Calculation Items

Right-click **Calculation items** or the calculation group → **New calculation item**. Each item is a separate DAX expression using `SELECTEDMEASURE()`.

For time intelligence, the standard items are:

| Item | DAX Expression |
|------|---------------|
| MTD | `CALCULATE(SELECTEDMEASURE(), DATESMTD('Date'[Date]))` |
| QTD | `CALCULATE(SELECTEDMEASURE(), DATESQTD('Date'[Date]))` |
| YTD | `CALCULATE(SELECTEDMEASURE(), DATESYTD('Date'[Date]))` |
| PY | `CALCULATE(SELECTEDMEASURE(), SAMEPERIODLASTYEAR('Date'[Date]))` |

### 5 — Fix Table Name Mismatch Errors

The MS Learn example uses `DimDate` as the table name. If your Date table is named differently, update the DAX expressions — otherwise red triangle error icons appear on the calculation items.

### 6 — Reorder Calculation Items

Select the **Calculation items** section in the **Properties** pane, or right-click a calculation item → **Move Up** / **Move Down** to set the logical display order.

### 7 — Add a Dynamic Format String (Optional)

Select a calculation item (e.g., `YOY%`), turn on **Dynamic format string** in the properties pane, and enter a format string expression:

```
#,##0.00%
```

This overrides the measure's default format when this item is active.

### 8 — Use in Reports

1. Create a **Matrix** visual
2. Add the Date column to **Rows**
3. Add the calculation group column to **Columns**
4. Add a measure to **Values**

Each calculation item appears as a column in the matrix, showing the measure's value under each time-intelligence scenario.

Alternatively, add the calculation group column to a **Slicer** visual to let users select which calculation applies.

### 9 — Set Precedence (Multiple CGs)

If adding multiple calculation groups to the model, set **Precedence** in the calculation group's properties pane to control the order in which groups apply when more than one is active simultaneously.

## TMDL View Alternative

Calculation groups can also be created directly via TMDL view. See [[TMDL-Syntax-Calculation-Group-Properties]] for the full syntax reference.

## Related

- [[Calculation-Groups]] — conceptual overview
- [[SELECTEDMEASURE-Function]] — the DAX placeholder inside every calculation item
- [[CG-Variant-Data-Type-Gotcha]] — variant data type side effect
- [[ISNUMERIC-Guard-Pattern-for-CG]] — guard against non-numeric measures
- [[Create-a-Calculation-Group]] — Tabular Editor workflow (existing note — extended)
