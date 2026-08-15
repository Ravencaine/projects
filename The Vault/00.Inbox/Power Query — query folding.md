---
title: "Power Query — query folding"
source: "https://medium.com/@michalmolka/power-query-query-folding-9f6facaaabbe"
author:
  - "[[Michal Molka]]"
published: 2021-02-19
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

When you want to speed up your Power Query transformations and queries. You can use a **Query Folding** mechanism. You need to fulfill two conditions. Your data must originate from a supported data source, e.g. most of relational databases. And your data transformations and queries have to be supported by the **Query Folding**. You can assume that if you can attain something by using SQL then this operation will be supported by the **QF**. You can check if the **QF** is applied in a Power Query editor.

For example, we want to download, filter and make a simple data transformation from a SQL SERVER source.

M language code:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*OtP6QRV1BcOsxE6xTpJ-UA.png)

As you see, there are filtering and two transformations. And they support the **Query Folding**.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Q1cHsw2fp6YR_CEFIim0ig.png)

If a **View Native Query** position is active, then a transformation supports the **QF**.

As you see, here is a native query code, the query is folded and it is processed directly in a SQL SERVER database.

![](https://miro.medium.com/v2/resize:fit:1174/format:webp/1*f6PNtf-IoDQ9q-WiQiqP4w.png)

At this stage the query is folded. Now it is the time to break something. In order to do this, I added next step: **Capitalize each word**. As you know, a SQL engine doesn’t support such an operation. As a result of this operation the query isn’t folded anymore. The **View Native Query** position is inactive.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-ACFg2Jefhfs0RxECM5mfQ.png)

Worth mentioning is a fact, that every step before the last one is still folded, only last and every next step is performed outside the source server.

Why you should use it? Because of performance. Entire work is done directly in a database. When it comes to small datasets, there is no visible difference. But, if your deal with a large amount of data the difference is noticeable.