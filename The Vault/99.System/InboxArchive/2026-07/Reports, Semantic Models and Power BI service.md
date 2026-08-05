---
title: "Reports, Semantic Models and Power BI service"
source: "https://medium.com/@2020ec0712/reports-semantic-models-and-power-bi-service-ce8639e5cf69"
author:
  - "[[LearnBI]]"
published: 2026-04-06
created: 2026-07-27
description: "More"
Processed: "Unprocessed"
---
(Article for beginners)  
When I first started to learn Power BI, I did not know that something called Power BI service even existed. All I knew was Power BI desktop and how you could get data from some Excel spreadsheets into it, choose a visual of your choice, pull some required columns into the field wells and instantly see interesting charts in the report view. A little later, I came across ‘Semantic Models’ and I had no clue what they were. Because all this while I had only made reports using my Power BI desktop application. All the data and the visuals were in it. Then I googled to understand what semantic models are.

![](99.System/Attachments/1!qZKhQtoL_NJDrzJTvbmCOg.png.webp)

When I made reports using Power BI desktop, I could make them in the way that I wanted. But if I or someone in my team wanted to make a different report, isolated from this one, on the same dataset, we will have to either load the data from scratch and then create the visuals of our choice, or, duplicate this Power BI report file, add visuals of our choice in a new page and delete the older report pages. When it is a simple dataset, like 1 or 2 Excel spreadsheets, it is easier to rebuild the same data model in Power BI multiple times — load the tables, build relationships between them and do the transformations. But when it is a complex data model, with multiple tables from different sources having very specific transformations for each of them, it becomes tedious to do these steps over and over again, just to build a report. This is why we need semantic models.

![](99.System/Attachments/1!E2waIHmus8ucSAE6V-J6Ng.png.webp)

**Semantic model** is basically a Power BI file that has just the data model and no visualizations. The data model or the semantic model comprises of the data source connections, the data, the relationships and the transformations on the data. Once you build a semantic model, you have a **single source of truth** — meaning an ideal and comprehensive dataset with all the required components, ready to be used for as many reports as you want. Hence, we say that semantic models enable self service BI — just share the semantic model with your end users, they can build reports as they like with this model. Since all the users use the same dataset, they will all see consistent values. In the future, if any change like the addition of a new table or a specific transformation on a particular column is to be done, it is enough if we just make the change to the semantic model. All the reports connected to this semantic model, will reflect the changes.

![](99.System/Attachments/1!yyWDSOa2MM3oK4oG6d5nTQ.jpeg.webp)

How should one share the semantic model file with the users? If it were a Microsoft Word Document or a Microsoft PowerPoint file, we could just upload it in Microsoft SharePoint (a cloud based tool for storing and sharing files). What makes a semantic model file unique is the need for refresh. The source from which Power BI gets its data could get updated periodically and we would want the same changes in our model too. If the semantic model file is uploaded in a regular cloud based sharing application, we would need to manually refresh the model each time to sync it with its source. What if we could set an automatic trigger to refresh the semantic model so that it syncs with its data sources periodically? Enter Power BI service.

![](99.System/Attachments/1!PFowdL1kLLVq3VJbbtF9AA.jpeg.webp)

**Power BI service** is a cloud based application for file sharing and collaboration — specifically for Power BI artifacts (semantic models, reports). Along with the feature to schedule refreshes on the semantic model, it allows us to grant specific access privileges and permissions to users on these artifacts using different roles. Hence, it is also useful for **security** purposes. Additionally, Power BI service makes it possible to build reports in cloud itself. So, if you have a semantic model ready in service, you do not need necessarily need Power BI desktop — just create a report on the semantic model shared with you. You can also create such a report using Power BI desktop by choosing the semantic model as the data source in Get Data.

![](99.System/Attachments/1!ZowdYtPxhGBJL7jIKrxjxw.png.webp)

As beginners, we tend to use the words **dashboard and report** interchangeably. But dashboards are created only in the Power BI service while reports can be created in both desktop as well as service. A report consists of multiple pages of visuals, offering detailed insights while a dashboard is a single page of pinned tiles of visuals, offering a quick glance at some important KPIs.

![](99.System/Attachments/1!NHLHhvdKxQMubcw5JYRIhg.png.webp)

Power BI service is divided into ‘ **workspaces** ’. With the right access privileges, you can create a report with the semantic model shared with you in the workspace and save the report right there. Other users with access to it can view or edit it. You can also choose to save the report in your personal workspace, instead of a shared workspace. When you build or edit a Power BI file in your local system using Power BI desktop, it is available only to you. Only when you upload it to Power BI service, it becomes accessible to everyone in the workspace. The process of uploading the Power BI file to a workspace in Power BI service is called ‘publishing’. When you publish a full.pbix file to service, service automatically splits the file into two components (the semantic model and the report file) and saves it in the workspace.

![](99.System/Attachments/1!YGWYIcOC_MCBi8lDCm1eDw.png.webp)

Also, you can download the Power BI artifact from service to your local system too. When you download a semantic model file, you are downloading the dataset in a.pbix format. When you download a report file, you can either download the full.pbix file (dataset + report — by clicking on download on the semantic model file) or just the report with the connection to the semantic model (also called thin report or **live connected report**). When the underlying dataset gets refreshed, the thin report also gets refreshed automatically. On the other hand, when a full.pbix file is downloaded, the dataset in it needs to be manually refreshed so that the data (and hence the report) reflect the changes.

Power BI service is a collaboration and consumption tool. While you can build some basic reports and edit them, do some minimal modeling and transformation tasks, it is not as powerful as Power BI desktop. Power BI desktop is very essential for development. As a consumer of the reports, one might not need Power BI desktop. But as a developer, you definitely need Power BI desktop.