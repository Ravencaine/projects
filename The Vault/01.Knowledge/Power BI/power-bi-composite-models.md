---
title: "Power BI composite models"
source: "https://www.flip-design.de/?p=1278"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Power BI composite models – a underestimated feature | flip-it.de :: SQL, BI and more Power BI composite models are not really new, but in my point of view, a really underestimated feature and in my experience, not really often used. Let’s assume, you have two different departments, and every department creates its own models and analysis. But if you want to create an overall analysis of the data, mostly you create a report with the data of both datasets. Okay, this will work, if you have access to both data sources and you have a data warehouse. But what you will do, if not? So, in this case you can connect to both datasets and create a model with all the data, and you need not to care about the actually of the data. The first report looks like this: And the other one looks same, but it contains other data. So, you can create a new report and connect to this dataset. Then, you can connect to the other dataset and convert the connection to a Direct Query. And now, you have a model like this: The color of the tables shows you the different datasets and if you have the same names of a table, it will iterate the names. But the cool thing, you can connect the tables and calculate with data. So, I created a simple measure, which summarize both sales amounts and then you get an overall number: You can also add other tables. But you should take care of refreshing your new report. So, if you schedule a refresh, you will see the new data of both datasets –or some more datasets. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1278)*
