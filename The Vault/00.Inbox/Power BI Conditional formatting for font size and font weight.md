---
title: "Power BI: Conditional formatting for font size and font weight."
source: "https://medium.com/microsoft-power-bi/power-bi-conditional-formatting-for-font-size-and-font-weight-e8f71e464eb2"
author:
  - "[[Mateusz Mossakowski]]"
published: 2026-01-10
created: 2026-08-12
description: "To continue on the topic of the conditional font size. Last time we checked, hacking Power BI to allow for font size conditional formatting through adjustments in the JSON definitions of the .pbip file did not work as intended. Maybe it's not the most burning challenge to solve, but it did not let me sleep well 🙃Thankfully, I realized we can try to attack the problem from a slightly different angle. This time we won't be doing any illegal stuff. It's all about an Image URL type measure, taking advantage of the SVG blessings."
Processed: "Unprocessed"
---
## To continue on the topic of the conditional font size. Last time we checked, hacking Power BI to allow for font size conditional formatting through adjustments in the JSON definitions of the.pbip file did not work as intended. Maybe it's not the most burning challenge to solve, but it did not let me sleep well 🙃Thankfully, I realized we can try to attack the problem from a slightly different angle. This time we won't be doing any illegal stuff. It's all about an Image URL type measure, taking advantage of the SVG blessings.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

Below is the first draft of the measure. The idea is to highlight both the top three and bottom three customers in terms of revenue year-over-year percentage change, and to make them stand out not only through the out-of-the-box background conditional formatting but also through the font size (for now; later we can take it a step further by applying conditional font weight to make the text bold).

There are still some aspects that require polishing, as you can see below.

The first item refers to the row height, which we can adjust quite easily by adjusting the image size settings of the matrix visual.

![](https://miro.medium.com/v2/resize:fit:1312/format:webp/1*u_bYG5dsp4yPOkTCY4dDzg.png)

Now it looks much cleaner. However, we still have an issue: the numbers are left-aligned, and this cannot be adjusted using the specific columns values alignment properties.

Though it’s not the dead end, fortunately 🙃 We need to take a couple more steps to tackle it. I highlighted in yellow the differences when compared against the initial version of the SVG measure. With two for the price of one, I also enhanced the measure a bit to make the top-three and bottom-three customers’ percentages bold (blue highlight). That’s where font weight comes into play.

I hope you agree it looks more readable after this little polishing of the code.

Well, nothing is perfect. Neither are SVG measures as Image URLs. They aren’t as flexible in some aspects as out-of-the-box ones. They need some predefined setup, and you can’t manually adjust the measure column width, as you can see in the GIF below.

Even though there are some limitations and complexities that come with SVG measures, I believe you might find some use cases for them. Maybe you won’t use it one-to-one, but I think it could be a starting point for your creative approach to solving other challenges.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----e8f71e464eb2---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** DAX, Data Visualization

**Tags:** Tutorial, DAX, Data Visualization