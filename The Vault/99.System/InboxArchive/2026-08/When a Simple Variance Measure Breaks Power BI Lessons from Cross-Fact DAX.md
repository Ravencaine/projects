---
title: "When a Simple Variance Measure Breaks Power BI: Lessons from Cross-Fact DAX"
source: "https://medium.com/microsoft-power-bi/when-a-simple-variance-measure-breaks-power-bi-lessons-from-cross-fact-dax-84cdd81420a4"
author:
  - "[[Mark Chen]]"
published: 2026-03-07
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
Today I ran into one of those Power BI situations that looks simple on the surface but turns into a surprisingly deep modeling exercise.

All I wanted was a **variance measure**:

> *Compare payroll vehicle hours against equipment hours recorded in another system, and calculate the difference.*

Conceptually, the logic was trivial.

```c
Variance = MAX(Payroll Hours – Equipment Hours, 0)
```

But the two datasets came from **different operational systems**, and that’s where things got interesting.

This post summarizes the lessons I learned while making this work in Power BI.

![](99.System/Attachments/1!3f5D9cjOC2uNQRHvHVQuKA.png.webp)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## The Data Model

I had two fact tables coming from two different systems.

```c
+-------------------+
                         |     dimDate       |
                         +-------------------+
                                   |
                                   |
                -----------------------------------------
                |                                       |
                |                                       |
+----------------------------------+        +----------------------------------+
|        fctPayrollVehicles        |        |            LN Eq Rev             |
|----------------------------------|        |----------------------------------|
| Vehicle                          |        | Equipment Serial Code            |
| Job_Number                       |        | Project                          |
| Employee_Name                    |        | Quantity                         |
| TotalHours                       |        |                                  |
+----------------------------------+        +----------------------------------+
                |
                |
                v
        +-------------------+
        |    dimEmpMaster   |
        +-------------------+
                |
               Type
```

Conceptually, the fields correspond like this:

```c
Payroll Table              Equipment Table
--------------             ----------------
Vehicle           ─────▶   Equipment Serial Code
Job_Number        ─────▶   Project
```

The challenge: **there was no relationship between the two fact tables.**

That means Power BI cannot naturally compare the two datasets.

## Step 1 — Creating a Virtual Relationship

To align the datasets, I used `TREATAS`.

```c
Vehicle Eq Hours =
CALCULATE(
    SUM('LN Eq Rev'[Quantity]),
    TREATAS(
        SUMMARIZE(
            fctPayrollVehicles,
            fctPayrollVehicles[Vehicle],
            fctPayrollVehicles[Job_Number]
        ),
        'LN Eq Rev'[Equipment Serial Code],
        'LN Eq Rev'[Project]
    )
)
```

This tells Power BI:

> *Treat the Vehicle + Job pairs from payroll as filters on the equipment table.*

## Filter Flow

```c
Payroll Context
(Vehicle + Job)
        │
        │  TREATAS
        ▼
LN Eq Rev
filtered by:
Equipment Serial Code
Project
```

So even without a physical relationship, we can **project filters from one fact table onto another**.

## Lesson 1: Virtual Relationships Are Powerful

`TREATAS` allows you to simulate relationships between tables that the model itself does not define.

This is extremely useful for:

- cross-system reconciliation
- comparing operational systems
- bridging datasets with different schemas

## Step 2 — The Invisible Data Problem

When I tried extending the logic with job numbers, the measure suddenly stopped working.

After digging deeper, the culprit turned out to be mundane.

One system stored job numbers like:

```c
23540
```

The other stored them like:

```c
23540
```

That **leading space** meant the values were not equal.

Once I applied `LTRIM` to clean the key, everything started working again.

## Lesson 2: Exact Matching Matters

DAX comparisons are **exact**.

These two values are not the same:

```c
"121-23540"
" 121-23540"
```

If you’re joining keys across systems, always normalize them first.

Invisible characters will break your logic.

## Step 3 — A “Simple” Variance Measure Breaks the Model

Next I wrote the obvious variance measure.

```c
Vehicle Hours True-up =
IF(
    [Vehicle Labour Hours] > [Vehicle Eq Hours],
    [Vehicle Labour Hours] - [Vehicle Eq Hours],
    0
)
```

Power BI responded with:

> This visual has exceeded the available resources.

What happened?

The two measures were being evaluated at **different grains**.

Payroll hours were sliced by:

```c
Vehicle
Job
Employee
Type
```

Equipment hours were calculated only at:

```c
Vehicle
Job
```

Visually:

```c
Payroll Context
Vehicle + Job + Employee + Type
          │
          ▼
Vehicle Labour Hours
```
```c
Equipment Context
Vehicle + Job
          │
          ▼
Vehicle Eq Hours
```

Power BI had to repeatedly reconcile these two contexts.

That gets expensive very quickly.

## Lesson 3: Variance Measures Must Compare the Same Grain

The fix was to force payroll hours to evaluate only at **Vehicle + Job level**.

```c
Vehicle Labour Hours VJ =
CALCULATE(
    SUM(fctPayrollVehicles[TotalHours]),
    REMOVEFILTERS(dimEmpMaster[Type]),
    REMOVEFILTERS(fctPayrollVehicles[Employee_Name])
)
```

Now both measures operate at the same grain.

```c
Vehicle
Job
```

## Step 4 — Using Variables to Stabilize Context

Next I rewrote the variance calculation using variables.

```c
VAR _Vehicle = SELECTEDVALUE(fctPayrollVehicles[Vehicle])
VAR _Job = SELECTEDVALUE(fctPayrollVehicles[Job_Number])
```

Variables ensure the measure evaluates both sides under the same context.

They also prevent expensive expressions from being recalculated repeatedly.

## Why SELECTEDVALUE Worked… Then Failed

## At Row Level

```c
Matrix Row
-------------------------
Vehicle = V1
Job     = J1
```
```c
SELECTEDVALUE(Vehicle)    = V1
SELECTEDVALUE(Job_Number) = J1
```

Everything works because there is exactly **one vehicle and one job**.

## At the Grand Total Level

```c
Grand Total
-------------------------
Vehicle   Job
-------   ------
V1        J1
V1        J2
V2        J1
V3        J4
```

Now the context contains **multiple vehicles and jobs**.

```c
SELECTEDVALUE(Vehicle) = BLANK
SELECTEDVALUE(Job)     = BLANK
```

That breaks the measure.

## Fixing Totals with Iterators

The solution is to evaluate the calculation **pair by pair**.

```c
Vehicle Hours True-up =
SUMX(
    SUMMARIZE(
        fctPayrollVehicles,
        fctPayrollVehicles[Vehicle],
        fctPayrollVehicles[Job_Number]
    ),
    ...
)
```

This creates a list of distinct pairs:

```c
(V1, J1)
(V1, J2)
(V2, J1)
(V3, J4)
```

For each pair:

```c
Variance = MAX(Payroll Hours – Equipment Hours, 0)
```

Then `SUMX` adds the results together.

## Total Calculation Flow

```c
Distinct Vehicle-Job Pairs
        │
        ▼
Evaluate variance for each pair
        │
        ▼
SUMX adds results
```

## Lesson 4: Totals Often Need Iterators

When totals break due to row-level logic, the solution is often:

```c
SUMX(
    DISTINCT business keys,
    row calculation
)
```

This restores the correct grain before aggregation.

## Final Thoughts

What started as a simple variance measure turned into a useful reminder:

Data problems rarely announce themselves clearly.

They show up as:

- blank totals
- resource errors
- slow visuals
- mysteriously wrong numbers

And the root cause is often **grain mismatch between datasets**.

Once both measures operated at the same grain and the filter flow was carefully controlled, everything worked.

Sometimes the hardest part of DAX isn’t writing the formula.

It’s understanding **what level of reality your numbers represent**.

## Key Takeaways

Here are the main lessons from this debugging journey:

**1️⃣ Virtual relationships can bridge fact tables**

`TREATAS` allows filters from one table to act on another table even when no relationship exists.

This is extremely useful when reconciling data across systems.

**2️⃣ Always normalize keys when joining systems**

Invisible characters like leading spaces can silently break logic.

Cleaning keys with `TRIM` or `LTRIM` should be standard practice.

**3️⃣ Variance measures must compare the same grain**

If two measures operate at different levels of detail, Power BI has to reconcile contexts repeatedly — which can cause incorrect results or resource errors.

**4️⃣** `**SELECTEDVALUE()**` **works only when one value exists**

At row level there is usually one value.

At totals there are many.

When that happens, `SELECTEDVALUE()` returns **blank**, which can break a measure.

**5️⃣ Iterators often fix totals**

When totals fail, the correct pattern is often:

```c
SUMX(
    distinct business keys,
    row-level calculation
)
```

This rebuilds the correct grain before aggregating.

Most DAX problems are not really syntax problems.

They are **grain problems**.

## A Quick DAX Debugging Checklist

When a Power BI measure behaves strangely — slow visuals, broken totals, blank results — I now run through this checklist.

## 1️⃣ Check the Grain First

Ask yourself:

> What level of detail does this measure actually represent?

Examples:

- Vehicle
- Vehicle + Job
- Vehicle + Job + Employee

If two measures operate at different grains, variance calculations will often break.

## 2️⃣ Inspect the Filter Context

Power BI measures are evaluated under the current filter context.

Check what filters are actually active:

```c
Vehicle
Job
Employee
Date
Type
```

Sometimes removing unnecessary filters stabilizes the calculation:

```c
REMOVEFILTERS(dimEmpMaster[Type])
```

## 3️⃣ Verify Key Matching Between Tables

Cross-system comparisons fail surprisingly often because of subtle key mismatches.

Look for:

- leading/trailing spaces
- different data types
- inconsistent formatting
- hidden characters

Even this difference matters:

```c
"121-23540"
" 121-23540"
```

Always normalize keys when joining systems.

## 4️⃣ Understand When SELECTEDVALUE() Works

`SELECTEDVALUE()` only returns a value when **exactly one value exists in the context**.

Row-level visuals usually satisfy this condition.

Totals often do not.

When totals break, check whether your logic depends on `SELECTEDVALUE()`.

## 5️⃣ Use Iterators When Totals Break

If totals do not behave correctly, rebuild the calculation at the correct grain:

```c
SUMX(
    DISTINCT business keys,
    row-level calculation
)
```

This forces Power BI to evaluate the logic pair-by-pair.

## 6️⃣ Use Variables to Stabilize Complex Measures

Variables help ensure expressions are evaluated once within a consistent context.

```c
VAR _Vehicle = SELECTEDVALUE(fctPayrollVehicles[Vehicle])
VAR _Job = SELECTEDVALUE(fctPayrollVehicles[Job_Number])
```

This improves readability and often improves performance.

## The Core Insight

Most frustrating DAX problems are not really about the formula.

They are about **understanding the grain of the data and how filters propagate through the model**.

Once those two pieces are clear, the DAX usually becomes straightforward.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----84cdd81420a4---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX