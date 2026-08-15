---
title: "Power BI conditional slicers with a little bit of fields parameters magic"
source: "https://medium.com/microsoft-power-bi/power-bi-conditional-slicers-with-a-little-bit-of-fields-parameters-magic-e00eb6c94b54"
author:
  - "[[Mateusz Mossakowski]]"
published: 2026-02-17
created: 2026-08-12
description: "Today I want to show you a technique to conditionally make slicers unavailable. Let’s imagine that tax measures are only available at the product manufacturer level. Revenue measures are also available at the granularity of product category and product brand. Since I’m a little allergic to bookmarks, I want to find a way to conditionally disable the category and brand slicers in case someone jumps into tax measures analysis. Let me show you how it works. This is built on top of some fields parameters magic and a single-cell dummy table."
Processed: "Unprocessed"
---
Featured

## Today I want to show you a technique to conditionally make slicers unavailable. Let’s imagine that tax measures are only available at the product manufacturer level. Revenue measures are also available at the granularity of product category and product brand. Since I’m a little allergic to bookmarks, I want to find a way to conditionally disable the category and brand slicers in case someone jumps into tax measures analysis. Let me show you how it works. This is built on top of some fields parameters magic and a single-cell dummy table.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

Let me start with a brief description of two view types available in this Power BI report tab.

- Option 1: lets you freely filter by product manufacturer, product category, and product brand. But it prevents viewing tax measures (only revenue measures are available).
- Option 2: gives full visibility of the measures (both revenue and tax), but since tax figures do not exist at the category or product granularity, those levels should be unavailable both in the rows of the matrix and in the slicers.

To have a single place to switch between these options, we will create a very simple table which we will relate later to two field-parameters tables, which I will describe shortly.

![](https://miro.medium.com/v2/resize:fit:1176/format:webp/1*XX1McH8zxEqbYTAKY7Wb4A.png)

option table

I’ll start with the simpler fields parameters table, which is the measures table. No rocket science here. The only trick here is that the set of revenue measures is repeated for the sake of Option 1. The `option_type` column is the only expansion from the out-of-the-box field-parameters table setup.

OK, I lied a bit there — there is one sorcery here: I am using REPT and UNICHAR(10) combinations to fake the measure grouping labels 😉

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LvjVirCfUy4Ky6T6AwNhjg.png)

measures fields parameters table

The second fields parameters table (for slicers and matrix rows purposes) is a bit more sophisticated. We also have repeated records for all three product attribute-related fields, though for Option 2 we want to make both category and brand fields unavailable. That is why in the fields column for Option 2 we do not refer to the real product dimension columns; instead we refer to the single-cell dummy table (the not\_available table), whose sole purpose is to show a single “Not available” field in the slicer drop-down. There is also a slicer label column which we use to indicate to the end user that those slicers are not available. To make our lives easier, we also have a binary availability flag.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Khj4gnA_GQJjuQqHhQcYTg.png)

slicers and matrix rows fields parameters table

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*_ALcACkRlwIpVqHe8GqYQQ.png)

not\_available table

The last piece of the data modeling setup is to create relationships between both fields parameters tables and the option table.

Last two polishing moves from the semantic model perspective — two extremely simple measures built on top of the pSlicer fields parameters table. The first will be used as a dynamic slicer title. The second will make the unavailable category and brand slicers visually stand out.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XVJh0EZ6r4rQmgFAyH-d8A.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*iwkNFz_7m9JPZ8XMe-goKQ.png)

Now we can jump into how the report tab is built. Let me divide it into three component groups.

### Number 1

A super simple button slicer built on top of a single point of selection option table (label column). One thing worth mentioning is that this slicer affects both the product dimension related slicers and the matrix.

### Number 2

Three product-dimension related slicers that are all built using the same methodology. Let’s take the category slicer as an example. In all three cases we use the `p_slicer` column in the Field section (nothing fancy here). One crucial thing is that in the Filter pane we filter the `p_slicer_order` column to an attribute-specific number (1 for manufacturer, 2 for category, and 3 for brand). Then, from the visual perspective, we use the two above-mentioned measures to add both a dynamic slicer title and to make the title font red in case it is unavailable for the Option 2.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*ea5nHcgqtSfZp_XyfJ0b4w.png)

product dimension related slicers setup

### Number 3

When it comes to the matrix itself, nothing complex here. We use both the column and measure-related fields parameters columns for the Rows and Values fields, respectively. The only thing worth mentioning is that we use the `available_flag` filter. The purpose is to avoid showing repeated “Not available” values in the matrix for the category and brand columns under Option 2.

![](https://miro.medium.com/v2/resize:fit:1130/format:webp/1*K7w41Fl-6y5fTliz1Nwr4A.png)

Once all the steps described above are complete, we’re ready for showtime. When Option 1 is selected, we only see revenue measures, but we can slice by manufacturer, category, and brand. When we switch to Option 2, both the category and brand slicers become unavailable, but as a reward we get tax measures 😉

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----e00eb6c94b54---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualizaton, DAX

**Tags:** Tutorial, Data Visualization, DAX