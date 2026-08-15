---
title: "Grouping & Binning in Power BI — Select Distinct"
source: "https://medium.com/@simon.harrison_Select_Distinct/grouping-binning-in-power-bi-select-distinct-048660a5a124"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2026-02-05
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*HtgpsZ-WF25OcYOl.png)

When you’re working with real‑world data, the raw numbers only tell part of the story. Whether you’re analysing sales, expenses, customer behaviour, or operational performance, the real insight comes from seeing how values are distributed — not just what the totals look like.

That’s where **grouping** and **binning** in Power BI come in. These features make it easy to turn detailed, granular data into clear and meaningful patterns. And once your bins are set up, you can take the analysis further by adding a cumulative frequency distribution to show how values build up across the different ranges.

This post breaks down what these tools do, why they’re useful, and how you can apply them to make your Power BI reports clearer, more intuitive, and far more insightful.

**What Are Grouping and Binning?** **Grouping**

Grouping lets you combine categories into logical clusters.

For example:

Grouping individual State‑Province entries into broader country‑level categories

It’s ideal when you want to simplify long lists or tidy up inconsistent categories

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*2imAwc0oZ5hh_xKd.png)

**How the Group Looks When Used in a Visual**

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*yHUWWbPhchZH6-7C.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*6OhzB2pYGqHpW6VW.png)

Breaking these out from ‘Other Components’ allows us to surface meaningful differences between product types and gives a more accurate picture of category performance across regions.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*wE1dd4WZa1FW5SKh.png)

**How to Create a Group in Power BI**

This chart shows how the Country group can be used to filter the report, with the grouped field limiting the view to sales for the United Kingdom only (or other countries).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*cyeJ9VDrXSzb_CVI.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*rJ00TYIzshQAWTYr.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*e7mvl6VQ3IVPp60s.png)

Step 1 — Choose the field you want to tidy  
Select a categorical column such as product type, region, or state‑province.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*BgWC5-v5J2LVC7lo.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*cgAVe4lS9LO84-80.png)

- Combine several small product types into **Other Components**
- Group individual state‑province entries into **Country** buckets

Step 2 — Create the group  
Right‑click the field → **New Group**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*SOOfSYIPEKS3DaDc.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*oxMSHYDgYF8cSsrz.png)

**Binning**

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*8x6_xBJmoXxAPHRU.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*uL6Vp1GhalC86P-f.png)

Step 3 — Select items to group  
In the *Ungrouped values* list, highlight the items you want to combine → click **Group**

- £0-£250
- £250-£500
- £500-£750
- £750-£1,000
- …and so, on up to £3,500+

**How Binning Looks When Used in a Visual**

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*4aEUXkgmAUzpXthW.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*DEOVjATovv9eK9oc.png)

Examples:

Step 4 — Name your group  
Give the new group a clear name such as **Other Components (Groups)** or **State‑Province (Country Groups)**

- Build histograms
- Identify clusters or gaps
- Spot outliers
- Understand typical value ranges
- Prepare for cumulative analysis

**Why Binning Matters**

Power BI creates a new field you can use in slicers, visuals, and hierarchies.

- *Where do most of my values sit?*
- *Are there many small items or a few large ones?*
- *Is my data tightly grouped or spread out?*

Binning creates numeric ranges

for example: Bin Size 250

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*2vbCBVeqCN34pjZR.png)

**How to Create Bins in Power BI** **Step 1 — Choose your numeric field**

This gives you ranges like:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*yHsT-lFDLKD4_0wk.png)

**Step 2 — Create a bin**

This visual shows how much sales value comes from products whose list price falls into each bin.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*2w0OICqYvR4k2Zns.png)

Power BI automatically assigns each record to the correct range, giving you a structured view of how your values are distributed.

- **Bin size** (e.g., £100 increments)
- **Number of bins**
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*IpLKeHu_BOKiVbTn.png)

**Step 3 — Add the bin to a visual**

Binning is especially useful when you want to:

- **Axis** → your bin field *(List Price — Bins)*
- **Values** → Sum or count of your original field *(Sum of Sales)*
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ecAhOAwjF8Ix9Ru2.png)

**Optional: Add a Cumulative Frequency Distribution**

Raw numbers can be overwhelming. Binning helps you answer questions like:

It’s a simple way to reveal the **shape** of your data — something totals alone can’t show.

- *What percentage of expenses fall under £200?*
- *At what point do 80% of invoices accumulate?*
- *How quickly do values rise across the bins?*

For example: *“By binning our list prices, we can quickly see that most of our sales come from products priced around £2,500,* with much smaller totals in the lower price brackets.

**Cumulative Frequency Measures** **A basic cumulative measure**

Select the column you want to analyse (e.g., sales amount, list price)

Right‑click the field → **New Group** → choose **Bin**

You can define:

Power BI creates a new field such as *List Price (bins)*

A column chart or bar chart works perfectly for a frequency distribution.

You now have a clear view of how your values fall across ranges.

Once your bins are in place, you can add a cumulative view to understand how values build up across the ranges.

A **cumulative frequency distribution** answers questions like:

**Cumulative percentage**

It’s a simple but powerful way to reveal thresholds and concentration.

Cumulative Frequency =

CALCULATE(

COUNTROWS(‘Table’),

FILTER(

ALLSELECTED(‘Table’\[Amount (bins)\]),

**Comparing the Cumulative Distribution Across Price Bins**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*l4JzVYC7bVGCYPuW.png)

**Tips for Cleaner, More Insightful Bins**

- Keep bin sizes consistent
- Avoid too many bins (8–15 is usually ideal)
- Rename bins for clarity (e.g., “£0-£100”)
- Sort bins numerically, not alphabetically
- Add tooltips to show exact cumulative values

‘Table’\[Amount (bins)\] <= MAX(‘Table’\[Amount (bins)\])

**Final Thoughts**

)

)

Cumulative % =

DIVIDE(

\[Cumulative Frequency\],

CALCULATE(COUNTROWS(‘Table’), ALLSELECTED(‘Table’))

)

You can either add a cumulative line to your existing column chart or create a separate cumulative chart using the same measures to compare both views.

These small touches make your visuals feel polished and professional.

Grouping and binning are some of Power BI’s most underrated features.

With just a few clicks, you can transform raw numeric data into a clear, intuitive distribution. And if you choose to add a cumulative frequency distribution, you unlock an even deeper understanding of how your values build up across ranges.

Whether you’re analysing expenses, sales, operational metrics, or care‑home fees, these techniques help you move beyond totals and into meaningful insight.

If you’d like to explore more:

Head over to our [Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/) for insights, walkthroughs and scenario-driven guides

Or our [Power BI Glossary](https://www.selectdistinct.co.uk/glossary-powerbi/) for clear, beginner friendly definitions