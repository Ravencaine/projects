---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# SUMMARIZE

## Syntax

```dax
SUMMARIZE(ResellerSales_USD, DateTime[CalendarYear], ProductCategory[ProductCategoryName], "Sales Amount (USD)
```

## Remarks

Each column for which you define a name must have a corresponding expression; otherwise, an error is returned. The first argument, name, defines the name of the column in the results. The second argument, expression, defines the calculation performed to obtain the value for each row in that column. groupBy_columnName must be either in table or in a related table to table. Each name must be enclosed in double quotation marks. The function groups a selected set of rows into a set of summary rows b
