---
title: "Creating a Measures Table in Power BI (And Why You Should) – Go Analytics"
source: "https://goanalyticsbi.com/creating-a-measures-table-in-power-bi"
author: "goanalyticsbi.com"
date: "2026-08-11"
tags: [imported, reading-list, power-query]
created: "2026-08-11"
---

> In this blog post, we explain the difference between Duplicate and Reference in Power Query in Power BI and Excel.

Creating a Measures Table in Power BI (And Why You Should) – Go Analytics Skip to content Post author: Camelia Nunez Post published: July 29, 2025 Post category: Connect to Data in Power BI / Data Visualization / How To / Power BI Reading time: 6 mins read In this blog, we show you how to create a dedicated Measures Table to keep your calculations organized, your data model clean, and your workflow efficient. Whether you’re working solo or collaborating with a team, this simple trick will save you time, and future-you will thank you. Have you ever felt overwhelmed trying to track down your DAX measures across different tables in Power BI? If so, you’re definitely not alone. Many Power BI beginners (and even seasoned users) fall into the same trap: creating measures directly within fact or dimension tables and then spending way too much time trying to find them later. Here, I’ll walk you through a simple but powerful solution: creating a dedicated Measures Table in Power BI . It’s a game-changer for keeping your work organized, efficient, and team-friendly. Why Use a Measures Table? Let’s start with the why ? Imagine you’ve built out a robust Power BI model with a dozen tables. Over time, you create dozens of DAX measures: some for total sales, some for KPIs, others for growth metrics. The problem? They’re scattered across various tables: Calendar, Provinces, Sales, and more. This setup can lead to: Wasted time scrolling through tables trying to find a measure Duplicated measures because you can’t locate the original A cluttered, confusing data model Headaches for collaborators trying to understand your work The fix? A centralized Measures Table! Your one-stop shop for all calculations and KPIs. How to Create a Measures Table in Power BI Here’s how to set it up in just a few steps: 1. Create a Dummy Table Go to the Home tab in Power BI Desktop. Click Enter Data . In the dialog box, enter a single dummy column (e.g., name it  , value  ). Rename the table to something meaningful like  . Click Load . This creates a placeholder table where you’ll store your measures. 2. Add or Move Measures into the Table Now, right-click on the new  and choose New Measure to create fresh DAX calculations. Already have measures elsewhere? No problem. You can move them. How? Click on an existing measure. Under the Measure Tools tab, use the Home Table dropdown to move it to your  . Once you’ve moved a few measures in, you can safely delete the dummy column (click the three dots next to it > Delete from model ). This transforms the table into a true Measures Table with the calculator icon, and it gets promoted to the top of your Fields pane Organize Measures with Folders and Subfolders Here’s where it gets even better. To keep your Measures Table clean and easy to navigate, group your measures into folders : Go to Model View . Select the measures you want to group (hold  to multi-select). In the Properties pane, enter a name under Display Folder (e.g.,  ). Want subfolders? Just add a backslash: Example:  This will nest the measure inside a “Start Numbers” subfolder under the main “Housing Starts” folder. Repeat this process for any grouping you need, such as organizing by time, geography, or metric type. Bonus Tips for Better Collection Even if you’re working solo, take the time to: Name your Measures Table clearly (e.g.,  ,  , or simply  ) Use meaningful folder names to make navigation easy for teammates or even future-you Prefix folders with numbers (e.g.,  ,  ,  ) to control their display order (since folders sort alphabetically). Need Help Getting Started With Power BI? Our Microsoft Certified consultants can help with the implementation of Power BI in your organization Book a meeting You Might Also Like Success Story: BuildForce Canada saves on editing time by automating development of presentations June 17, 2020 [How To] Connect to an Excel Workbook in Power BI Desktop November 27, 2022 How To Create a GANTT Chart in Power BI July 14, 2026 × × Cart

## Code / Examples

```
Dummy
```
```
1
```
```
Measures Table
```
```
Measures Table
```
```
Measures Table
```
```
Ctrl
```


---
*Source: [goanalyticsbi.com](https://goanalyticsbi.com/creating-a-measures-table-in-power-bi)*
