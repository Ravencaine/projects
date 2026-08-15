---
title: "Goals in Power BI have become Metrics and improved a lot"
source: "https://medium.com/microsoft-power-bi/goals-in-power-bi-have-become-metrics-and-improved-a-lot-593cf3eb62b6"
author:
  - "[[Tomas Kutac]]"
published: 2022-10-22
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
> [Unlock this article.](https://medium.com/microsoft-power-bi/goals-in-power-bi-have-become-metrics-and-improved-a-lot-593cf3eb62b6?sk=0737a2fd53dce53e916c4c674c8ea1d9)

One of the most interesting functionality in Power BI announced in 2021 were *Goals*. *Goals* added new possibility to define and share target KPIs defined above existing Power BI reports in Power BI cloud. Microsoft finally changed the name to Power BI *Metrics* and in this article I will describe all original functionalities and also the new ones.

## All KPIs in one place

Using *Metrics Scorecard* you can create dashboard that will include all KPIs that are important for your company. No need anymore to check many reports one by one to identify on which KPIs management should focus.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*UaFIZg4g2wcN9L-i.png)

## Metrics hierarchy

*Metrics* hierarchy can be defined within the *Scorecard.* This simplifies orientation and navigation through more KPIs levels. Each *Metric* can have four levels of *Sub-metrics.*

![](https://miro.medium.com/v2/resize:fit:1278/format:webp/0*XbqLy8nU5eab-oUD.png)

## Metrics responsibility

Responsible person can be assigned to each *Metric.* This person then can see all *Metrics* that were assigned to him and managers can quickly identify who is the person with whom they should follow up if KPI is not on a good track.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*JEox6FDW2nz-ZN2b.png)

## Connected Metrics

Each *Metric* has its Current and Target value and these values are compared over the time.

These values could be set:

- Manually entering the current and target values.
- Connecting either the current or target value to data in an existing Power BI report.
- Connecting both values to data in an existing Power BI report.

You can create *Connected Measure* in these steps:

### 1\. Choose report that contain metrics you would like to track

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Lev6ddNfqmL1nK72NISWzg.png)

### 2\. Select page, visual or data point that you would like to track

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EmXLzGvWLlskRFw8yl7iBw.png)

### 3\. Save the metrics

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*169W4QZrO1_lwl2w42np-Q.png)

## Metrics status

Each *Metric* in *Scorecard* has its status that can be customized for company specific needs. From the first look mangers will see which *Metrics* are fulfilled and which ones are behind the plan.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ErvLfbwdXnseBNTt.png)

Statuses could be customized:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*CecbBIKSZ0lsc7b0NczRVw.png)

Rules for status assignment could be defined:

![](https://miro.medium.com/v2/resize:fit:1396/format:webp/1*qGqQlwM5hp2d5lNh0waAgQ.png)

## Metrics Check-ins

*Metrics Check-ins* allow users to update target values of specific *Metric*, change status or post comment. Comments can explain reasons why *Metric* is not fulfilled, or better, define actions that responsible person will take to return *Metric* on the track.

![](https://miro.medium.com/v2/resize:fit:1378/format:webp/0*y8uFE2HVEjBxtU3Z.png)

## Metrics Milestones

*Milestones* helps to split final target goal into more steps to track progress during time. You can split yearly sales volume goal into monthly milestones for example.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*bBV0tLd1McyS9MOhG1gK3Q.jpeg)

Milestones are then also visible in *Metric* detailed view:

![](https://miro.medium.com/v2/resize:fit:1236/format:webp/1*6A2VFPDQyA49L2dwmGaHRg.jpeg)

## Categorical Metrics

*Categorical Metrics* are custom non-numerical metrics. For example you have four groups of customers A,B,C and D assigned based on yearly volume of shipment. The defined goal could be to move some specific customer from category B to category A.

Define *Categorical Metrics:*

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*5CW8JhO8dpA3XFrXnrVgWg.jpeg)

Choose *Categorical Metrics* goal:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*r6CdJY54pSo8r_WMiIWndA.jpeg)

See the *Categorical Metrics* fulfillment:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9jLop25i-MVgv6wemcz9uA.jpeg)

## Bulk updating

With bulk updating added in June 2022 release you can edit more *Metrics* in the same time as visible on the picture below.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-m8J5712BhQFclUfQvSsqA.jpeg)

## Power Automate Integration

As Power BI is part of Power Platform product family, Power Automate could be use to automate various task related to *Metrics.*

For example you can create Power Automate flow that will send you message in MS Teams when some *Metric* will be not fulfilled as requested.

Here some *Power Automate* triggers and actions:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*P_8EbPSekQS3Qz4MxkGDhQ.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*qQERNtwNLiAtR39pfm5i1A.png)

Now let’s see how all these functionalities can work in real life.

## Use case scenario: Top-down approach

Hierarchy of KPIs can be created using *Metrics Scorecard* and analysis can start from the top aggregated level and then continue up to the point when the root cause is identified.

For example, in the first step manager will see that target profitability is not fulfilled, drilling to next level he will identify that the reason is lower total sales and drilling down to the next level he will realize that sales quantity reached its target level but lower selling price is the main problem.

As a next step, manger will continue to Selling Price Analysis report which will give him comprehensive analysis and help him to understand what are exact reasons why target selling price was not reached. In this case, the reason of lower average selling price was lower sales volume of premium products with high selling price; it was impact of product mix.

> Please don’t forget to clap for this article if you like it. And you can do it even more times… just try it.;-)