---
title: "Data Reduction Techniques for Power BI"
source: "https://medium.com/microsoft-power-bi/data-reduction-technics-for-power-bi-e0d9e883a559"
author:
  - "[[Tomas Kutac]]"
published: 2023-02-05
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
> [Unlock this article…](https://tomaskutac.medium.com/e0d9e883a559?sk=40f0f54c8c61969321d93e3c939c9a61)

Data reduction is a crucial aspect of data analysis in Power BI, as it helps to minimize the data size and improve data model performance. By reducing the data volume, you can minimize the time taken to load and process the data, leading to faster report generation and improved visualization performance.

Data reduction techniques can help you get the most value from your data while maintaining the accuracy and integrity of the information. Power BI provides several data reduction techniques that you can use to optimize your data analysis and visualization.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*e7lYKpF5FJYjNMVPlQgaKg.png)

## Data Reduction Approaches

### Data Filtering

One of the most basic data reduction techniques is filtering. You can use filters to exclude data that is not relevant to your analysis, reducing the data size and improving performance. Filtering can be performed using a variety of criteria, including date ranges, values, and keywords. When you apply a filter in Power BI, only the data that meets the criteria will be displayed in the report, reducing the amount of data that needs to be processed and visualized.

### Data Aggregation

Data aggregation is the process of summarizing data into a smaller set of values, reducing the data volume and improving performance. Power BI provides several aggregation techniques, including sum, average, count, and minimum and maximum values. By aggregating data, you can simplify complex datasets and focus on the key insights that matter most.

### Data Sampling

Data sampling is a technique that involves selecting a smaller subset of data from a larger dataset to represent the entire dataset. This can be useful for reducing the data size and improving performance when working with large datasets. In Power BI, you can use random sampling or stratified sampling, depending on your specific data and analysis requirements. With stratified sampling, you can divide the data into smaller groups based on specific criteria, such as age, income, or location, and then select a smaller sample from each group.

### Data Compression

Compression techniques are used to reduce the data size by compressing the data stored in columns. In Power BI, you can use columnar compression, which stores data in a compact and efficient format that reduces the amount of disk space required to store the data. This can significantly improve the performance of your data analysis and visualization, as the compressed data can be loaded and processed more quickly.

### Data Partitioning

Partitioning involves dividing the data into smaller, more manageable chunks, making it easier to load and process the data. This can be especially useful when working with large datasets, as it reduces the amount of data that needs to be loaded into memory, improving performance and reducing the risk of memory constraints. In Power BI, you can use data partitioning to divide the data into smaller parts based on specific criteria, such as date, location, or product.

By using these data reduction techniques in Power BI, you can optimize your data analysis, improve performance, and deliver insights more efficiently. It’s important to choose the right technique based on your specific data and analysis requirements, to ensure that you get the most benefit from your data reduction efforts. For example, if you’re working with large datasets, you may want to consider using data sampling or data partitioning to reduce the data size and improve performance. On the other hand, if you need to perform complex analysis, data aggregation may be more appropriate.

## Power BI Data Model

Power BI data model is effectively compressed using VertiPaq storage engine with compress ratio about 10x so if you import 10 GB of data, output.pbix file is about 1 GB.

VertiPaq is a columnar storage engine used by Microsoft Power BI and Microsoft Power Pivot. It allows for fast and efficient data compression, querying, and retrieval, by organizing data in columns instead of rows. VertiPaq also uses advanced techniques like data type inference, aggregation and encoding to further optimize performance. This storage engine enables users to handle large data volumes with ease and offers improved query performance over traditional row-based storage engines.

Data compression helps to reduce final size of data model but entire size of data loaded into it remains unchanged.

Main reasons for data reduction \[1\]:

- Larger model sizes may not be supported by your capacity. Shared capacity can host models up to 1 GB in size, while Premium capacities can host models up to 13 GB in size. For further information, read the Power BI Premium support for large datasets article.
- Smaller model sizes reduce contention for capacity resources, in particular memory. It allows more models to be concurrently loaded for longer periods of time, resulting in lower eviction rates.
- Smaller models achieve faster data refresh, resulting in lower latency reporting, higher dataset refresh throughput, and less pressure on source system and capacity resources.
- Smaller table row counts can result in faster calculation evaluations, which can deliver better overall query performance.

## Data Reduction Timing

From timing point of view we can reduce data **before** importing them into data model or **after** import. Here the rule is simple, whenever you can reduce data before importing, you should do it. It will speed up refresh of report, because smaller amount of data will be loaded during import process.

If you reduce data after import, it will not impact total import time, but will make data model and visualization faster because size of final data model will be reduced.

Most of the technics mentioned below can be done before or after data import. In this case difference will be place where data reduction will be process.

Let’s take example of one source data model where data will be imported from [SQL database](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-sql-tutorial). Before import you can use [SQL syntax](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql?view=sql-server-ver16) to specify columns that you would like to import and where condition can filter rows just for these that are related to our data analysis purpose. Possibility to write SQL syntax is placed under Advanced options.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-ZilUdsOITfZA_R7dDLfzA.png)

If you will reduce data after import, you will use [Power Query Editor](https://learn.microsoft.com/en-us/training/modules/automate-data-cleaning-power-query/) which allow users to define step by step data transformation.

> Please don’t forget to clap for this article if you like it. You can do it even more times… just try it.;-)

## Data Reduction Techniques

### Remove unnecessary columns

Removing unnecessary columns (vertical filtering) from the data model in Power BI can lead to a more efficient, faster, and easier-to-use data model, ultimately improving the overall performance and user experience of Power BI reports and dashboards.

- Reduced Data Size: By removing unnecessary columns, the size of the data model is reduced, which can lead to faster query performance and less memory usage.
- Improved Query Performance: Fewer columns mean less data to process during query execution, leading to faster query performance and lower resource utilization.
- Simplified Data Model: A simpler data model is easier to understand and maintain, making it easier to create and manage reports and dashboards.
- Better Compression: The VertiPaq storage engine in Power BI uses advanced compression techniques that are optimized for columnar data. By removing unnecessary columns, the compression efficiency is improved, leading to smaller data sizes and faster query performance.

Data model should include exactly the right number of columns based on the known reporting requirements. Requirements may change over time, but bear in mind that it’s easier to add columns later than it is to remove them later. Removing columns can break reports or the model structure. \[1\]

### Remove unnecessary rows

Removing unnecessary rows (horizontal filtering) from the data model in Power BI has similar benefits as removing unnecessary columns.

For this purpose various filters can be used usually filtering data by entities or by time.

Filtering by entity involves loading a subset of source data into the model. For example, instead of loading sales facts for all sales regions, only load facts for a single region. \[1\]

Filtering by time involves limiting the amount of data history loaded into fact-type tables (and limiting the date rows loaded into the model date tables). It is highly suggested you don’t automatically load all available history, unless it is a known reporting requirement. It is helpful to understand that time-based Power Query filters can be [parameterized](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-dynamic-m-query-parameters), and even set to use relative time periods (relative to the refresh date, for example, the past five years). Also, bear in mind that retrospective changes to time filters will not break reports; it will just result in less (or more) data history available in reports. \[1\]

### GROUP BY and SUMMARIZE

One of the most effective techniques to reduce a model size is to load pre-summarized data. This technique can be applied before data load (which is always better) using for example SQL syntax for SQL database or after data loading using Power Query.

Using GROUP BY and SUMMARIZE help to:

- Simplifying Data: By aggregating data, the complexity of the data is reduced, making it easier to understand and analyze.
- Improving Query Performance: Aggregating data can significantly improve query performance by reducing the amount of data that needs to be processed.
- Creating Summary Information: The SUMARIZE function allows you to create summary information by aggregating data based on specific columns and calculations.
- Visualizing Trends and Patterns: By aggregating data, you can create visualizations that help highlight trends and patterns in the data, making it easier to identify insights and opportunities.

### Optimize column data types

Numeric data types allow VertiPaq storage engine use highly effective encoding that helps drastically reduce size of data model. Whenever it is possible you should set numeric data type. Some entities use numbering ranges with text prefixes, then prefix can be removed and remaining value can be format as numeric data. In this case, it is important to set the column Default Summarization property to “Do Not Summarize”. It will help to minimize the inappropriate summarization in visualizations.

### Preference for custom columns

Very often original data source needs to be enriched by custom calculated columns. There are more ways how to define these custom columns.

These are options for custom columns definition sorted from the most effective one:

1. Use Measures instead of custom columns, whenever it is possible. Measures are calculated on the fly and did not consume any space in data model. But are mostly restricted to numeric calculations.
2. Define custom columns on data source side. For example using SQL syntax to create custom column. In such a case, SQL server performance is used to calculate these columns before data are loaded into Power BI data model.
3. Use Power Query M language to calculate columns as part of Power Query import steps. Column is calculated during import procedure but this technic has better performance compare to DAX calculated columns.
4. Use DAX to add new calculated columns into data model is the least effective way, because these columns are calculated when all data are loaded and all Power Query steps are finished. Also they are stored in data model as any other data so it increase data model size.

### Disable Power Query query load

Data sources that are used as a part of data transformation or integration in Power Query should not be loaded into data model.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*XP4Wle195SNDuywXtHh0Pw.png)

### Disable auto date/time

Power BI Desktop includes an option called *Auto date/time*. When enabled, it creates a hidden auto date/time table for date columns to support report authors when configuring filters, grouping, and drill-down actions for calendar time periods. The hidden tables are in fact calculated tables that will increase the size of the model. For guidance about using this option, refer to the [Auto date/time guidance in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-auto-date-time) article. \[1\]

### Switch to Mixed mode

Mixed mode allows to use different storage mode for each table and create [Composite data model](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-composite-models). In this scenario, for main tables you can use Import mode and for tables that has a lot of data or will be used rarely you can set Direct Query mode.

This approach could be effectively combined with data summarization. Summarized data are using Import mode but when user needs to analyze details, these details are using Direct Query mode that loads full details for specific filtered area. This approach reduced size of data model because detailed data are not stored in the model and are loaded on request.

In conclusion, data reduction is an essential aspect of data analysis in Power BI. By reducing the data size, you can improve performance, minimize the time taken to load and process data, and deliver insights more efficiently. Whether you’re working with large datasets or complex data structures, Power BI provides a range of data reduction techniques that can help you get the most value

> Please don’t forget to clap for this article if you like it. You can do it even more times… just try it.;-)

Learning resources:

\[1\] [https://learn.microsoft.com/en-us/power-bi/guidance/import-modeling-data-reduction](https://learn.microsoft.com/en-us/power-bi/guidance/import-modeling-data-reduction)

\[2\] [https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-common-query-tasks](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-common-query-tasks)

\[3\] [https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-sql-tutorial](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-sql-tutorial)

\[4\] [https://learn.microsoft.com/en-us/training/modules/automate-data-cleaning-power-query/](https://learn.microsoft.com/en-us/training/modules/automate-data-cleaning-power-query/)

\[5\] [https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer)