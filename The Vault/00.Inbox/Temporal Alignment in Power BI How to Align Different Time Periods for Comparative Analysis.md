---
title: "Temporal Alignment in Power BI: How to Align Different Time Periods for Comparative Analysis?"
source: "https://medium.com/microsoft-power-bi/temporal-alignment-in-power-bi-how-to-align-different-time-periods-for-comparative-analysis-7c22025a3993"
author:
  - "[[Mateusz Mossakowski]]"
published: 2025-01-29
created: 2026-08-12
description: "Have you ever wondered what temporal alignment is and how it can be implemented in Power BI? No? Neither did I until last week. 🙃 However, a couple of days ago, everything changed. I was asked to develop a solution that allows for comparative analysis of data across different time periods. For instance, a certain group of products was introduced in Market A in March, while they were launched in Market B in June. Comparing these using standard time series analysis can be challenging or at least suboptimal. To facilitate more accurate comparisons, it is beneficial to unify the periods so that Period 1 for Market A represents March, while for Market B, it represents June. Let me guide you on how to achieve this in Power BI."
Processed: "Unprocessed"
---
## Have you ever wondered what temporal alignment is and how it can be implemented in Power BI? No? Neither did I until last week. 🙃 However, a couple of days ago, everything changed. I was asked to develop a solution that allows for comparative analysis of data across different time periods. For instance, a certain group of products was introduced in Market A in March, while they were launched in Market B in June. Comparing these using standard time series analysis can be challenging or at least suboptimal. To facilitate more accurate comparisons, it is beneficial to unify the periods so that Period 1 for Market A represents March, while for Market B, it represents June. Let me guide you on how to achieve this in Power BI.

Before we jump into more details, let’s talk about the secret ingredients. First of all, we need a calendar dimension, which, in addition to the already existing attributes, also requires ordering or offset columns for each time granularity for which we want the temporal alignment to be available. In our example, this is going to be year-month and week attributes. If you come from a SQL background, you can think of it in terms of a dense\_rank window function.

```c
select
        date_num
        , \`year\`
        , month_num
        , dense_rank() over (order by month_num) as month_num_order
        , year_month_name
        , week_num
        , dense_rank() over (order by week_num) as week_num_order
from
        some_schema.calendar_dim
order by
        date_num
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bQS39_XZR-ncqpR4kXiX8A.png)

Once this is done, we need to create duplicates for both the calendar and other dimensions for which we want to allow those comparisons. In our case, these will be both the product dimension and the store dimension (containing individual store data, store chains AKA customers, and countries).

For presentation purposes, I am also adding a second duplicate of the calendar dimension (calendar\_dim\_presentation) because this will help me visually and gradually represent what is happening with the final solution.

Last but not least, we need a disconnected period table. Depending on your needs, it can have fewer or more periods. For now, let’s assume that 24 periods are more than enough.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*HN_vAprIRn3C7yNZNVlgWg.png)

Let’s move step by step. The report page is designed so that the slicers on the left-hand side source from the original dimensions, while those on the right source from the duplicated ones. In the reference visual (which is not part of the final solution but can help us understand the behavior of the final visual), we use the year-month column from the second duplicate of the calendar dimension table.

Now let me reveal the logic behind the intermediate measures used in the reference visual. Nothing super fancy here — we just need to remove filters from either the duplicated or original dimension tables.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sL3_OIlaKvwLm9mrb0Qraw.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MJfv26mt4xdtW9hIDNsOJQ.png)

Let’s unhide the mystery of the final visual and final measures. The final visual uses periods from the disconnected table, which ultimately allows for the desired temporal alignment.

And now, the crème de la crème — the final measures. Let me walk you through one of them, as the second one is a mirror of the first. The only thing that needs to be changed is the REMOVEFILTERS part, which should be adjusted to refer to the original dimensions.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*Kn8dENo4Q0azimtFs2E85g.png)

final measure

First variable is responsible for retrieving all ordering/offset column values for year-month, irrespective of the duplicated dimension slicer selections. It is worth mentioning that we want to narrow down the list to only those for which we have relevant data in the sales fact tables (that's why we SUMMARIZE sales\_fact table). This is to avoid or be immune to the situation where, in the selected time frame, we might lack factual data, which could potentially undermine the concept of proper temporal alignment.

The second variable is pretty straightforward — the goal here is to find the overall minimum of the ordering column from the first table variable. Once we have it, we need to adjust the virtual @period column so that it contains values starting from 1 (for the minimum ordering value) and ending with the overall count of selected periods (months, in this case) that have related fact data. Apart from the virtual @period column, we also need to add the virtual @measure column, which refers to the appropriate intermediate measure described in the previous paragraphs.

The second-to-last variable is responsible for filtering the virtual table from the previous step to the disconnected periods — to virtually relate them — in order to visualize them later on in a visual.

The last step is a simple summation of the @measure virtual column, which in the line chart is not super crucial but can be useful, especially if you use any other visual that requires subtotals. If you do not anticipate the use of subtotals in any visuals, you can opt for a slightly simpler approach.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*V4dwxcP107N4tewCWYKz2w.png)

final measure simplified

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----7c22025a3993---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee