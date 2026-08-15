---
title: "What Everybody Ought to Know About Iterator functions in Power BI"
source: "https://medium.com/@BIWave/what-everybody-ought-to-know-about-iterator-functions-in-power-bi-a77b63889ac7"
author:
  - "[[Mikhail Mikushin]]"
published: 2026-06-25
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
A Simple Solution for Your Most Complex DAX Problems.

![Iterator Functions in Power BI tutorial guide with network data visualization background](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hFnQdY7DOxAWuFNcgJ6LWA.png)

Iterator Functions in Power BI tutorial guide with network data visualization background

Sometimes standard DAX functions in Power BI do not work, and a method exists to get calculations for different granularity.

Today, I will explain iterator functions, their use cases, and tips for optimal performance.

## Context:

Before you jump into the iterator functions, you should know [about the context of Power BI.](https://biwave.substack.com/p/power-bi-evaluation-context)

There are two types of context:

1. **Filter context** represents the set of filters applied by the current visual, slicer, or page. Simple aggregation functions work within the filter context.
2. **Row context.** The row context iterates row by row, but it has downsides, as it can’t see what is before and after that row. But it also has a benefit: the ability to perform the calculations on different levels of granularity.

Iterator functions operate within the row context and then aggregate within the current filter context.

[Power BI can switch between contexts](https://biwave.substack.com/p/complex-dax), and the CALCULATE function creates a transition from one to another.

A nested row-context expression or a measure evaluated inside an iterator triggers a context transition. In those cases the engine runs the equivalent of CALCULATE to convert row context to filter context so the inner expression will be evaluated per row.

### Context Transition with CALCULATE:

When an iterator function works inside a calculated column, the behavior changes.

The row context from the calculated column interacts with the row context that the iterator creates. Without additional intervention, the iterator aggregates across all rows and returns the same value for every row in the column.

The CALCULATE function resolves this problem through context transition. It transforms the row context into an equivalent filter context, which forces the iterator to process only the current row to get the correct per-row result.

Context transition works for scenarios where a calculated column is the only viable option, but it adds difficulty.

## DAX Engines:

[DAX operates with two engines:](https://biwave.substack.com/p/complex-dax)

1. **The formula engine** reads the data query, builds a plan, and decides what should be calculated; orchestrates the process; and often delegates raw data retrieval to the storage engine.
2. **The storage engine** is responsible for data retrieval, compression, and caching in the tabular data model. It processes requests from the Formula Engine and extracts and aggregates physical data in a columnar format. Storage engine performance is much better than FE.

[For best performance](https://biwave.substack.com/p/why-is-my-power-bi-so-slow-after), use expressions that the storage engine can translate to columnar, set-based operations: simple column references and arithmetic operations.

If you use the RELATED function inside the iterator or measures inside the iterator, then Power BI pushes the calculation into the formula engine.

The problem is that DAX automatically calls the CALCULATE function and forces context transition, which adds overhead.

Another problem happens when you use nested functions inside the iterator expression. DAX pushes only the inner expression to the storage engine, and the formula engine executes the outer expression.

Both engines work in parallel. The storage engine scans the functions and looks at the expression to see what it can translate into a set-based operation that the storage engine executes more efficiently, instead of the formula engine doing it row by row.

## Iterator function structure:

An iterator function consists of two parts:

1. **Table argument.**
2. **Expression.**

Iterator functions follow a sequence: The function receives a table as the first argument, then it creates a row context for the table and identifies the rows it must process.

Then it evaluates the expression in the second argument against every row individually and stores each result in memory.

Once the engine processes all rows, it performs the aggregation over those stored values.

## Iterator functions:

### SUMX:

SUMX returns the sum of an expression evaluated for each row.

There is common misconception that SUMX performance is worse than SUM, but this is true only for several cases.

SUM is a specialized aggregation that the engine can optimize more than SUMX. SUMX evaluates an expression row by row, so SUMX can be slower than SUM when the expression prevents storage engine aggregation.

You can use SUMX as an expression for multiple columns and conditions.

Example:

```c
SUMX(Sales, Sales[Quantity] * Sales[Unit Price])
```

If you want to calculate, for example, weighted sums, use the DIVIDE function inside to deal with the null values in a denominator.

### AVERAGEX:

Use this function when you want to calculate the order level average. Use the value expression inside that.

AVERAGE computes a simple unweighted mean. Use AVERAGEX to compute weighted averages or averages derived from complex expressions.

Examples:

```c
Weighted Avg Unit Price =
DIVIDE(
    SUMX( Sales, Sales[Quantity] * Sales[UnitPrice] ),
    SUM( Sales[Quantity] )
)
```
```c
3-Day Moving Average = 
AVERAGEX(
    DATESINPERIOD(Date[Date], 
    MAX(Date[Date]), -3, DAY), [Total Amount]
)
```

### COUNTX:

COUNTX counts rows where a condition evaluates to a specified value.

The function iterates over a table, evaluates an expression for each row, and counts the rows where the expression returns a non-blank, non-empty result.

COUNTAX is the text-aware variant that treats text results or FALSE as non-blank.

Use the DISTINCTCOUNT function when you can if you do not need to iterate over a different level of granularity.

```c
High Value Orders =
COUNTX(
    Sales,
    IF( Sales[Quantity] * Sales[UnitPrice] > 50000, 1 )
)
```

### RANKX:

RANKX is both a scalar function and an iterator. It evaluates an expression for every row of a reference table, builds a ranked list, and then returns the rank of the current row value within that list.

Example:

```c
Product Revenue Rank =
RANKX(
    ALLSELECTED( Product[ProductName] ),
    [Total Revenue],
    DESC,
    DENSE
)
```

There are certain requirements you need to follow if you want to use this function most effectively:

1. Floating point comparison issues can produce incorrect rankings when the values are close.
2. Use ALLSELECTED instead of VALUES as the first argument.
3. Use ISINSCOPE or HASONEVALUE to avoid meaningless values at total rows and replace them with blanks.

The function has a DENSE parameter that can change the way it calculates ties.

Every function inside it removes filters for global ranking within context.

### MINX and MAXX:

**MINX** and **MAXX** return the maximum or minimum value from an expression evaluated per row. They are useful when the extreme value should be computed from multiple columns or filtered subsets.

```c
Largest Line Total =
MAXX(Sales, 
    Sales[Quantity] * Sales[UnitPrice] )
```

The choice between a table reference and VALUES() as the first argument of MAXX or MINX depends on whether the blank row from invalid relationships should be included.

### CONCATENATEX:

Use this iterator function when you want to join the results with a delimiter with conditions.

Run string concatenation and other row-level transformations in Power Query when possible. You should push everything you can upstream and filter as fast as possible before you move to more expensive calculation methods in Power BI.

Example:

```c
Product Categories = 
CONCATENATEX(
    VALUES(Product[Category]),
    Product[Category],
    ", "
            )
```

### WINDOW:

It defines a dynamic range of rows (a window) and runs calculations: running totals, moving averages, rankings across the range.

Example:

```c
Running Total = CALCULATE(
    SUM(Sales[Amount]),
    WINDOW(-1, REL, 0, REL, ORDERBY(Sales[Date], ASC))
)
```

### PRODUCTX:

PRODUCTX evaluates an expression per row and returns the product of those values.

Example: Compound Growth Calculation

```c
FutureValue =
[PresentValue] *
PRODUCTX (
    AnnuityPeriods,
    1 + [FixedInterestRate]
)
```

### Table-Shaping Iterators:

Not all iterators return a scalar. ADDCOLUMNS, SELECTCOLUMNS, and GENERATE iterate over a table and return a modified table.

**ADDCOLUMNS** takes a table and one or more column definitions, evaluates the expression for each row, and appends the result as a new column:

```c
ADDCOLUMNS (
    VALUES ( Customer[Country] ),
    "Revenue", [Total Revenue],
    "Orders", [Total Orders]
)
```

**SELECTCOLUMNS** iterates over a table and returns only the columns specified, with optional renaming:

```c
SELECTCOLUMNS (
    Customer,
    "CustName", Customer[FullName],
    "CustRegion", Customer[Region]
)
```

**GENERATE** iterates over a table and for each row evaluates a second table expression, then concatenates the results.

```c
GENERATE (
    VALUES ( Product[Category] ),
    TOPN ( 3, Product, [Total Revenue], DESC )
)
```

**SUMMARIZECOLUMNS** groups data by specified columns and computes aggregations for each group and create a summary table:

```c
Sales Summary = 
SUMMARIZECOLUMNS(
    'Date'[Year],
    'Product'[Category],
    "Total Sales", SUM(Sales[Amount]),
    "Order Count", COUNTROWS(Sales)
)
```

## Performance:

- Filter columns and rows as early as possible. The less you process in the later stages in Power BI calculations, the worse would be the performance.
- Iterator functions’ performance is much faster than the calculated columns’.
- You can reduce cardinality when iterating over a table with many rows. Use VALUES() on the column inside the function to reduce the runs to distinct values only. If Customer has 10 000 distinct IDs but Sales has 10 million rows, it will limit iteration to only 10 000 rows.
- Use visual calculations. Power BI stores visual calculations only in one specific visual and will not load them to the whole data model.
- Use variables inside the functions to speed up the process. They calculate the expressions only once.
- Optimize the iterator functions with SUMMARIZE. It is efficient because it uses the pre-aggregation.
- Use the standard functions: SUM, MAX, and AVERAGE whenever possible. They are computationally more effective, especially on large fact tables.
- Use the CALCULATETABLE over the FILTER for the table arguments in most of the cases. A FILTER inside an iterator slows down the measure execution.
- When possible, replace nested iterators with a single iterator or use SUMMARIZE for pre-aggregation.

## Limitations:

Limitations exist for the use of iterator functions.

For example, you cannot use iterator functions inside Row Level Security rules in Direct Query mode.

In Direct Query mode, you should remove extra filters, as they make queries significantly slower.

> **Join my data analytics community today.**
> 
> **How do you approach Context Transition in your models?**
> 
> **Let me know in the comments👇**