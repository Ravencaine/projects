---
title: "Calculation Groups"
source: "https://www.flip-design.de/?p=1189"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Calculation Groups – How to exclude Measures | flip-it.de :: SQL, BI and more Mostly, if you read about Calculation Groups Inside Tabular Models, you get examples about Time Intelligence. But if you make other calculations, e.g., a Forex calculation, you don’t want to apply the calculation to every measure. So, you don’t want to apply the calculation to the Number of Sales or something like that. In that case, you can use SELECTEDMEASURENAME() to filter out these measures. To demonstrate it very simple, I have added a simple table to a Dashboard in a Day data model to get a forex to year. With this table we can calculate the USD vales to Euro. After creating this table, I created a calculation group with two members, one for Euro and one for USD to use this for a slicer. Inside the Tabular Editor I created following calculation for each member: The calculation checks, if the measure name is not the Number of sales, if yes, the results are divided by the given forex, if no, no calculation will be applied. With that solution you should be aware that, you need to add every measure that is not be calculated. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1189)*
