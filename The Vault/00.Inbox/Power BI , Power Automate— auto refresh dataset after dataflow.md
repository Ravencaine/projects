---
title: "Power BI , Power Automate— auto refresh dataset after dataflow"
source: "https://medium.com/@michalmolka/power-bi-auto-refresh-dataset-after-dataflow-af83b08735bb"
author:
  - "[[Michal Molka]]"
published: 2022-02-18
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*r1T-eLrzs4hCRZTuc6sqgg.png)

Today I want to show you how to implement an auto dataset refresh after a dataflow is refreshed. On order to this, we use **Power Automate**.

Let’s say that after an **Iowa\_Liquor\_Sales** **dataflow** is refreshed we want to refresh an **Iowa\_Liquor\_Sales** **dataset** automatically.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ffwma4y49vcMjsQb4nrnOg.png)

So, create a **New flow** and choose an **Automated cloud flow** option.

![](https://miro.medium.com/v2/resize:fit:1192/format:webp/1*0mgUqVT0haRK_XRqfngwBw.png)

Choose a **When dataflow refresh completes** trigger.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*w6l0NV6HYCCSDTHGhAJV_Q.png)

After creating the trigger, you are allowed to add steps to a flow.

For a trigger step, pick a workspace as a group type, a designated workspace and a dataflow from lists.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Sl7yLFREKe1NEr4lRTVdlg.png)

Add a **Condition** step, pick a **Refresh status** from available fields with a condition: **“is equal to** ” “ **Success** ”. Like bellow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aMbmxTWhDlzG1hSyG-jl0A.png)

Within an **If yes** section, add an **Refresh a dataset** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RTmxRdfuO2D48SWHBEHC2w.png)

Choose a workspace and a dataset.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*npizILCVVQgQJSgnG30Ikg.png)

Once you save the trigger. It is automatically invoked always when the dataflow is refreshed with a “ **Success** ” status.

You can check a run history as well as the flow details.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ieA2XNkkoRSMyVkycNSczQ.png)

One thing worth mentioning. Sometimes a trigger isn’t invoked immediately after a dataflow is refreshed.

As you see on the following screen. Time span is 14 min in this case.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FkpyvNDGXIftZETfEkLldA.png)