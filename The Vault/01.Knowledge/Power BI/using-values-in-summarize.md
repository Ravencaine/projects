---
title: "Using VALUES in SUMMARIZE"
source: "https://www.sqlbi.com/articles/using-values-in-summarize"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, reading-list]
created: "2026-08-11"
---

> This article describes when to use VALUES in a table grouped by SUMMARIZE, then goes on to explain why you cannot however use VALUES with SUMMARIZECOLUMNS.

Using VALUES in SUMMARIZE - SQLBI We discussed VALUES in previous articles: Choosing between DISTINCT and VALUES in DAX and Using VALUES in iterators . However, there is a third case where VALUES could be used with a table reference, which is when you use SUMMARIZE to group by columns you want to iterate. In this article, we describe this particular scenario to understand when VALUES is needed to retrieve the blank for an invalid relationship using SUMMARIZE and SUMMARIZECOLUMNS . When you use SUMMARIZE , you may want to use VALUES over the aggregated table in case it could have an additional blank row for an invalid relationship, and you must ensure that this blank row is included. This condition is uncommon because SUMMARIZE often includes blank rows for invalid relationships that are implicitly included. For example, consider the following measure that uses SUMMARIZE over the Sales table, grouping by Customer[State] and Customer[City] to apply an adjustment to Columbus, Ohio (note that there are other cities with that name in other states): Measure in Sales table  Because SUMMARIZE groups data from Sales , the presence of a blank row for Customer is included in the result of the SUMMARIZE function. However, grouping Customer in SUMMARIZE produces a different result: Measure in Sales table  The following report shows the differences between the Test Summarize Sales and Test Summarize Customer measures: the “Summarize Sales” column shows the right amount, whereas “Summarize Customer” shows that the Test Summarize Customer measure does not include the amount of the blank row, which in turn reduces the Total row. The report also shows two other measures that return the correct result. If you must use the Customer table in SUMMARIZE and you need the blank row, you can use VALUES around the table reference in SUMMARIZE , as we do in the Test Summarize Values Customer measure: Measure in Sales table  The last example of a correct measure uses SUMMARIZECOLUMNS instead of SUMMARIZE : Measure in Sales table  We must mention that using SUMMARIZECOLUMNS in this case includes the blank row if present, although the code of Test SummarizeColumns (not using best practice) does not follow the best practices of SUMMARIZECOLUMNS in a measure. Indeed, it does not include any aggregation. Here is a better implementation that considers the best practices for using SUMMARIZECOLUMNS in a measure: Measure in Sales table  To recap, use VALUES over the table reference for SUMMARIZE when you group by a table that is on the one-side of a regular relationship, and you want to make sure to include the blank row caused by an invalid relationship. Usually, this is unnecessary when you pass the table on the many-side of a relationship to SUMMARIZE . If you use SUMMARIZECOLUMNS , the blank row is included, but you should always follow the best practices for SUMMARIZECOLUMNS . When a column name is given, returns a single-column table of unique values. When a table name is given, returns a table with the same columns and all the rows of the table (including duplicates) with the additional blank row caused by an invalid relationship if present.  Creates a summary of the input table grouped by the specified columns.  Create a summary table for the requested totals over set of groups.  Downloads Insert your email address and press Download for access to the files used in this article. Download Keep me informed about BI news and upcoming articles with a bi-weekly newsletter (uncheck if you prefer to proceed without signing up for the newsletter) Send me SQLBI promotions (only 1 or 2 emails per year) By downloading the file(s), you agree to our Privacy Policy . This site is protected by reCAPTCHA.

## Code / Examples

```
Test Summarize Sales = SUMX ( SUMMARIZE ( Sales, Customer[State], Customer[City] ), [Sales Amount] * IF ( Customer[State] = "Ohio" && Customer[City] = "Columbus", .99, 1 ) )
```
```
Test Summarize Customer = SUMX ( SUMMARIZE ( Customer, Customer[State], Customer[City] ), [Sales Amount] * IF ( Customer[State] = "Ohio" && Customer[City] = "Columbus", .99, 1 ) )
```
```
Test Summarize Values Customer = SUMX ( SUMMARIZE ( VALUES ( Customer ), Customer[State], Customer[City] ), [Sales Amount] * IF ( Customer[State] = "Ohio" && Customer[City] = "Columbus", .99, 1 ) )
```
```
Test SummarizeColumns (not using best practice) = SUMX ( SUMMARIZECOLUMNS ( Customer[State], Customer[City] ), [Sales Amount] * IF ( Customer[State] == "Ohio" && Customer[City] == "Columbus", .99, 1 ) )
```
```
Test SummarizeColumns = SUMX ( SUMMARIZECOLUMNS ( Customer[State], Customer[City], "@Sales", [Sales Amount] ), [@Sales] * IF ( Customer[State] == "Ohio" && Customer[City] == "Columbus", .99, 1 ) )
```
```
VALUES ( <TableNameOrColumnName> )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/using-values-in-summarize)*
