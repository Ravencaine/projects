---
created: 2026-07-27
source: "Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included)"
source_url: https://medium.com/@shashanka.shekhar02/using-visual-calculation-to-easily-calculate-avg-3-month-sales-in-power-bi-pbix-included-0a6d3b76f703
note_type: source
tags: [dax-code]
---

## Calculating rolling averages is a common requirement in sales analysis, especially when managers want to smooth out fluctuations and identify consistent performance trends. In Power BI, this can be achieved through multiple approaches, but Visual Calculation offers a more intuitive and flexible way to handle such tasks without complex DAX formulas.

how Visual Calculation simplifies the process:

- **Sales Trend Analysis** Businesses often need to track average sales over a moving 3‑month window to spot growth patterns or seasonal dips.
- **Traditional DAX Approach** While possible, writing DAX for rolling averages can be time‑consuming, error‑prone, and difficult for non‑technical users to maintain.
- **Visual Calculation Advantage** This feature allows analysts to define calculations directly within visuals, reducing dependency on complex measures.
- **Ease of Use** Drag‑and‑drop functionality makes it accessible for business users who want quick insights without coding.

This is what we wish to achieve.



## Implementation in Power BI:

**We will go through these steps:**

- [About The Table Used](#c551)
- [Creating The Table](#c830)
- [Adding Visual Calculation](#44c2)
- [Completion Step](#1632)

Happy learning!

## 1\. About The Table Used:


- **Year**: All entries are from 2007.
- **Month**: Data is broken down by month from January to August.
- **Total Sales**: Represents the monthly sales figures.

## 2\. Creating The Table:

- Now in a **Table** visualization add Year, Month and Total Sales Columns.

Now in a Table visualization add Year, Month and Total Sales Columns

## 3\. Adding Visual Calculation:

- Select the table **right click** and select **New visual calculation.**

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

Now create the Avg Past 3 Months DAX

## 4\. Completion Step:

- Now select Back to report where you can easily visualize this data**.**

Now select Back to report where you can easily visualize this data

> 

## [Shashanka Shekhar - Medium](https://medium.com/@shashanka.shekhar02?source=post_page-----0a6d3b76f703---------------------------------------)

### Read writing from Shashanka Shekhar on Medium. Contributor for Microsoft Power BI. I like Data Analysis and Data…

medium.com

Thank you for your attention!


## [Easily Line Break A Complex Multiline Column Using Power Query(.pbix included)](https://medium.com/@shashanka.shekhar02/easily-line-break-a-complex-multiline-column-using-power-query-pbix-included-782235edc7eb?source=post_page-----0a6d3b76f703---------------------------------------)

### Working with complex datasets often means encountering columns that contain multiple lines of text packed into a single…

medium.com

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX

> See also [[all]] for reference.


> See also [[calculate]] for reference.


> See also [[movingaverage]] for reference.


> See also [[visual-calculations]] for reference.


> See also [[measures-vs-calculated-columns]] for reference.
