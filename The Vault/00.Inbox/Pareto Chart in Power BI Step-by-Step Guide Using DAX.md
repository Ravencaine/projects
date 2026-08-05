---
title: "Pareto Chart in Power BI: Step-by-Step Guide Using DAX"
source: "https://databear.com/pareto-chart-power-bi-dax/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-07-09
created: 2026-08-04
description: "Learn how to create a Pareto chart in Power BI using DAX to visualize the 80/20 rule and focus on top-performing categories."
Processed: "Unprocessed"
---
Creating a **Pareto chart in Power BI** is a powerful way to visualize the 80/20 rule in action. This type of chart helps you quickly identify the top contributors to your business metrics—whether you’re analyzing sales, categories, or customer segments. In this guide, you’ll learn how to build a dynamic Pareto chart using DAX, customize it, and apply it across different data dimensions.

---

## What is the Pareto Principle?

The **Pareto Principle**, also known as the **80/20 Rule**, states that roughly 80% of effects come from 20% of the causes. In business terms: 80% of your sales may come from 20% of your customers or products.

**Use Case Example**:  
Imagine you’re a business owner analyzing product sales. Instead of spreading resources across all products, the Pareto analysis helps you focus on the top-performing 20% that drive the bulk of your revenue.

---

## What is a Pareto Chart?

A **Pareto chart** combines a bar chart and a line graph. In Power BI:

- **Bars** represent individual values (e.g., sales by country).
- **The line** represents the cumulative percentage of the total (helping you see when you’ve hit the 80% threshold).

This dual-axis visualization allows you to quickly spot which elements deserve more attention.

---

## How to Create a Pareto Chart in Power BI

### 1: Create the Total Sales Measure

In your Power BI model, define a basic measure to calculate total sales.

```
Total Sales = SUMX('Order Details', 'Order Details'[Unit Price] * 'Order Details'[Quantity])<img fetchpriority="high" decoding="async" class="aligncenter wp-image-42771 size-full" src="https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-09-172046.png" alt="Pareto chart in Power BI showing total sales by country as blue bars and cumulative percentage as a line graph, highlighting top contributors reaching 80% of total sales." width="736" height="447" srcset="https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-09-172046.png 736w, https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-09-172046-300x182.png 300w, https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-09-172046-150x91.png 150w" sizes="(max-width: 736px) 100vw, 736px" />
```

### 2: Create a Line and Stacked Column Chart

- Add a **Line and Stacked Column Chart** to your report.
- Set the X-axis (e.g., `Country`) and the column values to `Total Sales`.![Pareto chart in Power BI showing total sales by country as blue bars and cumulative percentage as a line graph, highlighting top contributors reaching 80% of total sales.](99.System/Attachments/Pareto_chart_in_Power_BI_showing_total_sales_by_country_as_blue_bars_and_cumulative_percentage_as_a_.png)

---

### 3: Create the Pareto Line Measure

This DAX measure calculates the cumulative percentage:

```
Sales Pareto = 
VAR Total = CALCULATE([Total Sales], ALL('Order Details'))
VAR CurrentSales = [Total Sales]

VAR SummaryTable =
    SUMMARIZE(
        ALLSELECTED('Order Details'),
        'Geography'[Country],
        "Sales", [Total Sales]
    )

VAR CumulativeSum =
    SUMX(
        FILTER(
            SummaryTable,
            [Sales] >= CurrentSales
        ),
        [Sales]
    )

RETURN
    DIVIDE(CumulativeSum, Total)
```

> Note: Replace `'Geography'[Country]` with your actual country column. You can adapt this logic for products or categories as well.![Power BI data model view showing table relationships between Products, Categories, Order Details, Customers, and Orders, illustrating a typical star schema setup for sales analysis.](99.System/Attachments/Power_BI_data_model_view_showing_table_relationships_between_Products,_Categories,_Order_Details,_Cu.png)

---

### 4: Add the Pareto Line to the Chart

- Drag your new `Sales Pareto` measure into the **Line values** field.
- Format the measure as a **percentage**.
- Enable **Data Labels** for clarity.![: Power BI report showing a bar chart of total sales by country on the left and a detailed table on the right listing countries with corresponding total sales and identical cumulative sales Pareto values.](99.System/Attachments/_Power_BI_report_showing_a_bar_chart_of_total_sales_by_country_on_the_left_and_a_detailed_table_on_t.png)

---

### 5: Highlight the Top 80%

Use conditional formatting to emphasize the top 80% contributors.

#### Example using Rules:

- Go to **Data Colors > Conditional Formatting**.
- Set a rule: If `Sales Pareto` ≥ 0.8, color = Blue; else, color = Gray.

This visually separates the “vital few” from the “trivial many.” ![](99.System/Attachments/Screenshot-2025-05-09-174037.png)

---

## Apply Pareto Analysis to Categories or Products

The same DAX logic applies to other dimensions:

### For Categories:

Change the grouping in the DAX:

```
'Product Categories'[Category Name]
```

### For Products:

Adjust again:

```
'Products'[Product Name]
```

This flexibility allows deeper insights at every level of your data hierarchy.

---

## Enhance Your Power BI Skills

Understanding and implementing Pareto charts in Power BI provides immediate value in identifying high-impact opportunities. Whether you’re analyzing sales, support tickets, or inventory issues, the Pareto chart guides you to **focus where it matters most**.

---

## Try It Yourself

Ready to level up your Power BI game? Check out this [Power BI Training from Data Bear](https://databear.com/power-bi-training/) —a great way to master advanced reporting and visualization techniques.