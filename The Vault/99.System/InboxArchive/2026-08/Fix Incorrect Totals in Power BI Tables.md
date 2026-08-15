---
title: "Fix Incorrect Totals in Power BI Tables"
source: "https://databear.com/how-to-fix-incorrect-totals-in-power-bi-tables/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-09-08
created: 2026-08-04
description: "Learn how to fix incorrect totals in Power BI tables and matrix visuals using DAX functions like SUMX and CALCULATE."
Processed: "Unprocessed"
---
When working with Power BI, one common issue you may encounter is that the incorrect totals in Power BI tables don’t always add up as expected. This can happen quite frequently, and while it may seem like an error, it’s actually due to how Power BI handles summarization. In this blog post, we’ll dive into why this happens, how to fix it using DAX, and what steps to follow to ensure your totals display correctly.

#### Why Do Totals Appear Incorrect in Power BI?

In Power BI, totals in a table or matrix visual might not behave as expected because the way the total row calculates values differs from how individual rows do. This is especially true when using certain aggregations like **Max**, **Min**, or **Average**. Power BI treats the total as a single evaluation that ignores row context, leading to unexpected results. Let’s walk through a simple example.

Imagine you are visualizing sales data broken down by categories. You’ve created a measure that calculates the maximum unit price per category. While the individual rows show the correct max value per category, the total row might not reflect what you expect—it could show a completely unrelated number. This discrepancy occurs because Power BI summarizes the maximum value across all categories, not within each category individually.

![Fix Incorrect Totals in Power BI ](99.System/Attachments/Fix_Incorrect_Totals_in_Power_BI_.png)

#### The Problem: Incorrect Totals for Max Unit Price

Let’s say you create a table that shows the maximum unit price per category using a DAX measure like:

Max Unit Price = MAX(OrderDetails\[UnitPrice\])

While this displays the correct maximum unit price per category in each row, the total row shows the maximum price across all categories, which is misleading.

#### Why Does This Happen?

Measures in Power BI lack **row context** when calculating the total. In other words, Power BI doesn’t recognize that you want the total to sum the maximum prices for each category. Instead, it calculates a single max value across all rows, ignoring the category breakdown.

#### The Solution: Fixing Totals Using DAX

To fix this issue, we need to guide Power BI to calculate the total correctly by leveraging the **SUMX** function and **context transition** with **CALCULATE**. Here’s how we do it:

#### Step 1: Create a New Measure Using SUMX

We need to create a new measure that ensures Power BI recognizes the row context for each category. This is done by using the **SUMX** function, which iterates through a table and evaluates an expression for each row, ensuring that Power BI respects the category grouping.

Max Unit Price Corrected =

SUMX(

SUMMARIZE(

Categories,

Categories\[CategoryName\],

“MaxPerCategory”, MAX(OrderDetails\[UnitPrice\])

),

\[MaxPerCategory\]

)

#### Step 2: Wrapping with CALCULATE for Context Transition

In Power BI, **context transition** is required to ensure that row-level context is carried over to the measure level. The **CALCULATE** function converts row context into filter context, ensuring that Power BI calculates the maximum for each category rather than across all categories at once.

Max Unit Price Corrected =

SUMX(

SUMMARIZE(

Categories,

Categories\[CategoryName\],

“MaxPerCategory”, CALCULATE(MAX(OrderDetails\[UnitPrice\]))

),

\[MaxPerCategory\]

)

#### Step 3: Applying the Corrected Measure to Your Table

Once the corrected measure is created, simply replace the old measure in your table or matrix visual with the new measure. The total row should now correctly display the sum of the maximum unit prices for each category.

#### Example 2: Fixing Incorrect Totals for Average Quantity

This approach can also be applied in other situations, such as when calculating an average. Imagine you have a matrix showing the **average quantity** sold per month. By default, the total row might display the average of all months instead of summing the averages for each month.

Here’s how you can fix this:

#### Step 1: Create a New Measure for Average Quantity

Avg Quantity Corrected =

SUMX(

SUMMARIZE(

Calendar,

Calendar\[Year\], Calendar\[Month\],

“AvgPerMonth”, CALCULATE(AVERAGE(OrderDetails\[Quantity\]))

),

\[AvgPerMonth\]

)

This measure ensures that Power BI calculates the average per month, then sums those averages in the total row.

#### Step 2: Apply the Measure to Your Visual

Once you create this corrected measure, use it in your matrix visual. You will now see correct subtotals for each year and a grand total that sums the averages for all months.

#### Conclusion

Incorrect totals in Power BI can be frustrating, but with a solid understanding of how DAX handles row and filter contexts, you can easily fix these issues. By using functions like **SUMX**, **CALCULATE**, and **SUMMARIZE**, you can ensure that Power BI correctly sums or averages values in total rows based on your table’s groupings.

#### Key Takeaways:

- Power BI often miscalculates totals because it lacks row context when calculating measures.
- Use **SUMX** with **SUMMARIZE** to instruct Power BI to iterate over groups (such as categories or months) and calculate totals correctly.
- **CALCULATE** ensures context transition, which is necessary for maintaining row-level calculations at the total level.

I hope this blog helps you resolve incorrect totals in Power BI!