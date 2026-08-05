---
title: "Storage modes in Power BI"
source: "https://medium.com/@2020ec0712/storage-modes-in-power-bi-d32a57213041"
author:
  - "[[LearnBI]]"
published: 2026-04-15
created: 2026-07-27
description: "More"
Processed: "Unprocessed"
---
(Article for beginners)

![](99.System/Attachments/1!7wsgP90Uwi3sre39bsRPyQ.png.webp)

In Power BI, when you start building [semantic models](https://medium.com/@2020ec0712/reports-semantic-models-and-power-bi-service-ce8639e5cf69) or reports, the first step is to ‘Get data’. While there are many different data sources from which you can get the data (example Excel spreadsheets or CSV files, SQL server, Azure SQL databases, Dataverse, Fabric OneLake etc.), there are three ways in which you can fetch and store them in your.pbix file— direct query mode, import mode and composite.

Direct query mode:

![](99.System/Attachments/1!d-j-chUWQQViTTLL6duoSg.png.webp)

Direct query mode involves querying the data source directly each time. Data is **not stored locally** in the model. As a result, depending on the source and the size of data, the querying could take time. When the number of rows of data to be loaded is very large, direct query mode is recommended because we **don’t need to worry about the memory size** requirements — theoretically, the amount of data that can be loaded through direct query is unlimited. The best part about direct query is that, since the data is fetched directly from the source, regular **manual refreshes are not required**. As and when data changes in the source, the data model in the Power BI file also reflects the changes. So, when the data is changing rapidly and **real-time data** is required in dashboards, direct query is the go-to choice. The downside of direct query storage mode is that its **features are sometimes limited**, as compared to import mode. This is because, what we write as DAX or transform using power query, needs to be translated to SQL to query the source and some complex logic cannot be translated. Another thing to keep in mind is that a **constant connection** with the source is necessary for the data to be available in the Power BI file.

![](99.System/Attachments/1!gbrhLNbb2a4t-KDZ26z5Dw.png.webp)

Import mode:

In Import mode, instead of querying the source each time, we query it once and **store the results (the data)** in the.pbix file. Think of it like cache. Just like how cache helps fetch results faster, storing the data within the model makes **querying faster**. It utilizes something called the VertiPaq engine which compresses the data for **higher performance**. And just like how cache is fast but is a small memory and can’t store large volumes of data, import mode is very **memory-intensive** and hence is not recommended when there are too many rows to be loaded. Also, data is loaded once into the model and the connection with the source is not persistent. So, every time there is a change in the data at the source or every time newer rows of data is required in the model, we **have to manually refresh** the model for it to reflect the latest changes in data. The advantages of import mode are that it offers **full support for all features** like Power Query transformations, DAX logics, aggregations and has great flexibility making it suitable for complex BI models. Since all features that are supported by import mode are not supported by direct query mode while all features supported by direct query mode are supported by import mode, **you can switch from direct query mode to import mode** without any problem. But, switching from import mode to direct query mode is not always allowed due to restriction in some features.

Composite model:

In a star schema data model, there are one or two fact tables and they have massive number of rows. There are also quite a few dimension tables, but they have less number of rows. How about storing the fact tables in a direct query mode and the smaller dimension tables in import mode? This is what composite model lets you do — **store some tables in import mode and some in direct query mode**, harnessing the benefits of both the modes seamlessly. The tables stored in import mode will be queried faster while those stored in direct query mode will take more time. But overall, the **performance and memory consumption will be highly optimized**. Generally, fact tables require frequent refreshes while dimension tables do not change as much and do not require frequent refreshes. Hence, dimension tables in import mode need to be refreshed once in a while and fact tables in direct query mode get updated automatically. As expected, the support for features like Power Query transformations and DAX logic is also **mixed** — with the respective tables in each mode offering its own benefits and disadvantages. Composite models are therefore a **preferred choice for many business models**.

The three storage modes — Direct query mode, Import mode and Composite model are used in building the data models in both [semantic model](https://medium.com/@2020ec0712/reports-semantic-models-and-power-bi-service-ce8639e5cf69) files as well as report files that have data in them. Although **live connection is not a storage mode**, it is generally associated with them. Thin reports or live connected reports have only visuals in them. Their data is stored in semantic model files published to Power BI service.

![](99.System/Attachments/0!9qpC8uW4SWl0NYSs.webp)

A simple way to summarize is:  
**Import mode** — Data and Model belong to the Power BI file.

**Direct Query mode** — Data belongs to the source (the data source) and the model belongs to the Power BI file.

**Live Connection** — Data and the model belong to the source (the semantic model to which the report is connected).

You can tell if a table in a model is in import mode or direct query mode by going to the properties pane of that table in model view or by seeing the small icon on top of the table in the model relationship diagram in model view. In live connected reports, below the report canvas and the list of pages in the report in the report view, the semantic model to which the particular report is connected is specified along with the workspace in which the semantic model resides.