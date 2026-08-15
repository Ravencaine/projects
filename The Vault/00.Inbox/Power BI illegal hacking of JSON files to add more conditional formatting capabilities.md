---
title: "Power BI: illegal hacking of JSON files to add more conditional formatting capabilities."
source: "https://medium.com/microsoft-power-bi/power-bi-illegal-hacking-of-json-files-to-add-more-conditional-formatting-capabilities-485751bc4be2"
author:
  - "[[Mateusz Mossakowski]]"
published: 2026-01-02
created: 2026-08-12
description: "While I would never advise using this technique in a production environment, I’d like to walk you through how you can hack the system and have conditional formatting in places where it is not available out of the box. I would also mention some considerations and limitations. Though, if anyone knows how to overcome those limitations, I’d gladly learn them instantly."
Processed: "Unprocessed"
---
## While I would never advise using this technique in a production environment, I’d like to walk you through how you can hack the system and have conditional formatting in places where it is not available out of the box. I would also mention some considerations and limitations. Though, if anyone knows how to overcome those limitations, I’d gladly learn them instantly.

First things first, in order to stretch Power BI conditional formatting options a little bit, we need to start with saving our report as a `.pbip` file. Thanks to that, each visual has its own JSON definition that you can slightly customize (within some limits, of course...).

I was not able to find any official documentation (again disclaimer — never use it in production 😊), so I cannot 100% confirm, but it seems like you can only use this technique wherever in the JSON file definition you see an `expr` property.

Once you are able to find a static `expr` property in your code, you can experiment with replacing it with a measure-driven one. Below you can see an example of the static, out-of-the-box version, and then the “hacked” version.

```c
"expr": {
  "Literal": {
    "Value": "9D"
  }
}
```
```c
"expr": {
  "Measure": {
    "Expression": {
      "SourceRef": {
        "Entity": "table where measures are stored in your model"
      }
    },
    "Property": "conditional formatting measure name"
  }
}
```

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

I want to start my tests with a dynamic font size in the table visual. There are two scenarios to test.

First, to check if we can implement a dynamic font size based on a measure value that can be different for each row in the table (to verify that this hacked conditional formatting respects the context, just like the out-of-the-box background color formatting).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8c0X9Lf2XcGhsq8-FMjyTA.png)

Second scenario is to check whether this custom conditional formatting works when it is a simple switch driven by a helper table, based on which we can have a slicer to decide whether we want a big or small font size.

![](https://miro.medium.com/v2/resize:fit:1218/format:webp/1*LlG5Amd8AXU0mvfbP_5AXA.png)

Below you can see exactly what was modified in the table visuals JSON definitions to implement both measure-driven approaches (unpaid product placement: Visual Studio Code makes those manipulations super comfortable).

![](https://miro.medium.com/v2/resize:fit:3252/format:webp/1*YNT9tgkz8n-e-U1QJTMBcQ.png)

As you can hopefully see in the GIF below, the conditional formatting for font size does not “respect” the row context in the table visual. In our case, it refers to the grand total for the Revenue Year-over-Year percentage change. So we end up with a single font size for the whole table. For the simpler scenario, it works as intended because (no sh\*t, Sherlock 🙃) here the row context isn’t problematic, as there is one selected value of the `font_size` column in the `font_size` table for each and every row in the table visual.

![](https://miro.medium.com/v2/resize:fit:3822/format:webp/1*i5VPM71Hcf1PhM7ezt3qXw.gif)

There was also a different, slightly more complex scenario that I tried to explore. I wanted to test whether I can control whether a visual is visible or not (which, in my dreams, might be a slightly more “controllable” alternative to bookmarks). Therefore I created a visual and then hid it in the Selection Pane. Once saved, I was ready to proceed with the JSON hacking.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MkuRiJb8y5MQoRrflyWtqA.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*iGylTSNLzB_E74ACRON_yA.png)

Once saved as a `.pbip` file, you will find it at the very end of the JSON visual definition.

![](https://miro.medium.com/v2/resize:fit:1146/format:webp/1*GbFvWyf2VdiZ-6lemNlMEA.png)

Unfortunately there is no `expr` property here, so it is either not possible or there needs to be some more convoluted workaround to make it work. Even though the ‘Visual Is Hidden’ measure is of Boolean type (as it always returns either true or false depending on the slicer selections), there seems to be a type mismatch issue. Power BI expects a Boolean value there but gets an object reference. If there is any Power BI nerd who can crack this challenge, I’d be super grateful to learn the details.

![](https://miro.medium.com/v2/resize:fit:1128/format:webp/1*PsptYqDhUqjHVbrYWggwgQ.png)

![](https://miro.medium.com/v2/resize:fit:1380/format:webp/1*eMcE5J_6O4rAsvC5gUsfyA.png)

To sum up, hacking the JSON definitions was a fun exercise, though it did not live up to my expectations. There is also a possibility that this is due to my lack of expertise rather than technical limitations. However, if it’s the first, there is still some hope for me 😊 Have a great start to the new year, and remember: do not use this technique in production!!!

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----485751bc4be2---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Any

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization