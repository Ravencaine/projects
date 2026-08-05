---
title: "How to Use Stored Procedure in Power BI"
source: "https://medium.com/@ayigit/how-to-use-stored-procedure-in-power-bi-c3ecfe5e5429"
author:
  - "[[Ayşegül Yiğit]]"
published: 2022-09-07
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
Hello everyone, we will talk about how the data we call based on the “Stored Procedure” that we create in SQL Server is used with parameters to query the PBI.

Firstly, we need to create basic Stored Procedure in SQL Server:

![](99.System/Attachments/1!dZg8xqSVbWxlE0SnpaMnTA.png.webp)

Stored Procedure Get Customer Data Based on Order Date According to Entered Customer ID

![](99.System/Attachments/1!rGlFtjArn-Me506oLH_VaA.png.webp)

Querying with Stored Procedure

**Create a Parameter**

We need to define created parameters to run Stored Procedure in PBI.

Our first step will be switched to the Power Query Editor tab in this process.

![](99.System/Attachments/1!19JJfU2iBlAB7aRtSWy8Ag.png.webp)

Manage Parameters

At this stage, we will define “ID” parameter that we created in the Stored Procedure.

![](99.System/Attachments/1!cjVGKuSG1K2iK8OE3GzjnQ.png.webp)

> We need to identify in 3 fields:
> 
> 1)Type of the parameter  
> 2)Which suggested values  
> 3)Current Value

**Stored Procedure**

Now, import data from SQL Server by querying Stored Procedure:

![](99.System/Attachments/1!qK8ZJdqvCpLPlrKNX3R_7Q.png.webp)

Power Query will load a preview with M Language containing Stored Procedure.

![](99.System/Attachments/1!YsWnWjSCK223gTckqOykFg.png.webp)

M Language

**Advanced Editor**

We will view query on the Advanced Editor and edit query according to created parameter.(Customer ID)

![](99.System/Attachments/1!QplNLbn0YORcy8JoJfeGxQ.png.webp)

Click Edit Permission to allow Power Query to execute Stored Procedure.

![](99.System/Attachments/1!z5kRBLnzcsAa3rRVlG_oBA.png.webp)

Data loaded in Power Query

![](99.System/Attachments/1!l6-20Tg6qd6jq-q6btdO-A.png.webp)

**Report Output**

The output of the report with the customer ID 25 that we defined with the procedure is in the table below.

![](99.System/Attachments/1!Iogmm574vNaRjjFJQre83Q.png.webp)