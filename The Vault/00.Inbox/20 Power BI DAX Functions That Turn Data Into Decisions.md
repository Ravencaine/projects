---
title: "20 Power BI DAX Functions That Turn Data Into Decisions"
source: "https://medium.com/microsoft-power-bi/20-power-bi-dax-functions-that-turn-data-into-decisions-ce66c30bfcda"
author:
  - "[[Pooja Pawar]]"
  - "[[PhD]]"
published: 2025-09-19
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Open Power BI and you’ll see a formula bar waiting for you. Behind it lies DAX, a language with more than 250 functions. Impressive? Yes. Overwhelming? Absolutely.

But here’s the truth: you don’t need to learn them all. In practice, analysts and BI developers lean on a much smaller set — about 20 functions that cover the majority of real-world reporting needs. These are the workhorses, the ones that transform raw numbers into meaningful insights.

Let’s walk through them, not as a dry list, but as tools you’ll actually reach for when answering business questions.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MJXfbwAfBFxYd0tLPHNWfg.png)

Image Created by Author

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Core Calculation Functions

At the foundation of most DAX measures are a few key functions that shape almost every calculation.

**CALCULATE** is the beating heart of DAX. It allows you to change the filter context so your measures respond to conditions. Say your manager asks, *“What were sales last year, but only for premium customers?”* You can solve it elegantly with:

```c
Sales LY Premium =
CALCULATE(
    SUM(Sales[Amount]),
    SAMEPERIODLASTYEAR(Date[Date]),
    Sales[CustomerType] = "Premium"
)
```

This is the function that turns static totals into dynamic insights.

When you need totals, **SUM** is straightforward. But when you need to derive values row by row, **SUMX** takes over. Imagine calculating profit: simply summing revenue isn’t enough. You need to multiply quantity by unit price for each row, then add them all together.

```c
Total Profit =
SUMX(
    Sales,
    Sales[Quantity] * Sales[Unit Price]
)
```

That subtle difference turns raw data into business intelligence.

Averages are everywhere in business reporting — revenue per customer, spend per transaction, sales per store. **AVERAGE** does the basic job, but **AVERAGEX** allows for more precise context-based calculations. For example, to see the average sales per customer:

```c
Avg Sales per Customer =
AVERAGEX(
    VALUES(Customer[CustomerID]),
    [Total Sales]
)
```

Now your averages actually reflect customer behavior, not just simple arithmetic.

Sometimes you just need to know how many. That’s where **COUNTROWS** comes in. Counting orders, transactions, or records in a table is direct and powerful:

```c
Total Orders = COUNTROWS(Sales)
```

It’s a simple function, but it answers a question asked in almost every meeting.

And when uniqueness matters — customers, products, or even regions — **DISTINCTCOUNT** delivers. Marketing teams often ask, *“How many unique customers did we serve?”* With DAX, the answer is one line:

```c
Unique Customers = DISTINCTCOUNT(Sales[CustomerID])
```

## Business Logic and Relationships

Beyond raw math, business intelligence requires logic and the ability to navigate across relationships in your model.

With **FILTER**, you can narrow your analysis with precision. Want to know the sales amount where orders were greater than $1,000?

```c
High Value Sales =
CALCULATE(
    SUM(Sales[Amount]),
    FILTER(Sales, Sales[Amount] > 1000)
)
```

Suddenly your dashboard highlights only the transactions that matter most.

Relationships are the backbone of Power BI, and **RELATED** lets you pull in values from connected tables. Instead of manually merging datasets, you can bring in the customer’s city directly:

```c
Customer City = RELATED(Customer[City])
```

It keeps your model flexible while saving countless hours of work.

Sometimes you need to step back and ignore filters altogether. Functions like **ALL** and **REMOVEFILTERS** reset the view so you can calculate things like percentages of total.

```c
% of Total Sales =
DIVIDE(
    SUM(Sales[Amount]),
    CALCULATE(SUM(Sales[Amount]), ALL(Sales))
)
```

That’s how you move from “Sales are $10,000” to “Sales are 12% of the company total.”

Division errors can make dashboards look sloppy. **DIVIDE** prevents divide-by-zero problems while keeping your calculations clean:

```c
Profit Margin = DIVIDE([Total Profit], [Total Sales])
```

It’s one of those quiet functions that ensures your reports stay professional.

Business rules often need to be hard-coded into reports. With **IF** and **SWITCH**, you can classify values into categories or statuses. For example, grouping sales amounts into High, Medium, and Low:

```c
Category Group =
SWITCH(
    TRUE(),
    Sales[Amount] > 1000, "High",
    Sales[Amount] > 500, "Medium",
    "Low"
)
```

These functions bring real-world nuance into your analysis.

**VALUES** is another subtle but powerful function. It returns distinct values from a column and often supports more advanced measures. A common use is counting customers while respecting filter context:

```c
Customer Count = COUNTROWS(VALUES(Sales[CustomerID]))
```

Without VALUES, many dynamic measures wouldn’t be possible.

When datasets include multiple dates — order date, ship date, invoice date — **USERELATIONSHIP** lets you switch perspectives. If you want to calculate sales by ship date instead of order date:

```c
Sales by Ship Date =
CALCULATE(
    SUM(Sales[Amount]),
    USERELATIONSHIP(Sales[ShipDate], Date[Date])
)
```

It allows you to answer questions flexibly, without restructuring your model.

## Time Intelligence

Every business lives in time. Comparing periods, tracking progress, and analyzing growth are at the core of reporting — and DAX has dedicated functions for it.

With **SAMEPERIODLASTYEAR**, year-over-year analysis becomes effortless:

```c
Sales LY =
CALCULATE(
    SUM(Sales[Amount]),
    SAMEPERIODLASTYEAR(Date[Date])
)
```

It’s the function behind almost every growth discussion.

For cumulative annual progress, **DATESYTD** does the heavy lifting. If you want to track year-to-date sales:

```c
Sales YTD =
CALCULATE(
    SUM(Sales[Amount]),
    DATESYTD(Date[Date])
)
```

It’s a staple of performance tracking.

And for a quick version, **TOTALYTD** offers a shortcut to the same result:

```c
Total Sales YTD =
TOTALYTD(SUM(Sales[Amount]), Date[Date])
```

Even beginners can implement year-to-date metrics with ease.

## Ranking, Lookups, and Cleanup

Highlighting top performers, fetching details, and cleaning up data are common reporting tasks — and these functions make them possible.

**RANKX** creates rankings that stakeholders love to see. Whether it’s top 10 products or top customers, this function delivers:

```c
Rank by Sales =
RANKX(
    ALL(Sales[Product]),
    [Total Sales]
)
```

Now your dashboard can spotlight leaders at a glance.

For precise lookups, **LOOKUPVALUE** works like VLOOKUP in Excel. Suppose you want to fetch a product category from another table:

```c
Product Category =
LOOKUPVALUE(Product[Category], Product[ID], Sales[ProductID])
```

It’s direct, flexible, and reliable.

Peaks and lows tell powerful stories. With **MAX** and **MIN**, you can find your best and worst performers quickly:

```c
Max Sales = MAX(Sales[Amount])
```

These simple functions help identify records worth celebrating — or investigating.

And finally, clean dashboards need to handle missing values. **BLANK** and **ISBLANK** allow you to replace nulls with more meaningful numbers:

```c
Check Null =
IF(ISBLANK(Sales[Amount]), 0, Sales[Amount])
```

The result is a smoother, more trustworthy report.

## From Functions to Insights

Individually, these functions are powerful. Together, they form a toolkit that covers most of what you’ll ever need in Power BI. They let you answer tough questions, design flexible models, and — most importantly — tell stories that help people make better decisions.

The magic of DAX isn’t in memorizing hundreds of functions. It’s in mastering the essentials and practicing them on real data. Once you do, you’ll stop building dashboards that just report numbers — and start creating ones that change conversations.

👏🏻 Clap 🔎 [Follow](https://medium.com/@poojapawar0309) 📩 [Subscribe](https://medium.com/@poojapawar0309/subscribe) ✍🏻Comment

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----ce66c30bfcda---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX