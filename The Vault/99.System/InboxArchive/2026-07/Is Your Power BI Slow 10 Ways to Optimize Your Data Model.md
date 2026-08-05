---
title: "Is Your Power BI Slow? 10 Ways to Optimize Your Data Model📊🚀"
source: "https://medium.com/microsoft-power-bi/is-your-power-bi-slow-10-ways-to-optimize-your-data-model-6f3cc2f98398"
author:
  - "[[Janvi Gupta]]"
published: 2025-02-20
created: 2026-07-27
description: "Featured"
Processed: "Unprocessed"
---
Learn how to optimize your Power BI data model for peak performance and create lightning-fast reports that impress.😊

> 🎖️ Article was awarded as **Must-Read** by [**Power BI Masterclass community**](https://linktr.ee/powerbi.masterclass).

![](99.System/Attachments/0!wmrqUS4tqXwp7f-R.webp)

Let’s be honest, sometimes Power BI feels slow. Your reports lag,😞 dashboards take ages to load, and you’re left tapping your fingers, waiting for those insights. Often, the culprit is a poorly optimized data model.

Think of it as the engine of your Power BI reports — if the engine’s clogged, the whole thing runs rough. But you don’t need to be a mechanic to fix it!👨🔧 This post offers 10 simple tune-ups 🦾to get your reports running smoothly. ✨

> ***Free Access: This blog post is accessible to everyone, even non-Medium members, through this friend link👉*** [***https://medium.com/microsoft-power-bi/is-your-power-bi-slow-10-ways-to-optimize-your-data-model-6f3cc2f98398?sk=f5f7a5970696321ee467067e94108edd***](https://medium.com/microsoft-power-bi/is-your-power-bi-slow-10-ways-to-optimize-your-data-model-6f3cc2f98398?sk=f5f7a5970696321ee467067e94108edd)

## 1\. Clean Data Model: Remove Unused Columns and Tables 🗑️

![](99.System/Attachments/0!oCTR6mI3NvRTMvgv.png.webp)

Imagine a kitchen crammed with gadgets you never use. It’s cluttered and makes finding what you need a pain. A cluttered data model is not different. Start by identifying and removing any tables or columns that aren’t used in your reports.

If you’re analyzing sales, you probably don’t need employee addresses or phone numbers in your model. This is a quick win for reducing model size and improving performance.

- **How to find unused elements:** Utilize external tools like “Bravo” or the “Power BI Helper” to pinpoint unused columns and tables. These tools offer clear visualizations of model usage, making it easy to spot areas for improvement. Alternatively, you can manually review your report elements and trace back to the source data, noting which tables and columns are actually being used.

## 2\. Aggregate for Efficiency: Reduce Row Count without Sacrificing Insights 📊

![](99.System/Attachments/0!nVuksEcpbpa5bzhO.png.webp)

If your reports only require summarized data (e.g., sales by state and month), there’s no need to store every single transaction detail. ==Aggregate your data to the necessary level of granularity using Power Query’s “Group By” feature.== This drastically reduces the number of rows in your model, leading to significant performance gains.

- **Example:** Instead of storing 200,000 individual sales transactions, aggregate the sales amount by state and month, reducing the row count to a more manageable level (e.g., 1,500 rows). This still allows for the same visualizations while significantly shrinking your model size.
- **Caveat:** While aggregation improves performance, it can limit drill-down capabilities. If you need to drill down to transaction-level details, consider alternative approaches like drillthrough reports.

## 3\. Take Charge of Time: Disable Auto Date/Time and Create a Dedicated Date Table 📅

![](99.System/Attachments/0!L3W1LkDqu0NI2IYZ.png.webp)

![](99.System/Attachments/0!Ah6T1eTMsFpA67Sb.png.webp)

Power BI’s “Auto Date/Time” feature, while convenient, can create hidden date tables that bloat your model. Disable this feature and create a single, dedicated date table. This provides more control over date-related calculations and significantly reduces storage space.

- **Benefits of a dedicated date table:** Besides saving space, a dedicated date table enables more complex date-based calculations, hierarchies (year, quarter, month), and time intelligence functions. It also ensures consistency in date formatting and avoids ambiguity in calculations.

## 4\. Organize Your Data: Use the Star Schema 🌟

![](99.System/Attachments/0!D5XDZztkaOhgTTUq.png.webp)

Organize your data model using a star schema. This tried-and-true design consists of a central fact table (containing your core metrics) connected to surrounding dimension tables (providing descriptive context).

Imagine a library with books scattered everywhere versus one with books neatly organized by category. The star schema is like that organized library. This structure simplifies queries and significantly improves performance compared to flat tables or highly normalized snowflake schemas.

- **Why not a snowflake schema?** While normalization is generally good for database design, in Power BI, excessive normalization can lead to more complex queries and decreased performance. The star schema offers the best balance between normalization and query efficiency.

## 5\. Combine Related Data: Merge One-to-One Relationships 🤝

![](99.System/Attachments/1!j1_bZjpZbHawDlNYO5XEqA.png.webp)

![](99.System/Attachments/1!aUxbtKBpgsl1R-sNHAmf0g.png.webp)

One-to-one relationships often indicate that the data could be combined into a single table. Merging related tables simplifies the data model, reducing unnecessary joins and boosting performance.

- **How to merge tables:** Utilize Power Query’s “Merge Queries” feature to combine tables based on a common column.

## 6\. Bidirectional Filters and Many-to-Many Relationships: Please Use with Caution⚠️

![](99.System/Attachments/0!CdoqJuh0QoBjFrH0.png.webp)

While bidirectional filters and many-to-many relationships can be useful for complex analyses, they can also introduce performance bottlenecks and ambiguity. Use them sparingly and only when absolutely necessary. Consider alternative approaches like creating calculated columns or measures to achieve similar results.

Bidirectional filters can be powerful, letting slicers on one table affect visuals on another. But they can also slow things down, especially with lots of data. Use them only when needed.

## 7\. Simplify for Speed: Reduce Cardinality 🗜️

![](99.System/Attachments/0!9lpfNi4a4gYYkg2N.png.webp)

![](99.System/Attachments/0!SInb2ibnOdZoaQlZ.png.webp)

Cardinality refers to the “ **number of unique values in a column** ”. High cardinality can lead to larger model sizes and slower performance. Whenever possible, reduce cardinality, especially in frequently filtered columns.

For example, if you only need the date, don’t store the entire date and time.

## 8\. Right-Size Your Data: Optimize Data Types 🔡

![Before Changing the DataType](99.System/Attachments/Before_Changing_the_DataType.webp)

Before Changing the Data Type

![](99.System/Attachments/0!3w7itkav2YPsiHMN.png.webp)

![](99.System/Attachments/0!Eu5-Gtjjv2VjB9-e.png.webp)

After Changing the Data Type

Choose the most efficient data type for each column. For instance, use “Date” instead of “DateTime” for datetimestap column. Smaller data types require less storage space and lead to faster processing.

## 9\. Work Smarter, Not Harder: Use Calculated Columns Strategically 🤔

![](99.System/Attachments/0!jEKXf-kcM9aMfIUt.jpg.webp)

Measures are usually better for calculations, but sometimes a calculated column can improve performance. Use calculated columns for data transformations that add context or descriptive information. Use measures for calculations and aggregations based on filters and slicers.

Measures are generally more efficient for dynamic calculations, while calculated columns are better for static transformations. Be mindful of the trade-offs and choose the best approach for your specific scenario.

## 10\. Fast or Fresh? Choose the Right Storage Mode ➡️

![](99.System/Attachments/0!QZZ1VFUUaqhyR-hL.webp)

Import mode brings the data into Power BI, making it fast but **requiring scheduled refreshes**. DirectQuery queries the data source live, offering up-to-the-minute data but **potentially slower performance**. Choose the best fit for your needs.

**Conclusion:**

Optimizing your Power BI data model is an ongoing process, but the rewards are significant. By following these ten steps, you can create lightning-fast reports that impress your users and provide valuable insights efficiently.

Remember, a well-optimized data model is the foundation of a successful Power BI solution. Now go forth and build those blazing-fast dashboards!!

Now it’s your turn! What other tips do you have? Share them below! 👇 And if you’re just starting out, don’t be afraid to ask questions — we’re all learning together! 😊

**Connect me on LinkedIn —** [**Janvi Gupta**](https://www.linkedin.com/in/janvisgupta/)

![](99.System/Attachments/0!DJj6flesjWEh5WEK.webp)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----6f3cc2f98398---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee