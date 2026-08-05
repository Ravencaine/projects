---
title: "Using RANK instead of RANKX in DAX"
source: "https://www.sqlbi.com/articles/using-rank-instead-of-rankx-in-dax/"
author:
  - "[[Marco Russo & Alberto Ferrari]]"
published: 2025-12-01
created: 2026-08-04
description: "Should you use RANK or stick with RANKX? In which scenarios is one better than the other? This article provides an in-depth analysis to help readers make in"
Processed: "Unprocessed"
---
In this article, we are not going to discuss the syntax of the [RANK](https://dax.guide/rank/?aff=sqlbi) and [RANKX](https://dax.guide/rankx/?aff=sqlbi) functions. If you need more information, we suggest you consult [DAX Guide](https://dax.guide/) for syntax, as well as the following articles, which introduce both functions: [Introducing the RANK window function in DAX](https://www.sqlbi.com/articles/introducing-the-rank-window-function-in-dax/) and [Introducing RANKX in DAX](https://www.sqlbi.com/articles/introducing-rankx-in-dax/).

[RANKX](https://dax.guide/rankx/?aff=sqlbi) is the classic method of ranking in DAX; [RANK](https://dax.guide/rank/?aff=sqlbi) is a newer window function that works faster, better, and in a more flexible way. [RANK](https://dax.guide/rank/?aff=sqlbi) is used in both visual calculations and measures. Which function should you use in which scenario? The answer depends on your requirements: each solution has pros and cons.

If you are interested in a quick answer, [RANK](https://dax.guide/rank/?aff=sqlbi) is the preferred function to perform ranking, both in visual calculations and in measures. [RANKX](https://dax.guide/rankx/?aff=sqlbi) remains slightly more powerful in some complex scenarios, which, to be honest, are relatively rare in the real world. Since [RANK](https://dax.guide/rank/?aff=sqlbi) is the preferred choice, the article primarily focuses on the few scenarios where [RANKX](https://dax.guide/rankx/?aff=sqlbi) remains useful.

Consider the following report, which presents three methods for computing the ranking of brands based on their respective sales amounts. One measure uses [RANKX](https://dax.guide/rankx/?aff=sqlbi), while the other two use [RANK](https://dax.guide/rank/?aff=sqlbi): one in a measure and the other in a visual calculation. The results remain the same, despite significant differences in the DAX code.

![](99.System/Attachments/image1-121.png)

Here is the code of the three different versions:

Measure in Sales table

```
Rank =
RANK(
    ALLSELECTED('Product'[Brand]),
    ORDERBY([Sales Amount],DESC)
)
```

[Copy](#) [Conventions](#)

Measure in Sales table

```
RankX =
IF(
    ISINSCOPE('Product'[Brand]),
    RANKX(ALLSELECTED('Product'[Brand]),[Sales Amount])
)
```

[Copy](#) [Conventions](#)

Visual Calculation

```
Visual Rank =
IF(
    ISATLEVEL([Brand]),
    RANK(ROWS,ORDERBY([Sales Amount],DESC))
)
```

[Copy](#) [Conventions](#)

Please note that both *RankX* and *Visual Rank* require an [IF](https://dax.guide/if/?aff=sqlbi) function to prevent the total from being displayed. *Rank* does not, as it blanks values if more than one row is visible in the filter context.

## Visual calculations or measures?

The first choice is between a visual calculation and a measure. Mostly, values shown in Power BI are computed through measures. However, the main disadvantage of using a measure is that you need to hardcode in the measure itself the column over which you are performing the ranking. Both *Rank* and *RankX* require using *[ALLSELECTED](https://dax.guide/allselected/?aff=sqlbi) ( Product\[Brand\] )* to identify the table for ranking.

If a user removes the *Product\[Brand\]* column from the matrix and replaces it with, say, *Product\[Color\]*, then both measures produce a blank as a result. On the other hand, the visual calculation uses the ROWS keyword to identify the rows in the matrix, regardless of the actual columns used to populate the axis; therefore, it will work with whatever column is used. The only reference to *Product\[Brand\]* in the visual calculation is in the [ISATLEVEL](https://dax.guide/isatlevel/?aff=sqlbi) function call, not in [RANK](https://dax.guide/rank/?aff=sqlbi).

![](99.System/Attachments/image2-117.png)

Despite letting developers generate code that does not depend specifically on the column used for the ranking, visual calculations suffer from a drawback: a visual calculation can only work on data in the visual. It cannot use data from the model. For example, if one wants to compute the global ranking, regardless of the filters present in the report, a visual calculation is not the right choice. In contrast, both [RANK](https://dax.guide/rank/?aff=sqlbi) and [RANKX](https://dax.guide/rankx/?aff=sqlbi) work well, as they allow developers to specify the table to be used for the ranking. The following two measures perform ranking over [ALL](https://dax.guide/all/?aff=sqlbi) rather than [ALLSELECTED](https://dax.guide/allselected/?aff=sqlbi). Therefore, they produce a global ranking, ignoring the presence of filters from slicers and other visuals:

Measure in Sales table

```
Rank ALL=
RANK(
    ALL('Product'[Brand]),
    ORDERBY([Sales Amount],DESC)
)
```

[Copy](#) [Conventions](#)

Measure in Sales table

```
RankX ALL=
IF(
    ISINSCOPE('Product'[Brand]),
    RANKX(ALL('Product'[Brand]),[Sales Amount])
)
```

[Copy](#) [Conventions](#)

Visual Calculation

```
Visual Rank =
IF(
    ISATLEVEL([Brand]),
    RANK(ROWS,ORDERBY([Sales Amount],DESC))
)
```

[Copy](#) [Conventions](#)

The *Visual Rank* measure ranks brands from one to five, whereas the two measures maintain the global ranking, as if no filters were applied.

Suppose you need a ranking calculation that is nearly independent from the column being used in the report, and you are ok with the limitation that the ranking needs to be responsive to any filter being applied to the visual. In that case, visual calculations are likely to be your best choice. The main advantage, which should not be underestimated, is their simplicity.

However, if you need more power, you need a measure, and you still need to decide between [RANK](https://dax.guide/rank/?aff=sqlbi) and [RANKX](https://dax.guide/rankx/?aff=sqlbi).

## Choosing between RANK and RANKX

[RANK](https://dax.guide/rank/?aff=sqlbi) is a window function recently added to DAX. It is flexible, powerful, and easy to use. [RANKX](https://dax.guide/rankx/?aff=sqlbi) is the classic way of ranking; developers have never shown it too much love, because its syntax and semantics are somewhat intricate.

Currently, [RANK](https://dax.guide/rank/?aff=sqlbi) is a better alternative to [RANKX](https://dax.guide/rankx/?aff=sqlbi) because it is simpler for most tasks. [RANK](https://dax.guide/rank/?aff=sqlbi) however is missing some of the features of [RANKX](https://dax.guide/rankx/?aff=sqlbi). But these missing features are helpful in such exotic scenarios that they are rarely used.

The main differences between [RANK](https://dax.guide/rank/?aff=sqlbi) and [RANKX](https://dax.guide/rankx/?aff=sqlbi) are:

- [RANK](https://dax.guide/rank/?aff=sqlbi) can rank on multiple columns easily by specifying multiple columns in the [ORDERBY](https://dax.guide/orderby/?aff=sqlbi) section. [RANKX](https://dax.guide/rankx/?aff=sqlbi) does not have the option of ranking over multiple columns. While it is certainly possible to use [RANKX](https://dax.guide/rankx/?aff=sqlbi) to rank on multiple columns (see [RANKX on multiple columns with DAX and Power BI](https://www.sqlbi.com/articles/rankx-on-multiple-columns-with-dax-and-power-bi/)), the code is intricate and prone to errors.
- [RANK](https://dax.guide/rank/?aff=sqlbi) returns [BLANK](https://dax.guide/blank/?aff=sqlbi) if the filter returns more than one row – among other reasons it can return [BLANK](https://dax.guide/blank/?aff=sqlbi). This spares us the need for the conditional logic of [ISINSCOPE](https://dax.guide/isinscope/?aff=sqlbi) or [HASONEVALUE](https://dax.guide/hasonevalue/?aff=sqlbi), which is needed for [RANKX](https://dax.guide/rankx/?aff=sqlbi).
- [RANK](https://dax.guide/rank/?aff=sqlbi) does not suffer from the random issues [RANKX](https://dax.guide/rankx/?aff=sqlbi) faces with floating-point values. Indeed, [RANKX](https://dax.guide/rankx/?aff=sqlbi) may produce an incorrect ranking if the formula used to perform the ranking is a floating-point value. See [Use of RANKX with decimal numbers in DAX](https://www.sqlbi.com/blog/marco/2014/07/16/use-of-rankx-with-decimal-numbers-in-dax/) for more information.
- [RANK](https://dax.guide/rank/?aff=sqlbi) has a simpler syntax because most arguments are optional and they can be placed anywhere in the function call. In contrast, [RANKX](https://dax.guide/rankx/?aff=sqlbi) uses a regular syntax, and arguments are identified by position. Hence, the syntax of [RANK](https://dax.guide/rank/?aff=sqlbi) is easier to write than that of [RANKX](https://dax.guide/rankx/?aff=sqlbi).

Despite being a better solution, [RANK](https://dax.guide/rank/?aff=sqlbi) comes with several limitations:

- [RANK](https://dax.guide/rank/?aff=sqlbi) uses apply semantics to identify the row to rank against the source table. While this behavior is mostly intuitive, it can be intricate in complex scenarios. This is not a real disadvantage, because it is very rare to find a scenario where [RANK](https://dax.guide/rank/?aff=sqlbi) produces counterintuitive results. However, when this happens, it becomes a real brain teaser.
- [RANK](https://dax.guide/rank/?aff=sqlbi) lacks the flexibility to rank a value against a lookup table: it can only rank the current row (as determined by apply semantics) against the source table.
- [RANK](https://dax.guide/rank/?aff=sqlbi) cannot perform ranking using a source table that contains only extension columns. While this is not a substantial limitation, there may be scenarios where the source table is a variable with no model columns, in which case [RANK](https://dax.guide/rank/?aff=sqlbi) is not a good fit.

## RANK and apply semantics

Apply semantics is a feature used by window functions to determine the current row. If you are not familiar with apply semantics, you can reference the following article: [Understanding apply semantics for window functions in DAX](https://www.sqlbi.com/articles/understanding-apply-semantics-for-window-functions-in-dax/).

The goal of apply semantics is to find the current row in a table. [RANK](https://dax.guide/rank/?aff=sqlbi) computes the ranking of the current row relative to a source table sorted in a specific manner. However, what is the current row? Intuitively, if a report is slicing by *Product\[Brand\]* and we are ranking against *[ALLSELECTED](https://dax.guide/allselected/?aff=sqlbi) ( Product\[Brand\] )*, then the current row is the brand that is visible in the current row of the visual. In a more technical sense, it refers to the brand being filtered within the filter context – because each cell in the visual has its own filter context and no row contexts when the measure is evaluated.

Apply semantics inspects the current filter context and tries to use the filters in the filter context to identify a single row in the source table. If the filter context is not selective enough to identify a single row, then [RANK](https://dax.guide/rank/?aff=sqlbi) returns blank, because apply semantics would not return a single row.

If [RANK](https://dax.guide/rank/?aff=sqlbi) is used in a measure to rank the current row in a visual, it works as expected. Performing the ranking in a calculated column (where there is no filter context, only a row context) is somewhat more problematic. However, the primary use of [RANK](https://dax.guide/rank/?aff=sqlbi) is to rank in the current visual. Hence, the apply semantics operates in a relatively intuitive manner.

## Ranking against a lookup table

[RANKX](https://dax.guide/rankx/?aff=sqlbi) can use two formulas to perform the ranking: one is used during the creation of the lookup table, and the second is used to produce the number for the ranking.

Indeed, the third parameter of [RANKX](https://dax.guide/rankx/?aff=sqlbi) is an optional expression used to specify the value to be ranked, which can be different from the expression used to build the table. It is most useful when you want to rank an expression based on a lookup table that uses a different expression or value, for example ranking sales against a predefined sales segment table. If you do not specify the third argument, then [RANKX](https://dax.guide/rankx/?aff=sqlbi) uses the same expression (second argument) for both arguments.

As an example, let us pretend we want to classify sales based on a range table.

![](99.System/Attachments/image4-99.png)

Brands with sales exceeding 800,000 should be ranked 1. Brands with sales between 300,000 and 800,000 should be ranked 2, and brands with sales under 300,000, ranked 3. The *Level* measure can be implemented with [RANKX](https://dax.guide/rankx/?aff=sqlbi):

Measure in Sales table

```
Level =
RANKX(
    'Level',-- The lookup table source
    'Level'[Limit],-- The value to build the lookup table
    [Sales Amount]-- The value to rank
)
```

[Copy](#) [Conventions](#)

The second argument, *Level\[Limit\]*, is used to build the lookup table used to rank the third argument, *\[Sales Amount\]*. [RANK](https://dax.guide/rank/?aff=sqlbi) does not offer a similar feature, because [RANK](https://dax.guide/rank/?aff=sqlbi) relies on the apply semantics to determine the current row. In other words, [RANK](https://dax.guide/rank/?aff=sqlbi) ranks a row, whereas [RANKX](https://dax.guide/rankx/?aff=sqlbi) ranks an expression.

The thing is, [RANKX](https://dax.guide/rankx/?aff=sqlbi) is just one option for computing the *Level* measure, and it is not necessarily the best one. A simple iteration with a filter would produce the same result:

Measure in Sales table

```
Level =
MINX(
    FILTER('Level','Level'[Limit]<=[Sales Amount]),
    'Level'[Key]
)
```

[Copy](#) [Conventions](#)

A DAX developer is likely to find this second implementation easier and more intuitive.

## Ranking over variables

One scenario where [RANK](https://dax.guide/rank/?aff=sqlbi) is not an option is when there is a need to perform ranking over a variable containing only temporary columns. Indeed, [RANK](https://dax.guide/rank/?aff=sqlbi) requires at least one column of the source table to be a model column. The reason is – again – apply semantics. Apply semantics requires finding the current row in the source table by inspecting the row context and the filter context.

For example, if the source table contains *[ALLSELECTED](https://dax.guide/allselected/?aff=sqlbi) ( Product\[Brand\] )*, then [RANK](https://dax.guide/rank/?aff=sqlbi) searches for the values of *Product\[Brand\]* visible in the current filter context to identify which row to consider for the ranking. If the source table contains only columns with no data lineage, then this matching process cannot be executed, and [RANK](https://dax.guide/rank/?aff=sqlbi) returns an error.

For example, the following query correctly produces the list of brands, sales, and their ranking:

Query

```
EVALUATE
VARSourceTable =
    SELECTCOLUMNS(
        ALLSELECTED('Product'[Brand]),
        "@Brand",'Product'[Brand],-- Adding & "" to break the lineage
        "@Sales",[Sales Amount]-- causes RANK to stop working
    )
RETURN
    SUMMARIZECOLUMNS(
        'Product'[Brand],
        "Sales",[Sales Amount],
        "Rank",RANK(SourceTable,ORDERBY([@Sales]))
    )
ORDER BY[Sales]
```

[Copy](#) [Conventions](#)

As you can see, the *Rank* column is computed correctly.

![](99.System/Attachments/image5-84.png)

However, breaking the lineage of the *@Brand* column by just adding an empty string produces an error:

**[RANK](https://dax.guide/rank/?aff=sqlbi) ‘s Relation parameter only contains columns added by DAX table functions. This is not supported.**

In such scenario, [RANKX](https://dax.guide/rankx/?aff=sqlbi) would work fine:

Query

```
EVALUATE
VARSourceTable =
    SELECTCOLUMNS(
        ALLSELECTED('Product'[Brand]),
        "@Brand",'Product'[Brand]& "",
        "@Sales",[Sales Amount]
    )
RETURN
    SUMMARIZECOLUMNS(
        'Product'[Brand],
        "Sales",[Sales Amount],
        "Rank",RANKX(SourceTable,[@Sales],[Sales Amount],ASC)
    )
ORDER BY[Sales]
```

[Copy](#) [Conventions](#)

This last scenario is likely to be the only one where using [RANKX](https://dax.guide/rankx/?aff=sqlbi) is the preferred solution. As we mentioned, it is not common to need to rank variables containing only temporary columns; therefore, this significantly limits the use of [RANKX](https://dax.guide/rankx/?aff=sqlbi) over [RANK](https://dax.guide/rank/?aff=sqlbi).

## Conclusions

For simple ranking, visual calculations are the most effective approach. They are fast and straightforward, and they naturally produce local ranking, which is the type of ranking most likely to be needed. When visual calculations are not an option, then [RANK](https://dax.guide/rank/?aff=sqlbi) is your best friend. It is easier than [RANKX](https://dax.guide/rankx/?aff=sqlbi), and the features it misses are useful in a very limited number of scenarios.

[RANKX](https://dax.guide/rankx/?aff=sqlbi) can still be helpful in certain borderline scenarios, but it is mostly superseded by [RANK](https://dax.guide/rank/?aff=sqlbi). Does this mean you need to rush and replace all your measures containing [RANKX](https://dax.guide/rankx/?aff=sqlbi) with [RANK](https://dax.guide/rank/?aff=sqlbi)? Not at all: if a measure works, then there is no need to change it. Unless you are using [RANKX](https://dax.guide/rankx/?aff=sqlbi) with floating-point values. If that is the case… then [RANK](https://dax.guide/rank/?aff=sqlbi) works better and produces safer code.

Returns the rank for the current context within the specified partition sorted by the specified order or on the axis specified.

`RANK (  [<Ties>] [, <Relation>] [, <OrderBy>] [, <Blanks>] [, <PartitionBy>] [, <MatchBy>] [, <Reset>] )`

Returns the rank of an expression evaluated in the current context in the list of values for the expression evaluated for each row in the specified table.

`RANKX ( <Table>, <Expression> [, <Value>] [, <Order>] [, <Ties>] )`

Checks whether a condition is met, and returns one value if TRUE, and another value if FALSE.

`IF ( <LogicalTest>, <ResultIfTrue> [, <ResultIfFalse>] )`

CALCULATE modifier

Returns all the rows in a table, or all the values in a column, ignoring any filters that might have been applied inside the query, but keeping filters that come from outside.

`ALLSELECTED (  [<TableNameOrColumnName>] [, <ColumnName> [, <ColumnName> [, … ] ] ] )`

Report whether the column is present at the current level.

`ISATLEVEL ( <Column> )`

CALCULATE modifier

Returns all the rows in a table, or all the values in a column, ignoring any filters that might have been applied.

`ALL (  [<TableNameOrColumnName>] [, <ColumnName> [, <ColumnName> [, … ] ] ] )`

The expressions and order directions used to determine the sort order within each partition. Can only be used within a Window function.

`ORDERBY (  [<OrderBy_Expression> [, [<OrderBy_Direction>] [, <OrderBy_Expression> [, [<OrderBy_Direction>] [, … ] ] ] ] ] )`

Returns a blank.

`BLANK (  )`

Returns true when the specified column is the level in a hierarchy of levels.

`ISINSCOPE ( <ColumnName> )`

Returns true when there’s only one value in the specified column.

`HASONEVALUE ( <ColumnName> )`