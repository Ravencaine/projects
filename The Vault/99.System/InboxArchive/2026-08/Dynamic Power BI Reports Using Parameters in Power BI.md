---
title: "Dynamic Power BI Reports Using Parameters in Power BI"
source: "https://databear.com/master-dynamic-reporting-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-02-16
created: 2026-08-04
description: "Discover how to create dynamic reports in Power BI using parameters from Excel."
Processed: "Unprocessed"
---
Did you know that you can dynamically filter data in Power BI using parameters stored in an Excel workbook? If you didn’t, you’re about to find out how to do this in a few simple steps. In this blog post, I will walk you through the process of using parameters in Power BI to create dynamic reports. We’ll explore how to set up parameters, use stored procedures, and integrate data from Excel to automatically filter reports based on user input.

##### Understanding Parameters in Power BI

Parameters in Power BI are a powerful feature that allows users to input variable values that can change the way data is presented in reports. They enable dynamic report creation, allowing users to filter data based on their specific needs. This functionality is particularly useful in scenarios where end users are involved in report creation and data analysis.

##### The Challenge

Recently, a customer approached me with a fascinating request. They wanted to enable users in Power BI Desktop to call a stored procedure, pass parameters, and then publish the report to the Power BI service. After publishing, they wanted to enter data into an Excel spreadsheet, and upon refreshing the report, it should automatically filter based on the values in that spreadsheet. This sounded like an exciting challenge!

##### Setting Up the Stored Procedure

To start, we need a stored procedure. Open Power BI Desktop and navigate to the ‘Get Data’ option. Here’s how to connect to your SQL Server and execute the stored procedure:

1. Open Management Studio and choose ‘Get Data’. Select ‘SQL Server’.
2. Enter your server name and database name.
3. Grab the execution of the stored procedure and paste it into the query editor.
4. Click ‘OK’ to execute the stored procedure.

After a few moments, you should see the data returned from the stored procedure. Instead of clicking ‘Load’, click ‘Edit’ to modify the query.

![Executing the stored procedure in Power BI](99.System/Attachments/Executing_the_stored_procedure_in_Power_BI.webp)

##### Creating Parameters

Next, we need to create a parameter that will allow users to input their own values. Follow these steps to create a parameter:

1. Go to ‘Manage Parameters’ and click ‘New Parameter’.
2. Set the name to ‘Student ID’ and define it as text.
3. Input a sample student ID value and click ‘OK’.

Now that we have our parameter, we need to integrate it into our query. Right-click on your query and select ‘Advanced Editor’. Replace the hardcoded value in the query with the parameter name. This allows the query to execute using the user-defined value.

![Creating parameters in Power BI](99.System/Attachments/Creating_parameters_in_Power_BI.webp)

##### Handling Multiple Parameters

Initially, the customer needed to pass a single student ID. However, they later requested the ability to pass multiple student IDs and create a report that shows data for all of them. To achieve this, I created a simple spreadsheet with a single column of student IDs. Here’s how to proceed:

1. Create a single-column Excel spreadsheet with student IDs.
2. Save the spreadsheet in a known location.
3. In Power BI, go back to the query editor and import the Excel spreadsheet.
4. Rename the imported sheet to ‘Student ID’ and ensure the data type is set to text.

Now, we need to pass these values from the Excel spreadsheet into our stored procedure. Right-click on the query associated with the stored procedure and select ‘Create Function’. This function will accept a student ID as a parameter.

![Creating a function in Power BI](99.System/Attachments/Creating_a_function_in_Power_BI.webp)

##### Invoking the Custom Function

With the function created, we can invoke it using the values from our students table. Here’s the process:

1. Click on the ‘Students’ query and navigate to ‘Add Column’.
2. Select ‘Invoke Custom Function’ and choose the function we created earlier.
3. Pass the student ID from the spreadsheet as the parameter value.

After running the query, you should see a single row for each student ID stored in the spreadsheet. This demonstrates that the parameters are working correctly.

![Invoking the custom function](99.System/Attachments/Invoking_the_custom_function.webp)

##### Refreshing Data

Now that we have our setup ready, let’s see how refreshing works. If you add a new student ID to the spreadsheet and refresh the query in Power BI, the report will dynamically update to include the new data. This allows end-users to easily manage the data displayed in their reports without needing to modify the Power BI file itself.

![Refreshing data in Power BI](99.System/Attachments/Refreshing_data_in_Power_BI.webp)

##### Setting Up the Gateway

To ensure that the report functions correctly in the Power BI service, we need to set up a gateway. Here’s how to do it:

1. Install the personal or enterprise gateway on your machine.
2. Publish your report to the Power BI service.
3. Go to ‘Manage Gateways’ and set up your data sources, including the Excel workbook and SQL Server.

Once everything is configured, users will be able to refresh their reports in the Power BI service, and the data will automatically filter based on the values in the Excel spreadsheet.

##### Final Thoughts

The ability to dynamically filter data in Power BI using parameters is a game-changer for report creation. It empowers end-users to interact with their data in meaningful ways, allowing them to customize reports based on their specific needs. If you have a better way to handle parameters in Power BI.

Boost your data skills with expert-led [Power BI training](https://databear.com/power-bi-training/). We have partnered with Microsoft to bring high quality Power BI training.