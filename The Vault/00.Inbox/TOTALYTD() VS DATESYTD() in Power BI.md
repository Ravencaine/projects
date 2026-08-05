---
title: "TOTALYTD() VS DATESYTD() in Power BI"
source: "https://medium.com/@nilantha.sac/totalytd-vs-datesytd-in-power-bi-8cbdddd91531"
author:
  - "[[Nilantha KM]]"
published: 2025-11-18
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
In this article, I’m aiming to answer these key questions.

1. Difference between TOTALYTD() VS DATESYTD()?
2. Is it possible to use DATESYTD() inside TOTALYTD()?
3. Can we calculate the Total YTD value without using the TOTALYTD() function?

To answer these questions, I’m going to use the following tables and data models.

![](99.System/Attachments/1!y58uEIDNHUq3yRoNmVkLLQ.png.webp)

Figure 1

![](99.System/Attachments/1!exXWQsUL3G49Ik5uv8IU7Q.png.webp)

Figure 2

![](99.System/Attachments/1!yNQihKRtYNeJG5EqgKhfUg.png.webp)

Figure 3

Here, I have calculated Total Sales

**Total sales = CALCULATE(SUMX(Sales,Sales\[quantity\]\*RELATED(Products\[product\_cost\])))**

Here, I have created another measure using the **TOTALYTD()** function

**Total YTD = TOTALYTD(\[Total sales\],’Calendar’\[date\])**

![](99.System/Attachments/1!v0RhnmuZ1cymbMNfs1kEGw.png.webp)

Figure 4

I will now create a measure using both **TOTALYTD()** and **DATESYTD()**, as shown in Figure 5.

**Total YTD using DatesYTD = TOTALYTD(\[Total sales\],DATESYTD( ‘Calendar’\[date\]))**

![](99.System/Attachments/1!GiY5pYHKVWfgGP993aBv1Q.png.webp)

Figure 5

But both measures return the same value.

Next, I will create another measure as follows.

**TotalYTD with cal function = CALCULATE(\[Totalsales\],DATESYTD(‘Calendar’\[date\]))**

![](99.System/Attachments/1!qrZPeZRbDZmuShH3WpOqUg.png.webp)

Figure 6

As shown in Figure 6, all three measures return the same value. So, the conclusion is that the answer to both the second and third questions is “ **YES”**.

Sources:[https://learn.microsoft.com/en-us/dax/](https://learn.microsoft.com/en-us/dax/)