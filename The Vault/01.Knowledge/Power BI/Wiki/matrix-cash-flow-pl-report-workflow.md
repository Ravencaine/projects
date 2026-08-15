---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring New Matrix Visual Layouts in Power BI.md"
note_type: workflow
tags: [power-bi, matrix-visual, cash-flow, p-and-l, financial-report, workflow]
---

# Matrix Cash Flow P&L Report Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-new-matrix-visual-layouts-power-bi]]

Create a cash flow or P&L statement using the Matrix visual with Outline or Tabular layout and customized row subtotals.

## Step 1 — Prepare the data

Ensure the dataset contains:
- Revenue line items
- Expense line items
- Category field (Revenue, Expenses, or sub-categories)
- Period field (Year, Quarter, Month)

Structure flat or in a star schema with a fact table and dimension tables.

## Step 2 — Create the Matrix

1. Select **Matrix** from the Visualization pane
2. Add to **Rows**: Category → Line Item hierarchy
3. Add to **Columns**: Period (Year, Quarter, Month)
4. Add to **Values**: Amount measure

## Step 3 — Configure subtotals

1. Open the **Format pane**
2. Navigate to **Layout** → select **Outline** or **Tabular**
3. Go to **Subtotals** section
4. **Column subtotals**: turn **Off** (column totals not needed in P&L)
5. **Row subtotals**: turn **On**
6. **Position**: set to **Bottom** (standard for P&L reading)

## Step 4 — Rename subtotals

1. In the Fields pane, right-click the category field
2. Select **Rename**
3. Rename "Subtotal" row to **Subtotal** or **Net Profit** as appropriate

## Step 5 — Final formatting

1. Apply number formatting (currency, decimal places)
2. Add conditional formatting for positive/negative values (green/red)
3. Adjust column widths for readability
4. Disable steppers (show/hide buttons) if hierarchy is complete

## Related

- [[matrix-layout-setup-workflow]] — layout configuration steps
- [[matrix-outline-layout-column-based]] — Outline layout details
- [[matrix-tabular-layout-no-blank-rows]] — Tabular layout details
