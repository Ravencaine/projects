---
title: "Power BI — user defined aggregations"
source: "https://medium.com/@michalmolka/power-bi-user-defined-aggregations-d610dc44faf5"
author:
  - "[[Michal Molka]]"
published: 2026-04-01
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NP3rjylbs5BXlA_iBdr2OA.png)

From time to time, we can have a problem with model size. We own a model with huge fact table/s. The model reaches capacity size or is just expensive in cost and slow in refreshes. I’m thinking about imported tables. We can consider changing the storage mode to Direct Query. It has its advantages — no cost at the model size, no long refreshes, etc. Depending on the source, reading data may be slower or much slower.

If for some reason, we need to keep data at a very high granular level, for example, at a transaction or sold product level, then we often need to deal with a large amount of data.

End reports are mainly based on aggregates. Decision-makers use highly detailed reports less often. If we deal with such a case, then we can consider user-defined aggregations.

Initially, our example contains four tables:

- A fact table: iowa\_sales \[DirectQuery\] — let’s pretend that it’s a very big monster which we can’t fit into the capacity limit,
- Three dimension tables \[Import\] — pretty smal, nothing special.

In order to define user-defined aggregation, we need to add an aggregated version of our fact table. Let’s assume that we’ve made an evaluation of reports and queries. Then we typed that the most common aggregations are performed on a Category and/or Store level for expressions like: SUM(iowa\_sale.SalesDollars) or COUNTROWS(iowa\_sale).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GvNEYIWSckLHEFm3bMBItg.png)

So, we have to create an aggregated version of the iowa\_sale table. Here are the settings.

- storage mode: **Import**,
- relationships to dims — same as the original table. If we have matching dims, in this case, we don’t reference the iowa\_date dim table, thus no relationship is created,
- grouping: **Category\_ID**, **Store\_ID**,
- aggregation columns: **COUNTABLEROWS** (iowa\_sale), **SUM** (iowa\_sale.Sales\_Dollars)

The best practice is to have such a table or view in a backend system and import it directly.

After we had imported the table and created relationships, we can do the last step. In the Manage aggregations menu, we need to set grouping and aggregations. The pattern is the same as in the settings I presented above.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EE2bPm2NlVoiO276JgLecg.png)

We can verify settings in Tabular Editor in the **Alternate of** section for respective columns.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*V30mVax3A4WK9hp6P9K29Q.png)

Alright, we created a solution; now it would be sufficient to check whether it works. DAX studio is the best tool to do the job.

```c
EVALUATE
SUMMARIZECOLUMNS(
 iowa_category[CategoryName],
 "Qty",
 COUNTROWS(iowa_sale)
 )
```

The aggregation table has grouping on a Category level and the **COUNTROWS** aggregation calculation set. Thus, it’s coherent with the query.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KsGYKmpmmTD3xlsjs89AaQ.png)

DAX Studio confirms:

**\<matchFound>** means that the aggregated table has been used instead the original one.

Here’s the next proof.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*OxImu0B8z9-NUWvUuV2COQ.png)

The next query:

```c
EVALUATE
SUMMARIZECOLUMNS(
 iowa_category[CategoryName], iowa_store[County],
 "sum",
 sum(iowa_sale[SaleDollars])
 )
```

The grouping and the aggregate suit to the aggregation table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oVVn-3U7d_JTzTr9Jo3WHA.png)

The last query:

```c
EVALUATE
SUMMARIZECOLUMNS(
 iowa_category[CategoryName], iowa_store[County], iowa_date[CalendarYear],
 "sum",
 sum(iowa_sale[SaleDollars])
 )
```

We have a **SUM** aggregation — it exists in the aggregated table. But we don’t have grouping on a **Date** level, so the original iowa\_sales table is queried. **\<attemptFailed>** says more than a thousand words.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9u344nm4zBAnUuG6iyrQYQ.png)

You can notice that query timings are much longer for this Direct Query table in comparison to Imported ones.