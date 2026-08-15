---
title: "POWER BI —Direct Query on Clustered Columnstore Index"
source: "https://medium.com/@michalmolka/power-bi-direct-query-on-clustered-columnstore-index-4f94db572073"
author:
  - "[[Michal Molka]]"
published: 2021-05-14
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

When you don’t want to load your model into memory, you use a Direct Query mode. As you now, gap between an in-memory and DQ performance can be immense. We can use a Direct Query mode and attain a good effectiveness using a DQ on a Columnstore Clustered Indexed table.

I’ve prepared two identical tables.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*w_cG_ECSuRi19Q9nc2vZ2A.png)

The first: \[GHCN\_CCI\] — Clustered Columnstore Index

```c
CREATE CLUSTERED COLUMNSTORE INDEX CCI_GHC_CCI ON dbo.GHCN_CI
```

The second: \[GHCN\_RSI\] — a rowstore containing two indexes: Clustered and Non-Clustered.

```c
CREATE CLUSTERED INDEX IX_StationID_Alpha2 ON dbo.GHCN_RSI(StationID, Alpha2)
CREATE NONCLUSTERED INDEX IX_Date ON dbo.GHCN_RSI([Date])
```

Both tables contain 0.7 billion rows.

A Power BI model:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8uw3hQG9n85D0i1lSQc8XA.png)

A first query:

```c
DEFINE 
    MEASURE GHCN_CCI[COUNT_CCI] = COUNTROWS(GHCN_CCI)
    MEASURE GHCN_CCI[SUM_CCI] = SUM(GHCN_CCI[Value])/10
    MEASURE GHCN_CCI[AVG_CCI] = AVERAGE(GHCN_CCI[VALUE])/10

EVALUATE
SUMMARIZECOLUMNS(
    'ghcnd-countries'[CountryName], 
    CALCULATETABLE(
        GHCN_CCI, 
        GHCN_CCI[Type] = "TAVG", 
        'ghcnd-countries'[Alpha2] in {"PL"}
        ),
    "COUNT", GHCN_CCI[COUNT_CCI],
    "SUM", GHCN_CCI[SUM_CCI],
    "AVG", GHCN_CCI[AVG_CCI]
   )
```

The rowstore table is partly covered by indexes: **24.5 sec**.

![](https://miro.medium.com/v2/resize:fit:1152/format:webp/1*sJQOJhbYXWJdJPaWsi5ZSw.png)

The columnstore table: **0.7 sec.**

![](https://miro.medium.com/v2/resize:fit:1148/format:webp/1*qp3xA8Qa7J_SFt8N5-7mRg.png)

A second query, the rowstore table is covered by indexes:

```c
DEFINE 
    MEASURE GHCN_CCI[COUNT_CCI] = COUNTROWS(GHCN_CCI)
    MEASURE GHCN_CCI[SUM_CCI] = SUM(GHCN_CCI[Value])/10
    MEASURE GHCN_CCI[AVG_CCI] = AVERAGE(GHCN_CCI[VALUE])/10

EVALUATE
SUMMARIZECOLUMNS(
    'ghcnd-countries'[CountryName], 
    CALCULATETABLE(
        GHCN_CCI, 
        DATESBETWEEN(GHCN_CCI[Date], "2020-01-01", "2020-10-01")
        ),
    "COUNT", GHCN_CCI[COUNT_CCI],
    "SUM", GHCN_CCI[SUM_CCI],
    "AVG", GHCN_CCI[AVG_CCI]
   )
```

The rowstore table: **37.7 sec.** vs the columnstore table: **1.2 sec.**

A third one, without filters:

```c
DEFINE 
    MEASURE GHCN_CCI[COUNT_CCI] = COUNTROWS(GHCN_CCI)
    MEASURE GHCN_CCI[SUM_CCI] = SUM(GHCN_CCI[Value])/10
    MEASURE GHCN_CCI[AVG_CCI] = AVERAGE(GHCN_CCI[VALUE])/10

EVALUATE
SUMMARIZECOLUMNS(
    'ghcnd-countries'[CountryName], 
     GHCN_CCI, 
    "COUNT", GHCN_CCI[COUNT_CCI],
    "SUM", GHCN_CCI[SUM_CCI],
    "AVG", GHCN_CCI[AVG_CCI]
   )
```

The rowstore table: **39 sec.** vs the columnstore table: **2.3 sec.**

As you can see. During developing Power BI solutions. You may take an advantage of a columnstore index in combination with a Direct Query.