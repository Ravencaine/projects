---
title: "Query Power BI datasets to send an individual alert"
source: "https://www.flip-design.de/?p=1298"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Query Power BI datasets to send an individual alert | flip-it.de :: SQL, BI and more When you configure a data alter inside a Power BI dashboard, you cannot configure another email address or modify the text inside the email. Another problem is when you want to inform another user. So, here you can use Power Automate and the cool task !run a query against a dataset. With this task, you can run a query and get the responding data as a JSON. The only requirement is that you already have a Dashboard and an alert for your own. The alert is needed for a trigger inside Power Automate. A small hint, for easy creating the DAX query, you can use the Query Analyzer inside the Power BI desktop and you should use an explicit measure. Last one, makes it easier to modify the code. This small flow is triggered by an alert, gets the data, and sends an email for every alert You must parse the JSON response – to get the right schema, run one time the flow and get the response of the dataset query. This one, can use to generate it by a sample. Now, you can loop trough the response and generate email, for example you can also use an email group to inform more than one user. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1298)*
