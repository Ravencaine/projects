---
title: "Understanding the VALUE DAX function in Power BI"
source: "https://databear.com/value-dax-function-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2022-10-22
created: 2026-08-04
description: "Looking to streamline your operations expert Microsoft Power Apps consulting services? Streamline processes and enhance productivity with tailored solutions today!"
Processed: "Unprocessed"
---
The VALUE DAX function is one of the manipulative functions. When presented with a particular table or column, it produces a single-column table of unique values. The duplicates in the table are eradicated, leaving blanks and unique table values behind.

## DAX VALUE function Syntax:

VALUES(TableNameorColumnName)

The TableName/ColumnName represents the column or table from which the unique values returned have been derived.

When the input parameter passed is the column name. The output is a single-column table that contains unique values from the given column.

When a table name is the input parameter passed. The function returns all unique rows from this specific table while preserving duplicate rows.

When using this function in a context that has been filtered, the outcome is affected by these filters, and to remove this, the ALL function must be used.

## How to use the VALUES DAX function

Let’s use an example to explain how the VALUE DAX function works. Jobs is a fact table that has approximately 15-16 data tables.

![ VALUE DAX function](99.System/Attachments/_VALUE_DAX_function.jpg)

When a lot of data tables are in a fact table, it becomes complicated to create new measures, especially when a data range is involved.

The image below is the output of the above DAX expression. The outcome shows that there are several data tables, such as received, estimate approved, and started dates, among others.

![](99.System/Attachments/Result-of-valve.jpg)

I would have to create specific measures to establish the number of jobs that have dates in the columns stated in a specified date range.

![specific measures value function](99.System/Attachments/specific_measures_value_function.jpg)

## Measures using the VALUE DAX function

Let’s illustrate how the above measures were derived.

To filter out the fact table, I created two measures; the first is responsible for tallying all jobs containing all three dates (started, estimate approved, and received) for a particular date range.

![Measures using the VALUE DAX function](99.System/Attachments/Measures_using_the_VALUE_DAX_function.jpg)

The second measure was meant to calculate the total estimates.

![Measures using the VALUE DAX function](99.System/Attachments/Measures_using_the_VALUE_DAX_function.jpg)

To conduct the calculations, I incorporated the CALCULATE DAX function and added the COUNTROWS DAX functions to tally the total number of rows in the jobs table.

The goal was to obtain the **received date** by filtering the results. The image below shows the count of the jobs with the **received date,** which was equal to or less than the MAX in the given data range.

![data range](99.System/Attachments/data_range.jpg)

The function also counts all jobs **received** whose date is equal to or greater than the MIN date in the date range as indicated below.

![data range formula](99.System/Attachments/data_range_formula.jpg)

The same code can be applied in deriving estimate-approved and started jobs with very few alterations. The formula used for the **job count** measure is also applied to **total estimates.** The only difference is that the **SUM** function is used in this case, as shown below.

Instead of tallying the total number of jobs, the formula will also calculate the total amount of estimates. Every job whose received, approved, and started date fall in the given date range. The output, in this case, would be 57 jobs and 378,031.44 total estimates.

**Our Data Bear [Power BI Training](https://databear.com/power-bi-training/) is covering all these tips and more!**

## Testing the results

To check whether the results were correct, I created a page referred to as the **Testing page**, as shown below. This page represents a table that includes; total estimates, started date, estimate approved to date, and received date from the fact table.

To validate the above information, I filtered the date table of the three data tables and used the ALL function to obtain the total estimates, as shown in the image below.

![ALL function ](99.System/Attachments/ALL_function_.jpg)

I hope you found this helpful.

**Our Data Bear [Power BI Training](https://databear.com/power-bi-training/) is covering all these tips and more!**