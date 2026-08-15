---
title: "Power BI TMDL table creation"
source: "https://www.flip-design.de/?p=1533"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Power BI TMDL table creation | flip-it.de :: SQL, BI and more Using TMDL, entire environments can be prepared in this way. In this example—which can, of course, also be used in production—a complete date table is created exactly as it is typically used. Months and days are sorted in correct calendar order. Numeric fields are not aggregated, because aggregation generally doesn’t make sense in a calendar. You can find Microsoft’s official documentation here, including how to enable and use TMDL: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-tmdl-view The script listed below is inserted into the TMDL editor and then executed. As a result, the Dim Date table is available in the model. To populate the table, the CALENDARAUTO() function is used. The data model is scanned for columns of type DATE ; the smallest and largest date values are defined as the start and end dates. The date table therefore contains values between these two bounds. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1533)*
