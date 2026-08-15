---
title: "Analyzing the performance impact of visual calculations"
source: "https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, reading-list]
created: "2026-08-11"
---

> Visual calculations can either improve or degrade the performance of a report. In this article, we outline how we ensure visual calculations have a positive

Analyzing the performance impact of visual calculations - SQLBI The goal of visual calculations is to simplify some reports and calculations, rather than to optimize performance. However, it is common sense that – in some scenarios – visual calculations can bring some benefit from the performance point of view. The main idea is that a report may precompute some values and then, to further elaborate on them, it may use the content of the virtual table rather than recompute the values multiple times. Imagine we want to compute a report containing the distinct count of customers by year, as well as the growth in percentage between the current year and the previous years. The measure required is straightforward: Measure in Sales table  We chose DISTINCTCOUNT on purpose: we wanted a measure that is non-aggregatable and heavy in terms of computational requirements. When executed on the version of Contoso with 23M rows in Sales , the report requires around 13 seconds to execute, and this is not surprising at all. Before looking at the details in the server timings, let us reason as to why the measure is expected to be slow. First of all, not only is DISTINCTCOUNT a heavy operation to perform, but it is also non-additive – as such, it requires multiple scans of the fact table to compute. Secondly, time intelligence calculations require complex reasoning that is difficult to optimize. The DAX engine first computes the distinct count of customers by year. Then for each year, it determines the previous year; and to compute the previous year’s distinct count, it then runs another query against the database. In other words, each cell requires its own query to retrieve the value of the previous year. Indeed, when looking at the details, we see confirmation of our reasoning: there are many storage engine queries, each computing the distinct count for one year. As humans, the first consideration that comes to mind is quite simple: why compute the value of the measure on a single year when the engine has already computed the value of the measure grouped by year? The value is already there; just use it without needing to recalculate it, right? True, but this is a very human behavior: we see the yearly value because the matrix is sliced by year; therefore, we cut corners and use the previously-computed value. DAX is more generic; it needs to work no matter what we slice by, which is why it uses a slower, yet more generic algorithm. However, at the end of the day, we still feel that something can be improved. If the value is already there, there should be a way to use it with no further calculation. Indeed, a visual calculation does exactly this. When using visual calculations, the engine first computes the source query (that is, a query that retrieves all the values computed by model measures), and then the next step of calculation happens on the virtual table, with no further need to query the data model. The same algorithm, with a visual calculation, is the following: Visual Calculation  By using PREVIOUS , we are asking DAX to retrieve the value of # Customers in the previous column, with no need to invoke another query on the database. The version using the visual calculation is significantly faster. 6 seconds rather than the previous 13 seconds. Not only is it faster, but by analyzing the storage engine queries, we observe a much more reasonable behavior. The engine retrieves the base measure by the different aggregation levels – it requires subtotals, which is why there are multiple storage engine queries – and then the remaining part of the calculation is all in the formula engine. Because the virtual table is rather small, the cost to the formula engine is quite low. If we had used Sales Amount, an additive and lighter measure, rather than a distinct count, the result would be similar, but the timings would be so quick – with the query running in around 100 milliseconds – that we would have to use a much larger database to get a feeling for the behavior. Distinct count is used only to make the scenario clearer and to avoid optimizations specific to additive measures. So far, we have seen one side of the coin: visual calculations improve performance when there is a small number of basic heavy calculations on top of which we need to perform further elaboration. The good news is that this happens pretty frequently, so giving visual calculation a try is a good step in building reports. However, there is another side of the coin to investigate: is it possible that visual calculations slow down performance? Unfortunately, the answer is yes. When a visual calculation is added to a visual, the engine adds the VISUAL SHAPE structure to the source table so that it can navigate in the hierarchies defined by the visual (ROWS and COLUMNS). Adding VISUAL SHAPE forces the table to undergo a densification process. Densification adds to the source table all the combinations of values that may be present, but that were skipped as part 

## Code / Examples

```
YOY % = VAR CY = [# Customers] VAR PY = CALCULATE ( [# Customers], SAMEPERIODLASTYEAR ( 'Date'[Date] ) ) VAR Result = DIVIDE ( CY - PY, PY ) RETURN Result
```
```
YOY % = VAR CY = [# Customers] VAR PY = PREVIOUS ( [# Customers], COLUMNS ) VAR Result = DIVIDE ( CY - PY, PY ) RETURN Result
```
```
DISTINCTCOUNT ( <ColumnName> )
```
```
PREVIOUS ( <Column> [, <Steps>] [, <Axis>] [, <OrderBy>] [, <Blanks>] [, <Reset>] )
```
```
SUMMARIZECOLUMNS ( [<GroupBy_ColumnName> [, [<FilterTable>] [, [<Name>] [, [<Expression>] [, <GroupBy_ColumnName> [, [<FilterTable>] [, [<Name>] [, [<Expression>] [, … ] ] ] ] ] ] ] ] ] )
```
```
BLANK ( )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations)*
