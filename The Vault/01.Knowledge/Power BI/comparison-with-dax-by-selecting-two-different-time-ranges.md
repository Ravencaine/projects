---
title: "Comparison with DAX by selecting two different time ranges"
source: "https://www.flip-design.de/?p=1206"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Comparison with DAX by selecting two different time ranges | flip-it.de :: SQL, BI and more A customer asks me, who he can select an alternative comparison time series inside Power BI. He wants to select the actuals and compare it with another time series. The analysis should look like this: He wants to see in 1 the result of the time series of the selection by 2. Inside 4 he wants to see the result of the selection done by 2. The underlying data is only one fact table. So, I created two different timetables and connected these to the fact table: The relationship between the fact and the “compare date” are deactivated. Now, we can create two different measures, one to sum the actual sales, and one for the comparison. The second one, uses the inactive relationship and also ignores the filter: Now, you can select the different time series and compare the data Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1206)*
