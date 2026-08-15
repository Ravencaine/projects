---
title: "Incomplete Data at a self service BI project with Power BI?"
source: "https://www.flip-design.de/?p=899"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Incomplete Data at a self service BI project with Power BI? | flip-it.de :: SQL, BI and more Mostly at self service BI Projects the business users imports data from unproven sources – like Excel. But if you have a project and/or source like this, data can be have problems, because at a CSV or Excel file the data format can be anything. When you take look at following screenshot. There a two tables. One has the facts (sales per date and branch). The second table provides the branches and here, I’ve added a row with the ID “-2”, this provides as a key, which doesn’t exists at the most sources. This key can be used to map error rows. So, if you import the data, everything is fine and you can make insights of it: But after some time, it can be happen that user insert some data which can be not used by the data model: Then you get following error when you refresh the data and the row will not be loaded and the end-users thinks everything is fine. To avoid this problem you can edit your Power Query ETL process and replace this error by set the “-2” Now, you will get the row and will mapped to the Key from the dimension To notice the users or to build up a QA dashboard, you can write some DAX code to count the errors and give some notice to the users  Comments are closed.

## Code / Examples

```
Missings = var missings = CALCULATE(COUNTA(Facts[BranchId]), FILTER(Branch, Branch[BranchId] = -2 ) ) var message = IF(missings > 0, "Some branches are have incomplete data", "") return message
```


---
*Source: [flip-design.de](https://www.flip-design.de/?p=899)*
