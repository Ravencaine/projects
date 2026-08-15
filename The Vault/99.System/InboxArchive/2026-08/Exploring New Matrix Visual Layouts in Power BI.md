---
title: "Exploring New Matrix Visual Layouts in Power BI"
source: "https://databear.com/new-matrix-visual-layouts-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-06-23
created: 2026-08-04
description: "In this blog post, we’ll delve into the new layouts available for Matrix visual layouts  in Power BI."
Processed: "Unprocessed"
---
In this blog post, we’ll delve into the new layouts available for Matrix visual layouts in Power BI. We’ll explore different layouts, their purposes, and demonstrate how to create simple reports like cash flows or P&L reports using these new features. This update is part of Power BI’s May 2024 feature updates and aims to enhance the user experience, especially for those familiar with Excel pivot tables. Let’s get started!

### New Matrix Layouts in Power BI

Power BI has introduced new layout options for Matrix visuals, mimicking the Excel pivot table experience. These layouts are designed to be more intuitive for users transitioning from Excel to Power BI. Let’s explore these options in detail.

#### Compact Layout in Matrix Visual Layouts in Power BI

The compact layout is the new default setting for Matrix visuals. It uses indentation to represent hierarchical data, similar to the stepped layout previously available. This layout is efficient in terms of space, allowing more data to be visible on the report page without scrolling.

To enable the compact layout:

1. Create a Matrix visual.
2. Add your data fields (e.g., Category, Product, Year, and Sales).
3. Navigate to the Format pane, select Layout, and choose Compact.

![Compact Layout New Matrix Visual Layouts in Power BI ](99.System/Attachments/Compact_Layout_New_Matrix_Visual_Layouts_in_Power_BI_.png)

#### Outline Layout in Matrix Visual Layouts in Power BI

The outline layout removes the indentation and displays hierarchical data in separate columns. This layout is reminiscent of early Matrix visuals in Power BI, offering a clear and organized view of your data.

To enable the outline layout:

1. Create a Matrix visual.
2. Add your data fields.
3. Navigate to the Format pane, select Layout, and choose Outline.
4. Adjust the row subtotals to appear at the top or bottom as needed.

![Outline Layout New Matrix Layouts in Power BI](99.System/Attachments/Outline_Layout_New_Matrix_Layouts_in_Power_BI.png)

#### Tabular Layout in Matrix Visual Layouts in Power BI

The tabular layout is similar to the outline layout but eliminates the blank rows between categories, making the visual more compact. This layout is ideal for reports where space is a premium and a cleaner look is preferred.

To enable the tabular layout:

1. Create a Matrix visual.
2. Add your data fields.
3. Navigate to the Format pane, select Layout, and choose Tabular.

![Tabular Layout New Matrix Visual Layouts in Power BI ](99.System/Attachments/Tabular_Layout_New_Matrix_Visual_Layouts_in_Power_BI_.png)

### Creating a Simple Cash Flow Report

Now that we’ve covered the new layouts, let’s create a simple cash flow report using the Matrix visual.

1. **Prepare Your Data**: Ensure you have a dataset with revenue, expenses, and categories.
2. **Create the Matrix Visual**:
	- Add your data fields to the Matrix (e.g., Revenue, Expenses, Categories).
		- Change the visual to Matrix.
		- Organize your fields in the Rows and Columns wells.
3. **Format the Matrix Visual**:
	- Navigate to the Format pane.
		- Remove column subtotals.
		- Enable row subtotals and position them at the bottom.
		- Change the layout to Outline or Tabular for a cleaner look.
4. **Customize Subtotals**:
	- Rename row subtotals to more descriptive labels like “Subtotal” and “Net Profit”.

### Conclusion

The [new Matrix visual layouts in Power BI](https://learn.microsoft.com/en-us/power-bi/visuals/desktop-matrix-visual) offer flexibility and familiarity for Excel users, making data presentation more intuitive and efficient. By using these new layouts, you can create detailed and organized reports like cash flows and P&L statements with ease.