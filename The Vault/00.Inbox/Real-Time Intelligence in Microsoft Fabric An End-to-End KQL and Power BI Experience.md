---
title: "Real-Time Intelligence in Microsoft Fabric: An End-to-End KQL and Power BI Experience"
source: "https://medium.com/microsoft-power-bi/real-time-intelligence-in-microsoft-fabric-an-end-to-end-kql-and-power-bi-experience-570deaa31d6f"
author:
  - "[[Ayşegül Yiğit]]"
published: 2026-04-27
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
In modern data architectures, speed and integration are no longer a luxury, but a necessity. When we want to analyze and visualize millions of rows of telemetry data, logs, or instantaneous sales transactions within seconds, traditional relational databases can sometimes run out of breath. This is exactly where Microsoft Fabric’s Real-Time Intelligence (RTI) and the powerful Kusto Query Language (KQL) engine behind it come into play.

In this article, we will examine how to build an end-to-end Real-Time Intelligence scenario on Microsoft Fabric from start to finish. We will begin by creating a workspace, query our data using KQL, and transform the results into a Power BI report within seconds.

**Workspace Creation and Data Download**

***Workspace Creation:***

1. Select **Workspaces** from the left menu bar (icon appears similar to 🗇).
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*wGQnuKknzXLbQow7Pl9Qzw.png)

Create a new workspace with your desired name by choosing a licensing mode that includes Fabric capacity.

***Downloading the Data File:***

1. Download the data file you will process from [this address](https://raw.githubusercontent.com/MicrosoftLearning/dp-data/main/sales.csv) and save it to your local computer as `sales.csv`.

**KQL Database Creation and Data Ingestion**

***KQL Database Creation:***

1. Switch to the **Real-Time Intelligence** experience in the bottom left corner of the portal.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ugNpiYm9UZX8zX79ydIk1g.png)

On the Real-Time Intelligence home page, create a new KQL database with an **Eventhouse** of your choice.

**Data Ingestion:**

1. Select your newly created database from the list on the left.

Choose the option to ingest data from a **Local File** and follow the steps below to transfer the data into a new table:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*kon166NlAb4woiZsNykdwA.png)

- Click the **“+”** sign to create a new table named `sales`.

Upload the `sales.csv` file by dragging and dropping it or by using the "Browse for files" link.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cUtlJVVf5mqaEAPE6u4pRg.png)

Complete the process by checking the slider indicating that the first row is the column header and then clicking the **Finish** button.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*AQos1CDFqowuO4sOrtZlvQ.png)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

**Query Usage for Data from the Sales Table**

Querying Data from the Sales Table with KQL:

1. Select the `sales` table and choose the **"Show any 100 records"** option from the **Query table** dropdown menu.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*vyYbpmRJw779-wER_7BBOA.png)

2\. Run the query in the window that opens.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TqpyX4sDOU-7YjawnJQjyA.png)

**Note:** In KQL, the `|` (pipe) character is used to filter and transform data step-by-step.

Developing and Running the Query:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XYuRaMghVJU44UlDtvYoLQ.png)

To develop this query and focus on years after a specific date, let’s add another chain to our query.

### Summarizing and Sorting Total Revenue:

If we want to apply an analytical mindset and generate a revenue summary (Aggregation) by product, our query becomes as follows: With this query, we filtered sales within the year 2020, summed the net revenue by item, and sorted the results alphabetically.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mU1ceB_bwRwzkeEIYeekAQ.png)

**Saving KQL Queryset**

To avoid losing the query you wrote, click the **“Save as KQL queryset”** button in the top menu and save it with a name such as `Sales_KQL`. This allows you to transform your query into a reusable format.

Creating Power BI Reports with KQL Queryset

But how will we visualize this data? There is no need to export data or open Power BI Desktop.

**Power BI Report Creation:**

1. Select the **Power BI report** option and wait for the report editor to open.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xuMVMyM0UZmVd0SGUGvibw.png)

2\. In the report editor, you can design the report with the visuals of your choice.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UGjpAyL60k3Fu1rcrmmr8w.png)

Microsoft Fabric seamlessly combines data engineering, real-time data analytics, and business intelligence tools on a single platform. The entire process — from uploading a CSV file to the system to writing analytical queries with KQL and creating a dashboard in Power BI is completed in minutes. You can add a whole new level of speed and flexibility to your data analysis processes by using Real-Time Intelligence in your own projects.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Model

**Tags:** Tutorial, Data Model