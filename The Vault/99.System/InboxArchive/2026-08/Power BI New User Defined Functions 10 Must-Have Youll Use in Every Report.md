---
title: "⚡Power BI’s New User Defined Functions: 10 Must-Have You’ll Use in Every Report"
source: "https://medium.com/microsoft-power-bi/power-bis-new-user-defined-functions-10-must-have-you-ll-use-in-every-report-616523e70a65"
author:
  - "[[Isabelle Bittar]]"
published: 2025-09-24
created: 2026-08-02
description: "Fast, consistent DAX — packaged once, reused forever."
Processed: "Unprocessed"
---
## Fast, consistent DAX — packaged once, reused forever.

![](99.System/Attachments/1!RRbLou4_q9nzvVYWprSmbQ.png.webp)

By Isabelle Bittar for KI Data Science

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Introduction

Power BI recently introduced (in Preview) **DAX User-Defined Functions (UDFs)** — a way to package DAX logic once and call it anywhere, just like reusable helpers.

### Why they matter

- ♻️ **Reusability:** Write once, reuse across visuals, pages, and PBIX files.
- 🧭 **Consistency:** One source of truth for logic (time intelligence, colors, formats).
- 🚀 **Speed:** Fewer one-off measures → faster build, easier maintenance.

Here is a **short demo** on how they work:

They can be defined in Power BI Desktop using the DAX query view (DQV) or TMDL view. I personally prefer the DQV view and will show next how you can simply create one that lives in your model afterwards. For a deeper dive into syntax and current limitations, the official [**Microsoft documentation**](https://learn.microsoft.com/en-us/dax/best-practices/dax-user-defined-functions) is the best place to start.

[**Injae Park’s tutorial**](https://www.youtube.com/watch?v=kynJmgls6A4&list=PLrHF9RH5-_uuWyV0Ebr7MV_9Qj_4T5t9N&index=37) helped me get started in using them — I highly recommend watching it or any other Youtube tutorial when working for the first time with them 🤓.

### 🛠️ How to Use These UDFs

![](99.System/Attachments/1!GWvM_qQ2bNYfq7iE__ZOuw.png.webp)

How to Use These UDFs in Power BI’s DAX Query View

The sections that follow showcase **10 practical UDFs** that can be dropped directly into report! For each UDF, open the **DAX Query View** → paste a `DEFINE ... FUNCTION ...` block → **Update model with changes** → call the function from your measures. Anything marked `// 🔧 CONFIG` in this article is what you might adapt for your model (table/column names, thresholds, colors).

## 1\. Whole-Period Time Comparisons (YoY, QoQ, MoM, WoW, DoD)

![](99.System/Attachments/0!PbFWXaFzZAZKwYeG.png.webp)

A visualization I built in Using Time Periods as Slicers to Enhance Power BI Line or Area Charts’ Range. A reusable UDF like this would have made things much easier 😅

Reports often include some form of time comparison: year-over-year growth, quarter-over-quarter changes, month-over-month deltas, or even simple day-over-day checks. Here is how you can centralize these calculations in one UDF:

```c
DEFINE
    // Compare a base measure over the **whole prior period** relative to MAX visible date.
    // shift: "YOY"|"QoQ"|"MoM"|"WoW"|"DoD"
    // mode : "VALUE" (prior total), "DELTA", "PCT"
    FUNCTION CompareOverPeriodRange =
        ( base : AnyRef expr, shift : STRING, mode : STRING ) =>

        // 🔧 CONFIG: change to your Date table/column if different
        VAR _today  = MAX ( 'Date'[Date] )

        VAR _s      = UPPER ( shift )
        VAR _mode   = UPPER ( mode )

        // --- Current period boundaries (based on _today) ---
        VAR _curStart =
            SWITCH (
                TRUE(),
                _s = "YOY", DATE ( YEAR ( _today ), 1, 1 ),
                // Uses current quarter start via a 1-row date set around _today
                _s = "QOQ", STARTOFQUARTER ( DATESBETWEEN ( 'Date'[Date], _today, _today ) ),
                _s = "MOM", DATE ( YEAR ( _today ), MONTH ( _today ), 1 ),
                _s = "WOW", _today - 6,       // 7-day window ending today
                _s = "DOD", _today,           // single-day window (today)
                DATE ( YEAR ( _today ), MONTH ( _today ), 1 )
            )
        VAR _curEnd   = _today

        // --- Prior period boundaries ---
        VAR _priorStart =
            SWITCH (
                TRUE(),
                _s = "YOY", DATE ( YEAR ( _today ) - 1, 1, 1 ),
                _s = "QOQ", EDATE ( _curStart, -3 ),
                _s = "MOM", EDATE ( _curStart, -1 ),
                _s = "WOW", _curStart - 7,
                _s = "DOD", _today - 1,
                EDATE ( _curStart, -1 )
            )
        VAR _priorEnd =
            SWITCH (
                TRUE(),
                _s = "YOY", DATE ( YEAR ( _today ) - 1, 12, 31 ),
                _s = "QOQ", EOMONTH ( _priorStart, 2 ),   // 3-month span
                _s = "MOM", EOMONTH ( _priorStart, 0 ),
                _s = "WOW", _curEnd - 7,
                _s = "DOD", _today - 1,
                EOMONTH ( _priorStart, 0 )
            )

        VAR _currVal  = CALCULATE ( base, DATESBETWEEN ( 'Date'[Date], _curStart,  _curEnd  ) )
        VAR _priorVal = CALCULATE ( base, DATESBETWEEN ( 'Date'[Date], _priorStart, _priorEnd ) )
        VAR _delta    = _currVal - _priorVal
        VAR _pct      = IF ( NOT ISBLANK ( _priorVal ) && _priorVal <> 0, DIVIDE ( _delta, _priorVal ), BLANK () )

        RETURN
            SWITCH ( _mode,
                "VALUE", _priorVal,
                "DELTA", _delta,
                "PCT",   _pct,
                _pct   // default
            )
```

### 🛠️ How it works

- Anchors on the latest visible date (`MAX('Date'[Date])`).
- Defines the current period boundaries (month, quarter, year, etc.).
- Shifts those boundaries back to get the prior period.
- Calculates your measure in both contexts and returns either: prior value (`"VALUE"`), difference (`"DELTA"`), or percent change (`"PCT"`).

### ✅ Usage examples

Define a base measure:

```c
Total Sales = SUM ( Sales[SalesAmount] )

YoY Sales % (period) = CompareOverPeriodRange( [Total Sales], "YOY", "PCT" )
QoQ Sales Δ (period) = CompareOverPeriodRange( [Total Sales], "QoQ", "DELTA" )
MoM Sales (prior)    = CompareOverPeriodRange( [Total Sales], "MoM", "VALUE" )
```

Drop in any base measure (Revenue, Orders, Headcount, etc.) and reuse the same UDF.

## 2\. Variance & Status Colors (vs. Target or Prior Period)

![](99.System/Attachments/0!UjZBJ3ftM_3VkLiI.png.webp)

A visualization I built in Conditionally Color-Coding Line Charts in Power BI 📈

Whether you’re comparing actuals to a target **or** to the previous period’s results, you often need two things:

1. The variance (difference from reference).
2. A consistent color mapping (positive, negative, neutral).

Instead of duplicating this logic across cards and charts, you can centralize it with two UDFs.

```c
DEFINE
    // Variance between an actual and a reference (target or prior period)
    FUNCTION VarAbs =
        ( actual : NUMERIC, reference : NUMERIC ) =>
        actual - reference;

    // Status color based on variance thresholds
    // 🔧 CONFIG: adjust thresholds and color hex codes
    FUNCTION StatusColor =
        ( variance : NUMERIC, tolLow : NUMERIC, tolHigh : NUMERIC ) =>
        SWITCH (
            TRUE(),
            variance < tolLow,  "#E15759",  // red = underperformance
            variance > tolHigh, "#59A14F",  // green = exceeding
            "#BAB0AC"                       // gray = neutral
        )
```

### 🛠️ How it works

- `VarAbs` simply computes the gap between actual and reference. That reference can be a **target** (e.g., budget) or the **prior-period measure** (from `CompareOverPeriodRange`).
- `StatusColor` assigns a hex code depending on thresholds: negative → red, positive → green, in-between → gray.
- These outputs plug directly into KPI cards, charts, or tables via **conditional formatting by field value**.

### ✅ Usage examples

**Variance vs. Target:**

```c
Sales Variance = VarAbs( [Total Sales], [Sales Target] )
Sales Status Color = StatusColor( [Sales Variance], -5000, 5000 )
```

**Variance vs. Prior Period:**

```c
Sales Variance (MoM) =
    VarAbs( [Total Sales], CompareOverPeriodRange( [Total Sales], "MoM", "VALUE" ) )

Sales Status Color (MoM) =
    StatusColor( [Sales Variance (MoM)], -0.05 * [Total Sales], 0.05 * [Total Sales] )
```

This way, you can unify your **time comparisons** and **target tracking** under the same variance + color framework. Update thresholds or colors once, and all your visuals follow suit.

## 3\. Calendar Table (auto-columns + optional fiscal start)

![](99.System/Attachments/1!thdBWny5XFAC77quCWmp6g.png.webp)

Chandeep Chhabra showing how UDFs make Date tables cleaner — and easier to reuse.

I first came across [this idea](https://lnkd.in/p/ei9C6VhG) in a LinkedIn post by **Chandeep Chhabra**, who showed how UDFs can simplify messy Date table code into something clean and reusable. His example really highlighted the power of treating a Date table like a function you can drop into any model.

Building on that, here’s a slightly more configurable version — one that not only creates the standard columns (Year, Month, Quarter, etc.) but also adds fiscal support, “current” flags, and reusable keys. This way you can generate a consistent, ready-to-use Date table across projects with a single function call.

```c
DEFINE
    // Build a Date table between startDate and endDate with common columns
    // fiscalStartMonth: 1..12 (e.g., 7 = July)
    FUNCTION AutoDateTable =
        ( startDate : DATETIME, endDate : DATETIME, fiscalStartMonth : INT64 ) =>

        VAR dmin = DATE ( YEAR ( startDate ), MONTH ( startDate ), DAY ( startDate ) )
        VAR dmax = DATE ( YEAR ( endDate ),   MONTH ( endDate ),   DAY ( endDate ) )
        VAR base = CALENDAR ( dmin, dmax )

        // Shifted month for fiscal logic (1..12)
        VAR addCols =
            ADDCOLUMNS (
                base,
                "DateKey",       YEAR ( [Date] ) * 10000 + MONTH ( [Date] ) * 100 + DAY ( [Date] ),
                "Year",          YEAR ( [Date] ),
                "MonthNo",       MONTH ( [Date] ),
                "Month",         FORMAT ( [Date], "MMM" ),
                "Quarter",       "Q" & ROUNDUP ( MONTH ( [Date] ) / 3, 0 ),
                "StartOfMonth",  DATE ( YEAR ( [Date] ), MONTH ( [Date] ), 1 ),
                "EndOfMonth",    EOMONTH ( [Date], 0 ),
                "WeekNoMon",     WEEKNUM ( [Date], 2 ),                       // Monday-based weeks
                "YearMonth",     FORMAT ( [Date], "YYYY-MM" ),

                // ---- Fiscal helpers (shift by fiscalStartMonth) ----
                "FiscalYear",
                    YEAR ( [Date] ) + IF ( MONTH ( [Date] ) >= fiscalStartMonth, 1, 0 ),
                "FiscalMonthNo",
                    MOD ( MONTH ( [Date] ) - fiscalStartMonth + 12, 12 ) + 1,
                "FiscalQuarter",
                    "Q" & ROUNDUP ( ( MOD ( MONTH ( [Date] ) - fiscalStartMonth + 12, 12 ) + 1 ) / 3, 0 ),

                // Current flags
                "IsToday",       [Date] = TODAY (),
                "IsCurrentMonth", YEAR ( [Date] ) = YEAR ( TODAY () ) && MONTH ( [Date] ) = MONTH ( TODAY () )
            )
        RETURN addCols;
```

### 🛠️ How it works (quickly)

- Inputs define the date range and **fiscal start month** (e.g., 7 for July FY).
- Builds `CALENDAR(dmin,dmax)`, then adds **DateKey**, Year/Month/Quarter, **Month start/end**, **YearMonth**, **WeekNo (Mon)**, and **Fiscal** variants.
- Flags help with “Current Month” filters and indicators.

### ✅ Usage examples

**Standard (cap at end of max Sales month, FY starts in January):**

```c
Date =
AutoDateTable(
    DATE ( YEAR ( MIN ( Sales[Date] ) ) - 1, 1, 1 ),
    EOMONTH ( MAX ( Sales[Date] ), 0 ),
    1  // fiscalStartMonth
)
```

**Fiscal year starting in July (7):**

```c
Date =
AutoDateTable(
    DATE ( YEAR ( MIN ( Sales[Date] ) ) - 1, 1, 1 ),
    EOMONTH ( MAX ( Sales[Date] ), 0 ),
    7
)
```

After creating it: **Table tools → Mark as date table** → select `Date[Date]`.

### 💡 Why it’s handy

- One reusable UDF for **consistent Date tables** across PBIX files.
- Fiscal support built-in (no rework later).
- Includes the columns most reports end up adding anyway — so less model clutter, fewer ad-hoc calc columns.

## 4\. Rolling Window KPIs (last N days/weeks/months)

So many dashboards need “last 7 days,” “last 12 months,” or “last 4 quarters.” Instead of hand-coding each one, wrap the logic in a UDF that anchors on the **latest visible date** and uses `DATESINPERIOD` to build the window.

```c
DEFINE
    // Rolling total over the last N units ending at the max visible date.
    // unit: "DAY" | "WEEK" | "MONTH" | "QUARTER" | "YEAR"
    FUNCTION RollingTotal =
        ( base : AnyRef expr, n : INT64, unit : STRING ) =>
        VAR _u    = UPPER ( unit )
        // 🔧 CONFIG: change to your Date table/column if different
        VAR _end  = MAX ( 'Date'[Date] )
        VAR _span =
            SWITCH (
                TRUE(),
                _u IN { "DAY", "DAYS" },      DATESINPERIOD ( 'Date'[Date], _end, -n, DAY ),
                _u IN { "WEEK", "WEEKS" },    DATESINPERIOD ( 'Date'[Date], _end, -(7 * n), DAY ), // weeks via days
                _u IN { "MONTH", "MONTHS" },  DATESINPERIOD ( 'Date'[Date], _end, -n, MONTH ),
                _u IN { "QUARTER", "QUARTERS"},DATESINPERIOD ( 'Date'[Date], _end, -n, QUARTER ),
                _u IN { "YEAR", "YEARS" },    DATESINPERIOD ( 'Date'[Date], _end, -n, YEAR ),
                BLANK ()
            )
        RETURN
            IF ( ISBLANK ( _span ) || ISEMPTY ( _span ), BLANK (), CALCULATE ( base, _span ) );

    // Rolling average (per day/month/etc.) over the same window.
    FUNCTION RollingAverage =
        ( base : AnyRef expr, n : INT64, unit : STRING ) =>
        VAR _u    = UPPER ( unit )
        VAR _end  = MAX ( 'Date'[Date] )   // 🔧 CONFIG: Date table
        VAR _span =
            SWITCH (
                TRUE(),
                _u IN { "DAY", "DAYS" },      DATESINPERIOD ( 'Date'[Date], _end, -n, DAY ),
                _u IN { "WEEK", "WEEKS" },    DATESINPERIOD ( 'Date'[Date], _end, -(7 * n), DAY ),
                _u IN { "MONTH", "MONTHS" },  DATESINPERIOD ( 'Date'[Date], _end, -n, MONTH ),
                _u IN { "QUARTER", "QUARTERS"},DATESINPERIOD ( 'Date'[Date], _end, -n, QUARTER ),
                _u IN { "YEAR", "YEARS" },    DATESINPERIOD ( 'Date'[Date], _end, -n, YEAR ),
                BLANK ()
            )
        VAR _total = CALCULATE ( base, _span )
        VAR _denom =
            SWITCH (
                TRUE(),
                _u IN { "DAY", "DAYS", "WEEK", "WEEKS" },    DISTINCTCOUNT ( 'Date'[Date] ),
                _u IN { "MONTH", "MONTHS" },                 DISTINCTCOUNT ( 'Date'[Year] & "-" & 'Date'[MonthNo] ),
                _u IN { "QUARTER", "QUARTERS" },             DISTINCTCOUNT ( 'Date'[Year] & "-" & 'Date'[Quarter] ),
                _u IN { "YEAR", "YEARS" },                   DISTINCTCOUNT ( 'Date'[Year] )
            )
        RETURN DIVIDE ( _total, _denom )
```

✅ **Usage examples**

```c
Total Sales = SUM ( Sales[SalesAmount] )

// Rolling totals
Sales (30D)   = RollingTotal( [Total Sales], 30, "DAY" )
Sales (12M)   = RollingTotal( [Total Sales], 12, "MONTH" )
Sales (4Q)    = RollingTotal( [Total Sales], 4,  "QUARTER" )

// Rolling averages
Avg Daily Sales (7D)   = RollingAverage( [Total Sales], 7,  "DAY" )
Avg Monthly Sales (6M) = RollingAverage( [Total Sales], 6,  "MONTH" )
```

🛠️ **Notes**

- The window **ends at the latest date in context** (`MAX('Date'[Date])`). If your Date table extends past your facts, cap it at the data max (you already have a version of that Date table).
- Weeks are implemented as **7 × N days** since DAX doesn’t have a week unit for `DATESINPERIOD`. If you use ISO weeks, consider a Date column for `ISOYearWeek` and adapt the average denominator accordingly.
- Use these with your **CompareOverPeriod** UDFs: e.g., compare `Sales (30D)` vs prior 30D by calling `CompareOverPeriodRange` on a measure that references `RollingTotal`.

## 5\. Percentile Buckets (dynamic bins for any metric)

A quick way to show the **shape of a distribution** is to bucket values by percentiles (e.g., bottom 20%, next 20%, … top 20%) and plot a small bar/column visual of **count by bucket**. It’s great for risk amounts, response times, order values — anything that keeps changing as new data arrives. The UDFs below rebuild bucket boundaries **on the fly** (respecting your filter choices), so the bands and counts stay meaningful over time.

Paste into **DAX Query View → Update model with changes**. Anything marked `// 🔧` is where you may adapt names/behavior.

```c
DEFINE
    // ---------------------------------------------
    // Core: build percentile cutpoints for a measure
    // ---------------------------------------------
    // measureExpr : AnyRef expr (e.g., [Amount], [Duration])
    // wholeTable  : TABLE to evaluate over (use ALL(...) or ALLSELECTED(...))
    // q1..q4      : fraction cutpoints (0–1), e.g., 0.2, 0.4, 0.6, 0.8
    FUNCTION PercentileBoundsCustom =
        ( measureExpr : AnyRef expr,
          wholeTable  : TABLE,
          q1 : NUMERIC, q2 : NUMERIC, q3 : NUMERIC, q4 : NUMERIC ) =>

        VAR T   = wholeTable
        VAR vMin = CALCULATE( MINX( T, measureExpr ), T )
        VAR vMax = CALCULATE( MAXX( T, measureExpr ), T )
        VAR p1   = CALCULATE( PERCENTILEX.INC( T, measureExpr, q1 ), T )
        VAR p2   = CALCULATE( PERCENTILEX.INC( T, measureExpr, q2 ), T )
        VAR p3   = CALCULATE( PERCENTILEX.INC( T, measureExpr, q3 ), T )
        VAR p4   = CALCULATE( PERCENTILEX.INC( T, measureExpr, q4 ), T )
        RETURN ROW( "Min", vMin, "P1", p1, "P2", p2, "P3", p3, "P4", p4, "Max", vMax );

    // ---------------------------------------------
    // Map a value to a bucket index (0..5) + label
    // ---------------------------------------------
    // includeZeroBlank: TRUE => put blanks/zeros into a "No Value" bucket (index 0)
    FUNCTION BucketIndexFromBounds =
        ( value : NUMERIC,
          minV : NUMERIC, p1 : NUMERIC, p2 : NUMERIC, p3 : NUMERIC, p4 : NUMERIC, maxV : NUMERIC,
          includeZeroBlank : BOOL ) =>
        SWITCH(
            TRUE(),
            includeZeroBlank && ( ISBLANK(value) || value = 0 ), 0,
            value <= p1, 1,
            value <= p2, 2,
            value <= p3, 3,
            value <= p4, 4,
            5
        );

    FUNCTION BucketLabelFromBounds =
        ( value : NUMERIC,
          minV : NUMERIC, p1 : NUMERIC, p2 : NUMERIC, p3 : NUMERIC, p4 : NUMERIC, maxV : NUMERIC,
          includeZeroBlank : BOOL ) =>
        VAR band =
            BucketIndexFromBounds( value, minV, p1, p2, p3, p4, maxV, includeZeroBlank )
        VAR label =
            SWITCH(
                band,
                0, "No Value",
                1, FORMAT( minV, "#,##0" ) & " - " & FORMAT( p1, "#,##0" ),
                2, FORMAT( p1,   "#,##0" ) & " - " & FORMAT( p2, "#,##0" ),
                3, FORMAT( p2,   "#,##0" ) & " - " & FORMAT( p3, "#,##0" ),
                4, FORMAT( p3,   "#,##0" ) & " - " & FORMAT( p4, "#,##0" ),
                   FORMAT( p4,   "#,##0" ) & " - " & FORMAT( maxV, "#,##0" )
            )
        // prefix zero-width spaces so text sorts in bucket order without a separate column
        RETURN REPT( UNICHAR(8203), band + 1 ) & label;

    // ---------------------------------------------
    // Friendly wrapper (binds your table once)
    // ---------------------------------------------
    // 🔧 Change 'aggregate_risk' to your table; choose ALL or ALLSELECTED behavior
    FUNCTION QuantileBucketLabel =
        ( measureExpr : AnyRef expr,
          includeZeroBlank : BOOL,
          q1 : NUMERIC, q2 : NUMERIC, q3 : NUMERIC, q4 : NUMERIC ) =>
        VAR B =
            PercentileBoundsCustom(
                measureExpr,
                ALL( aggregate_risk ),      // or ALLSELECTED( aggregate_risk )
                q1, q2, q3, q4
            )
        RETURN
            BucketLabelFromBounds(
                measureExpr,
                B[Min], B[P1], B[P2], B[P3], B[P4], B[Max],
                includeZeroBlank
            );

    FUNCTION QuantileBucketIndex =
        ( measureExpr : AnyRef expr,
          includeZeroBlank : BOOL,
          q1 : NUMERIC, q2 : NUMERIC, q3 : NUMERIC, q4 : NUMERIC ) =>
        VAR B =
            PercentileBoundsCustom(
                measureExpr,
                ALL( aggregate_risk ),
                q1, q2, q3, q4
            )
        RETURN
            BucketIndexFromBounds(
                measureExpr,
                B[Min], B[P1], B[P2], B[P3], B[P4], B[Max],
                includeZeroBlank
            );
```

🛠️ **How it works**

- `PercentileBoundsCustom` computes **Min / P1 / P2 / P3 / P4 / Max** for any measure you pass. You choose the cutpoints (e.g., `0.2, 0.4, 0.6, 0.8` for quintiles).
- `BucketIndexFromBounds` maps each row to a band **0..5** (0 = optional “No Value”).
- `BucketLabelFromBounds` builds simple “a – b” labels (no unit abbreviations) and prefixes zero-width spaces so bucket text sorts in the right order.
- The **wrapper** binds your table once and is what you call from measures/columns.

✅ **Usage examples**

```c
// Example base measure
Amount = SUM( aggregate_risk[amount] )

// Label + sort index (quintiles)
Amount Bucket =
    QuantileBucketLabel( [Amount], TRUE, 0.2, 0.4, 0.6, 0.8 )

Amount Bucket Index =
    QuantileBucketIndex( [Amount], TRUE, 0.2, 0.4, 0.6, 0.8 )

// Visual: put Amount Bucket on rows, a count/amount on values.
// Sort the axis by Amount Bucket (or by Amount Bucket Index if you prefer an explicit sort).
Risk Count = COUNTROWS( aggregate_risk )
```

## 6\. Cool SVG Visualizations

![](99.System/Attachments/0!I4Y4MOEyMiC4vlve.png.webp)

Visualization I created for Step Up Your Power BI Game With SVGs 🔥

User-Defined Functions are also great for **standardizing SVG visuals** across models or different reports. You can wrap the SVG “template” in a UDF, pass in the few things that vary (values, colors, size), and you get visuals that are **consistent, reusable, and easy to tweak** from one place.

Below is a reusable **Gradient Sparkline** UDF that renders the last *N* days of any measure, chooses red/green styling based on performance, and outputs SVG that you can use in a table or matrix (like the Last 7 Days Sparkline I created in the picture above.

```c
DEFINE
    // SVG Gradient Sparkline for the last N days.
    // valueExpr: measure/expression returning the series value (e.g., [Current Price])
    // nDays: length of the window (e.g., 7)
    // pos/neg color sets: stroke + two gradient stops
    // width/height: SVG size
    FUNCTION SparklineSVG_LastNDays =
        ( valueExpr : AnyRef expr,
          nDays     : INT64,
          posStroke : STRING, posBg1 : STRING, posBg2 : STRING,
          negStroke : STRING, negBg1 : STRING, negBg2 : STRING,
          width     : NUMERIC, height : NUMERIC ) =>

        // 🔧 CONFIG: change to your date column
        VAR _maxDate = MAX ( 'Crypto Data'[timestamp] )
        VAR _minDate = _maxDate - ( nDays - 1 )

        // Window of dates to plot
        VAR _datesWin =
            CALCULATETABLE (
                VALUES ( 'Crypto Data'[timestamp] ),
                KEEPFILTERS (
                    'Crypto Data'[timestamp] >= _minDate &&
                    'Crypto Data'[timestamp] <= _maxDate
                )
            )

        // Evaluate series
        VAR _seriesRaw =
            ADDCOLUMNS ( _datesWin, "val", CALCULATE ( valueExpr ) )

        VAR _n    = COUNTROWS ( _seriesRaw )
        VAR _vMin = MINX ( _seriesRaw, [val] )
        VAR _vMax = MAXX ( _seriesRaw, [val] )
        VAR _den  = _vMax - _vMin
        VAR _midY = height / 2

        VAR _seriesXY =
            ADDCOLUMNS (
                _seriesRaw,
                "idx", RANKX ( _seriesRaw, 'Crypto Data'[timestamp], , ASC ),
                "x",   IF ( _n <= 1, 0, DIVIDE ( ( [idx] - 1 ) * width, _n - 1 ) ),
                "y",   IF ( _den = 0, _midY, height * ( 1 - DIVIDE ( [val] - _vMin, _den ) ) )
            )

        // Choose color set from first→last change in window
        VAR _firstVal = MINX ( TOPN ( 1, _seriesXY, 'Crypto Data'[timestamp], ASC  ), [val] )
        VAR _lastVal  = MAXX ( TOPN ( 1, _seriesXY, 'Crypto Data'[timestamp], DESC ), [val] )
        VAR _pctVar   = IF ( _firstVal = 0, BLANK (), DIVIDE ( _lastVal - _firstVal, _firstVal ) )

        VAR _stroke = IF ( _pctVar < 0, negStroke, posStroke )
        VAR _bg1    = IF ( _pctVar < 0, negBg1,    posBg1 )
        VAR _bg2    = IF ( _pctVar < 0, negBg2,    posBg2 )

        VAR _points =
            CONCATENATEX (
                _seriesXY,
                FORMAT ( [x], "0" ) & "," & FORMAT ( [y], "0" ),
                " ",
                'Crypto Data'[timestamp], ASC
            )

        RETURN
            "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 " & width & " " & height & "' width='" & width & "' height='" & height & "'>"
          & "<defs><linearGradient id='g' x1='0%' y1='0%' x2='0%' y2='100%'>"
          & "<stop offset='0%' style='stop-color:" & _bg1 & ";stop-opacity:1'/>"
          & "<stop offset='100%' style='stop-color:" & _bg2 & ";stop-opacity:0'/>"
          & "</linearGradient></defs>"
          & "<polyline fill='url(#g)' points='" & _points & " " & width & "," & height & " 0," & height & "'/>"
          & "<polyline fill='none' stroke='" & _stroke & "' stroke-width='1.5' points='" & _points & "'/>"
          & "</svg>";
```

✅ **Use it**

```c
// Example series
Current Price = AVERAGE ( 'Crypto Data'[price] )

// 7-day green↑ / red↓ sparkline
Sparkline (7D) =
    SparklineSVG_LastNDays(
        [Current Price], 7,
        "#2E7D32", "#A5D6A7", "#E8F5E9",   // positive: stroke, bg1, bg2
        "#C62828", "#FFCDD2", "#FFEBEE",   // negative: stroke, bg1, bg2
        70, 30                              // width, height
    )
```

**Display:** use this measure as a field with **Conditional formatting → Field value** (or as an Image URL/HTML-supported field depending on the visual).

## 7\. Humanize Numbers (K/M/B) + Dynamic Format

Short, consistent number abbreviations make dashboards easier to scan. Inspired by **Injae Park’s** excellent tutorial on UDFs, here’s a tiny helper that turns large values into **K/M/B** strings. Below I also show a **dynamic format string** so you keep the value numeric (best for sorting/aggregation) while displaying the short scale in visuals.

![](99.System/Attachments/1!ApaAbZHfBwrT0lWDsbFhHQ.png.webp)

Injae’s post is what nudged me to package this as a reusable UDF — worth checking out if you’re getting started with DAX UDFs.

```c
DEFINE
    // Humanize: return a short-scale string (K/M/B). Works for negatives & blanks.
    // Example: 1,234 -> "1.23K", 1,200,000 -> "1.2M"
    FUNCTION Humanize =
        ( x : NUMERIC ) =>
        VAR ax = ABS ( x )
        RETURN
            SWITCH (
                TRUE (),
                ISBLANK ( x ), BLANK (),
                ax >= 1000000000, FORMAT ( x / 1000000000, "0.##" ) & "B",
                ax >= 1000000,    FORMAT ( x / 1000000,    "0.##" ) & "M",
                ax >= 1000,       FORMAT ( x / 1000,       "0.##" ) & "K",
                FORMAT ( x, "#,0" )
            );

    // Optional: same idea but you control decimals (0..3 typical)
    FUNCTION HumanizeWithDecimals =
        ( x : NUMERIC, decimals : INT64 ) =>
        VAR ax   = ABS ( x )
        VAR fmt  = REPT ( "#", 0 ) & "0." & REPT ( "#", MIN ( 3, MAX ( 0, decimals ) ) )
        RETURN
            SWITCH (
                TRUE (),
                ISBLANK ( x ), BLANK (),
                ax >= 1e9, FORMAT ( x / 1e9, fmt ) & "B",
                ax >= 1e6, FORMAT ( x / 1e6, fmt ) & "M",
                ax >= 1e3, FORMAT ( x / 1e3, fmt ) & "K",
                FORMAT ( x, "#,0" )
            );
```

🛠️ **How it works**

- Checks the magnitude of the value and divides by **1K / 1M / 1B** as needed.
- Uses `FORMAT` with up to two (or configurable) decimals.
- Handles negatives (sign preserved) and blanks.

✅ **Usage examples**

```c
Total Sales = SUM ( Sales[SalesAmount] )

// As text (great for tooltips, cards, narrative text)
Total Sales (Humanized) = Humanize( [Total Sales] )

// With 1 decimal
Total Sales (Humanized 1dp) = HumanizeWithDecimals( [Total Sales], 1 )
```

**😎 Pro tip (dynamic format string):** Keep the measure numeric and switch only the **format**:

```c
VAR v = [Total Sales]
RETURN SWITCH( TRUE(),
  ABS(v)>=1e9, "0.##,,,'B'", ABS(v)>=1e6, "0.##,,'M'", ABS(v)>=1e3, "0.##,'K'", "#,0")
```

## 8\. Top-N Within Group

![](99.System/Attachments/1!kyZYkzVs4kGr2WBywjUJjA.png.webp)

From Learning Management Daeshbord by Shakil Mirja

Instead of writing a separate measure for every “Top X per Y,” use a UDF that ranks items **inside the current group context** and returns either a table of the top items or a rank you can filter on.

```c
DEFINE
    // Return a table of the Top N items *within the current group filter*.
    // items: TABLE (e.g., VALUES('Instructor'[Instructor]) or VALUES('Product'[Product]))
    // score: AnyRef expr (the measure to rank by, e.g., [Total Reviews], [Sales], [Avg Rating])
    // n: how many items to keep
    // order: "DESC" (highest first) or "ASC" (lowest first)
    FUNCTION TopNWithinCurrentGroup =
        ( items : TABLE, score : AnyRef expr, n : INT64, order : STRING ) =>
        VAR _ord = UPPER(order)
        VAR _withScore =
            ADDCOLUMNS( items, "__Score", CALCULATE( score ) )
        RETURN
            IF(
                _ord = "ASC",
                TOPN( n, _withScore, [__Score], ASC ),
                TOPN( n, _withScore, [__Score], DESC )
            );

    // Rank of the current item within the current group (1 = best by default)
    FUNCTION RankWithinCurrentGroup =
        ( items : TABLE, score : AnyRef expr, order : STRING ) =>
        VAR _ord = UPPER(order)
        VAR _withScore =
            ADDCOLUMNS( items, "__Score", CALCULATE( score ) )
        RETURN
            IF(
                _ord = "ASC",
                RANKX( _withScore, [__Score], , ASC, Dense ),
                RANKX( _withScore, [__Score], , DESC, Dense )
            );
```

🛠️ **How it works**

- You pass a **table of items** (usually `VALUES('Table'[Item])`).
- The UDF evaluates your **score measure** per item under the **current group filters** (e.g., current Category on a Matrix row).
- `TopNWithinCurrentGroup` returns only the top `n` rows; `RankWithinCurrentGroup` returns a rank you can filter on (`<= n`).

✅ **Usage examples**

**Scenario:** “Top 3 Instructors per Category,” ranked by **Total Reviews**.

```c
// Example score measure
Total Reviews = SUM ( 'Reviews'[ReviewCount] )

// Visual filter measure: keep only items that are in the Top 3 for the current Category
Is Top 3 Instructor =
VAR t =
    TopNWithinCurrentGroup(
        VALUES( 'Instructor'[Instructor] ),   // items
        [Total Reviews],                      // score
        3,                                    // n
        "DESC"                                // order
    )
RETURN IF(
    CONTAINS( t, 'Instructor'[Instructor], SELECTEDVALUE( 'Instructor'[Instructor] ) ),
    1
)KPI Narrative Text (auto-generated insights)
```
- Put **Category** on rows (or use a slicer), **Instructor** in a list/table, and add **Is Top 3 Instructor = 1** as a **visual filter**.
- Show `[Total Reviews]` and optionally a small **sparkline** or **star rating** measure per instructor.

## 9\. KPI Narrative Text

![](99.System/Attachments/0!n2xEK7Ddb0ZlzL79.png.webp)

Visualization I created in How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals

Adding **narrative text measures** to KPI cards that provide key highlights can take your KPI cards to the next level 🚀. With UDFs, you can standardize the logic so all your KPIs speak with the same “voice.”

For example, here’s a UDF that can produce a customizable **“biggest rise or drop highlight”** based on the context of your data, like the one created in the visualization above. It turns variance into a one-line insight (e.g., “🔺 Biggest rise in OT/FTE: ICU +12.6% — mainly on Evening (+7.4%)”) and reuse the same logic across KPIs. The core UDF controls **thresholds + wording**; tiny wrappers bind your **dimension** (e.g., Unit, Product) and optional **attribution** (e.g., Shift, Region).

```c
DEFINE
    // -------------------------------
    // Core narrative formatter (no columns here).
    // -------------------------------
    // varianceExpr : expression/measure that returns a % or numeric variance
    // shareCutoff  : e.g., 0.6 -> if the top contributor explains ≥60% of the rise, say "mainly on ..."
    // risePrefix   : e.g., "🔺 Biggest rise in {metric}: "
    // dropPrefix   : e.g., "🔻 Biggest drop in {metric}: "
    // metricName   : e.g., "OT/FTE" (used in the prefix)
    // dimLabelSing : e.g., "unit" (used when composing text)
    // attrLabelSing: e.g., "shift" (used when composing text)
    // mode         : "RISE" or "DROP"
    FUNCTION NarrativeTopChangeCore =
        ( varianceExpr : AnyRef expr,
          shareCutoff  : NUMERIC,
          risePrefix   : STRING,
          dropPrefix   : STRING,
          metricName   : STRING,
          dimLabelSing : STRING,
          attrLabelSing: STRING,
          mode         : STRING,
          // callbacks resolved by wrapper:
          dimAll  : TABLE,   // table of all dim members in current model context
          attrAll : TABLE,   // table of all attribution members (or an empty table)
          dimName : STRING,  // printable name of the dimension member (wrapper passes the text)
          attrName: STRING   // printable name of the attribution member
        ) =>

        VAR _mode = UPPER( mode )
        // pick the extreme variance across the dimension (max for rise, min for drop)
        VAR _extremeVar =
            SWITCH(
                _mode,
                "RISE", MAXX( dimAll, varianceExpr ),
                "DROP", MINX( dimAll, varianceExpr ),
                MAXX( dimAll, varianceExpr )
            )

        // dimension member that owns that extreme variance
        VAR _extremeDim =
            CALCULATE(
                FIRSTNONBLANK ( dimName, 1 ),
                FILTER( dimAll, varianceExpr = _extremeVar )
            )

        // Build attribution table (if provided) filtered by the chosen dimension
        VAR _attrTbl =
            ADDCOLUMNS(
                attrAll,
                "Var", CALCULATE( varianceExpr )
            )

        VAR _topAttrVar =
            IF( ISEMPTY( _attrTbl ), BLANK(), 
                SWITCH(
                    _mode,
                    "RISE", MAXX( _attrTbl, [Var] ),
                    "DROP", MINX( _attrTbl, [Var] ),
                    MAXX( _attrTbl, [Var] )
                )
            )

        VAR _topAttrName =
            IF( ISEMPTY( _attrTbl ), BLANK(),
                MAXX(
                    TOPN( 1, _attrTbl, [Var], IF( _mode = "DROP", ASC, DESC ) ),
                    attrName
                )
            )

        VAR _share = IF(
            OR( ISBLANK(_topAttrVar), _extremeVar = 0 ),
            BLANK(),
            DIVIDE( ABS( _topAttrVar ), ABS( _extremeVar ) )
        )

        VAR _prefix =
            SWITCH( _mode,
                "RISE", risePrefix,
                "DROP", dropPrefix,
                risePrefix
            )

        VAR _attrText =
            IF(
                ISEMPTY( _attrTbl ) || ISBLANK( _topAttrVar ),
                "",
                SWITCH(
                    TRUE(),
                    _mode = "RISE" && _topAttrVar > 0 && _share >= shareCutoff,
                        " — mainly on " & _topAttrName & " (" & FORMAT( _topAttrVar, "+0.0%" ) & ")",
                    _mode = "RISE" && _topAttrVar > 0 && _share <  shareCutoff,
                        " — spread across " & attrLabelSing & "s (top: " & _topAttrName & " " & FORMAT( _topAttrVar, "+0.0%" ) & ")",

                    _mode = "DROP" && _topAttrVar < 0 && _share >= shareCutoff,
                        " — mainly on " & _topAttrName & " (" & FORMAT( _topAttrVar, "+0.0%" ) & ")",
                    _mode = "DROP" && _topAttrVar < 0 && _share <  shareCutoff,
                        " — spread across " & attrLabelSing & "s (top: " & _topAttrName & " " & FORMAT( _topAttrVar, "+0.0%" ) & ")",

                    ""
                )
            )

        RETURN
            _prefix & metricName & ": "
            & _extremeDim & " " & FORMAT( _extremeVar, "+0.0%" )
            & _attrText;

    // -------------------------------------------------------
    // Wrapper EXAMPLE 1: Units (dimension) with Shift (attribution)
    // Bind your columns here. Keep the text flexible via parameters.
    // -------------------------------------------------------
    FUNCTION NarrativeTopChange_UnitShift =
        ( varianceExpr : AnyRef expr,
          shareCutoff  : NUMERIC,
          risePrefix   : STRING,
          dropPrefix   : STRING,
          metricName   : STRING,
          mode         : STRING
        ) =>

        // 🔧 BIND: Dimension table (must be the real column so filters propagate)
        VAR _dimAll   = ALL( Units[Unit] )
        VAR _dimName  = Units[Unit]

        // 🔧 BIND: Attribution table (optional)
        VAR _attrAll  = ALL( 'Scheduling Data'[Shift] )
        VAR _attrName = 'Scheduling Data'[Shift]

        RETURN
            NarrativeTopChangeCore(
                varianceExpr,
                shareCutoff,
                risePrefix, dropPrefix,
                metricName,
                "unit", "shift", mode,
                _dimAll, _attrAll, _dimName, _attrName
            );

    // -------------------------------------------------------
    // Wrapper EXAMPLE 2: Product with Region (or remove attr)
    // -------------------------------------------------------
    FUNCTION NarrativeTopChange_ProductRegion =
        ( varianceExpr : AnyRef expr,
          shareCutoff  : NUMERIC,
          risePrefix   : STRING,
          dropPrefix   : STRING,
          metricName   : STRING,
          mode         : STRING
        ) =>

        VAR _dimAll   = ALL( 'Product'[Product] )
        VAR _dimName  = 'Product'[Product]

        VAR _attrAll  = ALL( 'Region'[Region] )   // or use EMPTY to skip attribution
        VAR _attrName = 'Region'[Region]

        RETURN
            NarrativeTopChangeCore(
                varianceExpr,
                shareCutoff,
                risePrefix, dropPrefix,
                metricName,
                "product", "region", mode,
                _dimAll, _attrAll, _dimName, _attrName
            );
```

✅ **How to use:**

```c
// Your variance measure (example)
OT Hours per FTE Variance % =
DIVIDE( [OT Hours per FTE] - [OT Hours per FTE PrevWeek],
        [OT Hours per FTE PrevWeek] )

// Biggest rise (Unit → Shift)
Biggest Rise (Narrative) =
    NarrativeTopChange_UnitShift(
        [OT Hours per FTE Variance %],
        0.60,                                    // shareCutoff
        "🔺 Biggest rise in ",                   // risePrefix
        "🔻 Biggest drop in ",                   // dropPrefix (not used here)
        "OT/FTE",                                // metricName
        "RISE"                                   // mode
    )

// Biggest drop (Product → Region)
Biggest Drop (Narrative) =
    NarrativeTopChange_ProductRegion(
        [GM% Variance %],
        0.50,
        "🔺 Biggest rise in ",
        "🔻 Biggest drop in ",
        "Gross Margin %",
        "DROP"
    )
```

**Output examples**

- `🔺 Biggest rise in OT/FTE: ICU +12.6% — mainly on Evening (+7.4%)`
- `🔻 Biggest drop in Gross Margin %: Widgets −3.1% — spread across regions (top: West −1.4%)`

## 10\. Normalize Labels (Trim & Clean Pesky Spaces)

Data prep issues creep in everywhere — especially when dealing with text labels coming from multiple systems. A label that *looks* the same might actually have hidden characters: extra tabs, non-breaking spaces, or trailing whitespace. That’s enough to break a `LOOKUPVALUE`, create duplicate categories, or throw off groupings.

A simple **NormalizeLabel** UDF makes sure text fields are consistently trimmed and safe for joins or group-bys.

```c
DEFINE
    /// Normalize: trims whitespace and replaces common "invisible" characters.
    FUNCTION NormalizeLabel =
        ( s : STRING ) =>
            TRIM (
                SUBSTITUTE (
                    SUBSTITUTE ( s, UNICHAR (160), " " ),   // non-breaking space
                    UNICHAR (9), " "                        // tab
                )
            );
```

🛠️ **How it works**

- `TRIM` removes leading/trailing spaces.
- `SUBSTITUTE` swaps out common culprits:
- **UNICHAR(160)** = non-breaking space (common in copy/paste from Excel/HTML).
- **UNICHAR(9)** = tab character.
- You can extend this with more characters if your source systems have other oddities.

✅ **Usage examples**

```c
// Normalized category for grouping
Clean Category = NormalizeLabel( Sales[CategoryName] )

// Safe lookup (avoid mismatches caused by tabs/non-breaking spaces)
Region Code = LOOKUPVALUE(
    Regions[Code],
    Regions[Name], NormalizeLabel( Sales[RegionName] )
)
```

💡 **Why it’s handy**  
Instead of sprinkling `TRIM()` and `SUBSTITUTE()` all over your model, you keep a **single, reusable UDF**. Anytime you import a new dimension or need clean joins, you just wrap the column in `NormalizeLabel()` —one function call, consistent results.

## Conclusion

User-Defined Functions take the boilerplate out of Power BI: one place for time comparisons, rolling windows, buckets, colors, formats — then **call it everywhere**. The payoff is HUGE 😮: faster builds, fewer bugs, and a consistent look and feel across reports. Start with the simple wins (Normalize, Humanize, Calendar), move to patterns (Rolling, Buckets, Top-N), and finish with the “wow” layers (Narratives, SVG). Copy, paste, ship. 🚀

Have you started using UDFs? If so, please share your use cases, I’d love to hear about how your are using them 🤓!

**🎁** [**Here**](https://drive.google.com/file/d/1mz71uAEvZrvTgDJRe_iy5Pszm16TnV7T/view?usp=sharing) **is my PBIX from the demo to explore my UDF and measures yourself.**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

## Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

## Connect or Follow Me Here:

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

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----616523e70a65---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Any

**Category:** DAX, Data Model

**Tags:** Tutorial, DAX, Data Model