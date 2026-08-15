---
title: "Automate Data Validation in Power BI Reports using Power Automate"
source: "https://medium.com/@guna24x7/automate-data-validation-in-power-bi-reports-using-power-automate-6deea7b04dbb"
author:
  - "[[Gunarathinam M]]"
published: 2024-09-18
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Enterprises and small businesses invest significant money, time, and resources to harness the power of data for making timely, informed decisions. Reports and dashboards, such as Power BI Reports and Dashboards, play a crucial role in this initiative. However, preparing and presenting data to consumers and decision-makers involves many moving parts.

Ingesting data from upstream systems (data sources), cleaning and reshaping it, modeling, storing it in a data warehouse, and performing strict data testing before exposing it through reports — each step is vital. However, several issues can arise when the data displayed in reports or dashboards is bad or incorrect:

1. Loss of Trust and Customer Dissatisfaction: Incorrect data erodes trust in the system, leading to dissatisfaction among users and stakeholders.
2. Poor Decision-Making and Revenue Loss: Wrong decisions based on inaccurate data can result in significant financial losses.

When such problems occur, the entire data effort can be undermined in seconds. This is a real-world challenge faced by every enterprise data and analytics team.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*za1Xg4sgAnPO3fs3)

Simple Reporting flow in Power BI

One solution to perform data validation in Power BI is by using Power Automate. While there are alternative approaches available, this article focuses on leveraging Power Automate to address this problem. This method runs basic validation rules on report visuals in Power BI.

## Preparation Steps:

1. Open the Report: Open the report file in Power BI Desktop and wait for all visuals to load.
2. Open Performance Analyzer: Navigate to the Performance Analyzer.
3. Refresh Visuals: Click on “Refresh Visuals” and wait for the data to load.
4. Capture the Visual Query (DAX): Capture the Visual Query (DAX).
5. Store the Query: Copy and store the DAX query in a file.
6. Create a Scheduled Flow in Power Automate: Open Power Automate online, and create a scheduled flow, which will have recurrence action at the start.
7. Add Execute Dataset Query Action: Add the “Run a Query against dataset” action and paste the DAX query, by connecting the workspace and dataset
8. Test and Run the Flow: Test and run the flow on the scheduled interval.

The Step 1–5 covered using below screen shot. I have Used the sample Power BI Report to demonstrate on how to get the Query used to generate the ‘Category Breakdown” visual.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ELamIeL4ak01NOCJ)

Below is the DAX query generated internally by DAX Query engine to get the visual output.

```c
// DAX Query
DEFINE
 VAR __DS0FilterTable = 
  TREATAS({"Net sales - category breakdown"}, 'Tooltip Info'[nombre])

 VAR __DS0FilterTable2 = 
  TREATAS({"Sold"}, 'Sales'[Status])

 VAR __DS0FilterTable3 = 
  TREATAS({"June"}, 'LocalDateTable_d9fbe243-4814-4038-8eec-593e864a563b'[Month])

 VAR __DS0Core = 
  SUMMARIZECOLUMNS(
   'Product'[Product],
   __DS0FilterTable,
   __DS0FilterTable2,
   __DS0FilterTable3,
   "SumAmount", CALCULATE(SUM('Sales'[Amount])),
   "Product_Top_N", IGNORE('Design DAX'[Product Top N])
  )

 VAR __DS0PrimaryWindowed = 
  TOPN(1001, __DS0Core, [SumAmount], 0, 'Product'[Product], 1)

EVALUATE
 __DS0PrimaryWindowed

ORDER BY
 [SumAmount] DESC, 'Product'[Product]
```

We can use the ‘DAX Query View’ to test the query and understand the output.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*gmpfW94stKkF7Lsb)

Now that we have a clear understanding of the query output in a tabular format, we have a solid foundation for running all data validation rules. To enhance this approach, we can parameterize the query with different values to customize it for various parameters.

The next step is to integrate this query into a Power Automate flow and schedule it to run every day before business hours. Below is an overview of the Power Automate flow:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*rvYrHjd6IcX-3JPk)

1\. Create a Scheduled Flow:

\- Open Power Automate and create a new scheduled flow to run daily before business starts.

2\. Parameterize the Query:

\- Modify the query to include parameters for different values as needed.

3\. Add the ‘Run a Query against Dataset” Action:

\- Paste the parameterized DAX query into the action by connecting with respective workspace and dataset(Semantic Model).

4\. Set Up Data Validation Rules:

\- Define the basic validation rules to check the query output, using Compose Actions.

5\. Add Conditional Logic:

\- Include conditional steps to handle various validation outcomes (e.g., send an alert if data validation fails).

6\. Configure Notifications:

\- Set up email or Teams notifications to inform relevant stakeholders about the validation results.

7\. Test the Flow:

\- Run the flow to ensure it works as expected and all validation rules are correctly applied.

8\. Activate the Flow:

\- Schedule the flow to run daily before business hours.

By following these steps, we can automate data validation in Power BI using Power Automate, ensuring that any data issues are identified and addressed before the start of each business day.

> *Microsoft Fabric offers advanced, code-rich data validation using Semantic Link and Notebook integration with the Great Expectations library. This powerful combination enhances data quality and reliability. We will cover this in detail in a future article.*

Happy automating! Feel free to clap, comment, like, and share!

Note: This article is originally published by myself in [LinkedIn Article](https://www.linkedin.com/pulse/automate-data-validation-power-bi-using-gunarathinam-mahalingam-fnusc/).

References:

[https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer)

[https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view](https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view)

[https://learn.microsoft.com/en-us/connectors/powerbi/](https://learn.microsoft.com/en-us/connectors/powerbi/)

[https://learn.microsoft.com/en-us/connectors/powerbi/#run-a-query-against-a-dataset](https://learn.microsoft.com/en-us/connectors/powerbi/#run-a-query-against-a-dataset)