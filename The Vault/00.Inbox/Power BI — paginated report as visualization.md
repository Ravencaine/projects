---
title: "Power BI — paginated report as visualization"
source: "https://medium.com/@michalmolka/power-bi-paginated-report-as-visualization-d38b01910385"
author:
  - "[[Michal Molka]]"
published: 2022-01-21
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Sometimes your users are used to or need to use SSRS reports. With a **Paginated Report** visual you are able to use SSRS reports alongside with standard Power BI visualizations.

As an example, I’ve created a standard paginated report with the **Power BI Report Builder**.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eWNEEhuOYKghavcUQsHm6g.png)

…and deployed it to the Power BI service.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lajlq1x12fgHxR4JFAfoEw.png)

For now on, we can use this report as a visual. Connect to your data source (the same with you used to create the Paginated Report). And then pick a **Paginated Report** visualization.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Ih-QoyFEU1JBv8s7-Yy_zQ.png)

Once you are connected to the Power BI service. Choose the **Paginated Report** which you’d created.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vLTTtbELVgKoAZpXfBMXEA.png)

Proceed to a **Set Parameters** card.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZIlIgsGuXHG6JDjD4FORbg.png)

The **Paginated report** contains one parameter: **Country**. Place the same parameter column in the **Parameters** section inside the visualization pane and then select an available field on the report — like above.

Create a **Slicer** and put the same filed there.

Now, you can work with the **Paginated Report** like with any other visualization.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1x__3tidjgN49wC5ccgEmg.png)