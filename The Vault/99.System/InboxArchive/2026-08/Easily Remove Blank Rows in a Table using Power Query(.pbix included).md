---
title: "Easily Remove Blank Rows in a Table using Power Query(.pbix included)"
source: "https://medium.com/@shashanka.shekhar02/easily-remove-blank-rows-in-a-table-using-power-query-pbix-included-780c4bd164a8"
author:
  - "[[Shashanka Shekhar]]"
published: 2026-08-03
created: 2026-08-03
description: "Cleaning and preparing data is one of the most common tasks in Power Query. Blank rows often sneak into tables during imports or merges, and if left unchecked, they can distort analysis, cause errors, or simply make reports look untidy. Fortunately, Power Query provides straightforward techniques to identify and eliminate these unnecessary rows, ensuring your dataset remains clean and reliable."
Processed: "Unprocessed"
---
## Cleaning and preparing data is one of the most common tasks in Power Query. Blank rows often sneak into tables during imports or merges, and if left unchecked, they can distort analysis, cause errors, or simply make reports look untidy. Fortunately, Power Query provides straightforward techniques to identify and eliminate these unnecessary rows, ensuring your dataset remains clean and reliable.

- **Common issue**: Blank rows appear when importing from Excel sheets, CSV files, or databases with inconsistent formatting.
- **Impact on analysis**: They inflate row counts, break transformations, and mislead aggregations.
- **Power Query solution**: Built-in filters and conditional logic make removal quick and repeatable.
- **Automation advantage**: Once set, the query automatically cleans future data loads without manual effort.

This is what we wish to achieve from left to right.

![](99.System/Attachments/1!xzFb4BGFJnSt8XBr42rycg.png.webp)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Implementation in Power BI:

**We will go through these steps:**

Happy learning!

## 1\. Going through the Table:

The table is called **Dynamic\_Skip\_Rows.**

![](99.System/Attachments/1!w8iU6ftqKQMFH9qA7hIdOw.png.webp)

The table is essentially a **training/course allocation record**, showing which students are enrolled in which advanced technical courses. The validation metrics highlight **data completeness and quality issues** in Columns 2 and 3, which may need cleaning before analysis.

## 2\. Opening Power Query:

- In the **Home tab** press on the **Transform Data in the Queries section.**
- It will open the **Power Query** window.
![](99.System/Attachments/0!38YAru3jY2G2lI6U.gif)

In the Home tab press on the Transform Data in the Queries section

## 3\. Removing Blank Rows in Power Query:

- Select the **Dynamic\_Skip\_Rows** table in Queries**.**
- Click on **Advanced Editor tab.**
![](99.System/Attachments/1!14F7wAne2xYQO8vud8hyKw.gif)

Select the Dynamic\_Skip\_Rows table in Queries

- Now press **Advanced Editor** in Home tab and replace existing code full with below code.
- Ensure the replace the file path with your own file location.
```c
(let
    Source = Csv.Document(File.Contents("C:\Users\reinh\Downloads\All the work\My Tableau Repository\Datasources\Dynamic_Skip_Rows.csv"), [Delimiter=",", Columns=3, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    
    // 1. Filter out rows where Column2 is completely empty/blank/null
    FilterJunkRows = Table.SelectRows(Source, each ([Column2] <> "" and [Column2] <> null)),
    
    // 2. Promote the remaining first row to headers
    PromotedHeaders = Table.PromoteHeaders(FilterJunkRows, [PromoteAllScalars=true])
in
    PromotedHeaders
```
- All the blank rows got removed.
![](99.System/Attachments/1!3oy_d8LooBdCSMJ0xX4tPw.gif)

Now press Advanced Editor in Home tab and replace existing code with given code

## 4\. Applying The Changes And Completion:

- Click on **Close & Apply** in the upper right column.
![](99.System/Attachments/1!D5vG3JjFP1K6_Ctv7b3xlA.gif)

- In the **Report view**, you will find the new table Invoked Function in the **Data** section on the right side**.**
- Now in a **Table** visualization you can add the columns from new table for further analysis.
![](99.System/Attachments/1!IhAh-GvyI-TcTph6Aa4Tmw.gif)

> Download the data for the KPI from this [link](https://drive.google.com/file/d/18rVaub7tCQ5_5-qyjXO2B73r33AXud2x/view?usp=sharing).
> 
> Download the PBIX file from this [link](https://drive.google.com/file/d/18rVaub7tCQ5_5-qyjXO2B73r33AXud2x/view?usp=sharing).

## [Shashanka Shekhar - Medium](https://medium.com/@shashanka.shekhar02?source=post_page-----780c4bd164a8---------------------------------------)

### Read writing from Shashanka Shekhar on Medium. Contributor for Microsoft Power BI. I like Data Analysis and Data…

medium.com

Thank you for your attention!

[Follow](https://medium.com/@shashanka.shekhar02) me or [subscribe](https://medium.com/@shashanka.shekhar02/subscribe) to get all my Power BI articles!

## [Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included)](https://medium.com/microsoft-power-bi/easily-create-multiple-calculations-using-a-single-formula-in-power-query-pbix-included-e4c71b1e6835?source=post_page-----780c4bd164a8---------------------------------------)

### Working with Power Query often involves creating multiple calculations across different columns or scenarios. Instead…

medium.com

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX, Power Query