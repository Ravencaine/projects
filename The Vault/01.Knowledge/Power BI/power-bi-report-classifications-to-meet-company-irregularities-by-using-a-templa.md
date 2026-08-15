---
title: "Power BI report classifications to meet company irregularities by using a template"
source: "https://www.flip-design.de/?p=1160"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Power BI report classifications to meet company irregularities by using a template | flip-it.de :: SQL, BI and more In the past, I think it was at the Power BI Summit in Amsterdam, I attended at a very cool session about assigning Power BI reports to different types of data classes. The idea is, to give the users an idea if the data and the measures are approved or more of self service without approved data sources. So, there are bronze, silver or gold reports. Bronze means, that the data is not approved, silver means, that the data is approved and gold means, that the data is from secured and approved data sources. I’ve worked a little bit to improve the idea and created a solution like this. So, firstly I created a table to classify the reports with a link of the different classifications. Next, I created a parameter to give the report the classification: The next step, is to filter the table by the given parameter: The other parameter is to provide a hyperlink to provide information’s to the report and the data inside: The parameter is converted to a table, so we can use the link inside the report. Next, I’ve created a background image by using PowerPoint with the theme for the different classifications. The slides are exported to background images. Then I created a tooltip report with a text box inside to show the classifications. With the dynamic values you can create the textbox. Now, the user can edit the parameters to provide the needed information’s: At the main template report I’ve inserted the background image, unfortunately you cannot use a dynamic image, so, the user needs to add the image regarding to the chosen parameter. I’ve also added an information icon to refer to the provided webpage and a table, to show the classification. The table shows the tooltip report. Next, I’ve saved the report as PBIT template to create new reports based on the report and, by creating new report, the users are enforced to provide the needed parameter values. The result is like that: The solution can be used for import, direct query and hybring models. By using Live connections you need to create a solution inside the cube because, you cannot combine Power Query and the cube. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1160)*
