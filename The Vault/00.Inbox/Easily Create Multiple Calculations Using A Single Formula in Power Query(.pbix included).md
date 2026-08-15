---
title: "Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included)"
source: "https://medium.com/microsoft-power-bi/easily-create-multiple-calculations-using-a-single-formula-in-power-query-pbix-included-e4c71b1e6835"
author:
  - "[[Shashanka Shekhar]]"
published: 2026-07-30
created: 2026-08-12
description: "Working with Power Query often involves creating multiple calculations across different columns or scenarios. Instead of writing separate formulas for each, you can streamline the process by leveraging a single formula to generate multiple outputs. This approach not only saves time but also ensures consistency in your data transformation workflows."
Processed: "Unprocessed"
---
## Working with Power Query often involves creating multiple calculations across different columns or scenarios. Instead of writing separate formulas for each, you can streamline the process by leveraging a single formula to generate multiple outputs. This approach not only saves time but also ensures consistency in your data transformation workflows.

- **Efficiency**: Reduce repetitive steps by applying one formula across several calculations.
- **Consistency**: Maintain uniform logic across all derived columns, minimizing errors.
- **Scalability**: Easily extend the same formula to new datasets or additional columns.
- **Flexibility**: Adapt a single formula to handle diverse calculation needs without rewriting logic.
- **Optimization**: Improve performance by reducing redundant transformations.

This is what we wish to achieve, we will go from left table to right.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mWJDInJGaYn8UkvUXRF2Vg.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*QzIuMcqu7lptgrDWviebfQ.png)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Implementation in Power BI:

**We will go through these steps:**

Happy learning!

## 1\. Going through the Table:

The table is called **Multiple\_Columns.**

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*53jJoEKJ8dTr9jxRoXVsPw.png)

**Sales Rep**: Names of individuals (Varsha, Veronica, Ramesh, James, Rajat).

**Sales**: Ranges between 10,400 and 14,200 units of currency.

- Highest: Rajat (14,200)
- Lowest: James (10,400)

**Profit**: Ranges between 3,040 and 5,720.

- Highest: Ramesh (5,720)

## 2\. Opening Power Query:

- In the **Home tab** press on the **Transform Data in the Queries section.**
- It will open the **Power Query** window.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*GeFeP29ED1rA1lHt.gif)

In the Home tab press on the Transform Data in the Queries section

## 3\. Creating A Custom Column:

- In the top menu head to Add Column**.**
- Then select Custom Column.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LvyOtew__1OkBMMKIIz1GA.gif)

- Type the below code in **Custom column formula** and rename Column to **Multiple Column** and press OK.
```c
[
    Cost = [Sales] - [Profit],
    ProfitPct = [Profit] / [Sales],
    Comm = 0.1 * [Profit]
]
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Yvnsd8Y1p8dszxuNwWJ0sQ.gif)

Type the above code in Custom column formula and rename Column to Multiple Column and press OK

## 4\. Expanding the Custom Column:

- Now click on the side **small icon** on the left in the **Multiple Column** to get all the newly created three column.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yf2p4uVR7BxlnvuXPpW48w.gif)

Now click on the side small icon on the left in the Multiple Column to get all the newly created three column

- Click on **Close & Apply** in the upper right column in Home tab.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*q995XfZYOT_wkxa9FnYWtw.gif)

Click on Close & Apply in the upper right column in Home tab

## 5\. Applying The Changes And Completion:

- In the **Report view**, you will find the new table Invoked Function in the **Data** section on the right side**.**
- Now in a **Table** visualization you can add the columns from new table for further analysis.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BljNaWLFmv6saUfT1-VphA.gif)

> Download the data for the KPI from this [link](https://drive.google.com/file/d/1aTKHmQsP6__zJonEheM8Yl83huNK3sLU/view?usp=sharing).
> 
> Download the PBIX file from this [link](https://drive.google.com/file/d/1Kkhyu--606no5MOzmcGlItddQJpuTO5t/view?usp=sharing).

## [Shashanka Shekhar - Medium](https://medium.com/@shashanka.shekhar02?source=post_page-----e4c71b1e6835---------------------------------------)

### Read writing from Shashanka Shekhar on Medium. Contributor for Microsoft Power BI. I like Data Analysis and Data…

medium.com

Thank you for your attention!

[Follow](https://medium.com/@shashanka.shekhar02) me or [subscribe](https://medium.com/@shashanka.shekhar02/subscribe) to get all my Power BI articles!

## [Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included)](https://medium.com/microsoft-power-bi/using-visual-calculation-to-easily-calculate-avg-3-month-sales-in-power-bi-pbix-included-0a6d3b76f703?source=post_page-----e4c71b1e6835---------------------------------------)

### Calculating rolling averages is a common requirement in sales analysis, especially when managers want to smooth out…

medium.com

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX, Power Query