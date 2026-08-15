---
title: "Fully Controllable Best-Performing Items Comparison in Power BI"
source: "https://medium.com/microsoft-power-bi/fully-controllable-best-performing-items-comparison-in-power-bi-05d480cbea36"
author:
  - "[[Mateusz Mossakowski]]"
published: 2025-03-17
created: 2026-08-12
description: "In this article, I will explore the capabilities of Power BI that allow you to perform precise comparisons. Whether you’re aiming for a straightforward head-to-head analysis of your top products against those of your competitors or seeking the flexibility to create customized comparisons, I have some tips to help you implement these functionalities. Discover how to compare your leading products directly with the corresponding competitor products, or tailor your analyses to examine specific rankings, such as your best-seller against their third or fourth best-seller."
Processed: "Unprocessed"
---
## In this article, I will explore the capabilities of Power BI that allow you to perform precise comparisons. Whether you’re aiming for a straightforward head-to-head analysis of your top products against those of your competitors or seeking the flexibility to create customized comparisons, I have some tips to help you implement these functionalities. Discover how to compare your leading products directly with the corresponding competitor products, or tailor your analyses to examine specific rankings, such as your best-seller against their third or fourth best-seller.

Hopefully, the above GIF is self-explanatory regarding what I aimed to achieve, but in case it’s not entirely clear, let me clarify in this paragraph. The goal is to enable easy comparisons between our company’s best-selling products and the corresponding best-selling products from competitor companies. To make this process more robust and flexible, I wanted to provide the option for a straightforward head-to-head comparison of our top 1 to 5 products. Additionally, for users with more specific needs, I aimed to allow comparisons such as our 1st product against their 3rd, our 4th against their 5th, or any other combination that the end user might envision.

> 🎖️ Article was awarded as **Must-Read** by [**Power BI Masterclass community**](https://linktr.ee/powerbi.masterclass).

While aggregated TOPN analyses are relatively straightforward in Power BI, conducting head-to-head or custom comparisons of best-performing products requires additional setup and the creation of DAX measures. Let’s walk through the steps needed to deliver the solution described above.

First, we need a sort of disconnected ranking component within the semantic model. This part of the model should be entirely separate from the “core” semantic model. In this setup, in the “center” we should find the main ranking table, surrounded by our company ranking table (connected through an active relationship) and the competitor ranking table (connected via an inactive relationship that we will activate only for the “custom” comparisons). Additionally, we will include a comparison type dimension that drives the behavior of the comparisons, distinguishing between (a) head-to-head and (b) custom analyses.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DYX_KYFEg0kQ5dvJ6L_Lhw.png)

“disconnected” ranking part of the semantic model

### What does Dr. Dre have in common with Power BI?

You might think this question is confusing at first, and you’re right — it is! However, Power BI indeed has a property called DRE (Detail Row Expressions) 😅 We will make use of this concept. While DRE was primarily designed for Analyze in Excel ([link](https://www.sqlbi.com/articles/controlling-drillthrough-using-detail-rows-expressions-in-dax/)), we can use it in a “fake” and empty measure that will act as a reusable table expression, which is a perfect fit for our scenario.

In our case, we have two DREs: one for our company products and another for products from the competition. Each DRE results in a virtual table containing product IDs, along with ranking and revenue measures. These DREs can easily be extended with additional columns or measures depending on your reporting needs.

Firstly let’s stop for a sec on the ranking measure that is used within DRE. There is a little flavor added on top. And this is a fun way of forcing the ties to be actually split based on the secondary RANKX. In this case it’s based on the order of product ID but it can also be alphabetical sorting in case of strings, as well.

Now, let’s jump to the core measures. I will focus on those related to our company product IDs and revenue, as the measures for the competition would be nearly identical, with the only differences being a reference to another DRE “fake” measure and a different rank column from the ranking table. *You can find competition measures definitions at the end of the article.*

First, let’s examine the measure responsible for returning the top best-selling product IDs. As you can see in the first variable, depending on the comparison type, we either activate the relationship between the ranking and ranking\_competition tables (which narrows down the selected combinations of our products versus those of the competition) or simply use the selected ranking when opting for a straightforward head-to-head comparison. In this case we totally “ignore” what is selected in the competition rank slicer.

As you can see in the DAX editor in Power BI Desktop, it “does not like” empty DRE measures, which are underlined in red. Despite this visual cue, they work like a charm 😉

When it comes to the revenue measure, it’s a bit more complex due to the “dual” nature of the calculation. We cannot “embed” table variables within an IF statement — only measures can be used in that context. However, aside from the DAX coding nuances, the concept remains identical to that used for the product IDs measure.

Let’s look at a couple of examples to illustrate how this setup works in practice.

*Scenario 1:* ***Comparing the 3 Best-Selling Products***

*Scenario 2:* ***Comparing the 2nd Best-Selling Our Company Product with the 3rd Best-Selling Competitor Product***

*Scenario 3:* ***Comparing the 3rd Best-Selling Our Company Product with Both the 3rd and 4th Best-Selling Competitor Products***

To ensure you have the full picture, below I am also providing the definition of the competition measure. This will help you understand how it aligns with our previously discussed measures.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*2Y83Kj3iQQkHAOkDBUdEoA.png)

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*vjLNhEVHQpF9Go1rAHeQVQ.png)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----05d480cbea36---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee