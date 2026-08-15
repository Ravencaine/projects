---
title: "Power BI — seamless PRs"
source: "https://medium.com/@michalmolka/power-bi-assets-seamless-prs-96582595af58"
author:
  - "[[Michal Molka]]"
published: 2026-06-01
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Sjy6zXPs5w98t5YUBGO4Tg.png)

In these two posts, I’ve been writing about Power BI datasets differential update through ALM Toolkit: [Power BI — update dataset — ALM Toolkit](https://medium.com/p/f3e749f818f6) and a a visual layer control versioning: [Power BI report — control versioning](https://medium.com/p/b71a45f16ca6)

As I wrote, saving Power BI models and reports as text files makes them easier maintainable from a control version standpoint. There is another benefit. Pull request reviews are much easier.

Let’s look at the exemplary PR. The most important area is the Files section.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*QahGOkerxgQWyVYV5Ql36g.png)

All the changes are clear as day. We see every part of the report and the model. In the case above, a column had been added to a user-aggregation table.

Here, a measure has been added to the model.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sEG2jUdazxxj5YUyAe68Sw.png)

Let’s look at the visualization layer. One of the measures has changed.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SbevKSgIhCKsG5zRTdwdyw.png)

We can track changes through commits.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TcPCBOscVkjwOxksH5C9nQ.png)

And after the PR is merged into the main branch, all the history is more readable.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zDWF_eZTOBbNjF7CJwHUnw.png)

Besides the Azure DevOps portal, we can use our favorite text editor/IDE.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oTZ3S5N0PMTnLZM9ih_uAA.png)

And track changes in the same way directly through the Git console or functionality baked into an app.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FkcbxR2XvVH23MrqK71_NA.png)