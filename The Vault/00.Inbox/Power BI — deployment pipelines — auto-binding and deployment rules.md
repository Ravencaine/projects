---
title: "Power BI — deployment pipelines — auto-binding and deployment rules"
source: "https://medium.com/@michalmolka/power-bi-deployment-pipelines-auto-binding-and-deployment-rules-4822a7938e5"
author:
  - "[[Michal Molka]]"
published: 2023-03-03
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

In that short post I descripted Power BI deployment pipelines. [Power BI — deployment pipelines](https://michalmolka.medium.com/power-bi-deplyment-pipelines-86d20c10e346)

Today I show you how to manage a dataset connection using **parameters** and **Deployment Rules**.

There are 6 workspaces: 3 for reports and 3 for datasets and they are split into 3 stages: DEV, INT, PRD.

Assuming you want to keep a different connection data for every stage you can hardcode the connection data.

Here is a dataset example, hardcoded connection data:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*p1RBTeoLVUjHJEzill9G1A.png)

What happens when we create a dataset copy, change connection and deploy to respective workspaces. Nothing serious if you don’t plan to automate your deployments. And a necessity to change it on every control version branch isn’t a problem. In larger environments this approach is a dealbreaker.

Back to the pipelines topic. When you create a deployment pipeline for datasets containing hardcoded connection data you won’t be able to keep the different connection values for different stages. When you deploy a datasets between stages, the connection data will be propagated. At the end you will end with the same connection to the same source on every stage.

At the screen bellow the datasets are perfectly identical.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*QYGxdRx8W2U-9dqgkuWDtQ.png)

Only one distinction is a connection value: …Iowa\_DEV, …Iowa\_INT, …Iowa\_PRD.

```c
let
    Source = 
        AzureStorage.DataLake("https://<ADLS ADDRESS>.dfs.core.windows.net/core-files/Iowa_DEV"),
    #"https://eightfiveadls dfs core windows net/core-files/Iowa_DEV/_IowaLiquorSalesdf2022 parquet" = 
        Source{[#"Folder Path"="https://eightfiveadls.dfs.core.windows.net/core-files/Iowa_DEV/",Name="IowaLiquorSalesdf2022.parquet"]}[Content],
    #"Imported Parquet" = Parquet.Document(#"https://eightfiveadls dfs core windows net/core-files/Iowa_DEV/_IowaLiquorSalesdf2022 parquet"),
    #"Filtered Rows" = Table.SelectRows(#"Imported Parquet", each ([County] = "BENTON" or [County] = "BUCHANAN" or [County] = "CALHOUN" or [County] = "CARROLL" or [County] = "CEDAR" or [County] = "CERRO GORD" or [County] = "CHICKASAW" or [County] = "CLARKE" or [County] = "DICKINSON" or [County] = "FLOYD" or [County] = "FRANKLIN" or [County] = "GRUNDY"))
in
    #"Filtered Rows"
```

A simple solution is a parameter.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*jAr2eaVnWSMqh84sDI8UIQ.png)

Once the parameter is created, the code adjusted…

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IuPNVJK-rU-x_IkzMBDUww.png)

…and new dataset versions are uploaded to the service you are able to create a deployment rule for the INT and the PRD stage.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8A2qYFewRcghfYw24Q1TGA.gif)

As a side topic: if you use one of supported data sources, Azure SQL Server for example you can set a data source rule and change an entire connection between stages.

![](https://miro.medium.com/v2/resize:fit:1130/format:webp/1*m-QCFgo34iMyVqz4ph-u_w.png)

Back to the datasets. As you see, we have three separate environments, three different connections and the deployment pipeline doesn’t see any difference.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FAbRqfYzT9KagQPuA86MeA.png)

ALM toolkit says that there is no difference as well. Only a parameter value:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HbLKG4skqQkxOYr7OO87PA.png)

When we have reports connected to these datasets (Live connection), a separate report connected to a separate stage. The situation is simpler. Deployment pipeline doesn’t see any difference.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zbuYnB13WLZzPcuMjshxpA.png)

Even if each report is connected to a dataset placed in a separate workspace, hence there is a difference inside each.pbix file.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*STBjLsukgF4RlItH4oAlFQ.png)

Why? Because of an auto-binding. Power BI knows that you have different data sources connected to the reports on each stage and syncs these information across pipelines.

Here is a structure of the entities used in this post.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*AlXwywoKwAc5P-AIH9kOXg.png)

As you see above the connections are synched between the pipelines, the reports and the datasets.