---
title: "Dynamic subscriptions with email in Power BI / paginated reports – Part 2"
source: "https://www.flip-design.de/?p=1379"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Dynamic subscriptions with email in Power BI / paginated reports – Part 2 | flip-it.de :: SQL, BI and more As with Power BI, the paginated reports use the same procedure and the same requirements. The technology is currently still in preview mode and can only be used with a premium capacity. In this entry I show how to use this. The semantic model from the previous entry is currently still in my workspace: The semantic model also contains the addresses to which emails should be sent as a subscription. But first I created the report with an appropriate parameter to filter the data. This is similar to line-based security, but is not used here because the service is not the user calling the report, but the service. The report is created using the Power BI Report Builder. To do this, connect to the Power BI service: Now you can build the semantic model. It should be noted that this functionality is also available without adding premium capacity. However, this capacity is necessary when it comes to sending emails: A query must then be created on the semantic model to obtain the corresponding data: What is important is that the corresponding parameter is defined according to which the data should be filtered. To do this, I filter the data by country similar to the previous entry. This parameter can then be reused in the other datasets. After confirming, you will find the data in the report, including the parameters, and you can create the report. When you run the report, you will be asked to fill the parameter and then the data will be filtered accordingly: The report can now be uploaded to the Power BI service. The report can then be called up in the Power BI service and the corresponding parameters can be passed to it. A corresponding subscription can now be created for this. Premium capacity is then required for this functionality. The procedure here is the same as when subscribing to Power BI reports. With this functionality, however, it is possible to use additional export formats instead of just using a PDF or PowerPoint After the subscription is executed, the report will be sent to recipients in the selected export format: Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1379)*
