---
title: "Using RANK instead of RANKX in DAX"
source: "https://www.sqlbi.com/articles/using-rank-instead-of-rankx-in-dax"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> Should you use RANK or stick with RANKX? In which scenarios is one better than the other? This article provides an in-depth analysis to help readers make in

Using RANK instead of RANKX in DAX - SQLBI In this article, we are not going to discuss the syntax of the RANK and RANKX functions. If you need more information, we suggest you consult DAX Guide for syntax, as well as the following articles, which introduce both functions: Introducing the RANK window function in DAX and Introducing RANKX in DAX . RANKX is the classic method of ranking in DAX; RANK is a newer window function that works faster, better, and in a more flexible way. RANK is used in both visual calculations and measures. Which function should you use in which scenario? The answer depends on your requirements: each solution has pros and cons. If you are interested in a quick answer, RANK is the preferred function to perform ranking, both in visual calculations and in measures. RANKX remains slightly more powerful in some complex scenarios, which, to be honest, are relatively rare in the real world. Since RANK is the preferred choice, the article primarily focuses on the few scenarios where RANKX remains useful. Consider the following report, which presents three methods for computing the ranking of brands based on their respective sales amounts. One measure uses RANKX , while the other two use RANK : one in a measure and the other in a visual calculation. The results remain the same, despite significant differences in the DAX code. Here is the code of the three different versions: Measure in Sales table  Measure in Sales table  Visual Calculation  Please note that both RankX and Visual Rank require an IF function to prevent the total from being displayed. Rank does not, as it blanks values if more than one row is visible in the filter context. Visual calculations or measures? The first choice is between a visual calculation and a measure. Mostly, values shown in Power BI are computed through measures. However, the main disadvantage of using a measure is that you need to hardcode in the measure itself the column over which you are performing the ranking. Both Rank and RankX require using ALLSELECTED ( Product[Brand] ) to identify the table for ranking. If a user removes the Product[Brand] column from the matrix and replaces it with, say, Product[Color] , then both measures produce a blank as a result. On the other hand, the visual calculation uses the ROWS keyword to identify the rows in the matrix, regardless of the actual columns used to populate the axis; therefore, it will work with whatever column is used. The only reference to Product[Brand] in the visual calculation is in the ISATLEVEL function call, not in RANK . Despite letting developers generate code that does not depend specifically on the column used for the ranking, visual calculations suffer from a drawback: a visual calculation can only work on data in the visual. It cannot use data from the model. For example, if one wants to compute the global ranking, regardless of the filters present in the report, a visual calculation is not the right choice. In contrast, both RANK and RANKX work well, as they allow developers to specify the table to be used for the ranking. The following two measures perform ranking over ALL rather than ALLSELECTED . Therefore, they produce a global ranking, ignoring the presence of filters from slicers and other visuals: Measure in Sales table  Measure in Sales table  Visual Calculation  The Visual Rank measure ranks brands from one to five, whereas the two measures maintain the global ranking, as if no filters were applied. Suppose you need a ranking calculation that is nearly independent from the column being used in the report, and you are ok with the limitation that the ranking needs to be responsive to any filter being applied to the visual. In that case, visual calculations are likely to be your best choice. The main advantage, which should not be underestimated, is their simplicity. However, if you need more power, you need a measure, and you still need to decide between RANK and RANKX . Choosing between RANK and RANKX RANK is a window function recently added to DAX. It is flexible, powerful, and easy to use. RANKX is the classic way of ranking; developers have never shown it too much love, because its syntax and semantics are somewhat intricate. Currently, RANK is a better alternative to RANKX because it is simpler for most tasks. RANK however is missing some of the features of RANKX . But these missing features are helpful in such exotic scenarios that they are rarely used. The main differences between RANK and RANKX are: RANK can rank on multiple columns easily by specifying multiple columns in the ORDERBY section. RANKX does not have the option of ranking over multiple columns. While it is certainly possible to use RANKX to rank on multiple columns (see RANKX on multiple columns with DAX and Power BI ), the code is intricate and prone to errors. RANK returns BLANK if the filter returns more than one row – among other reasons it can return BLANK . This spares us the need for the conditional logic of

## Code / Examples

```
Rank = RANK ( ALLSELECTED ( 'Product'[Brand] ), ORDERBY ( [Sales Amount], DESC ) )
```
```
RankX = IF ( ISINSCOPE ( 'Product'[Brand] ), RANKX ( ALLSELECTED ( 'Product'[Brand] ), [Sales Amount] ) )
```
```
Visual Rank = IF ( ISATLEVEL ( [Brand] ), RANK ( ROWS, ORDERBY ( [Sales Amount], DESC ) ) )
```
```
Rank ALL = RANK ( ALL ( 'Product'[Brand] ), ORDERBY ( [Sales Amount], DESC ) )
```
```
RankX ALL = IF ( ISINSCOPE ( 'Product'[Brand] ), RANKX ( ALL ( 'Product'[Brand] ), [Sales Amount] ) )
```
```
Visual Rank = IF ( ISATLEVEL ( [Brand] ), RANK ( ROWS, ORDERBY ( [Sales Amount], DESC ) ) )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/using-rank-instead-of-rankx-in-dax)*
