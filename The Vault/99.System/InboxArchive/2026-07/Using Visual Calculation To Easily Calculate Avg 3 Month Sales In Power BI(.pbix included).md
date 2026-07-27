---
title: "Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included)"
source: "https://medium.com/@shashanka.shekhar02/using-visual-calculation-to-easily-calculate-avg-3-month-sales-in-power-bi-pbix-included-0a6d3b76f703"
author:
  - "[[Shashanka Shekhar]]"
published: 2026-07-27
created: 2026-07-27
description: "Calculating rolling averages is a common requirement in sales analysis, especially when managers want to smooth out fluctuations and identify consistent performance trends. In Power BI, this can be achieved through multiple approaches, but Visual Calculation offers a more intuitive and flexible way to handle such tasks without complex DAX formulas."
Processed: "Unprocessed"
---
## Calculating rolling averages is a common requirement in sales analysis, especially when managers want to smooth out fluctuations and identify consistent performance trends. In Power BI, this can be achieved through multiple approaches, but Visual Calculation offers a more intuitive and flexible way to handle such tasks without complex DAX formulas.

how Visual Calculation simplifies the process:

- **Sales Trend Analysis** Businesses often need to track average sales over a moving 3‑month window to spot growth patterns or seasonal dips.
- **Traditional DAX Approach** While possible, writing DAX for rolling averages can be time‑consuming, error‑prone, and difficult for non‑technical users to maintain.
- **Visual Calculation Advantage** This feature allows analysts to define calculations directly within visuals, reducing dependency on complex measures.
- **Ease of Use** Drag‑and‑drop functionality makes it accessible for business users who want quick insights without coding.

This is what we wish to achieve.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*42pam0CACVZ61UwW8Xgwbw.png)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Implementation in Power BI:

**We will go through these steps:**

- [About The Table Used](#c551)
- [Creating The Table](#c830)
- [Adding Visual Calculation](#44c2)
- [Completion Step](#1632)

Happy learning!

## 1\. About The Table Used:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*QvrgcVmN4xW3gyFKtpAtcA.png)

- **Year**: All entries are from 2007.
- **Month**: Data is broken down by month from January to August.
- **Total Sales**: Represents the monthly sales figures.

## 2\. Creating The Table:

- Now in a **Table** visualization add Year, Month and Total Sales Columns.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*W7GZoj1K6xJ1pORW2eKoaw.gif)

Now in a Table visualization add Year, Month and Total Sales Columns

## 3\. Adding Visual Calculation:

- Select the table **right click** and select **New visual calculation.**
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pTzKO57d-4NlhHPQ5IyDvA.gif)

Select the table right click and select New visual calculation

- Now create the below DAX.
```c
Avg Past 3 Months = 
IF(
    ISATLEVEL([Month]),
    FORMAT(MOVINGAVERAGE([Total Sales], 3), "#,#.0")
)
```

This is how the DAX works:

- `**ISATLEVEL([Month])**`: This acts as a safety check. It returns `TRUE` only if the current row in the visual is at the `[Month]` level. If the visual rolls up to a higher level (like `[Year]`), it returns `FALSE`, and the calculation returns blank. This prevents misleading averages from appearing on total rows.
- `**MOVINGAVERAGE([Total Sales], 3)**`: This section calculates the average of the current row's `[Total Sales]` and the previous 2 rows' sales (a 3-row moving window total).
- `**FORMAT(..., "#,#.0")**`: This portion converts the resulting average into a text string formatted with thousands separators and exactly one decimal place (e.g., `583.3`).
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*P3pacVrZURn15TBsZ9pHWQ.gif)

Now create the Avg Past 3 Months DAX

## 4\. Completion Step:

- Now select Back to report where you can easily visualize this data**.**
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-15IE91XEIy8vTz4rUw8EQ.gif)

Now select Back to report where you can easily visualize this data

> Download the data for the KPI from this [link](https://drive.google.com/file/d/1SLTazQhL8FrGi5nuvqfxvgUA_zb4EmdN/view?usp=sharing).
> 
> Download the PBIX file from this [link](https://drive.google.com/file/d/1OpS1zfVE7rHRdMUqePASZa9Ts-28frW3/view?usp=sharing).

## [Shashanka Shekhar - Medium](https://medium.com/@shashanka.shekhar02?source=post_page-----0a6d3b76f703---------------------------------------)

### Read writing from Shashanka Shekhar on Medium. Contributor for Microsoft Power BI. I like Data Analysis and Data…

medium.com

Thank you for your attention!

[Follow](https://medium.com/@shashanka.shekhar02) me or [subscribe](https://medium.com/@shashanka.shekhar02/subscribe) to get all my Power BI articles!

## [Easily Line Break A Complex Multiline Column Using Power Query(.pbix included)](https://medium.com/@shashanka.shekhar02/easily-line-break-a-complex-multiline-column-using-power-query-pbix-included-782235edc7eb?source=post_page-----0a6d3b76f703---------------------------------------)

### Working with complex datasets often means encountering columns that contain multiple lines of text packed into a single…

medium.com

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX