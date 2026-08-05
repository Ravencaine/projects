---
title: "Dynamic Single Slicer using DAX logic"
source: "https://databear.com/dynamic-single-slicer-using-dax-logic/"
author:
  - "[[Boniface Muchendu]]"
published: 2022-10-30
created: 2026-08-04
description: "Using DAX logic to create a dynamic single slicer and implementing the Dynamic M query parameters. There are situations where it is impossible to implement the dynamic M query parameter."
Processed: "Unprocessed"
---
Any Power BI report will always have specific requirements; this might range from applying restrictions of different levels to enhance data security and integrity to ensuring that the different slicers in the data report have been represented as a single slice selector. In Power BI, two methods can be implemented to represent multiple slicers as a dynamic single slicer sector: using DAX logic to create a dynamic single slicer and implementing the Dynamic M query parameters. There are situations where it is impossible to implement the dynamic M query parameter. This leaves us with dynamic single slices created from DAX logic. This blog will illustrate using the dynamic single slicer created from DAX logic in Power BI.

## Using Dynamic single slicers with DAX logic

To effectively explain the process and make it easy to understand, we will use a dataset obtained from AdventureWorksDW2012. In this case, we are trying to develop a combination of 6 columns obtained from the FactInternetSales table. These columns are slicers, and our goal is to combine them into a single slicer; it is important to note that you can combine any number of slicers into a single one in Power BI using this method.

To achieve our objective, there are several steps that we must follow chronologically, as illustrated below. I will attach images of the different steps to make it easy to understand what we are doing.

### Step1: Import the dataset

We cannot implement the dynamic single slicer on an empty report; we need datasets. To do this, we must establish a connection between Power BI and SQL Server and import the FactInternetSales table.

![Import the dataset](99.System/Attachments/Import_the_dataset.png)

After linking Power BI to SQL, select the table you wish to import and then click transform data. After importing the data, it is possible to perform any manipulations you want on this data.

![Import the dataset](99.System/Attachments/Import_the_dataset-1.png)

### Step 2: Create a calendar table and set up the data model.

Though the imported report contains a calendar table named Dim Date, we are making assumptions it does not exist, and thus we have to create one. To create a new table, select modeling on the Power BI dashboard and click on create a table.

![](99.System/Attachments/Picture3.png)

For date column visualization, we shall use the OrderDate column from the FactInternetSales table, which can then be applied to the calendar table we are creating.

![Create a calendar table and set up the data model](99.System/Attachments/Create_a_calendar_table_and_set_up_the_data_model.png)

DateTable = CALENDAR(MIN(FactInternetSales\[OrderDate\]),MAX(FactInternetSales\[OrderDate\]))

To establish a relationship between the table we have created and the FactInternetSales table, we need to set up a data model.

![Data Model](99.System/Attachments/Data_Model.png)

### Step 3: Create all measures table that has an index column

We will use several metrics in this process; we need to have a table containing all these metrics. These metrics (measures) include; Order Quantity, freight, total product cost, unit price, sales amount, and standard cost. They will be represented as columns in a table, which will also have an index column.

![Create all measures table that has an index column](99.System/Attachments/Create_all_measures_table_that_has_an_index_column-1.png)

From the Power Bi desktop, we have selected **enter data**; this allows us to add the names of all the columns in our slicer. Add an increment in the index column. It is not a must to write the names of these measures as they appear in the FactInternetSales table. Load the new table to complete the step.

![Create all measures table that has an index column](99.System/Attachments/Create_all_measures_table_that_has_an_index_column.png)

### Step 4: Create Selections DAX logic

As stated in the introduction, a single selection slicer uses the DAX logic. Which means we have to create the particular DAX logic.

Before creating the underlying DAX logic, we need to conduct aggregation calculations for the six columns.

Since the columns are numerical data types, we shall settle for the AVERAGE aggregation, as illustrated below.

**SalesAmtCal =AVERAGE(FactInternetSales\[SalesAmount\])**

Now we can jump right into applying the DAX logic calculations.

![Create Selections DAX logic](99.System/Attachments/Create_Selections_DAX_logic.png)

### Step 5: creating slicers and visuals

Reading through the code is insufficient; visuals will help show how the entire process works.

To create visuals, start by dragging the hierarchy column (date) into a clustered column chart. Then add the DAX slicer measure from step 4 in the value section as shown below.

It will be blank as we have not selected any measure we want to display.

![creating slicers and visuals](99.System/Attachments/creating_slicers_and_visuals.png)

A measure must be dragged from the **AllMeasuresTable** and made a slicer.

![AllMeasuresTable](99.System/Attachments/AllMeasuresTable.png)

Select any measures and they will be automatically visualized in the clustered column chart.

![All Measures Table](99.System/Attachments/All_Measures_Table.png)

Hope you enjoyed the post. Also see my [post](https://databear.com/report-design-ideas-in-power-bi/) on report design ideas. Have great week.