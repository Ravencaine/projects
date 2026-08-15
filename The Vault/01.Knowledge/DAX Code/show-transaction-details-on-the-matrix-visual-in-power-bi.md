---
title: "Show transaction details on the matrix visual in Power BI"
source: "https://www.sqlbi.com/articles/show-transaction-details-on-the-matrix-visual-in-power-bi"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> This article shows how to create a DAX measure that displays information from multiple columns in a business entity or transaction, into a single column of

Show transaction details on the matrix visual in Power BI - SQLBI A common challenge in Power BI reporting is how to display several pieces of information about a single item (such as sales transactions, product details, or customer details) without dedicating a separate column to each attribute. Using individual columns for each detail can consume space, especially for fields that are often empty. This article explores techniques to consolidate multiple fields from a business entity or transaction into a single column in a matrix visual, thus presenting transaction details in a space-efficient way. Dealing with multiple columns Presenting detailed information about a business entity often requires displaying values from multiple columns, which can take up too much space in Power BI reports and make them harder to read. Indeed, a consequence of there being too many columns is that we now have to use a horizontal scrollbar. So instead of using a separate column for each detail, it would be better to combine relevant fields and show them together in a single column, especially in a matrix visual. This section introduces the challenge and presents approaches to representing multiple attributes more efficiently, thus leading to advanced solutions using DAX measures in the next sections. Including multiple columns in a table To display transaction details across multiple columns in a table, we could create a separate table visual that shows the relevant fields for the selected item. This table must be synchronized with the matrix visual, typically by selecting an order number or unique identifier in the matrix, which then filters the table to display the associated details. In this example, the Order Number selection displays the customer details in a separate table. While this approach enables you to show all the details, it consumes additional space on the report canvas because you need both the matrix and the table visual. To partially address the space issue, we created a visual calculation that collapses multiple columns into a single Details column. This Details column can display concatenated information from several fields, which saves space (as illustrated by the green arrow). However, this solution comes with limitations: the synchronization between the matrix and the table is manual, and it requires users to click on the desired item in the matrix. Additionally, the columns used in the visual calculation cannot be hidden in the table; the common workaround is to set their width to 0, but this is not ideal, and in general, it is not a fully-integrated solution within the matrix visual because it requires a separate visual. Including multiple columns in a matrix Including multiple detail columns in a matrix visual adds hierarchical levels, making navigation difficult and potentially hurting query performance. The layout can also become unclear, as shown when several customer attributes appear under the order number (152200 in this example). Just adding columns to the matrix is not the way to go. Collecting data in a measure When presenting a unique business identifier, such as a Product Code , Customer Code , or Order Number , you may want to show extra details in a Details column that, in reality, is a measure appearing after other measures in the matrix. This allows you to display transaction information directly, which eliminates the need for additional drill-down actions. Here is an example of what we want to obtain. To create this example, we defined a prototype measure to validate the design: Measure in Sales table  The Details prototype measure displays a fixed string when a specific order is selected. However, a measure can navigate the internal structure of the model to retrieve the required data. There are multiple possible approaches, because we can obtain the same result with different techniques. The goal of the article is to present several of these techniques, along with considerations regarding the performance and maintainability of the solution. If you are interested in using the best solution, just skip to the final section. However, it is worth spending time learning the pros and cons of different approaches, because there is always a chance that you encounter scenarios where one of the other alternatives is better for you. Details measure – version 0 This section is purely educational and shows how to explore the individual features we will use in the following complete implementations. The first measure we implement displays the currency and exchange rate for the transaction, all of which are available in the Sales table: Measure in Sales table  The first issue to address is that the information is also visible when multiple orders share the same currency code. This can be solved by ensuring that only one order is visible: using ISINSCOPE guarantees that the Order Number is also displayed in the matrix visual, not just filtered outside of the visual. By checking that there is a row 

## Code / Examples

```
Details prototype = IF ( SELECTEDVALUE ( Sales[Order Number] ) = 152200, "Description of the customer" )
```
```
Details v0.A = VAR CurrencyCode = SELECTEDVALUE ( Sales[Currency Code] ) VAR ExchangeRate = SELECTEDVALUE ( Sales[Exchange Rate] ) RETURN IF ( NOT ISBLANK ( CurrencyCode ), CurrencyCode & "/USD=" & ExchangeRate )
```
```
Details v0.B = IF ( ISINSCOPE ( Sales[Order Number] ) && NOT ISEMPTY ( Sales ), VAR CurrencyCode = VALUES ( Sales[Currency Code] ) VAR ExchangeRate = VALUES ( Sales[Exchange Rate] ) RETURN CurrencyCode & "/USD=" & ExchangeRate )
```
```
Details v0.C = IF ( ISINSCOPE ( Sales[Order Number] ) && NOT ISEMPTY ( Sales ), VAR CurrencyCode = VALUES ( Sales[Currency Code] ) VAR ExchangeRate = VALUES ( Sales[Exchange Rate] ) RETURN IF ( NOT ISBLANK ( CurrencyCode ) && NOT ISBLANK ( ExchangeRate ), CurrencyCode & "/USD=" & ExchangeRate ) )
```
```
Details v0.D = IF ( ISINSCOPE ( Sales[Order Number] ), CONCATENATEX ( FILTER ( { VALUES ( Sales[Currency Code] ), VALUES ( Sales[Exchange Rate] ) }, [Value] <> "" ), [Value], ", " ) )
```
```
Details V1 = IF ( ISINSCOPE ( Sales[Order Number] ), CALCULATE ( CONCATENATEX ( FILTER ( { VALUES ( Customer[Country Code] ), VALUES ( Customer[State Code] ), VALUES ( Customer[City] ), VALUES ( Customer[Name] ), VALUES ( Customer[Age] ) }, [Value] <> "" ), [Value], ", " ), CROSSFILTER ( Sales[CustomerKey], Customer[CustomerKey], BOTH ) ) )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/show-transaction-details-on-the-matrix-visual-in-power-bi)*
