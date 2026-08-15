---
title: "Power BI — deployment pipelines"
source: "https://medium.com/@michalmolka/power-bi-deplyment-pipelines-86d20c10e346"
author:
  - "[[Michal Molka]]"
published: 2021-07-23
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Power BI service brings a great Deployment Pipelines feature. You can separate your environments and synchronize them in an easy way.

Every environment has its own workspace. You can name it whatever you want. Here is an example of configured **Deployment Pipeline**. There are three environments: Dev, Test, Production. One report is created. Now everything is in sync.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pbi27toOHOjJnWbWUTmDSA.png)

After we modified the report and deployed to the **Development** environment; we are out of sync with the **Test** environment.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wWP4vijgY-O8u39vV1PmuQ.png)

If we want to deploy objects to the next stage we pick a **Deploy to test** button. After reports were tested we can do the same and use a **Deploy to Production** option.

You can change a data source for reports on every stage. Here is a brief demo.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*t0lvAD_x3QNis8evwrlhkw.gif)