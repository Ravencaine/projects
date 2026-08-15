---
title: "How to Schedule Power BI Report Refreshes on Non-Fixed Interval Using Power Automate"
source: "https://medium.com/microsoft-power-bi/how-to-schedule-power-bi-report-refreshes-on-non-fixed-interval-using-power-automate-dcd3674effa3"
author:
  - "[[Avishek Ghosh (AV_DEVS)]]"
published: 2025-01-06
created: 2026-08-12
description: "Learn how to automate your Power BI report refreshes when your schedule requires specific, non-recurring dates"
Processed: "Unprocessed"
---
## Learn how to automate your Power BI report refreshes when your schedule requires specific, non-recurring dates

![](https://miro.medium.com/v2/resize:fit:1380/format:webp/1*DpytMArh-PPJIk-a_JGZUA.png)

H *ave you ever needed to refresh a Power BI report on a monthly basis or on specific dates without a fixed interval? The scheduled refresh option in Power BI Service doesn’t support monthly intervals. However, with Power Automate, you can refresh Power BI reports on any schedule you choose, even outside the options available in Power BI Service. You can also create flows to trigger data refreshes based on complex logic or event-driven triggers.*

This article provides a step-by-step guide to setting up Power Automate flows, giving you superpowers in data refresh for Power BI.

## Problem Statement

Imagine you’re developing a Power BI report to provide strategic insights to your client’s leadership team. This report includes various KPIs and metrics that measure performance across finance, sales, Salesforce effectiveness, and employee data. The data comes from different sources: finance data from a Power BI Dataflow Gen2, sales performance data from a Snowflake data warehouse, Salesforce effectiveness data from Salesforce CRM, and employee data from an on-premises Oracle database.

Your goal is to present the monthly movement of these KPIs in your strategic report. While you could refresh the report weekly, you don’t want incomplete data for a month that hasn’t ended. Therefore, you need to refresh the report once a month, preferably at the end of each month, to capture the full month’s data. However, Power BI Service doesn’t allow for a monthly refresh schedule.

Adding to the complexity, the CFO has instructed you not to refresh the finance data in the month following a quarter’s end until after the quarterly results are published. The CFO will provide a list of dates for the quarterly results’ public release. This means you can’t refresh the entire report on the last day of every month. For months like January, April, July, and October, the refresh dates should vary based on the quarterly performance announcement dates.

### The Challenge

How can you set up a scheduled refresh so that the report refreshes sales performance, Salesforce effectiveness, and employee data at the end of every month, but refreshes finance data at the end of all months except January, April, July, and October? In these months, the finance data should be refreshed the day after the public release of quarterly performance.

## Solution

To address the challenges, we need to break them down into smaller parts and tackle each one individually:

## Three Key Challenges

1. Monthly Scheduled Refresh: Power BI doesn’t support setting up a monthly refresh.
2. Variable Refresh Dates: Refreshes need to be set up based on different dates.
3. Selective Table Refresh: It’s not possible to refresh different tables inside the data model separately; the refresh happens for the entire report at once.

**Challenge 1: Monthly Scheduled Refresh**

This can be resolved by setting up a Power Automate flow that refreshes the semantic model on a monthly interval. Unlike Power BI Service, Power Automate offers “monthly” as an applicable interval for any scheduled activity.

**Challenge 2: Variable Refresh Dates**

This challenge can also be addressed using Power Automate. Instead of setting up a Power BI refresh trigger based on a fixed interval, we can use a simple logic. Given we have a list of dates for the public announcement of company performance, we can add a “Conditional” action in the flow to check if today’s date matches any date in that list. If true, the flow triggers a Power BI refresh; otherwise, it does not.

**Challenge 3: Selective Table Refresh**

For this challenge, we need to understand that finance data requires exclusive treatment. Instead of directly ingesting data from the source dataflow to the report’s semantic model, we can create an intermediate dataflow that ingests data from the source dataflow. Our report’s semantic model will then ingest the finance data from this intermediate dataflow. Consequently, we can set up a Power Automate flow to refresh this intermediate dataflow using the date-driven logic, while another Power Automate flow can refresh the report’s semantic model on a monthly interval.

![](https://miro.medium.com/v2/resize:fit:1372/format:webp/1*m-xSCKitW7gJ_ba1jdOoOg.png)

Following is the Power Automate Flow that creates that uses a specific list of dates in an excel to trigger a data refresh in a Power BI Dataflow and then once the Dataflow refresh is a success, it triggers a data refresh in the report semantic model.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*CXFZeeoLcxaPKNgC7_w0Tg.png)

Let us walk through this solution step-by-step:

**Step 1 — Set the recurrence:**

Create a “Recurrence activity” This is like a scheduler where we get to enter the frequency, time and other details:

![](https://miro.medium.com/v2/resize:fit:1246/format:webp/1*rpSL7q0y-T3z2-khA08Cdw.png)

Always remember, the start time takes in Zulu time. So, convert your preferred time into Zulu time before updating.

We are setting this up as a daily activity coz this flow will check every day if the day is available in the list of valid refresh dates.

**Step 2- Extract the dates from excel**

Create an action “List rows present in a table” and enter the SharePoint location, folder, filename and table name in excel that contains the dates.

Below is the sample of the excel:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*n7UKRRWA9Vtuky4vqqNyIw.png)

Ensure that the dates are in “mm/dd/yyyy” format and in text datatype in excel. Else Power Automate will extract the date value of the date which you don’t want to compare.

Below is the action that extracts the dates:

![](https://miro.medium.com/v2/resize:fit:1180/format:webp/1*90iil_CJmdyh-XZ54leO9Q.png)

**Step 3 — Initialize a variable and insert current date in mm/dd/yyyy format**

In this step we will add an action called “initialize variable”.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*n9K1py7BIkRxHON9M8wMlw.png)

After giving it a proper name, we will set this up a as a string variable and add the below expression in the value:

```c
formatDateTime(convertFromUtc(utcNow(), 'Central Standard Time'), 'MM/dd/yyyy')
```

This expression will convert current date into “mm/dd/yyyy” format for comparison with your extracted dates in the previous step.

**Step 4 — Create a for each loop**

Up next, we will set up for each activity to iterate over all the dates in the list of dates you captured.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TGLGRHixvLqYcq4sLdhZVw.png)

Select the “body/value” element from the output of the 2nd step as your input.

Step 5 — Set-up condition action

Inside the for each iterator, we will set up the condition that will check for each of the dates if they match the current date stored in the string variable, we initialized in step 3.

![](https://miro.medium.com/v2/resize:fit:1256/format:webp/1*9bEDlsP55IrP9vGJoC98_Q.png)

This step will check each date and match if any of them matches with our current date.

**Step 6 — Trigger refresh**

Next, we will set-up the “Refresh a dataflow” action in the “True” branch for this condition action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NdkvtGenVH60Se9Yn7wYGg.png)

Select “Workspace” from Group type dropdown, select workspace name from the dropdown of Group and then select the name of the dataflow from the next dropdown and you’re all set.

Remember: In Power Automate, the action “Refresh a dataflow” is not listed under Power BI activities but under Power Query activity.

**Step 7 — Wait for 4 hours**

Add the action “Delay” to wait for 4 hours

![](https://miro.medium.com/v2/resize:fit:1266/format:webp/1*dPZYCDK7mteaw24kcJOCqQ.png)

**Step 8 — Refresh dataset**

We now need to refresh the report semantic model to ensure that the latest finance data we just loaded into the dataflow are pushed into the semantic model as well. To do that we will now add another action “Refresh a dataset”.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4qP_AwDzcn4m53_egDKEpw.png)

This action also lets you select your workspace and semantic model that you want to refresh.

Please note that in the entire flow we have added two “Compose” actions, once after the initialization of the variable with current date and the other at the end of the flow. These are for debugging purposes only. They will confirm what output we are getting in previous steps. They are not important to the functionality of the flow.

Using the above steps you can improvise and experiment with different combinations of complex logics to trigger Power BI report refresh and eliminate unwanted refreshes and improve your capacity usage.

**Thank you for reading!**

Please feel free to give 50 claps 👏 if you found this article helpful and leave a comment or share it with others.

👉 [Follow](https://medium.com/@avdevs2501) me or ✉️ [subscribe](https://medium.com/@avdevs2501/subscribe) to get all my Power BI articles!

You can find me on [LinkedIn](https://www.linkedin.com/in/avishek-ghosh-aa3348153/).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*78l_CR1gsBUxlB9y.png)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----dcd3674effa3---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee