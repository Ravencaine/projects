---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring New Matrix Visual Layouts in Power BI.md"
note_type: workflow
tags: [power-bi, matrix-visual, layout, compact, outline, tabular, workflow]
---

# Matrix Layout Setup Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-new-matrix-visual-layouts-power-bi]]

Switch between Compact, Outline, and Tabular layouts in the Matrix visual.

## Step 1 — Create the Matrix visual

1. Select Matrix visual from the Visualization pane
2. Drag fields to the **Rows** well (hierarchy order: Category → Product → Year)
3. Drag fields to the **Columns** well if needed
4. Drag a measure to the **Values** well

## Step 2 — Open the Format pane

1. Click the Matrix visual to select it
2. Click the Format pane (paint roller icon)

## Step 3 — Find the Layout option

1. In the Format pane, scroll to **Layout** section
2. Three options appear: **Compact**, **Outline**, **Tabular**

## Step 4 — Select your layout

| Layout | Choose when |
|--------|------------|
| **Compact** | Default; space is tight; indented view acceptable |
| **Outline** | Each hierarchy level needs its own column; subtotals top or bottom |
| **Tabular** | Column view but no blank row gaps between groups |

## Step 5 — Adjust subtotals (Outline/Tabular)

1. In Layout section, find **Row subtotals**
2. Toggle **On/Off**
3. Set position: **Top** or **Bottom**

## Related

- [[matrix-compact-layout-default]] — default layout details
- [[matrix-outline-layout-column-based]] — column-based layout
- [[matrix-tabular-layout-no-blank-rows]] — gap-free tabular layout
- [[matrix-cash-flow-pl-report-workflow]] — practical P&L setup
