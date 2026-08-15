---
title: "Understanding Calculation Groups"
source: "https://www.sqlbi.com/articles/understanding-calculation-groups"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, reading-list]
created: "2026-08-11"
---

> This article explores the properties of calculation groups in detail and then it describes how a calculation item is applied to a measure. Before starting,

Understanding Calculation Groups - SQLBI There are two entities to consider: calculation groups and calculation items. A calculation group is a collection of calculation items, grouped together based on a user-defined criterion. For both calculation groups and calculation items, there are properties that the developer must set correctly. A calculation group is a simple entity, defined by: The calculation group Name . This is the name of the table that represents the calculation group on the client side. The calculation group Precedence . When there are multiple active calculation groups, a number that defines the precedence used to apply each calculation group to a measure reference. The calculation group attribute Name . This is the name of the column that includes the calculation items, displayed to the client as unique items available in the column. A calculation item is a much more sophisticated entity, and here is the list of its properties: The calculation item Name . This becomes one value of the calculation group column. Indeed, a calculation item is like one row in the calculation group table. The calculation item Expression . A DAX expression that might contain special functions like SELECTEDMEASURE . This is the expression that defines how to apply the calculation item. The sort order of the calculation item is defined by the Ordinal value. This property defines how the different calculation items are sorted when presented to the user. It is very similar to the sort-by-column feature of the data model. Format String Expression . If not specified, a calculation item inherits the format string of its base measure. Nevertheless, if the modifier changes the calculation, then it is possible to override the measure format string with the format of the calculation item. The Format String Expression property is important in order to obtain a consistent behavior of the measures in the model according to the calculation item being applied to them. For example, consider the following calculation group containing two calculation items for time intelligence: year-over-year ( YOY ) is the difference between a selected period and the same period in the previous year; year-over-year percentage ( YOY% ) is the percentage of YOY over the amount in the same period in the previous year:  The result produced by these two calculation items in a report is correct, but if the Format String Expression property does not override the default format string, then YOY% is displayed as a decimal number instead of a percentage. The example displays the YOY evaluation of the Sales Amount measure using the same format string as the original Sales Amount measure. This is the correct behavior to display a difference. However, the YOY% calculation item displays the same amount as a percentage of the value of the previous year. The number shown is correct, but for January one would expect to see 12% instead of 0.12. In this case the expected format string should be a percentage, regardless of the format of the original measure. To obtain the desired behavior, set the Format String Expression property of the YOY% calculation item to percentage, overriding the behavior of the underlying measure. If the Format String Expression property is not assigned to a calculation item, the existing format string is used. The format string can be defined using a fixed format string or in more complex scenarios by using a DAX expression that returns the format string. When writing a DAX expression, it is possible to refer to the format string of the current measure using the SELECTEDMEASUREFORMATSTRING function, which returns the format string currently defined for the measure. For example, if the model contains a measure that returns the currently selected currency and you want to include the currency symbol as part of the format string, you can use this code to append the currency symbol to the current format string:  Customizing the format string of a calculation item is useful to preserve user experience consistency when browsing the model. However, a careful developer should consider that the format string operates on any measure used with the calculation item. When there are multiple calculation groups in a report, the result produced by these properties also depends on the calculation group precedence. Introducing calculation item application The details of how a calculation item is applied are quite intricate. This article introduces the topic and provide some best practices. A following article will describe the topic in depth with more complex examples. Calculation items can be applied by the user using, for example, a slicer, or by using CALCULATE to filter the calculation group. For example, consider the following calculation item:  In order to apply the calculation item in an expression, you filter the calculation group:  There is nothing magical about calculation groups: They are tables, and as such they can be filtered by CALCULATE li

## Code / Examples

```
-- -- Calculation Item: YOY -- VAR CurrYear = SELECTEDMEASURE () VAR PrevYear = CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( 'Date'[Date] ) ) VAR Result = CurrYear - PrevYear RETURN Result -- -- Calculation Item: YOY% -- VAR CurrYear = SELECTEDMEASURE () VAR PrevYear = CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( 'Date'[Date] ) ) VAR Result = DIVIDE ( CurrYear - PrevYear, PrevYear ) RETURN Result
```
```
SELECTEDMEASUREFORMATSTRING () & " " & [Selected Currency]
```
```
-- -- Calculation Item: YTD -- CALCULATE ( SELECTEDMEASURE (), DATESYTD ( 'Date'[Date] ) )
```
```
CALCULATE ( [Sales Amount], 'Time Intelligence'[Time calc] = "YTD" )
```
```
CALCULATE ( CALCULATE ( [Sales Amount], DATESYTD ( 'Date'[Date] ) ) )
```
```
CALCULATE ( SUMX ( Sales, Sales[Quantity] * Sales[Net Price] ), 'Time Intelligence'[Time calc] = "YTD" )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/understanding-calculation-groups)*
