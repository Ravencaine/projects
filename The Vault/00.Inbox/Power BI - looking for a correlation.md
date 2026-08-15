---
title: "Power BI - looking for a correlation"
source: "https://medium.com/@michalmolka/power-bi-looking-f-2d0fffb081d0"
author:
  - "[[Michal Molka]]"
published: 2020-10-30
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

When it comes to Python or R. You can calculate a correlation coefficient pretty easy. But, how to do it in Power BI?

We will be looking for a correlation coefficient for a \[**Reputation**\] and a \[**Score**\] columns in the Stack Overflow database.

Here is the data structure.

![](https://miro.medium.com/v2/resize:fit:1242/format:webp/1*PuHqDoriaN9O3oFxaYGoRQ.png)

As we see bellow, the correlation coefficient for the \[**Score**\] and the \[**Reputation**\] columns is 0.86

```c
from sys import path
import pandas as pd
path.append("\\Program Files\\Microsoft.NET\\ADOMD.NET\\150")
from pyadomd import Pyadomd

CONNECTION_STRING = r"Provider=MSOLAP;Data Source=localhost:53914;Catalog=8c9e2314-8ba6-413f-8ba9-48527f217b26;"
QUERY_STRING = """EVALUATE StackOverflowCorrelation """

with Pyadomd(CONNECTION_STRING) as conn:
    with conn.cursor().execute(QUERY_STRING) as cur:
        users_df = pd.DataFrame(cur.fetchone(), columns=[i.name for i in cur.description])

users_df = users_df.fillna(0)
users_df.drop("StackOverflowCorrelation[UserId]", axis=1).corr()
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fSO3XcDub7zzU4qmGnf1Uw.png)

Now, we can implement a correlation coefficient formula in the DAX.

```c
Correlation = 
VAR FirstAvg = AVERAGE(StackOverflowCorrelation[Reputation])
VAR SecondAvg = AVERAGE(StackOverflowCorrelation[Score])
VAR Numerator = 
    SUMX(
        StackOverflowCorrelation, 
        (StackOverflowCorrelation[Reputation] - FirstAvg)*(StackOverflowCorrelation[Score] - SecondAvg)
    )
VAR Denumerator01 = 
    SUMX(
        StackOverflowCorrelation, 
        POWER(
            StackOverflowCorrelation[Reputation] - FirstAvg,
            2
        )
    )
VAR Denumerator02 = 
    SUMX(
        StackOverflowCorrelation, 
        POWER(
            StackOverflowCorrelation[Score] - SecondAvg,
            2
        )
    )

RETURN Numerator/SQRT(Denumerator01*Denumerator02)
```

And there is our result.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*M38i-oidNuzyAFmAfksC_A.png)