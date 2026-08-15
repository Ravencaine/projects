---
title: "Power BI visual templates made more dynamic"
source: "https://medium.com/microsoft-power-bi/power-bi-visual-templates-made-more-dynamic-4bc8d52e6f65"
author:
  - "[[Mateusz Mossakowski]]"
published: 2025-03-22
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
In today’s brief article, I’d like to expand on a brilliant concept introduced by [Injae Park](https://www.linkedin.com/in/injae-park/): **Visual Templates**. This innovative idea focuses on creating visuals that leverage visual calculations while making them more reusable. By definition, visual calculations are “encapsulated” within a single visual. However, what if we could develop templates that enhance their reusability? For a deeper dive into this concept, I encourage you to check out Injae’s latest [video](https://youtu.be/P0dQUoyQcsY?si=7yakbqE4aIgnq8UR).

> 🎖️ Article was awarded as **Must-Read** by [**Power BI Masterclass community**](https://linktr.ee/powerbi.masterclass).

Today, I aim to take this idea a step further by making these templates fully dynamic, allowing you to select the starting-point measure yourself. This enhancement builds on Injae’s original concept and relies on two key components:

Component 1) A blank measure.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*eek_EGQLoWOGRmN5Ebiqtg.png)

Component 2) A calculation group that ignores the blank measure and overwrites it with any measure we define as calculation items.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*iDwl13Tjy2OZXZKexrpxUw.png)

Once this setup is complete, you can seamlessly switch between different measures, ensuring that all dependent visual calculations function flawlessly.

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----4bc8d52e6f65---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee