---
title: "Best Practices for Using Explicit Measures in Power BI"
source: "https://medium.com/@simon.harrison_Select_Distinct/best-practices-for-using-explicit-measures-in-power-bi-f23d60b7cbcd"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2024-09-19
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
(Part 2 of a 2 part post about modelling in Power BI)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*TwKf2y8EdCmHsUnroSyqrg.png)

In our previous post we explained the differences between implicit and explicit measures  
[Understanding Implicit and Explicit Measures in Power BI](https://www.selectdistinct.co.uk/2024/09/12/implicit_explicit_measures_power_bi/)

This post builds on that and explains some best practices for using explicit measures

## Tips for Creating Effective Explicit Measures

**Use Descriptive and Meaningful Names**:

- Give your measures clear and descriptive names that reflect their purpose. This makes it easier to understand and maintain your data model.
- Example: Instead of naming a measure “Total,” use “Total Sales” or “Total Revenue.”

**Keep Formulas Simple and Readable**:

- Write DAX formulas that are easy to read and understand. Break down complex calculations into smaller, manageable parts.
- Use comments within your DAX code to explain the logic, especially for more complex measures.

**Optimize for Performance**:

- Avoid using resource-intensive functions like FILTER and EARLIER unless necessary. Instead, use more efficient alternatives like CALCULATE and SUMX.
- Test and validate your measures to ensure they perform well with large datasets.

**Understand Data Types and Relationships**:

- Be aware of the data types of your columns and how they interact with each other. This helps prevent errors and ensures accurate calculations.
- Ensure that relationships between tables are correctly defined to avoid unexpected results.

**Use Variables for Clarity and Efficiency**:

- Use variables (VAR) to store intermediate results within your DAX formulas. This not only makes your code cleaner but can also improve performance.
- Example:
- Total Sales =
- VAR SalesAmount = SUM(Sales\[SalesAmount\])
- RETURN SalesAmount

**Handle Errors and Blanks Gracefully**:

- Use functions like IF, ISBLANK, and COALESCE to handle errors or blanks in your data.
- This ensures your measures return meaningful results even when data is missing or incorrect.

**Test and Validate Measures**:

- Regularly test your measures to ensure they produce the expected results. Use sample data and different scenarios to validate your calculations.
- Create visualizations to check how your measures behave under various filters and conditions.

**Document Your Measures**:

- Maintain documentation for your measures, including their purpose, logic, and any assumptions made. This is especially useful for collaboration and future maintenance.

**By following these tips, you can create explicit measures that are not only effective but also efficient and easy to maintain**

## Common pitfalls to avoid when transitioning from implicit to explicit measures

**Not Understanding DAX Syntax:**

- Pitfall: Jumping into creating explicit measures without a solid understanding of DAX (Data Analysis Expressions) can lead to errors and inefficiencies.
- Solution: Take the time to learn DAX basics and practice writing simple formulas before tackling more complex calculations.

**Overcomplicating Measures:**

- Pitfall: Creating overly complex measures when simpler solutions would suffice can make your data model harder to maintain and understand.
- Solution: Start with simple measures and gradually build complexity as needed. Use variables (VAR) to break down complex calculations into manageable parts.

**Ignoring Performance Implications:**

- Pitfall: Writing inefficient DAX formulas that can slow down report performance, especially with large datasets.
- Solution: Optimize your DAX code by avoiding resource-intensive functions and using more efficient alternatives. Test your measures with large datasets to ensure they perform well.

**Not Documenting Measures:**

- Pitfall: Failing to document the purpose and logic of your measures can lead to confusion and errors, especially in collaborative environments.
- Solution: Use descriptive names for your measures and add comments within your DAX code to explain the logic and purpose.

**Inconsistent Naming Conventions:**

- Pitfall: Using inconsistent naming conventions for your measures can make it difficult to understand and manage your data model.
- Solution: Establish and follow a consistent naming convention for all your measures. This helps maintain clarity and organization.

**Not Testing Measures Thoroughly:**

- Pitfall: Assuming that your measures are correct without thorough testing can lead to incorrect results and insights.
- Solution: Regularly test your measures with different data scenarios and visualizations to ensure they produce accurate and expected results.

**Overlooking Data Types and Relationships:**

- Pitfall: Ignoring the importance of data types and relationships between tables can result in incorrect calculations and unexpected behavior.
- Solution: Ensure that data types are correctly defined and relationships between tables are properly set up to support accurate calculations.

By being aware of these common pitfalls and taking steps to avoid them, you can make a smoother transition from implicit to explicit measures and enhance the quality and performance of your Power BI reports

## Recommendations for Maintaining a Clean and Efficient Data Model

**Understand Your Data**:

- **Data Profiling**: Conduct data profiling to understand the structure, quality, and relationships within your data. This helps identify any issues that need to be addressed before modeling1.
- **Data Cleansing**: Remove duplicates, correct errors, and handle missing values to ensure data quality.

**Use a Star Schema**:

- **Star Schema Design**: Organize your data into fact and dimension tables. This simplifies relationships and improves query performance.
- **Avoid Snowflake Schema**: While sometimes necessary, snowflake schemas can complicate relationships and slow down performance

**Optimize Data Types**:

- **Appropriate Data Types**: Use the most appropriate data types for your columns. This can reduce memory usage and improve performance.
- **Reduce Cardinality**: Minimize the number of unique values in columns where possible to enhance performance.

**Manage Relationships Effectively**:

- **Define Clear Relationships:** Ensure relationships between tables are correctly defined and use single-directional relationships where possible to avoid ambiguity.
- **Avoid Circular Dependencies:** Circular relationships can cause performance issues and make the model harder to understand.

**Use Measure Tables**:

- **Centralize Measures**: Create dedicated measure tables to store all your DAX measures. This keeps your model organized and makes it easier to manage calculations.

**Limit the Use of Calculated Columns**:

- **Prefer Measures Over Calculated Columns**: Use measures instead of calculated columns whenever possible, as measures are calculated on the fly and do not consume additional memory.
- **Optimize Calculated Columns:** If you must use calculated columns, ensure they are optimized for performance.

**Hide Unnecessary Columns and Tables**:

- **Reduce Clutter**: Hide columns and tables that are not needed for reporting. This simplifies the data model and improves performance.
- Use Descriptive Names: Rename columns and tables with meaningful names to make the model more intuitive.

**Implement Data Validation Rules**:

- **Enforce Data Integrity:** Define and implement data validation rules to ensure data consistency and accuracy.

**Regularly Review and Optimize**:

- **Performance Monitoring:** Regularly review the performance of your data model and make necessary optimizations.
- **Update and Refine:** Continuously update and refine your data model as your data and reporting needs evolve

By following these recommendations, you can maintain a clean, efficient, and high-performing data model in Power BI.

## Real World Benefits of adopting Explicit Measures in Power BI

You have seen some examples of how explicit measures can be used to enforce better reporting disciplines across your reports

In many organisations there are efforts made to centralise and standardise the business calculations, often these are documented rigorously and quality standards checked and enforced

you can find some examples of explicit measures and how to create them here

[Comparing Year on Year in Power BI — Select Distinct](https://www.selectdistinct.co.uk/2024/04/16/year-on-year-power-bi/)

[SAMEPERIODLASTYEAR in Power BI — Select Distinct Limited](https://www.selectdistinct.co.uk/2023/06/08/sameperiodlastyear-in-power-bi/)

Or you can visit our YouTube Channel to see our videos

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful SQL, Power BI or other business analytics timesavers in our Blog

Our Business Analytics [Timesavers](https://www.selectdistinct.co.uk/category/tips-timesavers/) are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

By [Simon Harrison](https://www.selectdistinct.co.uk/about-select-distinct-limited/simon-harrison-select-distinct/)

This article is published in our blog  
[Best Practices for Using Explicit Measures in Power BI — Select Distinct](https://www.selectdistinct.co.uk/2024/09/19/best-practice-explicit-measures-in-power-bi/)