---
title: "Build automatic process on Power Automate to reduce efforts of routine tasks"
source: "https://medium.com/@wedodo/build-automatic-process-on-power-automate-to-reduce-efforts-of-routine-tasks-e31a0306cf3c"
author:
  - "[[Enthusiastic about enabling commercial excellence]]"
published: 2024-09-13
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Many of us have the same experience delivering reports and email documents regularly. We spend a lot of effort pulling out data, consolidating files, setting a format, and sending to distributor lists. All of these are valuable but time-consuming. Power Automate enables us to automate some processes to save energy for more critical and creative tasks.

> **I will cover process automation, including pulling data from SQL, inserting data into an Excel file, initiating a VB script to build a pivot table based on the Excel we built, automatic backup, and sending the Excel file through Outlook to stakeholders.**

The most crucial concept for power automate is the same as coding: building variables and leveraging the object-oriented concept to use objects moving through different processes. Example below

Before we start, let’s look at the action area in Power Automate. You can find different components you may be interested in, such as an Excel function, flow control, Python script, VB script, and HTML-related components. You can select what you need and build your process.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*oqXNnPsci81rMeKHvSV1dA.jpeg)

Functional componets in Power Automate

First, find a region component from the side area and build our variables. These are the same tasks we do while initiating code: define variables. Here, I make just a few, such as the route and time, so we can use them in any other places within this process, and you don't need to hardcode them every single time.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TM4iBYGx2P0-88YdERPcNA.jpeg)

Set variables in Power Automate

After the variables, we build an SQL connection and write our query directly in the component. You can test your query in the SQL server management tool and make sure you have done the version control at the SQL level.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pNcF0K4UeMLZHYtFU2PR_A.jpeg)

SQL connection in Power Automate

We export our query results to an Excel file and build column headers in the Excel document. Here, the blue sectors are all the instances (objects) that carry the key (or flag, data set, files) and move from step to step. Some steps carry variables we built initially, which is why variables are essential. We also insert a row into the Excel file to build the header.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1Jlcrr5QJnxSiVpcgT0pbg.jpeg)

Excel componet in Power Automate

After we exported the query to Excel, we initiated a VB script to create a pivot table automatically. This step helps us reduce the effort we put into building pivot tables for stakeholders every single time. Amazing.

![](https://miro.medium.com/v2/resize:fit:1336/format:webp/1*KYBGf3EtuM6Tx2ZjJ8q_CA.jpeg)

VB script in power automate

The next step is to rename the Excel file (two tabs in the sheet, raw data, and pivot table). We use build in function to automatically add date time to the file as our reference and backup purpose.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_lcxtzwpajjR9eppwiguZA.jpeg)

Automatlly update excel file name with date time capture

We built date time variables at the very beginning for the use here.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*CI9STPzriiLi6i-oIusyjw.jpeg)

Variable usage in power Automate

Okay, we have completed the query, Excel file, pivot table, backup preparation, and naming rules. The final step is to call out the components of Outlook and send the files we built through Outlook to stakeholders. Launch Outlook and complete the component setting (subject, content, cc, bcc, attached, and see if you need to save a draft)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*d_u8oRdy5aULSK9WEB_92A.jpeg)

Outlook componet in Power Automate

Awesome. We have just completed an automatic process to cover the query, Excel, pivot, and report sending. We can customize the report by adding some logic flows so we can fulfill the needs of different levels of stakeholders (VP, district managers, sales reps, etc. ). Stay tuned for more Power Automate to come.