---
title: "What is an on-premises data gateway in Power BI?"
source: "https://medium.com/@ayigit/what-is-an-on-premises-data-gateway-in-power-bi-4030ce6eccc1"
author:
  - "[[Ayşegül Yiğit]]"
published: 2022-09-21
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
Hello everyone, we will talk about what is an on-primes data gateway and how to work one in Power BI. When you create Power BI reports based on on-premises data and publish them online, you will need a way to access your on-premises data sources to refresh your datasets.  
Otherwise Gateway!

Most of the time, to share reports that you create in Power BI Desktop, you need to publish them to the Power BI service in the cloud. When this happens, the refresh mechanics of your dataset change are that the cloud, not your machine, should be accessing your data sources.

Gateway connects the cloud to your on-primes data sources. you can not only access your on-premises data sources, but also set up a refresh scheduler for datasets published in the Power BI service with them.

![](99.System/Attachments/1!FoUwuNhR76bStXxmaAUD8Q.png.webp)

**Power BI Gateway can be installed in two modes:**

**1)** **On-primes data gateway:**

· It will become available to multiple users with access to the server.

· It can be used for both refresh scheduler and live queries in Power BI.

· You can also it for PowerApps, Logic Apps, and Microsoft Flow.

· This gateway is well suited for complex scenarios where multiple user access multiple data sources.

**2)** **On-primes data gateway(personal mode):**

· This gateway has limited access. Just, you can able to use and you can set it up for refresh timer in Power BI.

· This mode can able to authorize just one user connect to source and it can not publish with another users.

· This mode only available in Power BI.

· This gateway is well suited for scenarios where you are the only one creating the reports and you do not need to share any data sources with others.

· Live connection mode, PowerApps, Logic Apps, Microsoft Flow are not supported.

**Note:**

1\. It can set up at most one gateway per mode on the same computer.

2\. For a scheduled refresh to occur successfully, the Power BI gateway must be turned on and the local machine it needs must be turned on and connected to the internet. If your computer is asleep during the refresh, the refresh will fail.

**On-Premises Data Gateway Architecture**

![](99.System/Attachments/1!y1AjBr_0EaJ5tdvdRTd7Fg.png.webp)

**What happens when we interact with an item connected to the on-premises data source?**

1) The cloud service generates a query and encrypted credentials for the on-premises data source. The query and credentials are sent to the gateway queue for processing.

2)The gateway cloud service analyzes the query and forwards the request to Azure Service Bus.

3)Azure Service Bus sends pending requests to the gateway.

4)The gateway receives the query, decrypts the credentials and connects to one or more data sources with these credentials.

5)The gateway sends the query to the data source to be executed.

6) Results data from the source to the gateway and then to the cloud service. The service then uses the results.

**Note:** In step 6, queries such as Power BI refreshes and Azure Analysis Services refreshes can return large amounts of data. Data for such queries is temporarily stored on the gateway machine. This data storage continues until all data is retrieved from the data source. The data is then sent back to the cloud service. This process is called spooling.