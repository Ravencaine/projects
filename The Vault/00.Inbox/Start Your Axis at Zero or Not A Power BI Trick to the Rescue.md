---
title: "Start Your Axis at Zero or Not? A Power BI Trick to the Rescue"
source: "https://medium.com/microsoft-power-bi/start-your-axis-at-zero-or-not-a-power-bi-trick-to-the-rescue-3e3310fcb857"
author:
  - "[[Mateusz Mossakowski]]"
published: 2025-08-21
created: 2026-08-12
description: "There’s an endless debate about whether it’s better to start your axis right at zero (the classic, orthodox way) or somewhere closer to the minimum value (which can exaggerate the scale but makes spotting changes much easier). I usually have my preferences, but I won’t reveal them here — because now, you don’t have to choose just one anymore. You can have your cake and eat it too! Let me show you how to do it in Power BI — super easy, I promise."
Processed: "Unprocessed"
---
## There’s an endless debate about whether it’s better to start your axis right at zero (the classic, orthodox way) or somewhere closer to the minimum value (which can exaggerate the scale but makes spotting changes much easier). I usually have my preferences, but I won’t reveal them here — because now, you don’t have to choose just one anymore. You can have your cake and eat it too! Let me show you how to do it in Power BI — super easy, I promise.

Here’s what you’ll need for this recipe:

1. A scale type table with two rows — I have “proper” for the axis starting at zero and “heretic” for the axis starting dynamically around the overall minimum value.
2. A simple measure that grabs the selected value from that scale type table
3. A measure that calculates the overall minimum (I suggest multiplying it by 0.95 so that markers don’t get cut off in the line chart or scatter chart).
4. Bonus: a measure for the overall maximum, multiplied by 1.05 — again, to avoid cutting off markers or labels.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

For the first point, I include the TMDL code containing also the Power Query part for a simple static table. Honestly, I much prefer this **Table.FromRows** approach over “Enter data” because it lets us tweak the input more naturally — especially useful when working with large models managed only through XMLA endpoints with external tools (shoutout to Tabular Editor 3 ❤️).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*UmoKSjococh8upBBMn482w.png)

scale type table

```c
createOrReplace

 table scale_type
  lineageTag: e6d0f146-fa60-406a-aa96-9de3d750bd17

  column order
   dataType: double
   formatString: 0
   lineageTag: 869e876f-89a7-4343-9115-e0ebe5015b31
   summarizeBy: none
   sourceColumn: order

   annotation SummarizationSetBy = Automatic

  column name
   dataType: string
   lineageTag: bf5fd923-f8e7-4ebc-a0bf-005911fae6aa
   summarizeBy: none
   sourceColumn: name
   sortByColumn: order

   changedProperty = SortByColumn

   annotation SummarizationSetBy = Automatic

  partition scale_type = m
   mode: import
   source =
     let
         Source =
             Table.FromRows(
                 {
                     { 0, "proper 🕊" },
                     { 1, "heretic 👹" }
                 },
                 type table [order = number, name = text]
             )
     in
         Source

  annotation PBI_ResultType = Table

  annotation PBI_NavigationStepName = Navigation
```

For the second point — nothing fancy, just good old SELECTEDVALUE.

The minimum and maximum measures might sound tricky, but only the minimum depends on the scale type selection made by the end user. If someone selects “proper” scale the axes start at zero. Otherwise they start “around” the overall minimum value.

And that’s it — all ingredients are ready. The final step is to tweak the axis minimum values so they’re no longer automatic but instead depend on your end user’s selection. The maximum will be dynamic and context-dependent.

Now your report delivers the best of both worlds: the orthodox *start-at-zero-no-matter-what* and the *I-don’t-care-about-zero* flexibility 😉

## [Get an email whenever Mateusz Mossakowski publishes.](https://medium.com/@mossakowski.mateusz/subscribe?source=post_page-----3e3310fcb857---------------------------------------)

### Get an email whenever Mateusz Mossakowski publishes. By signing up, you will create a Medium account if you don't…

medium.com

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-end) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----3e3310fcb857---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization