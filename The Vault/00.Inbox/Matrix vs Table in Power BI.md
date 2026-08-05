---
title: "Matrix vs Table in Power BI"
source: "https://databear.com/matrix-vs-table-power-bi/"
author:
  - "[[Annamarie Van Wyk]]"
published: 2023-05-12
created: 2026-08-04
description: "Learn about the difference between a matrix vs table visual in Power BI and how to use them for the best data display."
Processed: "Unprocessed"
---
In this blog post for Matrix vs tables in Power BI, I will compare and contrast the matrix visual and the table visual, and show you how to use them effectively in your reports and dashboards. Both visuals are useful for displaying tabular data, but they have some key differences that you should be aware of.

![Virtual Tables in Power BI](99.System/Attachments/Virtual_Tables_in_Power_BI.jpg)

## Where to find them on the Power BI visual gallery.

![Visual Gallery](99.System/Attachments/Visual_Gallery.png)

### Power BI Matrix Visual

The matrix visual is similar to a pivot table in Excel. It allows you to display data in a grid format, with rows and columns that can be expanded or collapsed to show different levels of detail. You can also add subtotals and grand totals to the matrix visual, as well as conditional formatting and drill-through actions.

![Matrix example](99.System/Attachments/Matrix_example.png)

![Matrix with levels](99.System/Attachments/Matrix_with_levels.png)

### Power BI Table Visual

The table visual is simpler and more compact than the matrix visual. It displays data in a flat table format, with no hierarchy or aggregation. You can sort and filter the table visual, as well as apply conditional formatting and drill-through actions. However, you cannot add subtotals or grand totals to the table visual.

![Table example](99.System/Attachments/Table_example.png)

### How to build a matrix visual

To use the matrix visual or the table visual in Power BI, you need to drag and drop the fields that you want to display from the Fields pane to the Values, Rows, and Columns buckets in the Visualizations pane. The Values bucket determines what measures or calculations are shown in the cells of the visual. The Rows and Columns buckets determine what dimensions or categories are shown in the rows and columns of the visual.

For example, if you want to create a matrix visual that shows the sales amount by product category and year, you would drag the Sales Amount field to the Values bucket, the Product Category field to the Rows bucket, and the Year field to the Columns bucket. You can then adjust the formatting options of the matrix visual, such as font size, color, alignment, etc.

![Data added to matrix](99.System/Attachments/Data_added_to_matrix.png)

If you want to create a table visual that shows the same data, you would drag the same fields to the bucket noting that a table visual only has a column bucket available. However, you would not see any hierarchy or subtotals in the table visual. You can also adjust the formatting options of the table visual, such as font size, color, alignment, etc.

![Table visual with data added](99.System/Attachments/Table_visual_with_data_added.png)

### Advantages and Disadvantages of matrix vs table in Power BI

The matrix visual and the table visual have different advantages and disadvantages depending on your data and your reporting needs. Here are some scenarios where you might prefer one over the other:

- *Use the matrix visual if you want to show hierarchical data with multiple levels of detail. For example, if you want to show sales by region, country, city, and product.*
- *Use the matrix visual if you want to show subtotals and grand totals for your data. For example, if you want to show the total sales amount for each product category and year.*
- *Use the matrix visual if you want to apply conditional formatting based on rules or scales. For example, if you want to highlight the cells that have high or low sales values.*
- *Use the table visual if you want to show flat data with no hierarchy or aggregation. For example, if you want to show a list of customers and their contact details.*
- *Use the table visual if you want to save space on your report or dashboard. For example, if you have limited room for displaying multiple visuals.*
- *Use the table visual if you want to apply conditional formatting based on icons or web URLs. For example, if you want to show a status icon or a link for each row of data.*

You can find some more information on the Matrix [here.](https://learn.microsoft.com/en-us/power-bi/visuals/desktop-matrix-visual)

I hope this blog post on Matrix vs Table in Power BI has helped you understand how to use the matrix visual and the table visual in Power BI. You can learn more about these visuals and other Power BI features from the official documentation or online tutorials. Happy reporting! Don’t forget to check out our Power BI Training [Page](https://databear.com/power-bi-training/) and our blog [Page.](https://databear.com/blog/)