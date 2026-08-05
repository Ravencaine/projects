---
title: "Mastering Grouping in Power BI: 5 Powerful DAX Measures You Need to Know"
source: "https://databear.com/grouping-in-power-bi-using-dax-measures/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-05-19
created: 2026-08-04
description: "In this post, we'll delve into the powerful capabilities of grouping in Power BI visuals using various DAX measures."
Processed: "Unprocessed"
---
In this post, we’ll delve into the powerful capabilities of grouping in Power BI visuals using various DAX measures. By exploring functions such as ALL, ALLSELECTED, ALLEXCEPT, and REMOVEFILTER, you’ll learn how to efficiently manage and manipulate your data for better insights. Grouping in Power BI is a crucial skill that can enhance your data analysis, making it more dynamic and insightful. If you’re eager to learn more about Power BI, visit our [training page](https://databear.com/power-bi-training/) to expand your knowledge and skills.

## Introduction to Grouping in Power BI

I have a Power BI report loaded with Adventure Works data. This dataset includes various sales territory groups, countries, and regions. Our goal is to display total sales across different regions and groups. For instance, we want to see total sales for Europe, North America, and the Pacific, and further drill down to countries and regions. This approach is useful for calculating percentages of totals, comparisons, or other analytical purposes.

### Creating a Measure for Total Sales

Let’s start with a basic example by creating a measure for total sales across all items. Here’s how we can do it:

1. **Create a New Measure:** Right-click on the table and select “New Measure.”
2. **Naming the Measure**: Call it “Total Sales Global” to indicate it encompasses all sales.
3. **Simple SUM Function:** Use the formula SUM(Sales\[SalesAmount\]). This will sum up the sales amounts without changing any filter context.

The result is a column displaying the same total sales value for every line item.

![Creating a Measure for Total Sales](99.System/Attachments/Creating_a_Measure_for_Total_Sales.png)

### Grouping Sales Using the ALL Function

Next, we want to group all sales by removing filters using the ALL function. Here’s the step-by-step process:

1. **Modify Filter Context:** Use the CALCULATE function combined with ALL.
2. **ALL Function:** This function returns all rows in a table, ignoring any filters.
3. **Apply to Sales Territory Table:** Use ALL(SalesTerritory) to ignore all filters from the sales territory table.

This measure will display the total sales value across every line item, regardless of the filters applied.

### Grouping Sales by Country

To group sales by country, we remove region-level filters:

1. **New Measure:** Create a measure named “Total Sales by Country.”
2. **Calculate Function:** Use CALCULATE(SUM(Sales\[SalesAmount\]), ALL(SalesTerritory\[Region\])).
3. **Group by Country:** This measure will show total sales for each country, aggregating regions within each country.

![Grouping Sales by Country](99.System/Attachments/Grouping_Sales_by_Country.png)

### Grouping Sales by Group

For grouping sales by larger groups (e.g., regions and countries), we need to remove filters from multiple columns:

1. **New Measure:** Create “Total Sales by Group.”
2. **Remove Multiple Columns:** Use CALCULATE(SUM(Sales\[SalesAmount\]), ALL(SalesTerritory\[Region\]), ALL(SalesTerritory\[Country\])).

This approach removes filters from both the region and country columns.

![Grouping Sales by Group](99.System/Attachments/Grouping_Sales_by_Group.png)

### Using ALLEXCEPT for Flexibility

To future-proof our measures and handle additional columns, we use the ALLEXCEPT function:

1. **New Measure:** Modify the “Total Sales by Group” measure.
2. **ALLEXCEPT Function:** Use CALCULATE(SUM(Sales\[SalesAmount\]), ALLEXCEPT(Sales, SalesTerritory\[Group\])).
3. **Exclude Specific Columns:** This measure removes filters from all columns except the specified one.

This approach ensures the measure remains accurate even if new columns are added to the visual.

![Using ALLEXCEPT for Flexibility](99.System/Attachments/Using_ALLEXCEPT_for_Flexibility.png)

### Handling Slicer Selections with ALLSELECTED

When slicer selections are applied, we want our measure to respect these selections. Use the ALLSELECTED function:

1. **New Measure:** Create “Total Sales Global 2.”
2. **ALLSELECTED Function:** Use CALCULATE(SUM(Sales\[SalesAmount\]), ALLSELECTED(SalesTerritory\[Group\])).

This measure adjusts based on the slicer selections, showing totals only for the selected groups.

![Handling Slicer Selections with ALLSELECTED](99.System/Attachments/Handling_Slicer_Selections_with_ALLSELECTED.png)

### Difference Between REMOVEFILTER and ALL

The REMOVEFILTER function is similar to ALL but has distinct uses:

1. **REMOVEFILTER:** Removes filters within the CALCULATE function without generating entire tables.
2. **ALL Function:** Can return entire tables and has broader applicability.

Both functions are useful, but ALL offers more versatility in different contexts.

![Difference Between REMOVEFILTER and ALL](99.System/Attachments/Difference_Between_REMOVEFILTER_and_ALL.png)

### Conclusion

Grouping in Power BI using DAX measures like [ALL, ALLSELECTED, ALLEXCEPT, and REMOVEFILTER](https://databear.com/all-allselected-and-allexcept-dax-filter-function/) allows for flexible and powerful data analysis. With these techniques, you can create dynamic and insightful reports that cater to various analytical needs.