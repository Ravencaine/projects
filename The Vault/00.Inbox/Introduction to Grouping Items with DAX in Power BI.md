---
title: "Introduction to Grouping Items with DAX in Power BI"
source: "https://databear.com/introduction-to-grouping-items-with-dax-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-07-20
created: 2026-08-04
description: "Discover how to grouping items with DAX in Power BI using DAX functions like ALL, ALLSELECTED, ALLEXCEPT, and REMOVEFILTER. Perfect for enhancing your data analysis skills."
Processed: "Unprocessed"
---
Grouping different items together in Power BI visuals using DAX measures can significantly enhance data analysis and reporting. By mastering measures such as ALL, ALLSELECTED, ALLEXCEPT, and REMOVEFILTER, you can create dynamic and insightful reports that cater to specific analytical needs.

### Getting Started with DAX in Power BI

To demonstrate these techniques, let’s use a Power BI report featuring Adventure Works data. This dataset is a standard one that many users can access and utilize. It includes various sales territory groups, countries, and regions, displayed with total sales figures. The Adventure Works dataset provides a comprehensive set of sales data, allowing us to showcase various grouping techniques effectively.

### Understanding the Basics: Total Sales Global Measure

A common task in data analysis is displaying the total sales across all countries, groups, and regions. To achieve this, you can create a measure called `Total Sales Global`. This measure will show the same total sales value across every line item in a visual, providing a benchmark or a total reference point.

`Total Sales Global = CALCULATE(SUM('Sales'[SalesAmount]), ALL('SalesTerritory'))   `

By using the `ALL` function, you ignore any filters that might be applied, ensuring that the measure represents the global total sales.

![Total Sales Global Measure](99.System/Attachments/Total_Sales_Global_Measure.png)

### Grouping Sales by Country

Analyzing total sales by country can provide valuable insights. To do this, create a measure called `Total Sales by Country`, which removes the filter context for regions, allowing you to view sales aggregated at the country level.

`Total Sales by Country = CALCULATE(SUM('Sales'[SalesAmount]), ALL('SalesTerritory'[Region]))   `

This measure helps you understand sales distribution across countries by eliminating the region-specific filters. It is particularly useful for high-level management reporting and comparative analysis.

![Grouping Sales by Country](99.System/Attachments/Grouping_Sales_by_Country-1.png)

### Grouping Sales by Group

To group sales by territory group, remove filters from both the region and country columns. This can be done as follows:

`Total Sales by Group = CALCULATE(SUM('Sales'[SalesAmount]), ALL('SalesTerritory'[Region]), ALL('SalesTerritory'[Country]))   `

This approach ensures that the measure reflects the total sales aggregated by territory group, providing a broader perspective on sales distribution across larger geographical areas.

### Future-Proofing with ALLEXCEPT

To make measures more flexible and robust, use the `ALLEXCEPT` function. This function removes all filters except for the specified column, ensuring that the measure adapts to changes in the filter context.

`Total Sales by Group = CALCULATE(SUM('Sales'[SalesAmount]), ALLEXCEPT('Sales', 'SalesTerritory'[Group]))   `

Using `ALLEXCEPT` helps future-proof measures, ensuring they are resilient and reliable for long-term use, regardless of how the filter context changes.

### Using ALLSELECTED for Slicer Selections

When working with slicers, it’s important to create measures that respect slicer selections while calculating totals. The `ALLSELECTED` function can be used to achieve this.

`Total Sales Global 2 = CALCULATE(SUM('Sales'[SalesAmount]), ALLSELECTED('SalesTerritory'[Group]))   `

The `ALLSELECTED` function allows measures to dynamically respond to user interactions with slicers, providing a more interactive and user-friendly reporting experience.

![Future-Proofing with ALLEXCEPT Grouping Items with DAX in Power BI](99.System/Attachments/Future-Proofing_with_ALLEXCEPT_Grouping_Items_with_DAX_in_Power_BI.png)

### REMOVEFILTER vs. ALL

Understanding the difference between `REMOVEFILTER` and `ALL` is crucial. Both functions are similar, but `REMOVEFILTER` only removes filters in a `CALCULATE` function, whereas `ALL` can return an entire table if needed.

`Total Sales by Country = CALCULATE(SUM('Sales'[SalesAmount]), REMOVEFILTERS('SalesTerritory'[Region]))   `

While `REMOVEFILTER` is useful for straightforward scenarios, `ALL` offers more versatility, especially when returning an entire table or working with more complex filter contexts.

### Conclusion

Grouping items using DAX measures in Power BI allows for powerful and flexible data analysis. By understanding and utilizing functions like ALL, ALLSELECTED, ALLEXCEPT, and REMOVEFILTER, you can create dynamic and insightful reports. These techniques enhance analytical capabilities and ensure that reports remain robust and adaptable to changing requirements.

Whether you are a beginner or an experienced Power BI user, mastering these DAX functions will significantly improve your data analysis skills. Experiment with these functions in your reports and see how they can transform your data insights.

Want to learn more about Power BI? Visit [Power BI training](https://databear.com/power-bi-training/)