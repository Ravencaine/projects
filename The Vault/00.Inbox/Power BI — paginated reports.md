---
title: "Power BI — paginated reports"
source: "https://medium.com/@michalmolka/power-bi-paginated-reports-5f3209933bb2"
author:
  - "[[Michal Molka]]"
published: 2022-07-08
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Not everyone knows that we can create reports nearly identical to SQL Server Reporting Services summaries. Standard Power BI reports are designed to show an aggregated data and for an exploration purpose. If your users are used to Reporting Services layout, they need to examine a detailed, non-aggregated data or print the result. Then paginated reports fit the bill. A short solution presentation bellow.

Firstly, you need to have Power BI Report Builder installed. An application layout and options are similar to a SSRS Report Builder or Visual Studio SSDT.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HFHiNNcKJf23RgkDwNT4WA.png)

Connect to a Data Source, create datasets and set parameters for filters.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*NN5zgMghQTFY-ooDhPxKLQ.png)

Next step is to create visualizations.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3LDOnILCKuNB1L9LWHXpbw.png)

…adjust visual options.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*0LyvLlGqdjQkmRm1Xp2Keg.png)

After you created and published the report to the Power BI Service. You can use it like Reporting Services reports.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DHTtmI3iysIjKSOJT6HdjQ.png)