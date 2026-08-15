---
title: "Power BI — Object Level Security"
source: "https://medium.com/@michalmolka/power-bi-object-level-security-a3f476dd6768"
author:
  - "[[Michal Molka]]"
published: 2022-03-18
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Everyone who works with Power BI has heard or used an Row Level Security. But not everyone knows that Power BI offers an OLS — Object Level Security. If you want to restrict an access to a particular object like a table or a column. You can use this functionality. As of today, you have to use Tabular Editor to implement the OLS. There is no option to implement it through the Power BI Desktop/Service UI.

At the beginning, I’ve created a model containing two identical tables, two measures and two visualizations. Each of measures and visualizations uses a different table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oBbp7omvQ4fvjp8GiCb2BQ.png)

The second step is to create a Role where we apply the OLS.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7_aCE4p6GyH1Zb3e2CZ5Lw.png)

In Tabular Editor, lets restrict an access to the entire table. In order to do this, you need to select a role. Afterwards, in the **Security** section -> select a table inside a **Table Permissions** subsection, and then select “ **None** ”.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lIXpWSjo_F3JRw-YTtq_rw.png)

Once you saved changes and selected a Role in PBI Desktop (View as roles).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*R0trg-kvtEjHZkpwves82g.png)

The second visualization is useless. Why? The restricted table is invisible from a model standpoint, theoretically it doesn’t exist in the model for this particular group (Restricted OLS).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NGlNj9D_E8sgNw3gX0XiLA.png)

Let’s assume that we want to restrict an access to two columns, not an entire table.

Expand a **Tables** folder, do the same with a table. Pick a column which you want to hide. In the **Object Security Section** change the state to “ **None** ”.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9L3b44aU41jkEfxacM7WYw.png)

After the model has been saved. You are no longer able to see affected columns. In this case the \[**ID**\]and the \[**Invoice\_Item\_Number**\].

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*aHndSfgrzuCMfQaduhzRhQ.png)

After the report is deployed to the Power BI Service, you can add users or groups who should belong to the restricted group. A configuration is performed in the Dataset Security section.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wr-M0vedc_H-HY6QZPkH1A.png)