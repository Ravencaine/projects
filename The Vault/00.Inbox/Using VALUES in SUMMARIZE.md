---
title: "Using VALUES in SUMMARIZE"
source: "https://www.sqlbi.com/articles/using-values-in-summarize/"
author:
  - "[[Marco Russo & Alberto Ferrari]]"
published: 2025-10-21
created: 2026-08-04
description: "This article describes when to use VALUES in a table grouped by SUMMARIZE, then goes on to explain why you cannot however use VALUES with SUMMARIZECOLUMNS."
Processed: "Unprocessed"
---
We discussed [VALUES](https://dax.guide/values/?aff=sqlbi) in previous articles: [Choosing between DISTINCT and VALUES in DAX](https://www.sqlbi.com/articles/choosing-between-distinct-and-values-in-dax/) and [Using VALUES in iterators](https://www.sqlbi.com/articles/using-values-in-iterators/). However, there is a third case where [VALUES](https://dax.guide/values/?aff=sqlbi) could be used with a table reference, which is when you use [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) to group by columns you want to iterate. In this article, we describe this particular scenario to understand when [VALUES](https://dax.guide/values/?aff=sqlbi) is needed to retrieve the blank for an invalid relationship using [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) and [SUMMARIZECOLUMNS](https://dax.guide/summarizecolumns/?aff=sqlbi).

When you use [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi), you may want to use [VALUES](https://dax.guide/values/?aff=sqlbi) over the aggregated table in case it could have an additional blank row for an invalid relationship, and you must ensure that this blank row is included. This condition is uncommon because [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) often includes blank rows for invalid relationships that are implicitly included. For example, consider the following measure that uses [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) over the *Sales* table, grouping by *Customer\[State\]* and *Customer\[City\]* to apply an adjustment to Columbus, Ohio (note that there are other cities with that name in other states):

Measure in Sales table

```
Test Summarize Sales =
SUMX(
    SUMMARIZE(
        Sales,
        Customer[State],
        Customer[City]
    ),
    [Sales Amount]
        *IF(Customer[State]="Ohio"&& Customer[City]="Columbus",.99,1)
)
```

[Copy](#) [Conventions](#)

Because [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) groups data from *Sales*, the presence of a blank row for *Customer* is included in the result of the [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) function. However, grouping *Customer* in [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) produces a different result:

Measure in Sales table

```
Test Summarize Customer =
SUMX(
    SUMMARIZE(
        Customer,
        Customer[State],
        Customer[City]
    ),
    [Sales Amount]
        *IF(Customer[State]="Ohio"&& Customer[City]="Columbus",.99,1)
)
```

[Copy](#) [Conventions](#)

The following report shows the differences between the *Test Summarize Sales* and *Test Summarize* *Customer* measures: the “Summarize Sales” column shows the right amount, whereas “Summarize Customer” shows that the *Test Summarize Customer* measure does not include the amount of the blank row, which in turn reduces the Total row.

The report also shows two other measures that return the correct result. If you must use the *Customer* table in [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) and you need the blank row, you can use [VALUES](https://dax.guide/values/?aff=sqlbi) around the table reference in [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi), as we do in the *Test Summarize Values Customer* measure:

Measure in Sales table

```
Test Summarize Values Customer =
SUMX(
    SUMMARIZE(
        VALUES(Customer ),
        Customer[State],
        Customer[City]
    ),
    [Sales Amount]
        *IF(Customer[State]="Ohio"&& Customer[City]="Columbus",.99,1)
)
```

[Copy](#) [Conventions](#)

The last example of a correct measure uses [SUMMARIZECOLUMNS](https://dax.guide/summarizecolumns/?aff=sqlbi) instead of [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi):

Measure in Sales table

```
Test SummarizeColumns (notusing best practice)=
SUMX(
    SUMMARIZECOLUMNS(
        Customer[State],
        Customer[City]
    ),
    [Sales Amount]
        *IF(Customer[State]=="Ohio"&& Customer[City]=="Columbus",.99,1)
)
```

[Copy](#) [Conventions](#)

We must mention that using [SUMMARIZECOLUMNS](https://dax.guide/summarizecolumns/?aff=sqlbi) in this case includes the blank row if present, although the code of *Test SummarizeColumns (not using best practice)* does not follow the best practices of [SUMMARIZECOLUMNS](https://dax.guide/summarizecolumns/?aff=sqlbi) in a measure. Indeed, it does not include any aggregation. Here is a better implementation that considers the best practices for using [SUMMARIZECOLUMNS](https://dax.guide/summarizecolumns/?aff=sqlbi) in a measure:

Measure in Sales table

```
Test SummarizeColumns =
SUMX(
    SUMMARIZECOLUMNS(
        Customer[State],
        Customer[City],
        "@Sales",[Sales Amount]
    ),
    [@Sales]
        *IF(Customer[State]=="Ohio"&& Customer[City]=="Columbus",.99,1)
)
```

[Copy](#) [Conventions](#)

To recap, use [VALUES](https://dax.guide/values/?aff=sqlbi) over the table reference for [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi) when you group by a table that is on the one-side of a regular relationship, and you want to make sure to include the blank row caused by an invalid relationship. Usually, this is unnecessary when you pass the table on the many-side of a relationship to [SUMMARIZE](https://dax.guide/summarize/?aff=sqlbi). If you use [SUMMARIZECOLUMNS](https://dax.guide/summarizecolumns/?aff=sqlbi), the blank row is included, but you should always follow the best practices for [SUMMARIZECOLUMNS](https://dax.guide/summarizecolumns/?aff=sqlbi).

When a column name is given, returns a single-column table of unique values. When a table name is given, returns a table with the same columns and all the rows of the table (including duplicates) with the [additional blank row](https://www.sqlbi.com/articles/blank-row-in-dax/) caused by an invalid relationship if present.

`VALUES ( <TableNameOrColumnName> )`

Creates a summary of the input table grouped by the specified columns.

`SUMMARIZE ( <Table> [, <GroupBy_ColumnName> [, [<Name>] [, [<Expression>] [, <GroupBy_ColumnName> [, [<Name>] [, [<Expression>] [, … ] ] ] ] ] ] ] )`

Create a summary table for the requested totals over set of groups.

`SUMMARIZECOLUMNS (  [<GroupBy_ColumnName> [, [<FilterTable>] [, [<Name>] [, [<Expression>] [, <GroupBy_ColumnName> [, [<FilterTable>] [, [<Name>] [, [<Expression>] [, … ] ] ] ] ] ] ] ] ] )`