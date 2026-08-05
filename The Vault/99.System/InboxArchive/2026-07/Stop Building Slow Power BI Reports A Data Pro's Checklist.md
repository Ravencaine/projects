---
title: "Stop Building Slow Power BI Reports: A Data Pro’s Checklist"
source: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
author:
  - "[[Bill Donofrio]]"
published: 2026-07-20
created: 2026-07-27
description: "More"
Processed: "Unprocessed"
---
*The patterns that separate a slow report from a fast one*

![](99.System/Attachments/1!Np_vVjaMTS-xGlcL2VCk5g.png.webp)

This is an AI generated image

Power BI can be an incredibly useful tool to quickly and accurately understand business insights. It is easy to learn and very customizable. However, that exact simplicity may be the hidden danger. Since the barriers to entry are much lower than other tools, it is easy to build a report fast, and then another, and then another, before you finally realize that the reports are getting slower and slower.

Below is a checklist of items that every data professional should review before building their first report. These are all mistakes I have made or have seen others make over the years. Some required entire re-builds while others can be fixed with a few clicks. This list will begin with some of the most obvious and severe examples and work down to some less common but very useful fixes. The list is organized around the basics and builds on those concepts throughout the article.

### 1.) Data not modeled using a star schema

Building your models using a star schema is an absolute must. As a new report developer, it is hard to resist the urge of just importing 10 Excel files and letting Power BI magically join these tables together. It is simple but costly.

If you are not familiar with this pattern, it is comprised of two types of tables. A dimensional table (dim for short) that is essentially a reference table. Think of this as a list of countries, products, customers, or dates. Then you have a fact table that contains all your calculations.

Let’s assume you own a car dealership. In this case, you might have a few dim tables like dim\_product to list the make and model of all the cars in your inventory, dim\_client for those who purchased a car, and dim\_date for when someone purchased the car, dim\_employee, and dim\_store for locations. Finally, you would have a fact\_sales table that would include the dealer’s cost of the car, price the car was sold for, interest rate, and years of credit.

Below is an example of how a basic star schema should look. This topic should be all over the internet, so I won’t dive too deep into the details. If your dim (reference) tables are not all joined to one fact table, performance will eventually become an issue.

![](99.System/Attachments/1!VEVn53fvxQsz46V1dHOtfQ.png.webp)

This is an AI generated image

### 2.) Composite keys were used instead of surrogate keys

For most seasoned professionals, step one is common practice. However, building everything properly may be another issue. In the above example, you will notice that the fact\_sales table is joined with all the dim tables on product\_key, client\_key, date\_key, store\_key, and employee\_key. In a perfect world, all the keys would be unique integers. In the real world, it is not so easy.

I have worked with some databases that did not store a primary or foreign key so there is no unique value for each row. To get around this you could join several columns together to create a unique value or composite key. This does resolve the issue but is not the most efficient way. The more elegant approach is to create a surrogate key. A surrogate key (in red below) is simply an arbitrary id that you create to ensure each row is unique. It should be set up as an integer to reduce memory.

![](99.System/Attachments/1!nT8XzxyZa2lfKd51RjFq3A.png.webp)

This is an AI generated image

The reason why this is a better option is because an integer only takes up 4 bytes. While a string is calculated as the one byte per of characters for a VARCHAR and 2 bytes per character for an NVARCHAR. If you can get away with using a tinyint or smallint that is even better. The below chart shows this difference in memory, so imagine multiplying this by millions of rows.

![](99.System/Attachments/1!fw0jKtrcQA9VLSxU4-KSdA.png.webp)

This is an AI generated image

### 3.) Not aggregating to the correct granularity

![](99.System/Attachments/1!md1u4wbDO1A_SMPxfXUUsg.png.webp)

This next example will use the above for reference. I once worked with a client that wanted to replace all their Tableau reports with Power BI because of performance issues. After 2 weeks of analysis, the culprit was obvious. They joined all their tables to one table that used very slowly changing dimensions. A slowly changing dimension means that any row can change one or more columns over time. In the example above, the Mustang was version “GT Premium” from 1/1/26 to 6/30/26 and then changed to “GT Premium (Perf Pack)” from 7/1/26 onwards.

Of the half a million records, only around 500 records ever changed. Apparently, this was missed early on since it only occurred in 0.1% of all records. However, when finance discovered the issues, they created a MAXX measure to search for the most current rows by key. This resolved the inaccurate data but forced their entire table to be re-calculated in memory.

Needless to say, switching to Power BI alone was not going to solve their problem. The actual fix was simply to create a unique surrogate key for every record and then just join the fact table to the appropriate record. Since the inactive records were never in the fact table, they were simply ignored. The query time went from seconds to milliseconds almost immediately.

### 4.) Using bridge tables for many to many joins

While the many-to-many option exists in Power BI, it should rarely if ever be used. This one issue can be incredibly costly if set up incorrectly. It is most common in survey responses when a respondent is allowed to choose multiple options.

Suppose you have a car survey asking someone what options they expect in a new car. In this example the respondent chooses: Reliability, Fuel Economy, and Performance.

![](99.System/Attachments/1!nsSiLR3B11uQ7bdusTGIBw.png.webp)

If you simply join the survey\_response to the dim\_survey\_options table and then the respondent to a separate table, then you will get duplicate counts for your RespondentID. You can use a DISTINCTCOUNT to resolve this issue, but that adds an additional burden on the engine.

Using a bridge table allows this process to remain one-to-one. Using a COUNTX on either the RespondentKey or the AnswerKey will be clean and efficient. The below diagram shows the alternative setup.

![](99.System/Attachments/1!nljHS35hlCrLIfPOJL_jZg.png.webp)

This is an AI generated image

### 5.) Always bring your own date table

This is a simple fix if you are using the pre-built date hierarchy Power BI provides. Simply turn that feature off and add your own table. Below is DAX to build a dim\_date table with values from 2020 to 2030. Once set up, all your dates should join to this table. You now have one table for dates instead of a bunch of separate hidden date hierarchies. It also gives you more flexibility to add additional columns like IsHoliday or FinanceCloseDate.

```sh
dim_date =

VAR StartDate = DATE(2020, 1, 1)

VAR EndDate   = DATE(2030, 12, 31)

RETURN

    ADDCOLUMNS (

        CALENDAR ( StartDate, EndDate ),

        "DateKey",        INT ( FORMAT ( [Date], "YYYYMMDD" ) ),

        "FullDate",       [Date],

        "Year",           YEAR ( [Date] ),

        "QuarterNum",     QUARTER ( [Date] ),

        "Quarter",        "Q" & QUARTER ( [Date] ),

        "MonthNum",       MONTH ( [Date] ),

        "MonthName",      FORMAT ( [Date], "MMMM" ),

        "MonthShort",     FORMAT ( [Date], "MMM" ),

        "WeekNum",        WEEKNUM ( [Date] ),

        "DayOfWeekNum",   WEEKDAY ( [Date], 1 ),

        "DayOfWeekName",  FORMAT ( [Date], "DDDD" ),

        "IsWeekend",      IF ( WEEKDAY ( [Date], 2 ) > 5, "Weekend", "Weekday" )

    )
```

### 6.) DirectQuery chosen over import

When I first started using Power BI, I always chose DirectQuery since I was afraid that the data model would eventually reach the limit and break. Now, the upper limits of import have grown exponentially so most models will fit into memory. Reading from memory is always quicker than reading from disk. If your model is too big for the import option, you may want to consider limiting your data to the most current year or two. You can also aggregate (sum or count) the data into smaller categories to reduce space.

### 7.) Incremental refresh for large tables

This feature is a game changer when I first discovered it. We were pulling millions of records from Google Analytics 4 at a very granular level. The refresh rate was very overwhelming. With most marketing tools you get daily snapshots. Since it is always an append into an existing model, it makes it a perfect fit for incremental refresh. Simply right click on the table and choose “Incremental refresh”. You can then choose the refresh schedule and how far back you can keep the older data.

![](99.System/Attachments/1!XyqSDBxUZTa4RGhSv2v6xQ.png.webp)

This ia an AI generated image

### 8.) Remove unnecessary columns

This one is also simple but powerful. I once incorrectly put a surrogate key on a fact table with millions of records. The surrogate key had no value at all. Once that column was removed, the query time improved dramatically. This process is known as column pruning.

I found Bravo to be a good tool to highlight every field that is not being used. The only caveat is it may flag surrogate keys since they are not used directly in your visualizations. As long as you use it properly, you can really reduce your model size and improve performance.

### 9.) Pivot your columns into rows

![](99.System/Attachments/1!R9-hKDWK4lhq9x_siH5ZZg.png.webp)

This pattern can be really helpful, but it is often used in more edge-case scenarios. I learned that you can sometimes pivot tables from row to columns to reduce space. In the survey example from before, instead of just listing every answer and questions in one table, you can pivot the answer by count. Then when you want to display the results, you just do a SUMX on the column. The advantage here is that you can build just one fact table for all your data.

Below is the code you can use in SQL to build this pivot.

```sh
SELECT
RespondentID,
ISNULL(Reliability, 0) AS IsReliability,
ISNULL([Fuel Economy], 0) AS IsFuelEconomy,
ISNULL(Safety, 0) AS IsSafety,
ISNULL(Performance, 0) AS IsPerformance
FROM
(
 -- 1. Select the base columns needed for pivoting
SELECT
RespondentID,
SelectedFeature,
1 AS FeatureExists - Used as the value to aggregate
FROM UnoptimizedStagingTable
) AS SourceTable
PIVOT
(
 -- 2. Aggregate the flag column across the distinct feature strings
MAX(FeatureExists)
FOR SelectedFeature IN (Reliability, [Fuel Economy], Safety, Performance)
) AS PivotTable;
```

### 10\. Don’t overcomplicate your visualizations

Adding too much complexity to your visualizations can be an issue. Reduce the number of visualizations on a page. Don’t build tables with millions of records since they will take a long time to load. If this is needed, you may want to consider using Power BI report builder for paginated reports. Finally, conditional formatting, dense scatter plots, and complex maps can cause a performance hit.

As I conclude, remember that before you start tuning, it is wise to benchmark first. Power BI’s built-in Performance Analyzer is the fastest way to see exactly which visual or query is actually slowing you down.

If you follow this checklist, you should end up with a genuinely fast, well-structured report. It isn’t completely exhaustive, but it covers the fundamentals of a clean, performant schema.

The key takeaways are to keep your model lean by pruning unused columns, use integer surrogate keys, and aggregate to the right granularity. Then build on a proper star schema with your own date table and choose your storage and refresh strategy deliberately. Choose Import over DirectQuery when you can and incremental refresh for large tables if they’re append-only. If you’ve run into a performance killer I didn’t cover here, I’d genuinely like to hear about it. Drop it in the comments and let’s build a more complete list together.