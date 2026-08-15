---
title: "How to display measure descriptions directly in Power BI reports?"
source: "https://medium.com/microsoft-power-bi/how-to-display-measure-descriptions-directly-in-power-bi-reports-c87e3579eb6a"
author:
  - "[[Mateusz Mossakowski]]"
published: 2024-11-07
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
## While Power BI report creators can easily check measure definitions by hovering over the measure name in Power BI Desktop or directly within the Service, report consumers face a different challenge. They interact solely with the visual layer of the report and do not have direct access to the semantic model. In today’s article, I will guide you through a straightforward method to display measure descriptions for report consumers with minimal effort. If time allows, next week I will explore a more advanced approach for those who prefer greater control over text alignment and overall formatting. 😉

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fXklElntSTnKP73OJ98PPw.png)

It would be fantastic to have out-of-the-box measure header tooltips that display measure descriptions (as I’ve attempted to illustrate in the image below 🙃). However, until that feature is implemented, we must rely on workarounds to enable end users to quickly access measure descriptions within the Power BI reporting interface.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ytzwoWsSeEwrlyFIoKlfIw.png)

Please excuse my limited Photoshop skills.

## What’s Needed?

Let’s begin with the essential components. We will need a table that acts as a repository for measure names and their corresponding descriptions. The simplest method to achieve this is by utilizing the newly introduced **INFO.VIEW.MEASURES** function. Additionally, we will require a placeholder element within a field parameter table; in this case, it will be used for the rows of a matrix. Finally, we will need a calculation group to activate the display of descriptions within the visual.

## Component 1

As previously mentioned, we need a table with two columns: one for the measure name and another for its description. By storing the descriptions directly within a measure property, we can effectively leverage the **INFO.VIEW.MEASURES** function to easily retrieve all the required information.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Rd3ROhZFCZMD-vpo2_tSGA.png)

## Component 2

The second component is a placeholder row in the field parameters table that does not refer to any object from the semantic model. Instead, it contains hardcoded text.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*dibuysh4jQ-MclPr6RShmQ.png)

## Component 3

The final component is the calculation group that “ignores” the standard measure calculation logic and instead presents the measure definitions. This override occurs only when the “placeholder” element in the field parameters table is selected. Under this condition, we identify the overall maximum period (i.e., the period with the highest sorting value) and display the measure definitions exclusively for this maximum period. This approach prevents duplication of descriptions when multiple months, quarters, years, etc., are selected. The measure definition is retrieved from the measure definitions table by utilizing a virtual relationship through **TREATAS**, linking **SELECTEDMEASURENAME()** with the measure name column from the measure definitions table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*s_KMjTpwTJjExffG70tJbQ.png)

## Final Result and Closing Thoughts

As you can hopefully see from the GIF below, it works like a charm. The implementation of measure definitions only affects the matrix when the measure definitions element is selected. However, when other “real” dimensions are added as rows, the matrix behaves normally, displaying numerical values for the measures.

The only drawback to this solution is the alignment of the description text, which inherits the right alignment from the numerical measures — an alignment that is appropriate for numbers but may not be suitable for text values. Left alignment would likely be more fitting for text descriptions. Additionally, if the description is lengthy and you don’t insert line breaks directly in the description property window, you may end up with a long, continuous line of text that is difficult and frustrating to read.

I plan to address this issue in a [follow-up article](https://medium.com/microsoft-power-bi/how-to-display-measure-descriptions-directly-in-power-bi-reports-c87e3579eb6a) next week, so please keep your fingers crossed for me to find the time to write it! 😉

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----c87e3579eb6a---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee