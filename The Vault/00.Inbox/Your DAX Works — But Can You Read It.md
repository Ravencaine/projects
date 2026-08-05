---
title: "Your DAX Works — But Can You Read It?"
source: "https://medium.com/@arhamislam808/your-dax-works-but-can-you-read-it-93caf8ee5b21"
author:
  - "[[Mohd Arham Islam]]"
published: 2025-12-20
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!W9qskrtT2l1ctZ9QRLQQlQ.png.webp)

As DAX measures grow, formatting stops being cosmetic and starts being **functional**. Poorly formatted DAX hides logic, makes bugs harder to spot, and increases the mental load every time you revisit the code. In this tutorial, we’ll go through seven real-world DAX measures in increasing complexity and see how **proper formatting transforms readability, debuggability, and confidence**.

## Nested IF Conditions

❌ Poorly Formatted

```c
Usage Status =
VAR d1 = MAX('DateDim'[Date])
VAR d2 = MAX(FactData[EventDate])
VAR lag = DATEDIFF(d2, d1, DAY)
RETURN IF(lag <= 7, "Optimal",IF(lag <= 21, "Needs Monitoring", "Under-utilized"))
```

✅ Properly Formatted

```c
Usage Status =
VAR maxCalendarDate =
    MAX ( 'DateDim'[Date] )

VAR maxUnitDate =
    MAX ( FactData[EventDate] )

VAR daysLag =
    DATEDIFF ( maxUnitDate, maxCalendarDate, DAY )

RETURN
IF (
    daysLag <= 7,
    "Optimal",
    IF (
        daysLag <= 21,
        "Needs Monitoring",
        "Under-utilized"
    )
)
```

Business logic reads like plain English, making validation easier.

## Filtering with Multiple Context Dependencies

❌ Poorly Formatted

```c
Avg Touchpoints =
VAR m = VALUES(FactData[Month])
VAR c = VALUES(FactData[Unit])
VAR t = FILTER(Activity,Activity[MonthKey] IN m && Activity[Unit] IN c)
RETURN AVERAGEX(t, Activity[Avg Value])
```

✅ Properly Formatted

```c
Avg Touchpoints =
VAR selectedMonths =
    VALUES ( FactData[Month] )

VAR selectedUnits =
    VALUES ( FactData[Unit] )

VAR filteredTable =
    FILTER (
        Activity,
        Activity[MonthKey] IN selectedMonths
        && Activity[Unit] IN selectedUnits
    )

RETURN
AVERAGEX (
    filteredTable,
    Activity[Avg Value]
)
```

Logical conditions become readable and easier to extend without breaking context.

## Iterators with Nested CALCULATE

❌ Poorly Formatted

```c
Capacity =
SUMX(VALUES(FactData[Unit]),CALCULATE(ROUNDDOWN(DIVIDE([Max Metric], [Avg Touchpoints]), 0)))
```

✅ Properly Formatted

```c
Capacity =
SUMX (
    VALUES ( FactData[Unit] ),
    CALCULATE (
        ROUNDDOWN (
            DIVIDE ( [Max Metric], [Avg Touchpoints] ),
            0
        )
    )
)
```

Nested logic is visually decomposed, reducing mistakes in iterator-heavy measures.

## Display Logic with Multiple Conditions

❌ Poorly Formatted

```c
Session Label =
VAR n = [Total Sessions]
VAR t = CALCULATE([Total Sessions], ALLSELECTED())
VAR p = DIVIDE(n, t)
RETURN IF(ISINSCOPE(FactData[Hour]) && ISINSCOPE('DateDim'[Day]) && n <> BLANK(), FORMAT(n, "#,##0"), IF(NOT ISBLANK(n), FORMAT(n, "#,##0") & " (" & FORMAT(p, "0.0%") & ")"))
```

✅ Properly Formatted

```c
Session Label =
VAR sessionCount =
    [Total Sessions]

VAR totalSessions =
    CALCULATE (
        [Total Sessions],
        ALLSELECTED ()
    )

VAR pctShare =
    DIVIDE ( sessionCount, totalSessions )

RETURN
IF (
    ISINSCOPE ( FactData[Hour] )
        && ISINSCOPE ( 'DateDim'[Day] )
        && sessionCount <> BLANK (),
    FORMAT ( sessionCount, "#,##0" ),
    IF (
        NOT ISBLANK ( sessionCount ),
        FORMAT ( sessionCount, "#,##0" )
            & " ("
            & FORMAT ( pctShare, "0.0%" )
            & ")"
    )
)
```

UI logic stays readable and safe to tweak later.

## Measure with Variables & Time Logic

❌ Poorly Formatted

```c
User Growth % =
VAR s = [Metric A]
VAR d = MIN('DateDim'[Date]) - 1
VAR m = LOOKUPVALUE('DateDim'[MonthKey], 'DateDim'[Date], d)
VAR p = DATESINPERIOD('DateDim'[Date], d, -1, MONTH)
VAR sp = CALCULATE([Metric A], ALL('DateDim'), 'DateDim'[MonthKey] = m)
VAR g = s - sp
RETURN IF(COUNTROWS(p) > 1, DIVIDE(g, sp))
```

✅ Properly Formatted

```c
User Growth % =
VAR currentValue =
    [Metric A]

VAR refDate =
    MIN ( 'DateDim'[Date] ) - 1

VAR refMonth =
    LOOKUPVALUE (
        'DateDim'[MonthKey],
        'DateDim'[Date],
        refDate
    )

VAR prevPeriod =
    DATESINPERIOD (
        'DateDim'[Date],
        refDate,
        -1,
        MONTH
    )

VAR prevValue =
    CALCULATE (
        [Metric A],
        ALL ( 'DateDim' ),
        'DateDim'[MonthKey] = refMonth
    )

VAR growth =
    currentValue - prevValue

RETURN
IF (
    COUNTROWS ( prevPeriod ) > 1,
    DIVIDE ( growth, prevValue )
)
```

## Why formatting matters?

Formatting matters because DAX is read far more often than it is written. In real-world projects, measures grow complex very quickly, and poorly formatted code becomes hard to decode — even for the person who originally wrote it. I’ve seen many teams skip formatting to save time, only to lose much more time later trying to understand or debug dense logic.

While formatting may take a few extra minutes upfront, it pays off by making the logic clearer, reducing mistakes, and helping even the original developer quickly understand what’s happening when revisiting the measure weeks or months later.