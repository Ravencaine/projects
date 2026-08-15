---
title: "Power BI Pro Trick: Highlight Months with Conditional Formatting (No Filtering!)"
source: "https://medium.com/learning-data/power-bi-pro-trick-highlight-months-with-conditional-formatting-no-filtering-5d3150fcc41b"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2025-12-12
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
## The Problem with Traditional Slicers

Picture this: You have a beautiful bar chart showing monthly sales data. Your stakeholders want to compare specific months (say, January and July) against the full year’s performance. A traditional slicer? It filters out everything else. The context disappears. The story breaks.

What if I told you there’s a way to **highlight** selected months while keeping all data visible? Enter: the power of disconnected tables, TREATAS, and conditional formatting.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yKUefIIeruDAx0x8OMr56A.png)

Before and after slicer selected

## What We’re Building

A monthly sales bar chart (2022–2024) for three product categories, where:

- All 12 months remain visible
- Selected months are highlighted in a bold color
- Non-selected months fade into the background
- No data is filtered out

Let’s dive in.

## Step 1: Prepare Your Sales Data

Create an Excel file named **SalesData.xlsx** with the following structure. Copy this data:

```c
Date,Category,Sales
2022-01-15,Electronics,45000
2022-01-20,Furniture,32000
2022-01-25,Clothing,28000
2022-02-10,Electronics,52000
2022-02-15,Furniture,38000
2022-02-20,Clothing,31000
2022-03-12,Electronics,48000
2022-03-18,Furniture,35000
2022-03-22,Clothing,29000
2022-04-14,Electronics,55000
2022-04-19,Furniture,41000
2022-04-25,Clothing,34000
2022-05-11,Electronics,58000
2022-05-16,Furniture,43000
2022-05-21,Clothing,36000
2022-06-13,Electronics,62000
2022-06-18,Furniture,47000
2022-06-23,Clothing,39000
2022-07-15,Electronics,68000
2022-07-20,Furniture,51000
2022-07-25,Clothing,43000
2022-08-12,Electronics,71000
2022-08-17,Furniture,54000
2022-08-22,Clothing,46000
2022-09-14,Electronics,64000
2022-09-19,Furniture,49000
2022-09-24,Clothing,41000
2022-10-16,Electronics,69000
2022-10-21,Furniture,52000
2022-10-26,Clothing,44000
2022-11-13,Electronics,75000
2022-11-18,Furniture,58000
2022-11-23,Clothing,49000
2022-12-15,Electronics,82000
2022-12-20,Furniture,64000
2022-12-25,Clothing,55000
2023-01-14,Electronics,47000
2023-01-19,Furniture,34000
2023-01-24,Clothing,30000
2023-02-11,Electronics,54000
2023-02-16,Furniture,40000
2023-02-21,Clothing,33000
2023-03-13,Electronics,50000
2023-03-18,Furniture,37000
2023-03-23,Clothing,31000
2023-04-15,Electronics,57000
2023-04-20,Furniture,43000
2023-04-25,Clothing,36000
2023-05-12,Electronics,61000
2023-05-17,Furniture,46000
2023-05-22,Clothing,38000
2023-06-14,Electronics,65000
2023-06-19,Furniture,49000
2023-06-24,Clothing,41000
2023-07-16,Electronics,71000
2023-07-21,Furniture,54000
2023-07-26,Clothing,45000
2023-08-13,Electronics,74000
2023-08-18,Furniture,57000
2023-08-23,Clothing,48000
2023-09-15,Electronics,67000
2023-09-20,Furniture,51000
2023-09-25,Clothing,43000
2023-10-17,Electronics,72000
2023-10-22,Furniture,55000
2023-10-27,Clothing,46000
2023-11-14,Electronics,78000
2023-11-19,Furniture,61000
2023-11-24,Clothing,51000
2023-12-16,Electronics,85000
2023-12-21,Furniture,67000
2023-12-26,Clothing,57000
2024-01-14,Electronics,49000
2024-01-19,Furniture,36000
2024-01-24,Clothing,32000
2024-02-12,Electronics,56000
2024-02-17,Furniture,42000
2024-02-22,Clothing,35000
2024-03-14,Electronics,52000
2024-03-19,Furniture,39000
2024-03-24,Clothing,33000
2024-04-16,Electronics,59000
2024-04-21,Furniture,45000
2024-04-26,Clothing,38000
2024-05-13,Electronics,63000
2024-05-18,Furniture,48000
2024-05-23,Clothing,40000
2024-06-15,Electronics,67000
2024-06-20,Furniture,51000
2024-06-25,Clothing,43000
2024-07-17,Electronics,73000
2024-07-22,Furniture,56000
2024-07-27,Clothing,47000
2024-08-14,Electronics,76000
2024-08-19,Furniture,59000
2024-08-24,Clothing,50000
2024-09-16,Electronics,69000
2024-09-21,Furniture,53000
2024-09-26,Clothing,45000
2024-10-18,Electronics,74000
2024-10-23,Furniture,57000
2024-10-28,Clothing,48000
2024-11-15,Electronics,80000
2024-11-20,Furniture,63000
2024-11-25,Clothing,53000
2024-12-17,Electronics,87000
2024-12-22,Furniture,69000
2024-12-27,Clothing,59000
```

Import this into Power BI using **Get Data > Excel**.

## Step 2: Create Your Date Table (Connected)

This is your standard date dimension table. Go to **Modeling > New Table**:

```c
Date = 
ADDCOLUMNS (
    CALENDAR (DATE(2022,1,1), DATE(2024,12,31)),
    "Year", YEAR([Date]),
    "MonthNo", MONTH([Date]),
    "Month", FORMAT([Date], "MMM"),
    "MonthYear", FORMAT([Date], "MMM YYYY")
)
```

**What this does:**

- Creates a continuous date table from Jan 1, 2022, to Dec 31, 2024
- This will be used as the slicer to control *highlighting*, not filtering.

**Critical step:** Create a relationship between `Date[Date]` and `SalesData[Date]`. Mark this date table as your date table in Power BI.

## Step 3: Create the Disconnected Date Table

Here’s where the magic begins. Create another table with **NO relationships**:

```c
Disconnected Date = 
DISTINCT (
    SELECTCOLUMNS (
        'Date',
        "Year", 'Date'[Year],
        "MonthNo", 'Date'[MonthNo],
        "Month", 'Date'[Month],
        "MonthYear", 'Date'[MonthYear]
    )
)
```

**What this does:**

- Extracts distinct values from your connected Date table
- Creates a mirror structure, but as a completely isolated table
- This table will power your slicer without affecting data relationships

**Why disconnected?** Because we want the slicer to control *highlighting*, not filtering. If this table had a relationship, selecting months would filter your data. By keeping it disconnected, all data remains visible.

## Step 4: Create Your Base Measure

First, create a simple Total Sales measure:

```c
Total Sales = SUM(SalesData[Sales])
```

This is your foundation measure that sums up all sales.

## Step 5: The TREATAS Bridge Measure

Now for the clever part. Create this measure:

```c
Highlighted Sales = 
VAR _SelectedMonths =
    VALUES ( 'Disconnected Date'[Month] )

RETURN
CALCULATE (
    [Total Sales],
    TREATAS (
        _SelectedMonths,
        'Date'[Month]
    )
)
```

**Breaking it down:**

**Line 2:** `VAR _SelectedMonths = VALUES('Disconnected Date'[Month])`

- Captures whatever months are selected in the disconnected slicer
- If you select “Jan”, “Jun”, “Dec”, this variable stores those three values
- If nothing is selected, it returns all distinct months

**Line 5–8:** `CALCULATE([Total Sales], TREATAS(...))`

- CALCULATE modifies the filter context
- TREATAS is the secret sauce here

**What TREATAS does:**

- It takes values from one table (`Disconnected Date[Month]`)
- Treats them AS IF they belong to another table (`Date[Month]`)
- Creates a virtual, temporary relationship for this calculation only
- Think of it as saying: “Take the selected months from my disconnected table and apply them as filters to my connected Date table.”

**The Flow:**

1. User selects “Jan” in the slicer (which uses connected Date)
2. Measure captures “Jan” in the variable
3. TREATAS says “filter the Date\[Month\] column to only ‘Jan’”
4. Total Sales calculates for January month
5. The bar chart shows values only for January

## Step 6: The Conditional Formatting Measure (The Real Star)

This is where we go from “showing data” to “highlighting data”. Create this measure:

```c
Bar Color = 
VAR CurrentMonth = MAX('Disconnected Date'[Month])
VAR IsMonthSelected =
    CALCULATE(
        COUNTROWS('Date'),
        KEEPFILTERS('Date'[Month] = CurrentMonth)
    ) > 0
RETURN
    IF (
        IsMonthSelected,
        "#1E293B",   -- Highlighted (dark slate blue)
        "#d0d4df"    -- Normal (light gray)
    )
```

**Let’s dissect this line by line:**

**Line 2:** `VAR CurrentMonth = MAX('Disconnected Date'[Month])`

- For each bar in your chart, this identifies which month it represents
- MAX works here because each bar represents one distinct month

**Line 3–7:** `VAR IsMonthSelected = CALCULATE(COUNTROWS('Date'), KEEPFILTERS('Date'[Month] = CurrentMonth)) > 0`

This is the detection logic. Let me break it down further:

- `CALCULATE(COUNTROWS('Date'), ...)` - Counts rows in the Date table under specific conditions
- `KEEPFILTERS('Date'[Month] = CurrentMonth)` - This is critical
- KEEPFILTERS respects both the visual context AND any filters from slicers
- It checks: “Does the current bar’s month match any month selected in the disconnected slicer?”
- If nothing is selected in the slicer, KEEPFILTERS returns true for all months
- If “Jan” is selected, it only returns true for January bar
- `> 0` - Converts the count to a boolean (TRUE/FALSE)
- If count is greater than 0, the month is selected → TRUE
- If count is 0, the month is not selected → FALSE

**Line 9–12:** `IF(IsMonthSelected, "#1E293B", "#d0d4df")`

- If the month IS selected: return dark color (#1E293B — a professional dark slate)
- If the month is NOT selected: return light gray (#d0d4df — faded background color)

**The Result:**

- When nothing is selected, all bars show in dark color
- When you select “Jan” and “Jul”: only January and July bars across all years turn dark, everything else fades to gray
- The data remains visible, but attention is drawn to what matters

## Step 7: Build Your Visual

Now let’s put it all together:

1. **Create a Clustered Column Chart**
2. **Configure the axes:**
- **X-axis:** `Disconnected Date[Month]`
- Sort this column by `Disconnected Date[MonthNo]` in ascending order to ensure chronological order
- **Y-axis:** `[Highlighted Sales]` (not Total Sales!)
1. **Apply Conditional Formatting:**
- Click on your visual
- Go to the **Format pane > Columns > Colors**
- Click **fx** next to the color picker
- Select **Field value**
- Choose `[Bar Color]` measure
- Click OK
1. **Add the Slicer:**
- Insert a Slicer visual
- Add `Date[Month]` to it
- Format as needed (list, dropdown, or tiles)

## How It All Works Together

Let me walk you through the entire flow:

**Initial State (Nothing Selected):**

1. The bar chart shows all the months of data
2. Highlighted Sales measure returns values for all months (because TREATAS with all months = all data)
3. Bar Color measure sees no specific selection, returns dark color for all bars
4. Result: All bars visible in dark color

**When You Select “Jan”, “Jun”, “Dec”:**

1. Date slicer passes these three months to the measures
2. Highlighted Sales uses TREATAS to filter to only Jan/Jun/Dec
3. Bar Color checks each bar:
- January? Selected month → dark color
- February? Not selected → gray
- June? Selected month → dark color
- And so on…
1. Result: 3 bars in dark color (Jan/Jun/Dec), 9 bars in gray, all data visible

## Why This Approach is Brilliant

**1\. Context Preservation:** Traditional filters remove data. This keeps everything visible while directing attention.

**2\. Year-over-Year Comparison:** Select “Dec” and instantly compare December performance across the year while seeing how it relates to other months.

**3\. Presentation Power:** During live demos, you can highlight different months dynamically without losing the full picture.

**4\. No Data Model Changes:** The disconnected table doesn’t affect your existing relationships or calculations.

**5\. Extensible Pattern:** Apply this same logic to categories, regions, products, or any dimension.

## Common Mistakes to Avoid

**1\. Forgetting to Keep the Table Disconnected:** If you accidentally create a relationship, the slicer will filter instead of highlight. Always verify that no relationships exist.

**2\. Using Total Sales Instead of Highlighted Sales:** The visual needs the TREATAS measure, not the base measure, for the highlighting to work properly.

**3\. Wrong Color Measure Reference:** Ensure conditional formatting points to the Bar Color measure, not a column.

**4\. Sorting Issues:** Always sort Month by MonthNo.

## Real-World Use Cases

**Retail:** Highlight holiday months (Nov, Dec) to see seasonal impact vs regular months

**Finance:** Emphasize quarter-end months (Mar, Jun, Sep, Dec) for reporting periods

**HR:** Focus on hiring months to analyze recruitment patterns

**Marketing:** Highlight campaign months to measure effectiveness against baseline

**Operations:** Identify peak season months for capacity planning

## The Bottom Line

This technique transforms Power BI from a tool that filters data to one that guides attention. By combining disconnected tables, TREATAS, and conditional formatting, you create interactive experiences that preserve context while highlighting insights.

Your stakeholders don’t just see data — they experience it.

The best part? Once you understand this pattern, you’ll find dozens of ways to apply it across your reports.

### About the Author:

Hi 👋 Thanks so much for reading! My name is **Ankan Bandyopadhyay,** a data visualization enthusiast/ Power BI Developer who believes that the best charts are the ones that disappear, leaving only the insights behind. Connect with me on **LinkedIn** to discuss data storytelling and visualization design.

☕ If you enjoy my articles and want to support me in writing more, you can [***buy me a coffee***](https://buymeacoffee.com/ankanbandyopadhyay) — every contribution means a lot and keeps this content going.

### Stay Tuned:

Make sure to [**follow me on Medium**](https://medium.com/@ankan.ab21) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@ankan.ab21)
- [***LinkedIn***](https://www.linkedin.com/in/bandyopadhyay-ankan/)

Now go build something amazing! 🚀

*The contents of external submissions are not necessarily reflective of the opinions or work of* [*Maven Analytics*](http://mavenanalytics.io/) *or any of its team members.*

*We believe in fostering lifelong learning and our intent is to provide a platform for the data community to share their work and seek feedback from the Maven Analytics data fam.*

[*Submit your own writing here*](https://medium.com/learning-data/how-to-get-your-work-published-by-learning-data-with-maven-analytics-7df21e466a3e?sk=020dfac485597d602e218968d9ffb395) *if you’d like to become a contributor.*

*Happy learning!*

*\-Team Maven*