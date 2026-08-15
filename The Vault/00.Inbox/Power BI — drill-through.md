---
title: "Power BI — drill-through"
source: "https://medium.com/@michalmolka/power-bi-drill-through-126571243783"
author:
  - "[[Michal Molka]]"
published: 2022-01-07
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Often your clients want to get a some part of an visualization detailed view. For example, a client or a product detailed view derived from the general view. A good solution is a drill-through feature.

Let’s assume, that we’ve created two visualizations and one filter. A matrix table with a **County / City / Category Name** breakthrough and a clustered bar chart with a **County** breakthrough.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*QjPb-62H-mBrLbsqaCFQpQ.png)

At this point, we would like to get more information about data on **County** or **City** level.

In order to achieve this we need to create a next tab. It is our detailed view.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GLajkz3wb7TAlYsYePBUhg.png)

At this point I want to emphasize, that you don’t need to create slicers on this page. I placed them for a better concept understanding.

After you created the new tab, go to the visualizations pane. And insert the mentioned **County** and **City** field from the dataset into the **Drill through** section.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*bOO5dWUVGc1g92dh63IXYw.png)

From now on, on the main page, when you choose **County** or **City** group on a visualization and select a Drill-through option. You will be moved to a tab which contains details.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*JodAiJJOOq_WzrjYs--U2g.png)

Worth mentioning is a fact, that all the filters applied in the first tab are propagated to the target tab — this behavior is caused by a **Keep all filters** button on.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VLIvQl42jNb3Mxtra6NVIw.png)

If you don’t want to propagate filters between tabs then turn the **Keep all filters** button off.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*W87grKEHAy0sSewMf5uHDw.png)

As you noticed, a **Date** filter hasn’t been propagated.