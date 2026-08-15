---
title: "Using calculation groups to selectively replace measures in DAX expressions"
source: "https://www.sqlbi.com/articles/using-calculation-groups-to-selectively-replace-measures-in-dax-expressions"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> This article describes how to use calculation groups to dynamically replace only a partial expression in a complex DAX calculation. This article contains a

Using calculation groups to selectively replace measures in DAX expressions - SQLBI This article contains a shorter technical description of the requirement and of the solution, and a longer explanation of the reasons why the solution proposed is required and why other approaches may fail. If you are familiar with calculation groups in DAX, you probably only need to read the first part of the article which is short and straight to the point. If calculation groups are relatively new to you, or if you would like to read a more detailed explanation about why this technique is required, then you can also enjoy the second part of the article. That longer section is designed to first make sense of the problem, then of the technique used, and possibly to make you want to know calculation groups better. Ready? Let’s begin! Part 1: Applying a calculation group to a specific measure Calculation groups replace measure references with the DAX expression of the calculation item that is active in the filter context. Because the replacement takes place only at the report level where the calculation groups are usually applied, it is not possible to propagate the replacement to measure references used in nested calculations. This behavior limits your ability to apply calculation groups only to a specific subexpression of a complex DAX calculation. For example, consider the following Daily Sales and Monthly Sales measures:  If your requirement is to modify the Sales Forecast measure through a slicer selection, you cannot use a calculation group to define different implementations of Sales Forecast . You should rewrite the DIVIDE expressions in the calculation group because SELECTEDMEASURE corresponds to Daily Sales or Monthly Sales . The solution is to move the original Sales Forecast implementation into an Internal Sales Forecast measure; then, you want to define Sales Forecast with a measure that applies the required calculation item based on the current selection of a table (called Choice ) that contains a copy of the items of the calculation group (called InternalChoice ):  The Sales Forecast implementation controls the application of the calculation item so that the latter affects only the Internal Sales Forecast measure. The Choice table is the only one visible to the user, whereas the calculation group implemented as InternalChoice is not visible to the user. This technique defers the application of the calculation group to the desired expressions; it does so without limiting your ability to create other measures on top of the ones affected by the calculation group. Part 2: Understanding how calculation groups can be applied to partial expressions We know: Part 1 is hard. However, you do not need to be scared. Our goal was to introduce the problem and pique your interest so you would read this long article – you may need it in the future when faced with a similar scenario. You can read Part 1 again once you complete the article. At that point, you will be able to understand all the implications of this calculation technique. Calculation groups require a lot of concentration. The first important detail we always need to remember with calculation groups is that things are seldom as easy as we would like them to be. Forgetting the theory of evaluation and application of calculation items can result in very undesired and hard-to-understand results. To demonstrate this, we start by analyzing a common scenario; we then guide you in understanding the problem, and finally we guide you towards the solution. We wrote the article describing exactly the path that led to the solution. In other words, we describe the same reasoning and the same mistakes we did back when we were studying the topic. This article is a sneak peek into two hours of real life at SQLBI! In order to show the problem with the Contoso database, we assumed that Contoso sometimes analyzes their sales taking the discounts into account, and sometimes ignoring them. Therefore, the value of Sales Amount can be computed using the Unit Price – which is not reflecting any discounts – or using the Net Price , consequently taking the discount as part of the equation. Different values for Sales Amount have a domino effect on other measures. The margin percentage for example is different depending on whether you consider the Unit Price or the Net Price . If you look at the following figure, you can see that the margin computed using Net Price ( Margin % NP ) is lower than the margin considering the Unit Price ( Margin % UP ). In order to build the report, we have authored different versions of the measures which reflect the different ways of computing Sales Amount :  In a real model, the number of measures would quickly grow: you might end up having two versions of each measure, depending on the definition of Sales Amount . The problem is not limited to the measures. The reports should be duplicated too, because the algorithm is hardcoded in the measures used by the repo

## Code / Examples

```
Daily Sales := DIVIDE ( [Sales Forecast], [Days] ) Monthly Sales := DIVIDE ( [Sales Forecast], [Months] )
```
```
Sales Forecast := CALCULATE ( [Internal Sales Forecast], TREATAS ( VALUES ( Choice[Selection] ), InternalChoice[Selection] ) )
```
```
Sales Amount (NP) := SUMX ( Sales, Sales[Quantity] * Sales[Net Price] ) Sales Amount (UP) := SUMX ( Sales, Sales[Quantity] * Sales[Unit Price] ) Margin % (NP) := VAR SalesAmount = Sales[Sales Amount (NP)] VAR SalesCost = [Total Cost] VAR Result = DIVIDE ( SalesAmount - SalesCost, SalesAmount ) RETURN Result Margin % (UP) := VAR SalesAmount = Sales[Sales Amount (UP)] VAR SalesCost = [Total Cost] VAR Result = DIVIDE ( SalesAmount - SalesCost, SalesAmount ) RETURN Result
```
```
CALCULATIONITEM 'PriceToUse'[PriceToUse]."Net Price" = SUMX ( Sales, Sales[Quantity] * Sales[Net Price] ) CALCULATIONITEM 'PriceToUse'[PriceToUse]."Unit Price" = SUMX ( Sales, Sales[Quantity] * Sales[Unit Price] )
```
```
Margin % := VAR SalesAmount = [Sales Amount] VAR SalesCost = [Total Cost] VAR Result = DIVIDE ( SalesAmount - SalesCost, SalesAmount ) RETURN Result
```
```
CALCULATIONITEM PriceToUse[PriceToUse]."Net Price" = IF ( ISSELECTEDMEASURE ( [Sales Amount] ), SUMX ( Sales, Sales[Quantity] * Sales[Net Price] ) ) CALCULATIONITEM PriceToUse[PriceToUse]."Unit Price" = IF ( ISSELECTEDMEASURE ( [Sales Amount] ), SUMX ( Sales, Sales[Quantity] * Sales[Unit Price] ) )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/using-calculation-groups-to-selectively-replace-measures-in-dax-expressions)*
