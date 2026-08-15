---
title: "Power BI predefined slicer selections with no generic labels."
source: "https://medium.com/microsoft-power-bi/power-bi-predefined-slicer-selections-with-no-generic-labels-9f1759015141"
author:
  - "[[Mateusz Mossakowski]]"
published: 2026-05-25
created: 2026-08-12
description: "Today I would like to showcase an alternative to the predefined selection in Power BI slicers. Usually you need to use generic labels (for example, “Current Month”, “Predefined Month”, etc.) so that the predefined value can shift to another predefined value — such as the next month’s data reload. Otherwise, if the report is saved with a regular column slicer selection, the selection won’t adjust."
Processed: "Unprocessed"
---
## Today I would like to showcase an alternative to the predefined selection in Power BI slicers. Usually you need to use generic labels (for example, “Current Month”, “Predefined Month”, etc.) so that the predefined value can shift to another predefined value — such as the next month’s data reload. Otherwise, if the report is saved with a regular column slicer selection, the selection won’t adjust.

Fortunately, there is a workaround for this. What are the needed ingredients? First, we need both a regular column with human-friendly names and a technical column with a predefined label (this label is the element we want to use as the predefined state).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kRs8IwqUzjy450E6_wqrtw.png)

Secondly, what needs to happen is to set the `groupByColumn` property for the regular column (`year_month_name`) to refer to the technical column (`year_month_name_group_by`). We can achieve it in two ways.

The first option is to set it in the `TMDL` view.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eV1Ct57t-U5AlwrUTa7jWA.png)

The second option is to use Tabular Editor and set it there.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cbX8k9Ngy-cxwk3uS6Y75g.png)

Once the groupByColumn property is adjusted, we no longer need the technical names, while the predefined selection would still move along.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization