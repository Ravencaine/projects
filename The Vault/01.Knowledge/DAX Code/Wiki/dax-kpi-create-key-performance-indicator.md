---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: workflow
tags: [dax, kpi, powerpivot, measure, performance]
---

# DAX KPI: Create Key Performance Indicator in PowerPivot

A KPI in PowerPivot establishes a target value and threshold ranges (red/yellow/green) around a base calculated field, making it easy to see at a glance whether performance is on track.

## Prerequisites

- PowerPivot add-in enabled in Excel
- A base calculated field (measure) already created in the PowerPivot calculation area
- Sufficient data loaded in PowerPivot

## Steps

1. **Create the base calculated field**
   - In PowerPivot calculation area, click a cell
   - Enter the base measure (e.g., `Average of Profit/Sales := AVERAGE([Profit/Sales])`)
   - Press Enter

2. **Create the KPI**
   - Right-click the calculated field cell in the calculation area
   - Select **Create KPI**
   - Set the **absolute value** target (e.g., `0.53` for a 53% profit margin target)
   - Drag the sliders to set thresholds:
     - **Green:** values at or above target
     - **Yellow:** values between lower threshold and target
     - **Red:** values below the lowest threshold
   - Click **OK**

3. **Use the KPI in a Pivot Table**
   - Create a new Pivot Table: PowerPivot tab → Pivot Table → New Worksheet
   - In the PivotTable Fields pane, expand the table containing your KPI
   - Drag the KPI field to Values
   - The Pivot Table shows the base value, and a small coloured indicator (💚🟡🔴) shows status
   - Click the indicator in the cell → select **Value, Goal and Status** to show all three columns

4. **Add KPI to Pivot Table by Product Line**
   - Drag a dimension field (e.g., `ProductCategoryName`) to Rows
   - The KPI shows status for each product category — green if the category's average profit/sales ≥ target

## Variations

- **Percentage target:** If the base metric is already a percentage, set the absolute target to that decimal (0.53 = 53%)
- **External target:** KPI can also reference another calculated field as the target (e.g., compare this year's sales to last year's sales as the goal)
- **Trend KPIs:** Add the same KPI to a Pivot Table with a time dimension (years as columns) to see trajectory

## Notes

- KPIs only work with calculated fields (measures), not calculated columns
- The status indicator is a visual only — the numeric values are still shown in the cells
- KPIs created in PowerPivot are visible in Power View reports as well

## Related

- [[calculated-column-vs-calculated-field]] — KPIs require a calculated field, not a column
- [[dax-year-over-year]] — YoY metrics are a common KPI target
- [[dax-aggregate-functions-average-min-max]] — AVERAGE as the typical KPI base metric
