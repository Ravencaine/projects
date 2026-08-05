---
title: "Unlocking Python Inside Power BI: How I Solved the Cumulative Value Challenge (and What I Learned Along the Way)"
source: "https://medium.com/@markchen69/unlocking-python-inside-power-bi-how-i-solved-the-cumulative-value-challenge-and-what-i-learned-25c984e0a940"
author:
  - "[[Mark Chen]]"
published: 2026-05-21
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
*A practical guide on how to go beyond what Power Query alone can do*

I never thought I’d be writing a blog post about Python inside Power BI. I’m a BI person — I live in Power Query, DAX, and dashboards. Python felt like a different world entirely. (Well, not quite, I do write some Python code, but by far less frequently.)

But then I hit a wall. A simple-sounding requirement: **calculate cumulative revenue by version and business unit, from January to December**. What followed was one of the most satisfying learning journeys I’ve had in a while — and it opened a whole new window for solving data problems inside Power BI that I didn’t know existed.

Here’s everything I learned, mistakes included.

![](99.System/Attachments/1!hVA2TdwLpTUjlJzUNK0hQQ.png.webp)

## The Problem: Cumulative Values That Power Query Couldn’t Handle Efficiently

My data lived in a table called `StackedData` in Power Query. It had monthly revenue figures across multiple versions — Actual 2025, Actual 2026, F1 2026, Forecast 2027 — and I needed each version to accumulate month by month from January through December, also broken down by enterprise unit (`EU#`).

The naive Power Query approach uses `List.FirstN()` inside a custom column:

```c
List.Sum(
    List.FirstN(
        #"Added Index"[Value],
        [Index]
    )
)
```

It works. But it is **painfully slow**. The reason: it’s O(n²) — for every row, it re-reads the entire list from the beginning. On a moderately sized dataset, this can turn a seconds-long refresh into minutes of waiting.

I needed something better.

## The Solution: Python’s cumsum() — One Line, Instant Results

Python’s `pandas` library has a `cumsum()` function that calculates running totals in a single vectorized pass — O(n) complexity. It's orders of magnitude faster, and the syntax is elegant:

```c
import pandas as pd

dataset = dataset.sort_values(["Version", "EU#", "MonthNum"])
dataset["Cumulative Value"] = (
    dataset.groupby(["Version", "EU#"])["Value"]
    .cumsum()
)
```

That’s it. The `groupby(["Version", "EU#"])` ensures the cumulative sum **resets for every unique combination** of version and enterprise unit — exactly what we need for a drill-down visual. The `sort_values` guarantees months accumulate in the right order (January → December).

## How to Run Python Inside Power Query

Here’s the part that surprised me most: you can run Python scripts **directly inside Power Query**, without leaving Power BI at all.

## Steps:

1. Open **Power Query Editor** (Transform Data)
2. Select your source query (more on why this matters below)
3. Click **Transform → Run Python Script**
4. Paste your script — Power BI automatically passes your table as a variable called `dataset`
5. Click **OK**
6. An embedded table result appears — click the **expand icon** to flatten it back into columns
7. **Close & Apply**

Power BI treats `dataset` as a pandas DataFrame representing your current query table. No file imports, no external scripts — everything runs in-pipeline.

## Lesson 1: Python Scripts Only Work on Direct Queries — Not Referenced Ones

This was my first hard lesson.

My instinct was to create a separate `Cumulative` query that **referenced** `StackedData`, then run the Python script there — keeping my original table clean. Logical, right?

Wrong. Power BI threw this error:

> Formula.Firewall: Query ‘Cumulative’ (step ‘Run Python script’) references other queries or steps, so it may not directly access a data source. Please rebuild this data combination.

This is Power BI’s **Formula Firewall** — a privacy protection mechanism that prevents queries from combining data across different privacy contexts. When a Python script runs inside a referenced query, Power BI blocks it because it can’t guarantee data isolation.

**The fix:** Run the Python script directly inside your source query (`StackedData`), not in a reference table. Yes, it modifies the original table — but that's actually cleaner, since everything downstream automatically sees the new `Cumulative Value` column.

## Lesson 2: How to Install a Missing Python Library

After getting past the Firewall error, I hit a new one:

> ModuleNotFoundError: No module named ‘matplotlib’

Power BI was trying to import `matplotlib` as part of its Python wrapper — and it wasn't installed in my local Python environment.

**You cannot install Python libraries from inside Power BI.** Installation must happen outside, in your system’s terminal or command prompt.

## To install:

**Command Prompt (simplest):**

```c
pip install matplotlib pandas numpy
```

**If you have multiple Python versions:**

```c
python -m pip install matplotlib
```

**If using Anaconda:**

```c
conda install matplotlib pandas
```

## Critical: Make sure Power BI is using the right Python

If the error persists after installing, Power BI might be pointing to a *different* Python installation than the one you just updated.

1. Go to **File → Options → Python Scripting**
2. Note the Python home directory (e.g. `C:\Python311\`)
3. Install directly into that path:
```c
C:\Python311\Scripts\pip install matplotlib pandas
```

**Always restart Power BI Desktop after installing new packages.**

To verify installation:

```c
python -c "import matplotlib, pandas; print('All good!')"
```

## Lesson 3: Data Types Set in Python Don’t Carry Into Power Query

This one caught me off guard. I set explicit data types in my Python script thinking it would save a step:

```c
dataset["Cumulative Value"] = dataset["Cumulative Value"].astype(int)
dataset["Year"] = dataset["Year"].astype(int)
dataset["MonthNum"] = dataset["MonthNum"].astype(int)
dataset["Value"] = dataset["Value"].astype(int)
```

But after expanding the output in Power Query, **every column still showed as text** (the `ABC` icon). Power BI converts all Python output to text during the expansion step — regardless of what pandas types you set. The `astype()` calls simply don't carry over.

**The fix:** Set data types explicitly in a `Changed Type` step in Power Query after expanding. To do it efficiently in one step, use the Advanced Editor:

```c
#"Changed Type" = Table.TransformColumnTypes(
    #"Expanded Value",
    {
        {"Value", Int64.Type},
        {"Year", Int64.Type},
        {"MonthNum", Int64.Type},
        {"Cumulative Value", Int64.Type}
    }
)
```

This handles all columns at once — far better than clicking each one individually in the UI.

## The Final Power Query Script

Here’s what the end of the query looks like fully optimized:

```c
#"Run Python script" = Python.Execute(
    "import pandas as pd
    
     dataset = dataset.sort_values([""Version"", ""EU#"", ""MonthNum""])
     
     dataset[""Cumulative Value""] = (
         dataset.groupby([""Version"", ""EU#""])[""Value""]
         .cumsum()
     )",
    [dataset=Result]
),
#"Removed Columns" = Table.RemoveColumns(#"Run Python script", {"Name"}),
#"Expanded Value" = Table.ExpandTableColumn(
    #"Removed Columns",
    "Value",
    {"EU#", "Enterprise Unit", "Period", "Value",
     "Year", "MonthNum", "Month", "Version", "Cumulative Value"},
    {"EU#", "Enterprise Unit", "Period", "Value",
     "Year", "MonthNum", "Month", "Version", "Cumulative Value"}
),
#"Changed Type" = Table.TransformColumnTypes(
    #"Expanded Value",
    {
        {"Value", Int64.Type},
        {"Year", Int64.Type},
        {"MonthNum", Int64.Type},
        {"Cumulative Value", Int64.Type}
    }
)
in
    #"Changed Type"
```

## Key Takeaways

1. **Python** `**cumsum()**` **solves what Power Query's** `**List.FirstN**` **cannot do at scale** — O(n) vs O(n²) is a real-world difference you'll feel immediately on any reasonably sized dataset.
2. **Python scripts in Power Query only work on direct source queries** — referenced queries are blocked by the Formula Firewall. Run your script on the source table directly.
3. **Install Python libraries outside of Power BI** — use `pip install` in Command Prompt, and make sure you're installing into the same Python path that Power BI is configured to use.
4. **pandas data types don’t carry into Power Query** — always add a `Table.TransformColumnTypes` step after expanding Python output. Do it in one step via Advanced Editor for efficiency.

## Why This Matters for BI Developers

Power Query is outstanding for shaping, filtering, and transforming data. But it was never designed for iterative row-by-row calculations at scale. Python fills that gap perfectly — and now that I know it’s available right inside Power Query, I see it as a legitimate tool in my BI toolkit rather than something for “data scientists only.”

The learning curve had its bumps — the Firewall error, the missing library, the data type gotcha. But each obstacle taught me something concrete about how Power BI, Power Query, and Python interact under the hood.

If you’ve been hesitant to try Python inside Power BI, I hope this walkthrough gives you the confidence to start. It’s more accessible than it looks — and the payoff is real.

*Have you used Python inside Power Query? I’d love to hear what problems you’ve solved with it. Drop a comment below!*