---
title: "Power BI — a field parameter"
source: "https://medium.com/@michalmolka/power-bi-a-field-parameter-afd2f24c2dcb"
author:
  - "[[Michal Molka]]"
published: 2023-03-17
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

A while ago I showed how to hide/insert a measure through a slicer. Here is the post: [Power BI — show and hide measures on slicer and visual](https://michalmolka.medium.com/power-bi-show-and-hide-measures-on-slicer-3b9609434466)

Microsoft has published a baked in functionality **Field Parameter**, so we don’t need to use workarounds and entire process is much simplified. I encourage you to look at the mentioned post to have some comparison.

Let’s switch over to an example. Go to Modeling -> New Parameter -> Fields.

Create a first parameter for measures:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rAV4jRFoRHMu7WWCCgzW6Q.png)

The same way create a parameter for fields.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jhla9GTmHzsjQIasuToBig.png)

Parameters are added as standard slicers. If you want to edit the parameter you can do this by editing DAX code.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6VEHGSQd1G1GMCVZ-SDV2Q.png)

Let’s create two visuals. Put previously created the **\[Iowa\_column\]** parameter into a Columns/X-axis section and the **\[Iowa\_measure\]** into a Values/Y-axis section.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KxW-5TIPtpkv_YIXkPCj_A.png)

And this is it. You can show or hide columns/measures dynamically through the slicers. Here is a demo:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*01q0o1L0HJlcx1Buog9Y_g.gif)