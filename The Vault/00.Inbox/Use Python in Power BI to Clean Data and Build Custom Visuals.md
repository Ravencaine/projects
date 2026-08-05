---
title: "Use Python in Power BI to Clean Data and Build Custom Visuals"
source: "https://databear.com/python-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-01-03
created: 2026-08-04
description: "Learn how to use Python in Power BI to clean messy data, detect outliers, and build advanced visuals. No coding needed thanks to ChatGPT."
Processed: "Unprocessed"
---
If you have ever had to manage messy CSV files with broken dates, inconsistent text, and confusing categories you know how difficult it can be to prepare data for reporting. In this post you will learn how to use Python in Power BI to clean and transform data on the back end and to build custom visuals using advanced analytics. You do not need to write your own code because ChatGPT will generate the Python scripts for you.

This approach makes it possible to go beyond the limits of Power Query and perform deeper analysis as part of your Power BI workflow.

[training resources:](https://databear.com/power-bi-training/)

##### Why Use Python in Power BI

Power Query in Power BI uses the M language to perform data transformation steps. M works well for most basic and intermediate transformations, but it has limitations when you need more advanced logic, pattern detection, or statistical analysis. Python integrates with Power Query and fills that gap. Python can handle complex text processing, statistical analysis, and can generate tables that simply would be difficult with M alone.

A further advantage is that you can use an AI tool such as ChatGPT to write the Python code for you. You only need to describe what you want to accomplish and the AI writes the script.

##### Two Ways to Use Python in Power BI

There are two main ways to use Python in Power BI:

##### 1\. Use Python as a Data Source

You can import data from Python by selecting **Get Data** then **Other** and choosing **Python script**. This lets Python load data from external files or databases before it enters Power BI.

This method works but it is not the focus of this tutorial.

##### 2\. Use Python for Data Transformation

The more common and powerful option is to use Python as part of your data transformation steps in Power Query. When you select **Transform data** and then **Run Python script** the current dataset flows into Python. Power Query places the existing data into a Python data frame called `dataset`. You then apply Python transformations that become part of the query steps.

This is the method shown in the tutorial and the method we will focus on here.

##### Using ChatGPT to Generate Python Scripts

Writing Python code manually can be challenging if you are not a developer. ChatGPT removes that barrier.

In the video example, the prompt to ChatGPT looked like this:

> Help me write a Python script for Power Query where the dataset is called `dataset`.  
> For the column product detail, separate out the product base and the product size into two new columns. Some products have sizes such as small, regular, or large and some do not.

ChatGPT returns a Python script that splits the text in the product detail column, creates new columns, and returns the transformed dataset.

After running the script in Power Query, the dataset shows two new columns: `product base` and `product size`. Products that had a size get properly separated. Products without a size retain their base name and an empty or null size column.

This new structure makes it possible to analyze products by size and base name separately.

##### Detect Outliers with Python in Power BI

Python can also be used to perform statistical analysis. For example you can ask ChatGPT to write a script that identifies outlier transactions in a dataset:

> Help me write a Python script for Power Query to analyze the dataset for outlier transactions and return transaction lines that do not follow expected patterns.

The script returned by ChatGPT performs the analysis, identifies outliers based on deviations from the mean, and creates a new output. After running the script in Power Query you get a table that contains only transactions identified as outliers. A second output may show summary statistics such as mean and standard deviation by product category or store location.

This type of analysis would be very difficult to complete using only M or DAX.

##### Create Custom Python Visuals in Power BI Reports

Python in Power BI is not limited to data transformation. You can also create visuals using Python.

To add a Python visual:

1. In the Visualizations pane, click the Python visual icon.
2. Add the fields you want to the Values section, for example `store location` and `transaction quantity`.
3. A Python script editor appears at the bottom of the visual.

In the video example the prompt to ChatGPT was:

> Help me write a Python script for a heat map that uses store location and transaction quantity.

ChatGPT writes a Python script that uses these fields to create a heat map. After pasting the script into the Python editor and running it, a heat map appears in the Power BI report showing how transaction quantity varies by location and hour.

This gives insights that would be difficult to achieve using only Power BI’s built‑in visuals.

##### What This Workflow Enables

Using Python with Power BI and AI support enables you to:

- Clean and transform text and complex data structures that are difficult with Power Query alone
- Perform advanced statistical analysis such as outlier detection
- Create visuals that require custom logic or advanced plotting capabilities
- Save time by having AI generate the Python code you need

This approach brings the power of Python into your Power BI reports without requiring you to be a programmer.

##### Final Thoughts

Integrating Python into Power BI with the help of AI opens up new possibilities for data transformation and visualization. You can automate repetitive tasks, perform complex analysis, and build visuals that extend beyond the standard chart options in Power BI.

If you would like structured training and more examples of [advanced analytics techniques, visit:](https://databear.com/power-bi-training/)