---
title: "How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals"
source: "https://medium.com/microsoft-power-bi/how-to-build-dynamic-kpi-cards-in-power-bi-using-only-core-visuals-34f537595716"
author:
  - "[[Isabelle Bittar]]"
published: 2025-09-16
created: 2026-08-02
description: "Leverage core visuals and advanced DAX to deliver executive-ready insights"
Processed: "Unprocessed"
---
## Leverage core visuals and advanced DAX to deliver executive-ready insights

![](99.System/Attachments/1!DIytgGQNmmjoH7bMPYno4A.png.webp)

By Isabelle Bittar for KI Data Science

*🎁PBIX available for download at the end of this article!*

## Introduction

Lately I’ve been working on several healthcare projects. One executive dashboard I built focused on operational efficiency and resource optimization. It fitted on just a couple of report pages and relied on just a few KPI cards — like the one in the cover image — to surface **dynamic highlights**, with a small chart underneath to show **unit-level detail**. Users can click different highlights to pivot the chart to the relevant topic.

Here’s a short demo video to see the KPI card in action:

I built all of this with **Power BI core visuals**. The *Key Observations* section is powered by the **Button slicer** (the new slicer type) and a few **DAX measures** that (1) compute the latest 7-day metrics, (2) presents key insights, and (3) swap the chart measure based on the selected highlight. Because everything is DAX-driven, the card automatically responds to **data refreshes** and **slicers/filters** (e.g., Role).

Below is a summary of the key components of the KPI card:

### Anatomy of the KPI Card

![](99.System/Attachments/1!vkeJMtURiyjkyNM3Z5D_xg.png.webp)

Key Components of the KPI Card in Power BI

In the following article, I will take you through step-by-step on how I got this to work in Power BI. I will focus mostly on the Key Observations section since it’s the most complex part of the KPI card.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Step 1: The Data and Starting Point

The foundation of this project was the **“Scheduling Data”** table, which contained the key information about employee shifts, including:

- Date of the shift
- Shift type (Day, Evening, Night)
- Unit (e.g., ER, Pediatrics, ICU, etc.)
- Employee ID
- Role (Nurse, Doctor, Technician, etc.)
- Overtime hours worked

All of the measures powering the KPI card were calculated from this table.

![](99.System/Attachments/1!HJx1xxwiZ4fRgKMUgYLokA.png.webp)

📊 Scheduling Data Table Loaded in Power BI

To make the model more flexible and easier to work with, I created a few supporting **dimension tables**:

- A **Calendar table** linked on the `Date` field
- A **Shift table** for distinct shift types
- A **Units table** for department-level analysis

These relationships allowed me to slice and filter the KPI card by time period, unit, and role while keeping the measures consistent and reusable.

![](99.System/Attachments/1!KaEL51iJVW_lUkUsy1shIA.png.webp)

Data Model in Power BI

Once the model was in place, I was ready to move on to building the KPI card itself 🚀.

## Step 2: Designing the Top of the KPI Card

![](99.System/Attachments/1!51ZTfmTf1LgzBzico_2Uig.png.webp)

Top of the KPI Card in Power BI

The top of the KPI card was straightforward to build using Power BI’s **core visuals**.

### 1\. Layout and Context Elements

![](99.System/Attachments/1!rppcPCG8QsHSJlUw-EBXuQ.png.webp)

Setting Up the Layout and Context Elements of the KPI Card in Power BI

I first inserted a **rectangle shape** to serve as the background and assigned the KPI title to its text.  
I also added a **small icon image** reflecting the KPI card’s theme, and I included a **slicer** based on the **Role** field from the `Scheduling Data` table so that users could view metrics by staff role.

### 2\. Main KPI: OT Hours per FTE (This Week)

![](99.System/Attachments/1!IjKdclaaCJaAtmXYO6sX-w.png.webp)

Adding the Main Indicator to the KPI Card in Power BI

Next, I used the **card visual** to display overtime hours per FTE for the current week. This was powered by a set of DAX measures built step by step, using the last one **OT Hours per FTE This Week** and renaming it **Since Last Week** in the card’s data field:

```c
OT Hours = SUM('Scheduling Data'[OvertimeHours])

Employee Count = DISTINCTCOUNT('Scheduling Data'[EmployeeID])

OT Hours per FTE = 
    DIVIDE(
        [OT Hours],
        [Employee Count]
    )

Max Date = MAX('Scheduling Data'[Date])

Max Date - 7 = [Max Date] - 7 

OT Hours per FTE This Week = 
VAR _MaxDate = [Max Date]
VAR _MinDate = [Max Date - 7]
VAR _OTHoursperFTE = 
    CALCULATE(
        [OT Hours per FTE],
        FILTER(
            'Scheduling Data',
            'Scheduling Data'[Date] <= _MaxDate &&
            'Scheduling Data'[Date] > _MinDate
        )
    )
RETURN _OTHoursperFTE
```

This measure allowed the card to always show the **most recent 7 days** based on the latest available date in the dataset.

### 3\. Trend Visualization: Week-over-Week Variance

![](99.System/Attachments/1!tpaOhl3mz-_w4tIJnSpjLA.png.webp)

Integrating the Trend Visualization to the KPI Card in Power BI

To provide context, I added a **line chart with a small KPI card** to show the week-over-week variation. This required a second set of measures:

```c
Max Date - 14 = [Max Date] - 14

OT Hours per FTE Last Week = 
VAR _MaxDate = [Max Date - 7]
VAR _MinDate = [Max Date - 14]
VAR _OTHoursperFTE = 
    CALCULATE(
        [OT Hours per FTE],
        FILTER(
            'Scheduling Data',
            'Scheduling Data'[Date] <= _MaxDate &&
            'Scheduling Data'[Date] > _MinDate
        )
    )
RETURN _OTHoursperFTE 

OT Hours per FTE Variance = [OT Hours per FTE This Week] - [OT Hours per FTE Last Week]

OT Hours per FTE Variance % = 
    DIVIDE(
        [OT Hours per FTE Variance],
        [OT Hours per FTE Last Week]
    )
```

With these measures in place, the line chart clearly highlighted **weekly trends** in overtime per FTE, while the card quantified the **variance percentage**.

👉 For conditional formatting, I applied **green for decreases** and **red for increases** in OT hours. If you’d like to see exactly how I built that logic, I covered it in detail in this article:

## [Conditionally Color-Coding Line Charts in Power BI 📈](https://medium.com/the-bi-corner/conditionally-color-coding-line-charts-in-power-bi-3978fd93a2cc?source=post_page-----34f537595716---------------------------------------)

### Step-by-step walkthrough (PBIX included!)

medium.com

Once the top of the KPI card was developed, I was ready to move on to develop the **highlights** that would be integrated under the **Key Observations** section.

## Step 3: Integrating the Highlights in the Key Observations Section

![](99.System/Attachments/1!adgsnBZWh2cOg1GvRe405g.png.webp)

Integrating the Highlights in the Key Observations Section to the KPI Card in Power BI

To make the KPI card actionable, I wanted to surface **key highlights** that would automatically adapt to new data or applied slicers. For this, I used Power BI’s **button slicer** combined with a simple helper table and a set of DAX measures.

### 1\. The Highlights Table

I started by creating a small table in **Power Query** called `Highlights`, which simply listed values from 1 to 4. This table remained **unconnected in the data model**, serving only as a driver for the button slicer.

![](99.System/Attachments/1!yg4g5RKKxGdvBpH2i2uucw.png.webp)

Highlights Table in Power BI

This way, I could use the “Order” field from this table to assign each highlight dynamically.

### 2\. The Four Key Highlights

I then developed four DAX measures, each designed to provide one specific type of operational insight:

### 🔹 High OT Flag Highlight

This measure counted the **number of employees who exceeded a fixed overtime threshold** (e.g., 10 hours in a week). It provided executives with a quick sense of staff potentially at risk of burnout.

```c
High OT Flag Hours = 10

High OT Employees (Last 7 Days) = 
VAR _MaxDate   = [Max Date]
VAR _MinDate   = [Max Date - 7]
VAR Threshold =
    COALESCE ( [High OT Flag Hours], 10 )

RETURN
COUNTROWS (
    FILTER (
        ADDCOLUMNS (
            SUMMARIZE (
                FILTER (
                    'Scheduling Data',
                    'Scheduling Data'[Date] > _MinDate
                        && 'Scheduling Data'[Date] <= _MaxDate
                ),
                'Scheduling Data'[EmployeeID]            -- one row per employee
            ),
            "OT7",
                CALCULATE (
                    SUM ( 'Scheduling Data'[OvertimeHours] ),
                    'Scheduling Data'[Date] >= _MinDate,
                    'Scheduling Data'[Date] <= _MaxDate
                )
        ),
        [OT7] > Threshold
    )
)

High OT Flag Highlight = "👥 " & [High OT Employees (Last 7 Days)] & " employees >" & [High OT Flag Hours] & "h OT this week"
```

### 🔹 Biggest Rise Highlight

This one identified the **unit with the largest week-over-week rise in OT hours per FTE**, with extra detail on whether the increase was concentrated in a single shift or spread across multiple. It helped spot **emerging problem areas** before they escalated.

```c
Biggest Rise Highlight = 
VAR _MaxVariance =
    MAXX (
        ALL ( Units[Unit] ),
        [OT Hours per FTE Variance %]
    )

VAR _MaxUnit =
    CALCULATE (
        FIRSTNONBLANK ( Units[Unit], 1 ),
        FILTER ( ALL ( Units[Unit] ), [OT Hours per FTE Variance %] = _MaxVariance )
    )

-- Build variance by Shift for the identified Unit
VAR _ShiftVarTbl =
    ADDCOLUMNS (
        ALL ( 'Scheduling Data'[Shift] ),                  -- examine all shifts regardless of page filters
        "VarPct",
            CALCULATE (
                [OT Hours per FTE Variance %],
                KEEPFILTERS ( Units[Unit] = _MaxUnit )     -- lock to the chosen Unit
            )
    )

VAR _TopShiftVar =
    MAXX ( _ShiftVarTbl, [VarPct] )

VAR _TopShiftName =
    MAXX ( TOPN ( 1, _ShiftVarTbl, [VarPct], DESC ), 'Scheduling Data'[Shift] )

-- How much of the unit's rise is attributable to the top shift?
VAR _ShiftShare =
    DIVIDE ( _TopShiftVar, _MaxVariance )

-- Text fragment for shift attribution:
--   - If the top shift is positive and explains at least 60% of the rise, call it out
--   - If positive but <60%, say it's spread across shifts
--   - If not positive, omit shift detail
VAR _ShiftDetail =
    SWITCH (
        TRUE(),
        NOT ISBLANK ( _TopShiftVar ) && _TopShiftVar > 0 && _ShiftShare >= 0.6,
            " — mainly on " & _TopShiftName & " (" & FORMAT ( _TopShiftVar, "+0.0%" ) & ")",
        NOT ISBLANK ( _TopShiftVar ) && _TopShiftVar > 0 && _ShiftShare < 0.6,
            " — spread across shifts (top: " & _TopShiftName & " " & FORMAT ( _TopShiftVar, "+0.0%" ) & ")",
        ""
    )

RETURN
"🔺 Biggest rise in OT/FTE: "
& _MaxUnit & " " & FORMAT ( _MaxVariance, "+0.0%" )
& _ShiftDetail
```

### 🔹 Top Unit Highlight

Here, I calculated which unit had the **highest total OT hours** in the latest week, and broke it down by shift contribution. This gave leaders a clear view of **where overtime was being driven most heavily**.

```c
OT Hours This Week = 
VAR _MaxDate = [Max Date]
VAR _MinDate = [Max Date - 7]
VAR _OTHours = 
    CALCULATE(
        [OT Hours],
        FILTER(
            'Scheduling Data',
            'Scheduling Data'[Date] <= _MaxDate &&
            'Scheduling Data'[Date] > _MinDate
        )
    )
RETURN _OTHours

Top Unit Highlight = 
VAR _MaxOT =
    MAXX (
        ALL ( Units ),
        [OT Hours This Week]
    )
VAR _MaxUnit =
    CALCULATE (
        FIRSTNONBLANK ( Units[Unit], 1 ),
        FILTER ( ALL ( Units[Unit] ), [OT Hours This Week] = _MaxOT )
    )

-- Per-shift OT for the selected top unit (hospital-wide scope across shifts)
VAR _ShiftOTTbl =
    ADDCOLUMNS (
        ALL ( 'Scheduling Data'[Shift] ),
        "OT_Hours",
            CALCULATE (
                [OT Hours This Week],
                KEEPFILTERS ( Units[Unit] = _MaxUnit )
            )
    )
VAR _TopShiftOT   = MAXX ( _ShiftOTTbl, [OT_Hours] )
VAR _TopShiftName = MAXX ( TOPN ( 1, _ShiftOTTbl, [OT_Hours], DESC ), 'Scheduling Data'[Shift] )
VAR _ShiftShare   = DIVIDE ( _TopShiftOT, _MaxOT )

-- Shift attribution text
VAR _ShiftDetail =
    SWITCH (
        TRUE(),
        NOT ISBLANK ( _TopShiftOT ) && _TopShiftOT > 0 && _ShiftShare >= 0.6,
            " — mainly on " & _TopShiftName & " (" & FORMAT ( _TopShiftOT, "#,##0" ) & "h)",
        NOT ISBLANK ( _TopShiftOT ) && _TopShiftOT > 0 && _ShiftShare < 0.6,
            " — spread across shifts (top: " & _TopShiftName & " " & FORMAT ( _TopShiftOT, "#,##0" ) & "h)",
        ""
    )

RETURN
IF (
    ISBLANK ( _MaxOT ),
    BLANK(),
    "🏥 Top unit: " & _MaxUnit & " with " & FORMAT ( _MaxOT, "#,##0" ) & "h" & _ShiftDetail
)
```

### 🔹 Lowest Fill Rate Highlight

Finally, I built a measure to find the **unit with the lowest filled-shift percentage**. It also pointed out which shift contributed most to the staffing gap. This was critical to track **resource allocation issues** that directly impacted patient care.

```c
Lowest Fill Rate Highlight = 
VAR _lastDate  = [Max Date]
VAR _weekStart = [Max Date - 7]

-- Fill rate per unit in the window (respects current page filters except date)
VAR _UnitFill =
    ADDCOLUMNS (
        SUMMARIZE ( VALUES ( 'Scheduling Data'[Unit] ), 'Scheduling Data'[Unit] ),
        "FillRate",
            CALCULATE (
                DIVIDE ( SUM ( 'Scheduling Data'[Filled] ), SUM ( 'Scheduling Data'[Scheduled] ) ),
                'Scheduling Data'[Date] > _weekStart,
                'Scheduling Data'[Date] <= _lastDate
            )
    )

VAR _lowestRate = MINX ( _UnitFill, [FillRate] )
VAR _dept       = MAXX ( TOPN ( 1, _UnitFill, [FillRate], ASC ), [Unit] )

-- Shift-level attribution for the identified unit (look across ALL shifts)
VAR _ShiftFillTbl =
    ADDCOLUMNS (
        ALL ( 'Scheduling Data'[Shift] ),
        "Sched",
            CALCULATE (
                SUM ( 'Scheduling Data'[Scheduled] ),
                KEEPFILTERS ( 'Scheduling Data'[Unit] = _dept ),
                'Scheduling Data'[Date] > _weekStart,
                'Scheduling Data'[Date] <= _lastDate
            ),
        "Filled",
            CALCULATE (
                SUM ( 'Scheduling Data'[Filled] ),
                KEEPFILTERS ( 'Scheduling Data'[Unit] = _dept ),
                'Scheduling Data'[Date] > _weekStart,
                'Scheduling Data'[Date] <= _lastDate
            )
    )
VAR _ShiftFillTbl2 =
    ADDCOLUMNS (
        _ShiftFillTbl,
        "Unfilled", MAX ( 0, [Sched] - [Filled] ),
        "FillRateShift", DIVIDE ( [Filled], [Sched] )
    )

VAR _UnitUnfilledTotal = SUMX ( _ShiftFillTbl2, [Unfilled] )
VAR _TopShiftUnf       = MAXX ( _ShiftFillTbl2, [Unfilled] )
VAR _TopShiftName      = MAXX ( TOPN ( 1, _ShiftFillTbl2, [Unfilled], DESC ), 'Scheduling Data'[Shift] )
VAR _TopShiftRate      = MAXX ( FILTER ( _ShiftFillTbl2, 'Scheduling Data'[Shift] = _TopShiftName ), [FillRateShift] )
VAR _Share             = DIVIDE ( _TopShiftUnf, _UnitUnfilledTotal )

-- Shift attribution text:
--  - If one shift accounts for >=60% of unfilled slots, call it “mainly on …”
--  - Else, say it’s spread, but show the lowest-fill shift with its rate and unfilled count
VAR _ShiftDetail =
    SWITCH (
        TRUE(),
        _UnitUnfilledTotal > 0 && _Share >= 0.6,
            " — mainly on " & _TopShiftName
            & " (fill " & FORMAT ( _TopShiftRate, "0.0%" ) & ", "
            & FORMAT ( _TopShiftUnf, "#,##0" ) & " unfilled)",
        _UnitUnfilledTotal > 0 && _Share < 0.6,
            " — spread across shifts (lowest: " & _TopShiftName
            & " " & FORMAT ( _TopShiftRate, "0.0%" ) & ", "
            & FORMAT ( _TopShiftUnf, "#,##0" ) & " unfilled)",
        ""
    )

RETURN
IF (
    ISBLANK ( _lowestRate ),
    BLANK(),
    "⚠️ Lowest filled rate: "
        & FORMAT ( _lowestRate, "0.0%" )
        & " in " & _dept
        & _ShiftDetail
)
```

### 3\. The Highlight Headers Switch

Once these measures were in place, I tied them together with a single `Highlight Headers` measure. This SWITCH statement mapped the “Order” from the Highlights table to the right text:

```c
Highlight Headers = 
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, [High OT Flag Highlight],
        2, [Biggest Rise Highlight],
        3, [Top Unit Highlight],
        4, [Lowest Fill Rate Highlight]
    )
```

### 4\. Adding the Highlights to the KPI Card

I then added a **button slicer** to the report, binding it to the `Highlights[Order]` field.

- For the **Callout value label**, I assigned the `Highlight Headers` measure so that each button dynamically displayed the text of one of the four insights.
![](99.System/Attachments/1!N8FGpbKwbjfOtEToLGHlHw.png.webp)

Adding the Highlight Headers Measure to the Button Slicer’s Label

- I formatted the slicer in a **vertical list layout** with four rows, hid the values, and used **conditional formatting** to style the borders, fill, and hover effects.
- Finally, I changed the slicer title to **“Key Observations”**.
![](99.System/Attachments/1!NGitEPh6jH7oWc2T3b8A-w.png.webp)

Formatting the Button Slicer in Power BI

At this point, the KPI card dynamically displayed whichever highlight was selected, and I was ready to connect it to the detailed chart below.

## Step 4: Linking the Highlights to a Dynamic Chart

![](99.System/Attachments/1!TDiF3FwZlkzvSPWOV5iYhg.png.webp)

Integrating the Dynamic Chart Linked to the Selected Highlight

The heart of the Key Observations section was making sure the **chart updated dynamically** based on the highlight selected. To achieve this, I first created a set of measures that handled the **values, colors, titles, and subtitles**.

### 1\. Column Value (dynamic metric)

This measure determined which metric should be displayed in the clustered column chart, depending on the highlight chosen:

```c
Column Value = 
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, [High OT Employees (Last 7 Days)],
        2, [OT Hours per FTE Variance %],
        3, [OT Hours This Week],
        4, [Filled Rate % This Week]
    )
```

### 2\. Column Color (conditional formatting)

To guide interpretation, I applied **conditional formatting** so that the columns’ colors reflected risk or opportunity. For example, units with the highest OT hours or lowest fill rate stood out in red, while other values remained neutral.

```c
Column Color = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE(Highlights[Order]) = 1 
            && [High OT Employees (Last 7 Days)] = [Most Employees Flagged for High OT per Unit], [_Color Red],

        SELECTEDVALUE(Highlights[Order]) = 2 
            && [OT Hours per FTE Variance %] <= 0, [_Color Green],
        SELECTEDVALUE(Highlights[Order]) = 2 
            && [OT Hours per FTE Variance %], [_Color Red],

        SELECTEDVALUE(Highlights[Order]) = 3 
            && [OT Hours This Week] = [Highest OT Hours per Unit], [_Color Red],

        SELECTEDVALUE(Highlights[Order]) = 4 
            && [Filled Rate % This Week] = [Lowest Fill Rate], [_Color Red],

        [_Color Medium Blue]
    )
```

👉 The **color measures** stored the color codes. In my PBIX file (linked at the end of the article), I grouped these measures under the folder *\_Constants/Colors*.

### 3\. Chart Titles and Subtitles

To make the visuals more readable, I used two extra measures to **dynamically generate the title and subtitle**:

```c
Graph Title = 
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, "Employees with >10h of OT This Week",
        2, "Variation of OT Hours per FTE Since Last Week",
        3, "OT Hours This Week",
        4, "Shift Fill Rate by Department"
    )

Graph Subtitle = 
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, [High OT Flag Highlight Subtitle],
        2, [Biggest Rise Highlight Subtitle],
        3, [Top Unit Highlight Subtitle],
        4, [Lowest Fill Rate Highlight Subtitle]
    )
```

👉 The **subtitle measures** were designed to mirror the text logic of the main Highlight measures, but with added detail. In my PBIX file, I grouped these measures under the folder *Graph/Subtitles*.

### 4\. Setting Up the Visual

Once the measures were ready, the clustered column chart itself was simple:

![](99.System/Attachments/1!sT6TgRMFTYF6McOb59jzNA.png.webp)

Building the Clustered Column Chart in Power BI

- **Axis:** `'Scheduling Data'[Unit]`
- **Values:** `Column Value`
- **Conditional Formatting (Data Colors):** `Column Color`
- **Title & Subtitle:** bound to the `Graph Title` and `Graph Subtitle` measures

This ensured that whenever a user clicked a different highlight in the button slicer, the chart automatically shifted to display the right metric, in the right color, with the right contextual narrative.

![](99.System/Attachments/1!CGv-RVInSj3Xsku0aPCxkg.png.webp)

KPI Cards with the Dynamic Chart Integrated in Power BI

I wrapped things up by applying a few final formatting touches to refine the overall look and feel of the chart. To make the experience even more interactive, I also integrated a **custom tooltip**, allowing users to hover over any column and instantly view the underlying details by shift.

![](99.System/Attachments/1!qrgZGnK8Oot9IW76v8GGKg.png.webp)

Adding a Custom Tooltip to the Chart in Power BI

## Conclusion

What I like most about this approach is how **simple it actually was to build**. The KPI cards and the Key Observations section look polished and dynamic, yet everything was done using **Power BI’s core visuals**. The only “advanced” part was writing the DAX measures to calculate metrics, highlight insights, and control the formatting logic.

Because the logic was DAX-driven, the highlights and charts automatically adapted to refreshed data and applied filters. This meant that once it was set up, it stayed relevant without constant manual adjustments.

### Lessons Learned

- **Keep it simple, but smart**: Core visuals can go a long way if paired with dynamic measures.
- **Use helper tables strategically**: An unconnected Highlights table allowed me to control multiple visuals from a single button slicer.
- **Narrative matters**: Subtitles and tooltips didn’t just add context — they gave **cues to users on how to interpret the results and where to look next** in the dashboard for more detail.
- **Design for interaction**: By letting users switch highlights and hover for shift-level details, the dashboard became both compact and insightful.

This technique can easily be adapted beyond healthcare projects — any time you want to present **dynamic KPIs and context-rich highlights** in a compact format.

**🎁 Don’t forget, you can download the PBIX** [**here**](https://drive.google.com/file/d/1TfRB5Z9fOr5jly3cmNu2YNuvPlL0nXFs/view?usp=sharing) **and explore all the measures yourself.**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)

👏🏻 Clap 🔎 [Follow](https://isabittar.medium.com/) 📩 [Subscribe](https://isabittar.medium.com/subscribe) ✍🏻Comment

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----34f537595716---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Visualization

**Tags:** Guide, Data Visualization