---
title: "Why should you create explicit measures?"
source: "https://www.flip-design.de/?p=987"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Why should you create explicit measures? | flip-it.de :: SQL, BI and more Some people ask me, why should I create a measure by using Power BI? Yes, you can use every column which contains a number and put them into a value box in Power BI and create different calculations on it. My first answer by this question is, if you need a calculation e.g., Sales Amount without canceled orders, you must filter on ever page or on the whole report the canceled order out. But if you want to compare the canceled orders to the others, then it is maybe a little bit complicated. F you create a measure with and without the filter, it is much easier. Another point is, when you want to analyze the dataset with Excel to use it with an XMLA endpoint by using Excel. There it is not possible to put a column, which is not a measure, into the values. The reason is, that the Power BI dataset is an Analysis Services Model in behind. So, I suggest creating for every calculation a measure, it does not matter if it is only a simple SUM() or a complex calculation. If you do so, then you do not have troubles by using other tools than Power BI. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=987)*
