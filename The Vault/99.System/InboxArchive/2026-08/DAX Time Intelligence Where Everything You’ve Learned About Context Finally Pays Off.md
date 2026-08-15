---
title: "DAX Time Intelligence: Where Everything You’ve Learned About Context Finally Pays Off"
source: "https://medium.com/@jeseenaparveenk/dax-time-intelligence-where-everything-youve-learned-about-context-finally-pays-off-8de1bb67adcb"
author:
  - "[[Jeseena]]"
published: 2026-07-08
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
*Part 3 of the DAX series. This is where CALCULATE stops being abstract and starts doing serious business work.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wHFDqa_MnNIW4V8vmN-rhA.png)

DAX Time Intelligence

If you’ve been following this series, you’ve spent two posts building up some models: row context vs. filter context, how CALCULATE modifies filters, when to use ALL vs. ALLSELECTED. It might have felt theoretical at times.

This is the post where it all clicks.

Time intelligence is the category of DAX that stakeholders *actually ask for*. ***Year-over-year growth. Month-to-date sales. Rolling 3-month averages.*** These are the calculations that show up in every business dashboard I’ve ever built.

The good news: if you understand CALCULATE and filter context, time intelligence is mostly just learning which function shifts the date window and by how much. Let’s get into it.

### The One Thing You Must Have First: A Proper Date Table

Before a single time intelligence function will work correctly, you need a dedicated Date table in your model. Not the auto date/time that Power BI generates. A real, marked Date table.

It needs to:

- Have one row per date, with no gaps
- Cover the full range of dates in your data (and ideally a bit beyond)
- Be marked as a Date Table in Power BI (right-click the table → Mark as date table)
- Have a single, clean Date column that connects to your fact tables

If this isn’t set up correctly, every function in this post will either break or give you wrong results. Get the Date table right first. Everything else follows.

### Year-Over-Year Calculations

### DATEADD: “Shift the Date Context by Any Amount”

**What it does:** Returns a table of dates shifted by a specified interval (days, months, quarters, or years) in either direction.

```c
Sales LY =
CALCULATE(
    SUM(Sales[Amount]),DATEADD(Dates[Date], -1, YEAR))
```

This shifts the current filter context back by one year and calculates sales for that period. The result is last year’s sales for whatever time window is currently selected.

**The structure:**

```c
DATEADD(<dates>, <number_of_intervals>, <interval>)
```

Intervals: `DAY`, `MONTH`, `QUARTER`, `YEAR` Use negative numbers to go back in time, positive to go forward.

**Why CALCULATE is involved:** DATEADD returns a table of dates. CALCULATE takes that table and uses it to override the date filter context. This is exactly the context-shifting behavior from Post 1, now applied to dates.

**When you’d use it:** Any comparison to a prior period: last year, last quarter, last month, previous 30 days. DATEADD is the most flexible time shift function because you control the interval and direction.

### SAMEPERIODLASTYEAR: “Exactly One Year Ago, Same Window”

**What it does:** Returns a set of dates from exactly one year prior, matching the same period currently in context.

```c
Sales SPLY =
CALCULATE(SUM(Sales[Amount]),SAMEPERIODLASTYEAR(Dates[Date]))
```

**SAMEPERIODLASTYEAR vs DATEADD(-1, YEAR):**

They often return the same result. The difference is intent and readability:

- `DATEADD(Dates[Date], -1, YEAR)` is explicit. You're shifting by one year.
- `SAMEPERIODLASTYEAR` is self-documenting. Anyone reading your measure immediately knows it's a year-over-year comparison.

In practice, I use SAMEPERIODLASTYEAR when the measure is specifically a YoY comparison and DATEADD when I need flexibility (shifting by months or quarters).

**When you’d use it:** Year-over-year sales, YoY growth rate calculations, trend comparisons in executive dashboards.

### PARALLELPERIOD: “Same Length, Shifted by Full Periods”

**What it does:** Returns a parallel period shifted by a full number of intervals, but unlike DATEADD, it always returns *complete* periods.

```c
Sales Prior Quarter =
CALCULATE(SUM(Sales[Amount]), PARALLELPERIOD(Dates[Date], -1, QUARTER))
```

**The key difference from DATEADD:**

If you’re currently in mid-March (so your date context is Jan 1 to Mar 15), DATEADD(-1, QUARTER) gives you Oct 1 to Dec 15 of last year, a partial prior quarter. PARALLELPERIOD(-1, QUARTER) gives you the *full* prior quarter: Oct 1 to Dec 31.

PARALLELPERIOD always snaps to complete periods. DATEADD is a literal shift of whatever window is currently selected.

**When you’d use it:** Comparing full quarter or full year totals, when you want clean complete-period benchmarks rather than partial-period shifts.

### Month-to-Date, Quarter-to-Date, Year-to-Date

### TOTALMTD, TOTALQTD, TOTALYTD: “Cumulative From the Start of the Period”

These three work identically. They just differ in which boundary they reset at.

```c
MTD Sales = TOTALMTD(SUM(Sales[Amount]), Dates[Date])
QTD Sales = TOTALQTD(SUM(Sales[Amount]), Dates[Date])
YTD Sales = TOTALYTD(SUM(Sales[Amount]), Dates[Date])
```

**What they do:** Calculate a running cumulative total from the start of the month / quarter / year up to the last date in the current filter context.

**TOTALYTD has an optional fiscal year end parameter:**

```c
Fiscal YTD Sales =
TOTALYTD(SUM(Sales[Amount]), Dates[Date], "06-30")
```

If your fiscal year ends in June, pass that date and TOTALYTD resets at the right boundary instead of December 31.

**When you’d use it:** Running totals on time series visuals, progress-to-date KPIs, monthly or quarterly performance tracking.

### DATESYTD, DATESMTD, DATESQTD: “The Table Versions”

**What they do:** Return a table of dates from the start of the period to the current date in context, the same logic as the TOTAL versions, but as a date set you can pass into CALCULATE yourself.

```c
YTD Sales = CALCULATE(SUM(Sales[Amount]),DATESYTD(Dates[Date]))
```

**Why both versions exist:**

TOTALYTD is a shortcut. It wraps CALCULATE and DATESYTD together for you. DATESYTD gives you the raw date table, so you can combine it with other filter arguments inside your own CALCULATE.

Use the TOTAL versions when the YTD/MTD/QTD calculation is all you need. Use the DATES versions when you need to combine the period logic with other filters.

```c
-- YTD sales for a specific region, using DATESYTD for flexibility
YTD North Sales =
CALCULATE(
    SUM(Sales[Amount]),
    DATESYTD(Dates[Date]),
    Sales[Region] = "North"
)
```

### Rolling Calculations

### DATESINPERIOD: “Give Me a Rolling Window of Dates”

**What it does:** Returns a table of dates for a specified duration ending (or starting) at a given date. This is the go-to function for rolling period calculations.

```c
Rolling 3 Month Sales =
CALCULATE(
    SUM(Sales[Amount]),
    DATESINPERIOD(
        Dates[Date],
        LASTDATE(Dates[Date]),   -- end at the last date in context
        -3,                       -- go back
        MONTH                     -- by 3 months
    )
)
```

**The structure:**

```c
DATESINPERIOD(<dates>, <start_date>, <number_of_intervals>, <interval>)
```

Use a negative number to look backwards from the start date (rolling trailing window). Use positive to look forward.

**When you’d use it:** Rolling 7-day averages, trailing 12-month revenue, 90-day customer activity windows. Any time you need a window that slides with the current date rather than resetting at a fixed boundary like MTD.

### LASTDATE and FIRSTDATE: “Anchor to the Boundary of the Current Context”

**What they do:** Return the last or first date in the current filter context. Simple, but essential as building blocks inside other time intelligence functions.

```c
Last Sale Date = LASTDATE(Sales[OrderDate])
```

You’ve already seen LASTDATE used inside DATESINPERIOD above. It’s also useful for:

```c
-- Get sales as of the most recent date in context
Sales to Date =
CALCULATE(
    SUM(Sales[Amount]),
    DATESBETWEEN(Dates[Date], FIRSTDATE(Dates[Date]), LASTDATE(Dates[Date]))
)
```

**When you’d use it:** As an anchor point inside other date functions, or when you need to surface the boundary dates of a selected period.

### DATESBETWEEN: “Give Me Exactly This Date Range”

**What it does:** Returns a table of dates between two specified dates, inclusive of both endpoints.

```c
Sales in Custom Range =
CALCULATE(
    SUM(Sales[Amount]),
    DATESBETWEEN(Dates[Date], DATE(2024, 1, 1), DATE(2024, 6, 30))
)
```

**When you’d use it:** Fixed date range comparisons, fiscal period calculations with custom boundaries, or when you need precise control over the date window rather than relying on relative shifts.

## The Mind Map

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EoehXake9CiUIcEYQuwk0Q.png)

Mindmap

## How the Series Fits Together

If you’ve read all three posts, here’s the full picture:

**Post 1 (Relationships):** getting the right data across tables.

**Post 2 (CALCULATE & Context):** understanding how filters shape what your measures see.

**Post 3 (Filter Modifiers):** controlling exactly which filters CALCULATE keeps or removes.

**This post (Time Intelligence):** applying all of that to date-based calculations.

Every time intelligence function is really just CALCULATE with a specially constructed date table passed as a filter modifier. That’s it. Once you see that, the functions stop being a list to memorize and start being a logical extension of everything you already know.

*If this series has been useful, follow along. I write about Power BI, DAX and AI product development from the perspective of someone who’s certified, building real things, and still learning every day.*

*Connect here:* [*https://www.linkedin.com/in/jeseena-parveen-k/*](https://www.linkedin.com/in/jeseena-parveen-k/)

*If this was useful, the clap button is down there, it genuinely helps more people find this.*