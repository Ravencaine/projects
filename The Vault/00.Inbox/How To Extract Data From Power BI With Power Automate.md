---
title: "How To Extract Data From Power BI With Power Automate"
source: "https://medium.com/@thomas.j.blessing/how-to-extract-data-from-power-bi-with-power-automate-55fe3d797913"
author:
  - "[[Tom | Power BI Guide]]"
published: 2024-06-10
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*HsHLUj_fZRhltBB1.png)

Power BI is a powerful tool for data visualization and analysis, but there are instances when you need to extract data from your Power BI reports for further processing or integration with other applications. Power Automate, formerly known as Microsoft Flow, provides a seamless way to automate the extraction of data from Power BI reports.

In this guide, I will walk you through the process of using Power Automate to extract data from Power BI, enabling you to streamline your data workflows and make the most of your Power BI reports.

## Prerequisites

Before you get started, make sure you have the following prerequisites in place:

- **Power BI Report**: You should have a Power BI report that contains the data you want to extract. If you need help creating one, [this Intro to Power BI DataCamp course](https://www.datacamp.com/courses/introduction-to-power-bi?irclickid=V0Vw5YTZAxyPTEMQXVWukXN9UkHXdDSxRWrQxY0&irgwc=1&utm_medium=affiliate&utm_source=impact&utm_campaign=000000_1-5190561_2-mix_3-all_4-na_5-na_6-na_7-mp_8-affl-ip_9-na_10-bau_11-Quickly+Learn+Power+BI&utm_content=ONLINE_TRACKING_LINK&utm_term=) is a great starting point. I earn a small commission if you click and purchase.
- **Power Automate Account**: Access to Power Automate is required. You can use a Power Automate account or access it within a Microsoft 365 environment.

## Extracting Data from Power BI with Power Automate

Follow these steps to extract data from Power BI using Power Automate:

### Step 1: Create a New Flow

Go to the Power Automate portal or open the Power Automate app within Microsoft 365. Click on “Create” to start creating a new flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*n_pgEgAV3_awu2xN.jpg)

### Step 2: Choose a Trigger

Search for and select the trigger that will initiate the flow. In this case, you can use the “Power BI” trigger called “When a data-driven alert is triggered.” Sign in and connect your Power BI account. Configure the trigger settings. Select the dataset for which you want to extract data.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*jHCK1zUlhjjADUyW.jpg)

> ***Alert ID****: When setting up the trigger, you will need to enter the Alert ID. This ID corresponds to the specific data alert you’ve set up in Power BI. To find the Alert ID, navigate to the alert you created in Power BI, and copy the ID from the alert settings. This ID ensures that the flow is triggered by the correct data alert.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Hwv3kfHe_z-MjEDn.jpg)

### Step 3: Add an Action to Export Data

After setting up the trigger, click on “New Step” to add an action that exports data. Use the “Export to File for Power BI Reports” action to export your report to a desired format (such as PDF or Excel) and save it to a specified location or send it via email.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*PXgP9QOfGYl_DYPF.jpg)

### Step 4: Configure the Export Action

In the action, configure the settings to specify what data you want to export and how you want to format it. For example, if you’re creating a file, specify the file format (e.g., PDF, Excel) and the destination folder. If you’re sending an email, define the recipient(s), subject, and email body.

### Step 5: Save and Test

Save your flow. Test the flow by manually triggering it to ensure it correctly exports data from your Power BI report.

### Step 6: Automate and Schedule

To automate data extraction, consider setting up a schedule or using other triggers that suit your needs. Power Automate allows you to schedule flows to run at specific times or based on events.

By following these steps, you can automate the extraction of data from Power BI using Power Automate. This streamlined process enables you to easily integrate your Power BI data into other workflows, applications, or storage locations, enhancing your data utilization and efficiency.