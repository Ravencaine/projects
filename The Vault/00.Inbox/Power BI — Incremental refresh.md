---
title: "Power BI — Incremental refresh"
source: "https://medium.com/@michalmolka/power-bi-incremental-refresh-46ab3f23ca01"
author:
  - "[[Michal Molka]]"
published: 2021-04-02
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

When we deal with large datasets, a data refreshing process might take a long time. No wonder, Power BI refreshes an entire data set, even if any record hasn’t changed. So, we can use an incremental refresh functionality.

You can find how to configure the incremental refresh in the [Microsoft Docs](https://docs.microsoft.com/en-us/power-bi/admin/service-premium-incremental-refresh). It is pretty simple.

We compare time of refreshing a dataset without the incremental refresh and with the incremental refresh.

My test dataset contains 6.5 million rows and 3 columns and it is stored inside a SQL Server database.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*CVLtRn-Dg2jtFfthdO7jRg.png)

A dataset refresh process took around 40 seconds.

Next, I’ve set the incremental refresh like bellow. A filter is set on a \[**Created**\] column.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*j1fxqNrgtnZJbvsiTRgAag.png)

Two full years are stored and two complete months are refreshed.

I’ve inserted around 1 million rows with \[**Created**\] column values set to ‘2020–11–01’. So that, it is in an incremental refresh rule range.

A dataset refresh process took 55 seconds.

Afterwards I added 300 rows to the source table.

A process took 12 seconds. The difference is visible. Instead of updating an entire dataset you can add only new records.

Here is a summary:

![](https://miro.medium.com/v2/resize:fit:1390/format:webp/1*MLdxpdVQmR5IVQZAi4H8FQ.png)

At the end, I’ve set a **Detect data changes** feature and updated 300 rows.

![](https://miro.medium.com/v2/resize:fit:1304/format:webp/1*5HMIMgEz7xeRTgHwhEdYgg.png)

It took 14 seconds.

![](https://miro.medium.com/v2/resize:fit:1186/format:webp/1*jjRruHcG6XQJPgzn3m1A_A.png)

As you see the Incremental Refresh saves a lot of time and resources. In this scale the difference is small, several dozen seconds. But when you store hundreds millions or billions rows it makes the difference.