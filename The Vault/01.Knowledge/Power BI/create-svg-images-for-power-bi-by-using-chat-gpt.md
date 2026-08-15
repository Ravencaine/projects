---
title: "Create SVG images for Power BI by using Chat GPT"
source: "https://www.flip-design.de/?p=1503"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Create SVG images for Power BI by using Chat GPT | flip-it.de :: SQL, BI and more Last week, a friend asked me why he could no longer create functioning SVG graphics from Chat GPT that he could use in Power BI. This surprised me a bit. I then entered a query for a graphic there, had the graphic output as an SVG, and then inserted it into Power BI. Unfortunately, this didn’t work. The problem was relatively simple; in the end, the following function was used: ENCODEURL However, this doesn’t exist in Power BI, only in Excel. Personally, I think creating SVG graphics for Power BI is great; I also use this for icons, which I then use for graphics in Visio. Here is a sample query for Chat GPT that returns such an SVG graphic, which you can then insert as a measure within Power BI. The following result is then returned: The returned code can then be inserted into Power BI: I gave a further description of this in the following blog entry: SVG image inside Power BI with Figma Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1503)*
