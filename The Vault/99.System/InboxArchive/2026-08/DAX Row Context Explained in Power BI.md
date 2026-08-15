---
title: "DAX Row Context Explained in Power BI"
source: "https://databear.com/dax-row-context-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-03-13
created: 2026-08-04
description: "Learn DAX row context in Power BI with a clear visual explanation. Understand how iterators, column references work together to calculate"
Processed: "Unprocessed"
---
Understanding **DAX row context** is fundamental to mastering calculations in Power BI. While many developers grasp filter context first, row context is equally important for writing correct measures and calculated columns. In this guide, we break down DAX row context using clear, visual explanations and practical examples so you can confidently apply it in real-world models.

If you want structured, expert-led Power BI learning, [you can explore professional training](https://databear.com/power-bi-training/)

##### Evaluation Context in DAX: Row Context vs Filter Context

Before diving deeper, remember that DAX evaluation context has two primary components:

- Filter context
- Row context

Filter context determines which rows are visible for a calculation.  
Row context determines which single row is currently being evaluated.

In a previous discussion, filter context was described visually. Now, we focus on understanding row context in the same intuitive way.

##### What Is DAX Row Context?

DAX row context exists when a calculation is performed row by row over a table.

Consider a classic Contoso example with a Sales Amount measure:

```
Sales Amount =
SUMX(
    Sales,
    Sales[Quantity] * Sales[Net Price]
)
```

Two important elements appear here:

- Sales\[Quantity\]
- Sales\[Net Price\]

These are column references. A column reference means:  
“Give me the value of this column from the current row.”

But what is the current row?

That current row is defined by the row context.

##### Visualizing Row Context

Imagine a table with many rows and columns.

When an iterator function like SUMX scans a table:

1. It evaluates the first row.
2. Then the second row.
3. Then the third row.
4. And so on.

At each step, DAX creates a temporary conceptual table containing:

- All columns
- Only one row

This single-row structure represents the row context.

So if your Sales table has 3 visible rows, the iterator produces 3 separate row contexts, one for each row during iteration.

This is why column references work inside SUMX. The iterator creates the row context that makes “current row” meaningful.

##### When Does Row Context Exist?

Row context is created in two main scenarios:

1. Iterator functions (such as SUMX, AVERAGEX, ADDCOLUMNS)
2. Calculated columns

If you try to use a column reference in a measure without an iterator, and no row context exists, the expression fails.

For example, this works:

```
SUMX(Sales, Sales[Quantity] * Sales[Net Price])
```

But this would not:

```
Sales[Quantity] * Sales[Net Price]
```

Because there is no row context available.

##### How Row Context and Filter Context Work Together

Row context does not replace filter context. Both can exist simultaneously.

Here is the evaluation sequence:

1. Filter context determines which rows of Sales are visible.
2. The Sales table reference returns only those filtered rows.
3. SUMX iterates over those visible rows.
4. For each row, a row context is created.
5. Column references retrieve values from that current row.

Filter context limits the dataset.  
Row context evaluates each row individually.

They serve different purposes but combine to produce the final result.

##### Example: Using SELECTEDVALUE Inside an Iterator

Consider a measure that changes display scale based on a slicer selection:

```
SUMX(
    Sales,
    Sales[Quantity] * Sales[Net Price] /
    SELECTEDVALUE(Scale[Scale Value])
)
```

Here’s what happens:

- Sales\[Quantity\] and Sales\[Net Price\] use row context.
- SELECTEDVALUE reads from filter context.
- The slicer selection does not change during iteration.

Best practice: retrieve slicer values before iteration.

Improved version:

```
VAR Factor = SELECTEDVALUE(Scale[Scale Value])

RETURN
SUMX(
    Sales,
    Sales[Quantity] * Sales[Net Price] / Factor
)
```

This makes the code cleaner and avoids unnecessary repetition inside the iterator.

##### Cardinality Matters: Iterating Different Tables

The number of rows you iterate directly impacts results.

##### Example 1: SELECTCOLUMNS

```
VAR SalesProjection =
    SELECTCOLUMNS(
        Sales,
        "Quantity", Sales[Quantity],
        "Net Price", Sales[Net Price]
    )
```

SELECTCOLUMNS:

- Keeps the same number of rows
- Reduces the number of columns

If the original table has 3 rows, the new table still has 3 rows.

Iteration result remains the same.

##### Example 2: SUMMARIZE

```
SUMMARIZE(
    Sales,
    Sales[Quantity],
    Sales[Net Price]
)
```

SUMMARIZE:

- Groups data
- Removes duplicates
- Reduces row count

If duplicate rows exist, they are collapsed.

Now you are iterating fewer rows, which changes the final result.

This highlights a critical principle:

When you iterate a table expression, you iterate the result of that expression not the original table.

Always verify the cardinality of the table being passed to an iterator.

##### Key Takeaways About DAX Row Context

- Row context represents the current row during iteration.
- It is created by iterator functions and calculated columns.
- Column references require row context.
- Filter context filters data; row context iterates data.
- Table expressions can change row count and affect results.
- Always verify the cardinality of your iterator input.

Understanding DAX row context at a conceptual level makes advanced topics like context transition much easier to grasp.

##### Final Thoughts

Mastering DAX row context is essential for writing accurate and efficient Power BI measures. Once you clearly understand how iterators create row context and how it interacts with filter context, your DAX debugging skills improve dramatically.

Keep practicing, analyze how many rows are being iterated, and always question where your row context is coming from.