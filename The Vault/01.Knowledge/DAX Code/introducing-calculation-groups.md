---
title: "Introducing Calculation Groups"
source: "https://www.sqlbi.com/articles/introducing-calculation-groups"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> This article is the first of a series dedicated to calculation groups in DAX. This introduction explains the capabilities of this feature and how to create

Introducing Calculation Groups - SQLBI Calculation groups are a new feature in DAX, inspired from a similar feature available in MDX known as calculated members. Calculation groups are easy to use; however, designing a model with calculation groups correctly can be challenging when you create multiple calculation groups or when you use calculation items in measures. Before we provide a description of calculation groups, it is useful to spend some time analyzing the business requirement that led to the introduction of this feature. An example involving time-related calculations fits perfectly well. Our sample model contains measures to compute the sales amount, the total cost, the margin, and the total quantity sold by using the following DAX code:  All four measures are useful, and they provide different insights into the business. Moreover, all four measures are good candidates for time intelligence calculations. A year-to-date over sales quantity can be as interesting as a year-to-date over sales amount and over margin. The same consideration is true for many other time intelligence calculations: same period last year, growth in percentage against the previous year, and many others. Nevertheless, if one wants to build all the different time intelligence calculations for all the measures, the number of measures in the data model may grow very quickly. In the real world, managing a data model with hundreds of measures is intimidating for both users and developers. Finally, consider that all the different measures for time intelligence calculations are simple variations of a common pattern. For example, the year-to-date versions of the previous list of four measures would look like the following:  All the previous measures only differ in their base measure; they all apply the same DATESYTD filter context to different base measures. It would be great if a developer were given the opportunity to define a more generic calculation, using a placeholder for the measure:  The previous code is not a valid DAX syntax, but it provides a very good description of what calculation items are. You can read the previous code as: When you need to apply the YTD calculation to a measure, call the measure after applying DATESYTD to the Date[Date] column . This is what a calculation item is: A calculation item is a DAX expression containing a special placeholder. The placeholder is replaced with a measure by the engine just before evaluating the result. In other words, a calculation item is a variation of an expression that can be applied to any measure. Moreover, you will likely find yourself needing several time intelligence calculations. Indeed, year-to-date, quarter-to-date, and same period last year are all calculations that somehow belong to the same group of calculations. Therefore, DAX offers calculation items and calculation groups. A calculation group is a set of calculation items that are conveniently grouped together because they are variations on the same topic. Let us continue with DAX pseudo-code:  As you can see, we grouped four time-related calculations in a group named Time Intelligence . In only four lines, the code defines dozens of different measures because the calculation items apply their variation to any measure in the model. Thus, as soon as a developer creates a new measure, the CY, PY, QTD, and YTD variations will be available at no cost. There are still several details missing in our understanding of calculation groups, but only one is required to start taking advantage of them and to define the first calculation group: How does the user choose one variation? As we said, a calculation item is not a measure; it is a variation of a measure. Therefore, a user needs a way to put in a report a specific measure with one or more variations of the measure itself. Because users have the habit of selecting columns from tables, calculation groups are implemented as if they were columns in tables, whereas calculation items are like values of the given columns. This way, the user can use the calculation group in the columns of a matrix to display different variations of a measure in the report. For example, the calculation items previously described are applied to the columns of a matrix, showing different variations of the Sales Amount measure. Creating calculation groups using Tabular Editor Tabular Editor is the first tool that enables developers creating calculation groups. Because calculation groups need the compatibility version 1470 of the Tabular model, as of June 2019 they only are available in Analysis Services 2019 and Azure Analysis Services. In Tabular Editor, the Model / New Calculation Group menu item creates a new calculation group, which appears as a table in the model with a special icon. In the following figure the calculation group has been renamed Time Intelligence . A calculation group is a special table with a single column, named Attribute by default in Tabular Editor. In our sample model 

## Code / Examples

```
Sales Amount := SUMX ( Sales, Sales[Quantity] * Sales[Net Price] ) Total Cost := SUMX ( Sales, Sales[Quantity] * Sales[Unit Cost] ) Margin := [Sales Amount] - [Total Cost] Sales Quantity := SUM ( Sales[Quantity] )
```
```
YTD Sales Amount := CALCULATE ( [Sales Amount], DATESYTD ( 'Date'[Date] ) ) YTD Total Cost := CALCULATE ( [Total Cost], DATESYTD ( 'Date'[Date] ) ) YTD Margin := CALCULATE ( [Margin], DATESYTD ( 'Date'[Date] ) ) YTD Sales Quantity := CALCULATE ( [Sales Quantity], DATESYTD ( 'Date'[Date] ) )
```
```
YTD <Measure> := CALCULATE ( <Measure>, DATESYTD ( 'Date'[Date] ) )
```
```
CALCULATION GROUP "Time Intelligence" CALCULATION ITEM CY := <Measure> CALCULATION ITEM PY := CALCULATE ( <Measure>, SAMEPERIODLASTYEAR ( 'Date'[Date] ) ) CALCULATION ITEM QTD := CALCULATE ( <Measure>, DATESQTD ( 'Date'[Date] ) ) CALCULATION ITEM YTD := CALCULATE ( <Measure>, DATESYTD ( 'Date'[Date] ) )
```
```
-- -- Calculation Item: YTD -- CALCULATE ( SELECTEDMEASURE (), DATESYTD ( 'Date'[Date] ) ) -- -- Calculation Item: QTD -- CALCULATE ( SELECTEDMEASURE (), DATESQTD ( 'Date'[Date] ) ) -- -- Calculation Item: SPLY -- CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
```
```
-- -- Calculation Item: Margin -- [Margin] -- -- Calculation Item: Sales Amount -- [Sales Amount] -- -- Calculation Item: Sales Quantity -- [Sales Quantity] -- -- Calculation Item: Total Cost -- [Total Cost]
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/introducing-calculation-groups)*
