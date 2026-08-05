---
title: "CROSSFILTER Function: Control Relationships in Power BI DAX"
source: "https://databear.com/crossfilter-function-in-dax/"
author:
  - "[[Boniface Muchendu]]"
published: 2022-10-15
created: 2026-08-04
description: "Use the CROSSFILTER Function in Power BI to control relationship direction in DAX and improve model clarity and calculation flow."
Processed: "Unprocessed"
---
The CROSSFILTER Function falls under the category of FILTER functions in DAX. CROSSFILTER function can be used in a calculation for a relationship that exists between two columns.

The CROSSFILTER function is not a scalar or tubular function; it is a function that changes the directions of relationships in data models. We can use the function with other basic functions in Power BI, such as the CALCULATE function.

## Syntax of the DAX CROSSFILTER Function

CROSSFILTER(\<columnName1>, \<columnName2>, \<direction>

- **Column1**: The column on one side of the relationship
- **Column2**: the column on the other side of the relationship
- **direction**
- None: no filtering
- Both; filtering will propagate both ways
- Oneway; the filter propagates from one side of the relationship to the many sides
- Oneway\_LeftFiltersRight; the left table filters the right table in a one-to-one relationship.
- Oneway\_RightFiltersLeft; in a one-to-one relationship, the right table filters the left table.

## How to use DAX CROSSFILTER Function

To understand how the CROSSFILTER Function works, it would be ideal to use an example.

The table below shows a section of data obtained from fictional sales. The requirement is to establish a list of clients and the sales that are associated with them. This is possible as the Factinternetsales table is filtered by the DimCustomer table, as shown below.

![How to use DAX CROSSFILTER Function](99.System/Attachments/How_to_use_DAX_CROSSFILTER_Function.png)

The output below shows a single relationship between the two tables.

![ CROSSFILTER-Function-in-DAX-1.](99.System/Attachments/_CROSSFILTER-Function-in-DAX-1.png)

One of the requirement is to obtain a sum of all reseller sales of products every client has purchased. Obtaining this sum won’t be possible as their directions of relationships differ, and we have to find a way to change the relationships into bidirectional ones.

This does not work because the reseller sales were not filtered on the DimCustomer side; it is only filtered on the DimProduct side and DimProduct side is concurrently not filtered on the DimCustomer side as well.

![How to use DAX CROSSFILTER Function](99.System/Attachments/How_to_use_DAX_CROSSFILTER_Function.png)

### There are two ways of solving this:

We could decide to change the relationship between InternetFactSales and DimProduct both-directional – this would be a permanent change.

Alternatively, we could let the relationship stay as it is and establish a new, both-directional measure for this particular requirement. This is where DAX CROSSFILTER Function comes in.

Reseller Sales of the products purchased by a particular customer =

Calculate(

SUM(FatcResellerSales\[Reseller Sales\]),

CROSSFILTER(

DimProduct\[ProductKey\],

FactInternetSales\[ProductKey\],

Both

)

In the above code (expression), the CROSSFILTER Changes the direction of the relationship between DimProduct and FactInternetSales from a one-direction to a both-directional relationship. The result will be functional and work correctly, as shown below.

![There are two ways of solving this:](99.System/Attachments/There_are_two_ways_of_solving_this.png)

For multiple relationships for a data set, the CROSSFILTER function can apply using the same syntax as used above.

Just like other functions, there are several merits of using the CROSSFILTER Function that include:

The CROSSFILTER Function only works with an existing relationship between the two tables.

This is an ideal way of changing the direction of the relationship between two data tables. It is important to consider best modeling practices. This will ensure improved performance.

Ready to sharpen your DAX skills? Start using the [**CROSSFILTER Function**](https://databear.com/power-bi-training/) in your Power BI reports and experience cleaner, smarter data modeling.