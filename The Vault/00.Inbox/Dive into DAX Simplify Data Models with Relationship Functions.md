---
title: "Dive into DAX: Simplify Data Models with Relationship Functions"
source: "https://medium.com/microsoft-power-bi/dive-into-dax-simplify-data-models-with-relationship-functions-57d41587e83a"
author:
  - "[[Ethan Guyant]]"
published: 2024-06-04
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Learn the art of data modeling and how to enhance your analysis with DAX Relationship Functions.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7_S8KclciaI_OfXie9afOg.png)

## The Basics of DAX Relationship Functions

DAX Relationship Functions are an essential part of our data modeling toolkit. These functions allow us to navigate the relationships connecting our data model tables facilitating complex calculations and deriving the insights they provide.

Relationships in our data models matter because they help maintain the integrity and consistency of our data. They connect different tables, enabling us to create insightful and dynamic reports. When creating our Power BI reports understanding these relationships becomes crucial since they dictate how data filters and aggregations are applied throughout our reports.

DAX Relationship Functions allow us to control and manipulate these relationships to suite our specific needs. Using these functions, we can perform in-depth calculations that involve multiple tables. They can be particularly useful in scenarios where we need to bring data from different sources into a single coherent view. Understanding and utilizing these functions can significantly elevate our data analysis.

For details on these functions visit the DAX Function Reference documentation.

## [Relationship functions (DAX) - DAX](https://learn.microsoft.com/en-us/dax/relationship-functions-dax?source=post_page-----57d41587e83a---------------------------------------)

### Learn more about: Relationship functions

learn.microsoft.com

For those eager to start experimenting there is a Power BI report pre-loaded with the same data used in this post ready for you! So don’t just read, follow along and get hands-on with DAX in Power BI. Get a copy of the sample report here:

## [GitHub - EMGuyant/powerbi-dax-functions-series](https://github.com/EMGuyant/powerbi-dax-functions-series?source=post_page-----57d41587e83a---------------------------------------)

github.com

## RELATED: Fetching Related Values

The RELATED function in DAX is designed to fetch a related value from another table. Its syntax is straightforward.

```c
RELATED(column_name)
```

Here, `column_name` is the column from the related table that we want to retrieve. This function can be particularly useful in calculated columns when we need to access data from a lookup table in our calculations.

The RELATED function requires that a relationship exists between the two tables. Then the function can navigate the existing many-to-one relationship and fetch the specified column from the related table. In addition to an existing relationship, the RELATED function requires row context.

Our `Sales` table has a `ProductID` which is used to establish a relationship in our data model to the `Products` table. Let's bring in the `Product` field from the `Products` table into our `Sales` table.

```c
Product Category = RELATED(Products[Product])
```

We can use this DAX formula to add a new calculated column to our `Sales` table showing the product category corresponding to each sales record. This can help make our sales data more informative and easier to analyze, as we can now see the product category directly in the sales table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*YCePaiA57VpHdRnQ)

We can also use RELATED and the existing relationship between our `Sales` and `Regions` table to filter our `Sales` and create an explicit United States Sales. Let's take a look at this measure.

```c
United States Sales = 
SUMX(
   FILTER(
      Sales, 
      RELATED(Regions[Region]) = "United States"
   ), 
   Sales[Amount]
)
```

This formula is much more informative and clearer than filtering directly on the `RegionID` field contained within the `Sales` table. Using RELATED within our FILTER function like this makes our measure more readable and it can immediately be identified what this measure is calculating.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*T93G4DFpobM7h8UB)

The RELATED function is a powerful tool for enhancing our data models by seamlessly integrating related information. This can help us create more detailed and comprehensive reports.

## RELATEDTABLE: Navigating Related Tables

The RELATEDTABLE function in DAX allows us to navigate and retrieve a table related to the current row from another table. This function can be useful when we need to summarize or perform calculations on data from a related table based on the current context. Here is its syntax.

```c
RELATEDTABLE(table_name)
```

Here, `table_name` is the name of an existing related table that we want to retrieve. The `table_name` parameter cannot be an expression.

Let’s consider a scenario where we want to calculate the total sales amount for each product using the RELATEDTABLE function. Here is how we can use it to create a new calculated column in our `Products` table.

```c
Total Sales by Product = 
SUMX(
   RELATEDTABLE(Sales), 
   Sales[Amount]
)
```

In the DAX expression, we sum the `Amount` column from the `Sales` table for each product. The RELATEDTABLE function fetches all the rows from the `Sales` table that are related to the current product row in the `Products` table, and SUMX sums the `Amount` column for these rows.

![](https://miro.medium.com/v2/resize:fit:1276/format:webp/0*Hk-3XP_cw_Q0Auco)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*OtZcMlkBdXybaljQ)

When we use RELATEDTABLE, we can navigate and perform calculations across related tables, enhancing our ability to analyze data in a more granular and insightful way.

## USERELATIONSHIP: Activating Inactive Relationships

The USERELATIONSHIP function in DAX is designed to activate an inactive relationship between tables in a data model. This is useful when a table has multiple relationships with another table, and we need to switch between these relationships for different calculations. Here is its syntax.

```c
USERELATIONSHIP(column1, column2)
```

Here, `column1` is the name of an existing column and typically represents the many side of the relationship to be used. The `column2` is the name of an existing column and typically represents the one side or lookup side of the relationship to be used.

The USERELATIONSHIP returns no value and can only be used in functions that take a filter as argument (e.g. CALCULATE, TOTALYTD). The function uses existing relationships in the data model and cannot be used when row level security is defined for the table in which the measure is included.

Let’s take a look at a scenario where we are interested in calculating the number of employees who have left the organization based on their end dates using the USERELATIONSHIP function.

The `Employee` table includes each employee's `StartDate` and `EndDate`. Each of these columns are used to establish a relationship with the `DateTable` in the data model. The relationship with `StartDate` is set to active, while the relationship with `EndDate` is inactive.

![](https://miro.medium.com/v2/resize:fit:1182/format:webp/0*nXAu5xnnV-4pIVlk)

We can use the following DAX formula to define our Employee Separations measure.

```c
Employees Separations USERELATIONSHIP = 
CALCULATE(
   COUNT(Employee[EmployeeID]), 
   USERELATIONSHIP(Employee[EndDate], DateTable[Date]), 
   NOT(ISBLANK(Employee[EndDate]))
)
```

This measure calculates the number of employees who have left the organization based on their `EndDate` by activating the inactive relationship between `Employee[EndDate]` and `DateTable[Date]` and ensuring that it only counts employees who have an `EndDate`.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*CBAjQLqqWhGMMQqM)

We can better understand the power of USERELATIONSHIP by comparing these results to the results of the same measure but this time without activating the inactive relationship.

```c
Employee Separations No USERELATIONSHIP = 
CALCULATE(
   COUNT(Employee[EmployeeID]), 
   NOT(ISBLANK(Employee[EndDate]))
)
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*wMDavxJyZnjP1ekO)

In the `No USERELATIONSHIP` measure we try to calculate the number of employees who left the company based on `EndDate`. However, we can see that without activating the relationship the active relationship is used in the context of the calculation.

Of the 9 employees that have left the organization, we can see that for 2022 the `No USERELATIONSHIP` measure is counting the 8 employees that started in 2022 rather than the 3 that left in 2022.

## CROSSFILTER: Controlling Cross-Filtering Behavior

The CROSSFILTER function in DAX helps us manage the direction of cross-filtering between two tables in our data model. With this function we specify whether the filtering direction is one-way, both ways, or none, providing control over how data flows between our tables. This becomes useful in complex models where bidirectional filtering can lead to unintended results. Here is its syntax.

```c
CROSSFILTER(column1, column2, direction)
```

The parameters `column1` and `column2` are similar to the parameters of USERELATIONSHIP, where `column1` is the name of an existing column and typically represents the many side of the relationship and `column2` is a column name and typically represents the one side of the relationship.

The `direction` parameter specifies the cross-filter direction to be used and must be one of the following values.

- **None** — no cross-filtering occurs along this relationship
- **Both** — filters on either side filters the other side
- **OneWay** — filters on the one side of a relationship filter the other side. This option cannot be used with a one-to-one relationship and is not recommended for many-to-many relationships.
- **OneWay\_LeftFiltersRight** — filters on the side of `column1` filter the side of `column2`. This option cannot be used with a one-to-one or many-to-one relationship.
- **OneWay\_RightFiltersLeft** — filters on the side of `column2` filter the side of `column1`. This option cannot be used with a one-to-one or many-to-one relationship.

The CROSSFILTER function returns no value and can only be used within functions that take a filter as an argument (e.g. CALCULATE, TOTALYTD). When we establish relationships in our data model we define the cross-filtering direction, when we use the CROSSFILTER function it overrides this setting.

Let’s consider the scenario where we want to analyze the distinct products sold and the total sales amount by month and year. We start by creating a Distinct Product Code Count measure.

```c
Distinct Product Code Count = 
DISTINCTCOUNT(Products[Product Code])
```

If we add this measure to a table visual, we will notice an issue with the count. The count is returning the total product code count, and not the intended results of the count of distinct products sold that month.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*catgLZN-5XQgSNB_)

We see this because the relationship is one-to-many (Product-to-Sales) with single direction relationship (i.e. Product filters Sales). This default set up does not allow for our Sales table to filter our Product tables leading to the unintended results.

Now, we could correct this by changing the cross-filtering direction property on the Product-Sales relationship. However, this would change how filters work for all data between these two tables, which may not be a desired or an acceptable outcome.

Another solution is to utilize the power of the CROSSFILTER function. We can use this function to change how the Product-Sales relationships works within a new measure.

```c
Distinct Product Code Count Bidirectional = 
CALCULATE(
   [Distinct Product Code Count], 
   CROSSFILTER(Sales[ProductID], Products[ProductID], Both)
)
```

We can add this new measure to our table and see we get the expected results. This measure gathers all the sales records in the current context (e.g. Jan 2022), then filters the Product table to only related products, and finally returns a distinct count of the products sold.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*IHh8wzb_t3t5xRg4)

This measure and the Sales Amount can now be used to analyze our sales data with details on the number of different products sold each month.

![](https://miro.medium.com/v2/resize:fit:1152/format:webp/0*R2ROpWCBqs261rf-)

By using CROSSFILTER, we maintain control over our data relationships, ensuring our reports reflect the precise insights we need without unintended data flows. This level of control is crucial for building robust and reliable Power BI models.

## Wrapping Up

DAX relationship functions are powerful tools that significantly enhance our ability to manage and analyze data in Power BI. We have explored how these essential functions empower us to connect and manipulate data and relationships within our data model. By understanding and knowing when to leverage these functions we can create dynamic, accurate, and insightful reports. Here is a quick recap of the functions.

- **RELATED** simplifies data retrieval by pulling in values from a related table, making our data more informative and easier to analyze
- **RELATEDTABLE** enables us to navigate and summarize related tables, providing deeper insights into our data.
- **USERELATIONSHIP** gives us the flexibility to activate inactive relationships, allowing us to create more complex and context-specific calculations.
- **CROSSFILTER** allows us to control the direction of cross-filtering between tables, ensuring our data flows precisely as needed.

To further explore and learn the details of these functions visit the DAX Relationship Function reference documentation.

## [Relationship functions (DAX) - DAX](https://learn.microsoft.com/en-us/dax/relationship-functions-dax?source=post_page-----57d41587e83a---------------------------------------)

### Learn more about: Relationship functions

learn.microsoft.com

By adding these functions into our DAX toolkit, we enhance our ability to create flexible and robust data models that ensure our reports are both visually appealing and deeply informative and reliable.

To explore other function groups that elevate our data analysis check out the Dive into DAX series, with each post comes the opportunity to enhance your data analytics and Power BI reports.

## [Dive into DAX - Ethan Guyant](https://ethanguyant.com/tag/diveintodax/?source=post_page-----57d41587e83a---------------------------------------)

### Explore DAX in Power revealing the potential to enhance your data analytics with every post.

**Thank you for reading! Stay curious, and until next time, happy learning.**

And, remember, as Albert Einstein once said, “Anyone who has never made a mistake has never tried anything new.” So, don’t be afraid of making mistakes, practice makes perfect. Continuously experiment, explore, and challenge yourself with real-world scenarios.

If this sparked your curiosity, keep that spark alive and check back frequently. Better yet, be sure not to miss a post by subscribing! With each new post comes an opportunity to learn something new.

## [Don't miss a story!](https://medium.com/subscribe/@emguyant?source=post_page-----57d41587e83a---------------------------------------)

medium.com

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)