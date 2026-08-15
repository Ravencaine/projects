---
title: "Power BI — backup and restore datasets"
source: "https://medium.com/@michalmolka/power-bi-backup-and-restore-datasets-f1ab490bcff4"
author:
  - "[[Michal Molka]]"
published: 2022-03-04
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Today I show you, how you can create backups of your datasets. In order to do this, you need an ADLS2 (Azure Data Lake Storage) connected to the Power BI Service on a workspace or a tenant level.

So that, the first point is to create a Data Lake Storage.

Create a **Storage Account** with a **Hierarchical Namespace**.

![](https://miro.medium.com/v2/resize:fit:1166/format:webp/1*MGZVMXMuB1wJXZnDCbwSzw.png)

In the Power BI service, you can assign the ADLS2 to a workspace or to a tenant. In this case we assign the storage account to a workspace.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*1UXMcm9ZotcMB__pncKi0A.png)

After your storage is successfully connected to the workspace. You notice that inside the Data Lake are two new containers: **power-bi-backup** and **power bi**.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-afGel4ahGk8bNCtcMqICQ.png)

Azure connection information in the workspace settings section should look like bellow:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*hOdZF9L04AIeBBZlmzFQ-A.png)

Now, we can connect to our workspace by XMLA endpoint.

I’ve created one dataset:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7YLwxFVpbMVtvUeCYoUwlg.png)

And without any surprises, the same dataset is visible in SQL Server Management Studio. Select a **Back Up…** option.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*kdz0rvR6u8nTUwYhzmLY9Q.png)

You can adjust some options like a compression, an encryption, etc.:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*i2VYuG3A64dJvnQb0Zjulw.png)

You can check if a backup has been created. Head over to the storage account and inside the power-bi-backup folder you find an **.abf** file.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qCAD5woLe--k03hyoW2-WQ.png)

If you want to restore a dataset. You need to choose a backup file, a name for a new dataset or decide if an existing file should be overwritten.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EMRvBt5WPPBllt9qRWVSbw.png)

As you can see, the dataset has been restored.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*HwoHMnc2FmDUSx4y2ABkQw.png)

And it is visible in the Power BI Service.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pAiuUKZZWLwmbed1y8-oeA.png)