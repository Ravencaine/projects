---
title: "Power BI — change detection"
source: "https://medium.com/@michalmolka/power-bi-change-detection-8e4b39b281ac"
author:
  - "[[Michal Molka]]"
published: 2021-10-15
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Today I will show you how to implement a change detection in Power BI. It gives you a possibility to refresh a report automatically within a specified range of time.

Our example is a \[**Badges**\]table. A connection type is a Direct Query. I’ve filtered two statuses and added a measure named **Quantity**. Now, we have 43 rows.

```c
Quantity = COUNTROWS(Badges)
```
![](https://miro.medium.com/v2/resize:fit:1330/format:webp/0*pRDrVaujB-a4kbge.png)

Next step is to configure the **Change Detection** functionality. In this case, I set checking for data changes which influences on the **Quantity** measure.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*-O0Shl1LnWH3uapr.png)

Next step is to select a **Change detection** in a **Page Refresh** section.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*T-ms9gmF5xr--sKY.png)

After you publish the report to the Power BI service. The service checks if data in a data source is changed every minute. If this change influences on a selected measure, the report is automatically updated.

After two records are added to the source table, the visual is automatically updated.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*1RdgVqY6YzmF9Ya0Eogzbw.gif)

It is a better alternative to the **Auto Page Refresh** functionality which refreshes an entire page even if nothing has been changed.