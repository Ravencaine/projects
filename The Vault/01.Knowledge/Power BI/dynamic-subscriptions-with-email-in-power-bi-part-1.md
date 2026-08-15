---
title: "Dynamic subscriptions with email in Power BI – Part 1"
source: "https://www.flip-design.de/?p=1367"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Dynamic subscriptions with email in Power BI – Part 1 | flip-it.de :: SQL, BI and more The function is currently still in preview mode. An available function is to subscribe to reports and receive the report unfiltered as an email. Of course, this is difficult if you don’t want all the data to be displayed to a user. So he would be able to see everything. With this new function, filters, similar to those in RLS, can be applied to pre-filter the data. The function is similar to what we know from Reporting Services as data-driven subscriptions. To create a subscription, premium is required as a capacity on the workspace. Here the premium per user is not enough. To create a subscription to a report, click subscribe as usual. Now you can choose from the report, but semantic models are also offered here that make little sense in this context. If you now select the corresponding reports, you now have the option to create the subscription: Now select the table that provides the email address and filters: What is important here is that the user is in the tenant and the user also has access to it. In the next form, the email is configured, where the dynamic data from the query or fixed values can be used. What is irritating here is that you also have the option to select a report page. However, the report that is sent contains all pages. On the next page, the filtering is configured. The same filters as used in the RLS must then be applied here. The existing role cannot be reused. In the last window only the schedule is configured. Please note that emails can only be sent every 15 minutes. In addition, you should simply have a little patience, as the emails take 1 to 2 minutes to reach the recipient. Then, as soon as the schedule has been reached or you trigger the manual sending of the email in the subscription, the email will be in your inbox. Manual sending is preferred after one has been developed. This makes it easier to detect errors.Wie bereits erwähnt, befindet sich im Anhang der E-Mail der Bericht mit allen Seiten, sofern man den Anhang mit sendet: The preview of the report in the email is also the first page from the report, but filtered. However, the attachment is filtered the way it was configured: Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1367)*
