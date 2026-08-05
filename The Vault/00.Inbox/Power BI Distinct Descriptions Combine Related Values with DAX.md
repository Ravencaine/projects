---
title: "Power BI Distinct Descriptions: Combine Related Values with DAX"
source: "https://databear.com/power-bi-distinct-descriptions/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-03-16
created: 2026-08-04
description: "Learn to use DAX in Power BI to return distinct task descriptions from related tables using CONCATENATEX and DISTINCT."
Processed: "Unprocessed"
---
One of the most common Power BI challenges is displaying **Power BI distinct descriptions** from related tables especially when each row in your report needs a clean, de-duplicated summary of associated details. In this post, you’ll learn how to solve that exact problem using DAX functions like `CONCATENATEX`, `DISTINCT`, and `SUMMARIZE`.

##### The Scenario: Order Headers and Task Details

Let’s set the stage. Imagine you have:

- An **Order Header** table with one row per order.
- An **Order Details** table with multiple task items per order.

Each row in the Order Details table contains:

- A task ID
- A task description

The goal? **To display a distinct, concatenated list of task descriptions** in each row of the Order Header table.

##### Step 1: Understand the Data Model

The `Order Header` and `Order Details` tables are connected via the `Order Number`. This is a one-to-many relationship, where one order has many task details.

You’ll create a **calculated column** in the `Order Header` table to return the task descriptions for each order.

##### Step 2: Use RELATEDTABLE to Bring in Related Rows

To get all related rows from the `Order Details` table, use:

```
RELATEDTABLE('Order Details')
```

This function returns all rows related to each order from the `Order Header` table. You can use this as the base for iteration.

##### Step 3: Combine Descriptions with CONCATENATEX

Now iterate over the related rows and concatenate the task descriptions:

```
Task Description =
CONCATENATEX(
    RELATEDTABLE('Order Details'),
    'Order Details'[Task Description],
    " | "
)
```

This creates a pipe-delimited string of all task descriptions for each order. But there’s one problem: **duplicates**.

##### Step 4: Remove Duplicates with SELECTCOLUMNS + DISTINCT

##### \<img loading="lazy" decoding="async" class="aligncenter wp-image-49125 size-full" src="https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-183911.png" alt="Combine Descriptions with CONCATENATEX" width="1050" height="494" srcset="https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-183911.png 1050w, https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-183911-300x141.png 300w, https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-183911-1024x482.png 1024w, https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-183911-150x71.png 150w" sizes="(max-width: 1050px) 100vw, 1050px" />

To return only unique task descriptions, wrap your table expression in `SELECTCOLUMNS` and `DISTINCT`:

```
Task Description Distinct =
CONCATENATEX(
    DISTINCT(
        SELECTCOLUMNS(
            RELATEDTABLE('Order Details'),
            "Description", 'Order Details'[Task Description]
        )
    ),
    [Description],
    " | "
)
```

##### Explanation:

- `SELECTCOLUMNS`: Returns only the `Task Description` column.
- `DISTINCT`: Ensures repeated descriptions are removed.
- `CONCATENATEX`: Combines the unique values into a single text string.

This version meets the user’s goal: **a clean, readable list of unique task descriptions per order.**

##### Bonus: Using SUMMARIZE as an Alternative

Prefer SQL-style thinking? You can also use the `SUMMARIZE` function to achieve the same result:

```
Task Description Grouped =
CONCATENATEX(
    SUMMARIZE(
        'Order Details',
        'Order Details'[Task Description]
    ),
    'Order Details'[Task Description],
    " | "
)
```

`SUMMARIZE` implicitly returns a distinct list of the specified column, removing duplicates without needing `DISTINCT`.

##### When to Use Each Method

- **`SELECTCOLUMNS` + `DISTINCT`**: Great for flexibility and renaming columns.
- **`SUMMARIZE`**: Ideal if you’re used to SQL-style `GROUP BY` logic.
- **`RELATEDTABLE` + `CONCATENATEX`**: Best for simple use cases without duplicate values.

Each approach works choose the one that best suits your model and personal style.

##### Real-World Tip

This technique is powerful when building customer-facing reports where clarity and precision matter. By showing a clean list of distinct tasks, you improve user experience and avoid confusion.

Want to level up your DAX skills even more? Check out [Data Bear’s Power BI Training](https://databear.com/power-bi-training/) for hands-on, real-world lessons in DAX, modeling, and report design.

##### Conclusion

Whether you’re creating operational dashboards or executive summaries, presenting **Power BI distinct descriptions** ensures your visuals are clean, accurate, and user-friendly especially when working with complex one-to-many data relationships