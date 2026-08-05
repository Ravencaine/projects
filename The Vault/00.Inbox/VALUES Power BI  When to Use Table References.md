---
title: "VALUES Power BI | When to Use Table References"
source: "https://databear.com/values-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-10-29
created: 2026-08-04
description: "Learn how to use VALUES in Power BI DAX to handle blank rows, fix invalid relationships, and improve report accuracy."
Processed: "Unprocessed"
---
When working with DAX, you’ve likely used `VALUES` or `DISTINCT` to get unique values from a column. But did you know that you can also use **VALUES with a table reference in [Power BI](https://databear.com/power-bi-restaurant-dashboard/ "Power BI Restaurant Dashboard: Build a Full Solution")**?

This use case often appears when you need to handle **blank rows** created by invalid relationships or when performing **context transitions** inside iterators such as `SUMX`, `MAXX`, or `AVERAGEX`.

In this guide, we’ll explore:

- What happens when you use a table reference directly versus using `VALUES`
- Why blank rows appear and how they affect totals
- When to use each approach for accurate and efficient results

##### Understanding Invalid Relationships and Blank Rows

In a typical **one-to-many relationship** (for example, **Customer → Sales**), Power BI ensures data consistency by linking customer records to their transactions.

However, when the **Sales** table contains customer keys that **don’t exist** in the **Customer** table, Power BI creates a **blank row** on the one side (Customer). This row groups all transactions from unknown customers into a single “blank” entry.![Understanding Invalid Relationships and Blank Rows](99.System/Attachments/Understanding_Invalid_Relationships_and_Blank_Rows.png)

This behavior ensures totals remain accurate but only if your DAX expressions include that blank row.

##### Table References vs. VALUES in DAX

When you iterate a table directly (for example, `SUMX(Customer, …)`), Power BI iterates over **existing customers only**, excluding the blank one.

That means any sales linked to the blank row representing unmatched customers will be left out of your calculation. As a result, your totals will be smaller than expected.

Here’s the key difference:

| Expression | Includes Blank Row? | Description |
| --- | --- | --- |
| `Customer` (table reference) | No | Iterates only existing customers |
| `VALUES(Customer)` | Yes | Iterates all customers, including blank row |

##### Practical Example: The Net Cashback Measure

Imagine you need a measure that applies a cashback rate to each customer’s sales.

If you iterate directly over `Customer`, your calculation might miss unknown customers causing a total mismatch.

To fix this, use `VALUES(Customer)` inside your iterator, ensuring that the blank customer (and related sales) are included in your computation.

```
Net Cashback :=
SUMX(
    VALUES(Customer),
    [Sales Amount] * (1 - Customer[Cashback %])
)
```

This approach ensures totals are accurate because every transaction, even those tied to unknown customers, is represented in the iteration.![Practical Example: The Net Cashback Measure](99.System/Attachments/Practical_Example!_The_Net_Cashback_Measure.png)

##### When to Use VALUES Over a Table Reference

You should use **VALUES with a table reference in Power BI** when:

1. The table is on the **one** side of a one-to-many relationship.
2. There might be an **invalid relationship** (unmatched keys).
3. Your expression includes a **context transition** (e.g., `CALCULATE`, `RELATEDTABLE`, or a measure reference).

In these situations, `VALUES` ensures the blank row is part of the iteration, maintaining accurate totals.

However, don’t overuse it. Adding `VALUES` unnecessarily can slightly impact performance, especially on large models.

##### When NOT to Use VALUES

There are cases where using `VALUES` is **not appropriate** particularly when you want to avoid grouping everything under a blank row.

For example, when calculating:

- `MAXX(Customer, [Sales Amount])`
- `MINX(Customer, [Sales Amount])`
- `AVERAGEX(Customer, [Sales Amount])`

In these cases, using `VALUES(Customer)` would create a single blank customer representing the sum of all unknown transactions, distorting your results.

Instead, iterate directly over the table reference (`Customer`) to exclude that row:

```
Max Customer Sales :=
MAXX(Customer, [Sales Amount])<img decoding="async" class="aligncenter wp-image-45900 size-full" src="https://databear.com/wp-content/uploads/2025/10/Screenshot-2025-10-26-131444.png" alt="When NOT to Use VALUES" width="667" height="522" srcset="https://databear.com/wp-content/uploads/2025/10/Screenshot-2025-10-26-131444.png 667w, https://databear.com/wp-content/uploads/2025/10/Screenshot-2025-10-26-131444-300x235.png 300w, https://databear.com/wp-content/uploads/2025/10/Screenshot-2025-10-26-131444-150x117.png 150w" sizes="(max-width: 667px) 100vw, 667px" />
```

##### Best Practices and Recommendations

- Use `VALUES` only when you **need** to include blank rows for completeness.
- For additive measures (like `SUMX`), `VALUES` can help ensure accuracy.
- For statistical or aggregation measures (`MAXX`, `MINX`, `AVERAGEX`), use the **table reference** directly.
- Prefer iterating over **columns** rather than entire tables for better performance.
- Always test your totals large discrepancies can reveal missing blank rows or relationship issues.

##### Conclusion

Using **VALUES with a table reference in Power BI** is an advanced yet crucial DAX technique. It ensures that blank rows from invalid relationships are included when necessary, helping maintain accurate totals and consistent data interpretation.

However, use it thoughtfully not every measure needs it. Understanding when to use `VALUES` versus a direct table reference will help you write cleaner, faster, and more reliable DAX code.

For deeper insights and hands-on learning, explore:  
[**Power BI Training with Data Bear**](https://databear.com/power-bi-training/)