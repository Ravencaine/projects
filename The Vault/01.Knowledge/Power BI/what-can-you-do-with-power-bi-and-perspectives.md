---
title: "What can you do with Power BI and perspectives?"
source: "https://www.flip-design.de/?p=1014"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

What can you do with Power BI and perspectives? | flip-it.de :: SQL, BI and more Perspectives are very popular when you are using Analysis Services Tabular. With this feature you can create different views to your cube and hide tables, columns and measures and make the cube easier to use for each user group. So, that means for example, that salespeople do not see measures which are used for deep dive analysis of your data. Mostly I see that the organization created different cubes, but mostly with the same underlying data model and the same programming of each measure and so on. This can also manage by using OLS, but for business needs, perspectives are easier to handle. Now, if you want to use perspectives with Power BI, you can create them with the Tabular Editor. For this example, I have created a Power BI file and with the Tabular Editor I created a perspective named “Sales “and hidden the column “country”. After publishing the report tom Power BI, you cannot use the perspective. If you create a new report based at this dataset, there is no question which perspective do want to use: But if you have Premium or Premium per User, you can access to the XMLA endpoint: With this URL you can access to the cube and select the perspective or the whole cube. This URL can also used with Paginated Report Builder or Excel. After selecting the Sales perspective, you see, that the column “Country” is not available. Conclusion : Mostly ‘OLS is by my point of view better if you want to secure your data. But if you only create different views of your data for different use cases, I think you should use this feature. But it depends 😉 Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1014)*
