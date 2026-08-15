---
title: "Integrating Power BI with Power Apps and Power Automate Using SharePoint List"
source: "https://medium.com/fabric-bi/integrating-power-bi-with-power-apps-and-power-automate-using-sharepoint-list-e0e29612d29b"
author:
  - "[[Hussam Dabbas]]"
published: 2024-09-15
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
**Introduction**

Integrating Power BI with Power Apps and Power Automate using a SharePoint list as the data source can significantly enhance your data analysis and workflow automation capabilities. This guide will walk you through the process step-by-step, ensuring you can create a seamless integration between these powerful tools.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MCbQLClhkQVKCyphUbu9OA@2x.jpeg)

**Prerequisites**

Before you begin, ensure you have the following:

Power BI Desktop

Power Apps

Power Automate

A Microsoft 365 account with the necessary licenses

A SharePoint Online site

**Step 1: Setting Up Your SharePoint List**

Create a SharePoint List: Navigate to your SharePoint Online site, click on “New” and select “List”. Name your list (e.g., “SalesData”) and add the necessary columns (e.g., “Salesperson”, “Region”, “SalesAmount”, “Date”).

Populate the List: Add some sample data to your SharePoint list to use in your Power BI report.

**Step 2: Loading SharePoint Data into Power BI**

Open Power BI Desktop: Launch Power BI Desktop and click on “Get Data”.

Select SharePoint Online List: Choose “SharePoint Online List” from the data source options and enter the URL of your SharePoint site.

Load Data: Select your SharePoint list (e.g., “SalesData”) and load it into Power BI.

**Step 3: Creating a Power BI Report**

Create Visuals: Design your Power BI report by adding various visuals such as tables, charts, and graphs to display your SharePoint list data.

Add a Power Apps Visual: Go to the “Visualizations” pane, click on the Power Apps visual, and add it to your report.

Configure the Power Apps Visual: Select the fields you want to pass to Power Apps. This will allow Power Apps to interact with the data in your Power BI report.

**Step 4: Building a Power App**

Create a New Power App: Click on the Power Apps visual in Power BI and choose to create a new app. This will open Power Apps Studio.

Design Your App: Use Power Apps Studio to design your app. You can add forms, galleries, and other controls to interact with your SharePoint data.

Connect to SharePoint: Connect your app to the SharePoint list used in Power BI. This ensures data consistency across both platforms.

Add Logic: Use Power Apps formulas to add logic to your app. For example, you can create buttons that update data or trigger workflows.

**Step 5: Integrating Power Automate**

Create a Flow: Open Power Automate and create a new flow. Choose a trigger that suits your needs, such as “When an item is created” or “When a button is clicked”.

Add Actions: Add actions to your flow that interact with your SharePoint data. For example, you can create actions to send emails, update records, or create tasks.

Connect Power Apps to Power Automate: In Power Apps, add a button or other control that triggers the flow. Use the “Power Automate” connector to link the button to your flow.

**Step 6: Testing and Deployment**

Test Your Integration: Test the entire integration to ensure everything works as expected. Check that data flows correctly between Power BI, Power Apps, and Power Automate.

Deploy Your Solution: Once testing is complete, deploy your solution to your users. Ensure they have the necessary permissions to access the data and use the app.

**Example Use Case: Sales Dashboard**

Create a Sales Report in Power BI: Load your sales data from the SharePoint list into Power BI and create a report with visuals showing sales performance.

Add a Power Apps Visual: Add a Power Apps visual to the report and configure it to pass sales data to Power Apps.

Build a Sales App: Create a Power App that allows sales representatives to update sales records and add comments.

Automate Notifications: Use Power Automate to send notifications to managers when sales targets are met or exceeded.

**Conclusion**

Integrating Power BI with Power Apps and Power Automate using a SharePoint list provides a powerful way to enhance your data analysis and workflow automation. By following these steps, you can create a seamless integration that improves efficiency and decision-making in your organization.

**Additional Resources**

Microsoft Learn: Integrate Power Apps, Power Automate, and Power BI with SharePoint Online

Power BI Tips: Using Power Apps, Power BI, and Power Automate Together

YouTube Tutorial: How To Integrate A Power App Into Your Power BI Report

By leveraging these tools, you can create dynamic, interactive reports and automate complex workflows, driving greater insights and productivity within your organization.