---
title: "VALUES with SUMMARIZE Power BI"
source: "https://databear.com/values-with-summarize-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-10-31
created: 2026-08-04
description: "Learn VALUES with SUMMARIZE in Power BI DAX. Handle blank rows, improve accuracy, and apply best practices for faster, cleaner reports."
Processed: "Unprocessed"
---
In this post, we’ll explore **VALUES with SUMMARIZE in Power BI**, a DAX combination that often confuses even experienced modelers. Understanding how and when to use `VALUES` with `SUMMARIZE` in [Power BI](https://databear.com/trace-power-bi-report-in-service/ "Trace Power BI Report: Debug Performance Using Browser Tools") is essential for managing blank rows, optimizing relationships, and ensuring accurate calculations in your reports.

You’ll learn:

- When the `VALUES` function is required inside `SUMMARIZE`
- How one-to-many relationships affect results
- Why `SUMMARIZECOLUMNS` is often a better choice
- Best practices for performance and accuracy

By the end, you’ll understand how to avoid common mistakes and write DAX expressions that are both efficient and reliable.

##### Recap: One-to-Many Relationships and Blank Rows

When working with **VALUES with SUMMARIZE in Power BI**, it’s important to recall how relationships behave. In one-to-many relationships for instance, between *Customer* and *Sales* unmatched keys can generate blank rows.

If a `CustomerKey` exists in the **Sales** table but not in **Customer**, Power BI inserts a **blank row** in the **Customer** table. Whether that blank row appears in your DAX results depends on how you reference the table inside `SUMMARIZE` or whether you use the `VALUES` function.

##### Using SUMMARIZE and Table References

Consider a [DAX measure](https://databear.com/3-easy-steps-to-write-dax-measure/ "Steps to Write DAX Measure in Power BI") where you group transactions by **State** and **City** to apply a specific business rule. For instance, you might apply a 99% adjustment to sales made in **Columbus, Ohio**, while keeping other cities at 100%.

You might start with a measure like this:

```
Sales Adjusted :=
SUMX(
    SUMMARIZE(
        Sales,
        Customer[State],
        Customer[City]
    ),
    IF(
        Customer[State] = "Ohio" && Customer[City] = "Columbus",
        [Sales Amount] * 0.99,
        [Sales Amount]
    )
)
```

In this case, since the table referenced in `SUMMARIZE` is **Sales** (the “many” side of the relationship), any blank rows automatically appear. This means you don’t need to use the `VALUES` function it’s already handled correctly.![Using SUMMARIZE and Table References](99.System/Attachments/Using_SUMMARIZE_and_Table_References.png)

##### When the Blank Row Disappears: Using the “One” Side

However, if you change your table reference to the **Customer** table, things work differently:

```
SUMMARIZE(
    Customer,
    Customer[State],
    Customer[City]
)
```

Now, since **Customer** is on the **one** side of the relationship, it doesn’t include the blank row by default. This means some transactions may not be included in the results leading to inaccurate totals.

You might notice that your **Grand Total** becomes smaller than expected. That’s because Power BI isn’t including transactions linked to the blank customer row.

To fix this, you can wrap the table reference in a `VALUES` function:

```
SUMMARIZE(
    VALUES(Customer),
    Customer[State],
    Customer[City]
)
```

By using `VALUES(Customer)`, you’re telling Power BI to include the blank row ensuring your calculation reflects all transactions accurately.![When the Blank Row Disappears: Using the “One” Side](99.System/Attachments/When_the_Blank_Row_Disappears!_Using_the_“One”_Side.png)

##### Performance Considerations

While using `VALUES(Customer)` works, it’s not always the best option. If your **Sales** table has billions of rows and **Customer** has only thousands, summarizing **Customer** might be faster.

However, if performance isn’t an issue, it’s usually safer and simpler to use the **Sales** table directly in your `SUMMARIZE` expression. This approach automatically handles blank rows and ensures full coverage of your dataset.

##### The Modern Approach: Using SUMMARIZECOLUMNS

Today, it’s often better to use `SUMMARIZECOLUMNS` instead of `SUMMARIZE`. This function provides more predictable results and follows current DAX best practices.

Here’s an example:

```
SUMMARIZECOLUMNS(
    Customer[State],
    Customer[City],
    "Sales Amount", [Sales Amount]
)
```

A few best practices when using `SUMMARIZECOLUMNS`:

- Always include **at least one aggregation**, such as `COUNTROWS(Sales)` or `SUM(Sales[Amount])`.
- Avoid using `SUMMARIZECOLUMNS` without an aggregation it can behave unexpectedly in some models.
- Use it within a measure to ensure predictable and optimized performance.

This approach ensures that your calculation includes the correct blank rows and produces reliable results across your [Power BI reports](https://databear.com/report-design-ideas-in-power-bi/ "Report Design Ideas in Power BI").![The Modern Approach: Using SUMMARIZECOLUMNS ](99.System/Attachments/The_Modern_Approach!_Using_SUMMARIZECOLUMNS_.png)

##### Key Takeaways

- Use **`VALUES`** with **`SUMMARIZE`** only when referencing a table on the **one** side of a relationship and you need to include the blank row.
- When referencing a table on the **many** side (like **Sales**), **you don’t need `VALUES`** blank rows are already included.
- Prefer **`SUMMARIZECOLUMNS`** for clarity, predictability, and best practices in modern DAX.
- Always include an **aggregation** when using `SUMMARIZECOLUMNS` inside a measure.
- Be aware of **performance trade-offs** summarizing large tables can be costly.

##### Conclusion

While the need to use `VALUES` with `SUMMARIZE` in Power BI is relatively rare, understanding **when and why** to use it is crucial for writing robust DAX expressions.  
In most cases, referencing the **many** side of a relationship or using **`SUMMARIZECOLUMNS`** will give you the results you need without the complexity.

For deeper learning and hands-on [Power BI training](https://databear.com/what-is-power-bi-training-and-what-skills-will-you-learn/ "What is Power BI Training, and What Skills Will You Learn?"), check out  
[**Data Bear’s Power BI Training**](https://databear.com/power-bi-training/)