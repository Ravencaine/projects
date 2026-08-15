---
title: "Understanding the interactions between composite models and calculation groups"
source: "https://www.sqlbi.com/articles/understanding-the-interactions-between-composite-models-and-calculation-groups"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> When used in a composite model, calculation groups show a very unique behavior that a good DAX developer must understand well to build sound models. In this

Understanding the interactions between composite models and calculation groups - SQLBI Both composite models and calculation groups are extremely powerful features that were added to Power BI rather recently. Specifically, composite models are changing the way users build their models. Users can extend an existing corporate model rather than starting from scratch every time. That said, when building a composite model you must pay attention to several subtle details: performance, the use of ALLSELECTED , and calculation groups. In this article, we cover only calculation groups, and we take for granted that the reader has some knowledge of local and remote models, and of wholesale and retail queries. If you are not familiar with the terms, you can find more information here: Introducing wholesale and retail execution in composite models . Though you can define calculation groups in both the local and the remote models, there is a limitation in the way calculation groups are applied. The limitation is short in its definition, but its effects are rather surprising: A local calculation group is applied to any sub-query, whereas a remote calculation group is applied only to wholesale sub-queries; it is not applied to retail sub-queries. The key to understanding the limitation well is the word sub-query. Any query executed by the local server results in multiple sub-queries. Some are retail (if they use any local table) whereas others are wholesale (if the entire execution can be pushed to the remote server). Both wholesale and retail sub-queries are part of an individual query: part of the query is executed locally and other parts are executed remotely. In such scenarios, remote calculation groups are applied only to wholesale sub-queries. Any retail sub-query is not affected by the remote calculation group. On the other hand, local calculation groups are applied to both local and remote sub-queries. The reason is that the DAX engine applies the calculation group before executing the query. The engine must know the definition of the calculation items to apply the calculation group. For a locally-defined calculation group, the engine knows the DAX code used in the definition of the calculation group itself, so that it can apply the calculation group. The code of remotely-defined calculation groups is not available to the local DAX engine. Therefore, the local DAX engine cannot apply a remotely-defined calculation group to retail code. In order to better understand the scenario, we prepared a Contoso model with one calculation group containing two items, CY and YTD:  When used in a report, the calculation group works just fine and provides the current value and the year-to-date variation of any measure. The model is published on the Power BI service. Based on this model, we create a new composite model to simulate a discount based on the product category. Therefore, we add a new table to the composite model containing the discount percentage by category, and then we use the table to compute the discounted price. Below is the new table added to the model. We create a relationship between Product and the new Discounts table, based on Product[Category] . The next step is to create a measure that computes the discounted sales. The same measure can be computed in different ways, leading to different execution plans. Instead of providing just one version, we prefer to show different ways to express the code along with a few considerations about the accuracy of the code. Beware that here, we are not interested in analyzing performance. Instead, the focus is only on how different formulations of the same code produce different results. A first attempt to author the Discounted Sales measure could be the following – which is incorrect:  This first version does not work, because you cannot use RELATED to fetch a column through a limited (weak) relationship. RELATED works only through regular (strong) relationships. You could avoid using RELATED by replacing it with LOOKUPVALUE , thus mimicking the relationship through more verbose DAX code:  Apart from performance considerations (this measure is awful), the Discounted Sales (Wrong) measure produces the correct result. Nonetheless, the Discounted Sales (Wrong) measure displays a major drawback. Its execution is retail, because in the same expression it is mixing values retrieved by the remote model and values retrieved from the local model. Therefore, most of the calculation is executed locally after the local model retrieved the content of Sales . Because the measure is retail, the remote calculation group is not applied to Discounted Sales . In the next figure, the YTD calculation item works on Sales Amount but it does not produce any effect on Discounted Sales . The measure can be written so that the calculation of Sales Amount becomes wholesale before the application of the discount. Indeed, the following version of Discounted Sales is faster, easier, and it executes whole

## Code / Examples

```
------------------------------------------------ -- Calculation Group: 'Remote Time Intelligence' ------------------------------------------------ CALCULATIONGROUP 'Remote Time Intelligence'[Remote Time Intelligence] CALCULATIONITEM "CY" = SELECTEDMEASURE () CALCULATIONITEM "YTD" = CALCULATE ( SELECTEDMEASURE (), DATESYTD ( 'Date'[Date] ) )
```
```
Discounted Sales (Error) := SUMX ( Sales, Sales[Quantity] * Sales[Net Price] * ( 1 - RELATED ( Discounts[Discount%] ) ) )
```
```
Discounted Sales (Wrong) := SUMX ( Sales, Sales[Quantity] * Sales[Net Price] * ( 1 - LOOKUPVALUE ( Discounts[Discount%], Discounts[Category], RELATED ( 'Product'[Category] ) ) ) )
```
```
Discounted Sales := SUMX ( Discounts, [Sales Amount] * ( 1 - Discounts[Discount%] ) )
```
```
Discount := [Sales Amount] - [Discounted Sales (Wrong)]
```
```
ALLSELECTED ( [<TableNameOrColumnName>] [, <ColumnName> [, <ColumnName> [, … ] ] ] )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/understanding-the-interactions-between-composite-models-and-calculation-groups)*
