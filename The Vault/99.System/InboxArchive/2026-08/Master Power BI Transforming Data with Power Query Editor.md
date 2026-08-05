---
title: "Master Power BI: Transforming Data with Power Query Editor"
source: "https://medium.com/microsoft-power-bi/master-power-bi-transforming-data-with-power-query-editor-0822b52ffd8c"
author:
  - "[[Janvi Gupta]]"
published: 2025-09-22
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
From Messy Exports to Perfect Reports: Why Every Analyst Needs This One Skill?🤔

![](99.System/Attachments/0!soz_EKaN0QBQIDTX.webp)

Imagine you’ve just exported three months of sales data from your company’s system. You’re excited to create some beautiful visualizations in Power BI, but when you open the data… 😱

- Column headers are in row 3, with company info cluttering the top
- The “Amount” column shows $1,200.50 next to “N/A” and “PENDING”
- Dates are formatted as text: “Jan-15–2024” mixed with “1/15/24”
- Three different files have slightly different column names
- Empty rows are scattered throughout your data

**Sound familiar?** This is exactly why Power Query Editor exists!

![](99.System/Attachments/0!NHao6aZ6JkL8VaYR.webp)

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> **Free Access: This blog is accessible to everyone, even non-Medium members, through this friend link👉** [https://medium.com/microsoft-power-bi/master-power-bi-transforming-data-with-power-query-editor-0822b52ffd8c?sk=5a992ad171dad2a3c6aae2351b58b9e1](https://medium.com/microsoft-power-bi/master-power-bi-transforming-data-with-power-query-editor-0822b52ffd8c?sk=5a992ad171dad2a3c6aae2351b58b9e1)

Power Query Editor is your **Data Preparation Workspace** inside Power BI Desktop. Think of it as a powerful kitchen where you take raw ingredients (messy data) and transform them into a perfectly prepared meal (analysis-ready data).

**🎯 Here’s the key insight:** Power Query Editor sits between your data sources and your Power BI reports. It’s where the magic happens **before** you start building visualizations.

**To Access It:**

- Import data → Click “Transform Data”
![](99.System/Attachments/1!qB1iTb7Qlhf7KrWitqUjzg.png.webp)

- Or from Home tab → “Transform Data”
![](99.System/Attachments/1!Ex-ldc7wpr3pn024QyELZg.png.webp)

## The Five Core Components You Need to Know

## 1\. The Ribbon

Your control center with four main tabs:

![](99.System/Attachments/1!Jp8cJ6eTRQLkZ3DH2Hn_bQ.png.webp)

- **Home:** Connect to data, basic transformations
- **Transform:** Advanced data reshaping options
- **Add Column:** Create new calculated columns
- **View:** Control what you see and access advanced features

## 2\. Queries Pane (Left Side)

Shows all your data connections and queries. Each query represents a table you’re working with. You can:

![](99.System/Attachments/1!JH2GaSylY66jRhy0BSDLRw.png.webp)

- Rename queries for clarity
- Organize related queries into groups
- See query dependencies

## 3\. Data Preview (Center) 👀

Your live preview of the data as you transform it. This is where you see the results of each step you apply. The preview shows up to 1,000 rows by default.

![](99.System/Attachments/1!lbhnjHI-9kD_1OuU8kXQJQ.png.webp)

## 4\. Applied Steps (Right Side)

The **game-changer!** Every transformation you make gets recorded as a step. You can:

![](99.System/Attachments/1!fCgKYZduwgIisxW15JkgiA.png.webp)

- See exactly what you’ve done
- Edit, delete, or reorder steps
- Go back to any point in your transformation process

## 5\. Formula Bar

Shows the M code (Power Query’s language) for each step. Don’t worry — you don’t need to write code, but seeing it helps with troubleshooting!

![](99.System/Attachments/1!XKwbw4-myaVY-xoBXehdkw.png.webp)

## What Can You Actually DO with Power Query? (Real Examples)

Let me show you the **six major transformation categories** with simple examples:

## 1\. Structure Transformation

**Problem:** Your data isn’t shaped correctly for analysis.

**Example:** Monthly sales data where each month is a separate column:

```c
Product    Jan-2024    Feb-2024    Mar-2024
Laptop     $1,200      $1,500      $1,100
Phone      $800        $900        $750
```

**Solution:** Unpivot columns to create proper rows:

```c
Product    Month       Sales
Laptop     Jan-2024    $1,200
Laptop     Feb-2024    $1,500
Phone      Jan-2024    $800
```

**How:** Select month columns → Transform → Unpivot Columns

## 2\. Data Cleaning 🧹

**Problem:** Inconsistent, dirty, or incorrectly formatted data.

**Example:** Customer names with inconsistent formatting:

```c
Before: "john SMITH", "Jane Doe", "bob johnson"
After:  "John Smith", "Jane Doe", "Bob Johnson"
```

**Solution:** Transform → Format → Proper Case

## 3\. Data Type Correction

**Problem:** Numbers stored as text, dates not recognized properly.

**Example:** Sales amounts showing as “1200.50” (text) instead of 1200.50 (number)

**Solution:** Click the data type icon next to column name → Select “Decimal Number”

## 4\. Combining Data

**Problem:** Information spread across multiple files or tables.

**Example:** You have separate files for each sales region that need to be combined:

- Regoin1\_Sales.xlsx
- Regoin2\_Sales.xlsx
- Regoin3\_Sales.xlsx

**Solution:** Home → Append Queries → Combine all files into one table

## 5\. Adding Calculated Information

**Problem:** You need additional insights derived from existing data.

**Example:** Adding a “Sales Category” based on amount:

```c
If Sales > $1,000 = "High Value"
If Sales ≤ $1,000 = "Standard"
```

**Solution:** Add Column → Custom Column → Write simple if-then logic

## 6\. Filtering and Grouping

**Problem:** Too much data or need summary information.

**Example:** You only want sales from the last quarter, grouped by product category.

**Solution:**

1. Filter: Click dropdown on Date column → Date Filters → Last Quarter
2. Group: Transform → Group By → Select Product Category, Sum Sales

## The Power Query Transformation Process (Your Workflow)

Here’s how you’ll typically work with Power Query Editor:

## Step 1: Connect

Import your data from any source (Excel, CSV, Database, Web, etc.)

## Step 2: Assess

Look at your data quality:

- Enable View → Column Quality (shows error percentages)
- Enable View → Column Profile (shows data distribution)
- Spot obvious issues
![](99.System/Attachments/1!T-K7_6ffah-x_U93FFzw1Q.png.webp)

## Step 3: Transform

Apply transformations in this typical order:

1. Fix structure (remove unnecessary rows, fix headers)
2. Clean data (handle errors, standardize formats)
3. Correct data types
4. Add calculations if needed
5. Filter unnecessary data

## Step 4: Load

Click “Close & Apply” to send clean data to your Power BI model

![](99.System/Attachments/1!tkppGWK9PUBr8SAE5tQEvQ.png.webp)

## The Magic of Applied Steps (Why This Changes Everything)

Here’s what makes Power Query Editor incredibly powerful: **Every step is recorded and repeatable.**

![](99.System/Attachments/1!IgV8nD6sbvj1i9TvF7jkjA.png.webp)

**Real Scenario:** Your monthly sales report changes format slightly each month. With traditional Excel, you’d manually fix it every time. With Power Query:

1. ✅ Build your transformation once
2. ✅ Next month, just refresh your data
3. ✅ All transformations apply automatically
4. ✅ New clean data flows into your reports instantly

**Example Applied Steps for a typical cleanup:**

```c
1. Source (connect to file)
2. Remove Top Rows (remove header info)
3. Use First Row as Headers  
4. Change Data Types
5. Replace Errors (handle "N/A" values)
6. Add Custom Column (calculate categories)
7. Filter Rows (remove test data)
```

## What Power Query Editor CAN’T Do (Limitation) 🚫

**It’s NOT for:**

- Complex statistical analysis (use DAX measures instead)
- Real-time data streaming
- Creating visualizations (that’s for the main Power BI interface)
- Advanced machine learning (though it can handle simple predictive functions)

**It IS for:**

- Preparing and shaping your data
- Connecting to virtually any data source
- Automating repetitive data cleaning tasks
- Creating reusable data transformation processes

## Why This Matters for Your Power BI Success

**Before Power Query Editor:**

- Hours spent manually cleaning data each month
- Frustration with inconsistent data formats
- Errors creeping into reports from manual processes
- Repeating the same cleanup tasks over and over

**After Mastering Power Query Editor:**

- Automated data preparation that runs in minutes
- Consistent, reliable data feeding your reports
- Confidence that your data is clean and accurate
- More time for actual analysis and insights

## Quick Start Challenge 🎯

**Try this with your own data:**

1. Import any Excel file or CSV into Power BI Desktop
2. Click “Transform Data”
3. Make one simple change (like renaming a column)
4. Notice how it appears in Applied Steps
5. Click “Close & Apply”

**Congratulations!** 🎉 You’ve just completed your first Power Query transformation.

> **Want to practice these concepts with real data?** Let me know in the comments and I’ll share a sample Excel file with common transformation challenges!

## What’s Your Data Challenge? 🤔

Every dataset tells a story, but most need some translation first. Power Query Editor is your translator, turning messy real-world data into the clean, structured information your reports need.

**What data transformation challenge are you facing?** Share in the comments below — the Power BI community loves solving real problems together!

*🚀 Coming up next: We’ll take your clean, transformed data and create your first compelling visualizations. Get ready to see your data come to life!*

**Connect me on LinkedIn —** [**Janvi Gupta**](https://www.linkedin.com/in/janvisgupta/)

![](99.System/Attachments/0!sJflKWekqedcrxi3.webp)

👏🏻 Clap 🔎 [Follow](https://medium.com/@janvigupta1507) 📩 [Subscribe](https://medium.com/@janvigupta1507/subscribe) ✍🏻Comment

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----0822b52ffd8c---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Model

**Tags:** Tutorial, Data Model