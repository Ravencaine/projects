---
title: "BI Case Study: Automating Quarterly Financial Reporting for Contoso Ltd using Power BI and Power Automate"
source: "https://medium.com/@benjohnokezie/automating-quarterly-financial-reporting-for-using-power-bi-and-power-automate-22b07300a706"
author:
  - "[[Ben-John Okezie]]"
published: 2025-08-07
created: 2026-08-09
description: "Building an Automated Reporting System"
Processed: "Unprocessed"
---
## Building an Automated Reporting System

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TVC1cdWRmEJezM9a-JbMcQ.png)

## Introduction

Contoso Ltd is a global manufacturing company that produces outdoor equipment. Contoso has quarterly board meetings for which financial analysts manually prepare Microsoft Excel reports, including profit and loss statements for each of the company’s four business units, the company’s balance sheet and net income projections for the next quarter.

This case study simulates a real-world BI solution scenario for **Contoso Ltd.** I designed a Power BI solution that automates and standardizes quarterly financial reporting, demonstrating how such transformation can reduce risk and free up analysts for higher-value work.

## Problem Context

Contoso Ltd’s finance team faced the following challenges:

- Analysts manually build P&L and balance sheet reports in Excel every quarter
- Frequent formula errors due to incorrect cell references
- Conflicting numbers caused by inconsistent business unit logic
- Long lead time — two analysts spend up to a week per cycle

## Objectives

To address this, the reporting solution needed to:

- Automate and standardise financial reporting using Power BI
- Cut report turnaround time from 7 days to 2 days
- Establish consistent logic across business units
- Incorporate security, maintainability, and documentation
- Automate report and KPI sharing using Power Automate

## Deliverables

The final solution would have the following deliverables

- A Power BI report
- A Power Automation flow
- Documentation of the solution

## Data Source

Contoso uses Azure SQL and Dynamics 365 Business to store its financial data, and so a connection would need to be established between Power BI and the sources.

I don’t have an available Azure SQL database and Dynamics 365 data source, so I’d be simulating an instance of connecting to an actual database.

The sample code below establishes a connection with Azure SQL in Power BI to access the financial data.

```c
Server: contoso-sql.database.windows.net  
Database: FinancialDB  
Table: dbo.FactFinancials
```

While Dynamics 365 can be accessed using Power BI’s built-in connector, you can use your business account tied to your D365 environment.

## Report Design

For my report design, I kept it simple and professional, taking inspiration from public works. I favour simple design and good UX above flashy, beautiful designs, because focus should be on the insights and data and not the design.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MqVCvLXk7zHlDcwpYxn_dw.jpeg)

Using neutral tones and low saturation colors is my top choice, the reason being that bright and high saturation colors pull the brain's attention regardless of context, increasing cognitive load on the user.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9pFkDA0Luh4rWQmCZu1taA.jpeg)

So while flashy dashboards might grab the attention of viewers, they might also weaken the memory of recalling relevant insights, but remember colorful shapes.

😅 It’s like trying to make your dashboard look good enough to be useful, but not so good it’s distracting. And the dashboard's design can be improved based on feedback.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*gGUQ26LYIPhtkxSoLMZXxw.jpeg)

> Note to self: Make chart colors standout more than background colors (nav bar & background)

## Refresh Schedule

Data refresh can be scheduled automatically from Power BI Service, I can set how often I want the data to be refreshed and what time. Credentials for the data source also have to be authenticated since it’s coming from an external source (Azure SQL & D365).  
Since I’m using simulated data from Excel, those options aren’t available.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Nf4HLTGD9_2CSqIQ19mWsg.jpeg)

## Report Automation

Now for the interesting part

Using Power Automate + Power BI Service, I designed a Power Automate flow that exports Reports every quarter as PDFs and mails them to Executives.

Financial reports are made from Power BI’s semantic model and consistent DAX formulas, so calculations are done without manual input.

In Power Automate below, all I need to do is create an Automated cloud flow or a Scheduled cloud flow, which allows me to connect to Power BI Services and create my flows.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZMlb0t8w5BSRZGYIKt5azg.jpeg)

Name and configure my cloud flow for how often I want it to run, setting the period for the flow to run, and then design my flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hRzeDfmKJKDptOvTgA7ACA.jpeg)

My flow is set to run at a set time, which exports my Power BI Report as a PDF, then sends the PDF through email, with an email template.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HDnnSmWxQGFD_qQ_fs6veQ.jpeg)

The email template

```c
Hello,

Please find attached the quarterly Power BI report.

Regards,  
Power BI Automation System
```

For this flow, I used a Scheduled cloud flow. The main difference between Scheduled cloud flow and Automated cloud flow is that Scheduled cloud flow is set to run on a time basis, while Automated cloud flow is run by a certain set of triggers.  
And the possibility of automation with these two options is endless, which allows for the creation of several automations, such as:  
✅ Send automated Alerts: Weekly revenue falls short by 12%  
✅ Send Report Snapshot and KPIs every Monday to team members  
✅ Alert the team if a certain threshold is crossed or not met  
and many more.

Reports can be sent to email, stored in SharePoint/OneDrive or even populated into an Excel template for easier consumption.

Power Automate already has numerous automation templates that can be used and customized for various purposes with powerful AI capabilities.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vCDb0beW-n6N5xo2TEqo8A.jpeg)

> Note: a number of these features for both Power BI and Power Automate require Premium or Pro user account

## Documentation

Here is a very important aspect of every project: documentation allows users to properly understand every aspect of the project, and for future developers of the project to easily reference material for modifications.

A proper documentation also ensures that the project is developed using proper standards and due diligence, since data is a sensitive and confidential asset.

It also helps in creating a central resource for all team members across the organization, large or small, to reference to adhere to general business logic definitions and naming conventions.

For this project, I’d be creating the documentation in an Excel file for simplicity. I would be structuring the documentation into 3 parts: ***Data Source and Metadata***, ***Business Logic/Calculations and Report Page and KPIs.***

These aren’t standards but preferences.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zDgt-lpIzdWDGcc09W_xDQ.jpeg)

Documentation could be more detailed, stored in different sources, i.e., SharePoint, Notion, etc. But it’s important that it’s comprehensible, acts as a central reference point for all users/members and is easily accessible.

## The Final Result and Value

By automating report generation and standardizing data logic, I have been able to achieve the following for Contoso Ltd:

- The Reporting time will be reduced from 7 days → 2 days or less
- Errors from Excel formulas eliminated through DAX measures and Power Query transformations
- Business units are now aligned on consistent definitions since the Power BI semantic model is used as a single source of truth.
- The finance team spends more time analyzing, less time fixing

## Final Thoughts

This simulated case study reflects the power of Business Intelligence and Automation in enterprises, mid-to-large firms looking to automate reporting and processes, saving time and reducing errors.

If you loved this piece, please give it a huge clap, it encourages me to keep delivering much value as I navigate myself through the world of Data, Automation and AI. Thank you.