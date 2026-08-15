---
title: "When to Transform Data for Power BI"
source: "https://medium.com/microsoft-power-bi/when-to-transform-data-for-power-bi-e9ed4bdf2c41"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-12-04
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
SQL or Power Query or DAX?

![](https://miro.medium.com/v2/resize:fit:1314/format:webp/0*egJT8MBk4CbclzmN.png)

## When to transform data

As a general principle we should always look to transform data **close to its source** to gain efficiencies and minimise potential for discrepancies

Over the last few weeks we have shown how data can be combined from multiple sources in three different ways

[UNION in SQL](https://www.selectdistinct.co.uk/2023/09/21/union-in-sql/)

[APPEND data in Power Query](https://www.selectdistinct.co.uk/2023/09/27/append-data-in-power-query/)

[UNION in DAX](https://www.selectdistinct.co.uk/2023/10/04/union-in-dax/)

A common question we get asked, and a common mistake we see is when the data transformations are not done in the right place

## When to transform data for Power BI

There is a well known saying

**“Data Should be transformed as far upstream as possible, and as far downstream as necessary”**

This is called ROCHES MAXIM, by Matthew Roche Principal Program Manager Power BI

If we apply this to our three options

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3BSzLX6z-sWyDlU_cTWtUg.png)

In general,

With these three options to combine data together

We should first look to see if we can do it in SQL using the UNION method

If we can’t, then look to do it within Power Query

And lastly, look to using DAX

## Benefits of transforming data further upstream

Transforming data further upstream (closer to its source) means that it can be better controlled and can be made more widely available

For example, a fact table in a data warehouse that has already combined multiple data sources can be used by more users in more use cases

This means that it only needs to be done once, upstream and it can have controls in place there to ensure it is complete and accurate

The data can be available on a consistent basis for all users

You get all subsequent reports sharing a common data source and really do have….

## One version of the truth

## Reasons to transform downstream

It’s not always possible to perform all of the transformations upstream

**When to use Power Query instead of SQL**

Data could be coming from multiple systems and not from a central data warehouse, it maybe a combination of a SQL Server database for some parts of the organisation, and a separate Oracle Database for a newly acquired part of the organisation which is being kept separate for strategic reasons

If you had the facility, you could look at creating a simple reporting database to combine these into one, but assuming that is not an option

Then you will use the next best option of Power Query to combine these sources using the APPEND functionality

**How to decide between Power Query or DAX for data transformation**

Generally, Power Query is better option as its further upstream as the work is done in the data model itself

The data model as an entity can be shared and made available for wider use

This also means that report building is less complex and easier to maintain

But, If you need to create a measure that is responsive to slicers then you need to use a DAX measure

**For example**

You need to create a card that returns aggregated sales from multiple sources that are not already combined, maybe the data is held at a different level of granularity

You can use the DAX UNION function to combine the data you need

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Fat20RRr1-SiqPPJ.png)

## Learn More about Roches Maxim

**You can learn more about Roche’s Maxim of Data Transformation on the ssbipolar.com blog**

[Roche’s Maxim of Data Transformation — BI Polar (ssbipolar.com)](https://ssbipolar.com/2021/05/31/roches-maxim/)

## Conclusion of when to transform data

We have outlined the key reasons why you can combine data in multiple ways for Power BI

When to use SQL,

When to use Power Query

And when you need to use a DAX Measure

For more details of any of these specific techniques please visit our Blog

Subscribe to our channel to see more SQL tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful SQL, Power BI or other business analytics timesavers in our Blog

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work and are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people. Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)