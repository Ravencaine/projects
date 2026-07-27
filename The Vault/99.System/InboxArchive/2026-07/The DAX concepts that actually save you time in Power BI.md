---
title: "The DAX concepts that actually save you time in Power BI"
source: "https://medium.com/@oluwafikayore/the-dax-concepts-that-actually-save-you-time-in-power-bi-f193466f5b8f"
author:
  - "[[Daniel Olatunji]]"
published: 2026-07-27
created: 2026-07-27
description: "More"
Processed: "Unprocessed"
---
I still remember the afternoon a client’s Power BI report crashed my laptop’s fan into overdrive.

The file was 400MB, refreshes took twelve minutes, and every filter click froze the whole report for three or four seconds. When I finally opened the model to see what was going on, I found the problem right away: someone had built fourteen calculated columns to answer questions that should have taken one measure and thirty seconds.

That was the day I actually understood DAX. Not the day I first read about it. The day I saw, in a real broken file, what happens when you don’t.

If you’re a Power BI or Excel person and DAX still feels like a language you’re memorizing rather than a tool you’re using, this is for you. No “in this article we will explore.” Just the parts of DAX that matter, explained the way I wish someone had explained them to me.

## What DAX actually is

DAX stands for Data Analysis Expressions. Microsoft built it for Power Pivot back in 2010, and it now runs Power BI, Power Pivot in Excel, and Analysis Services. People assume it’s a full programming language because the syntax looks like Excel formulas mixed with SQL. It isn’t. DAX is a formula language built for one job: pulling numbers out of a data model based on filters.

That single fact explains almost everything confusing about DAX. Every weird moment where your number suddenly changes for no obvious reason comes back to how DAX handles context, which is really just a fancy word for “what’s currently filtered.”

### Measures vs calculated columns, and why mixing them up costs you

![](https://miro.medium.com/v2/resize:fit:1378/format:webp/1*vHFE8bV-zNj96wMXgnDgwg.png)

This is the first fork in the road, and it’s where that 400MB file went wrong.

A calculated column is computed once, per row, when you load or refresh your data. The result gets stored physically in the table, taking up space in memory the same way any other column does. Once it’s there, it doesn’t recalculate when someone clicks a slicer. It just sits there like a printed label.

A measure works differently. It has no stored value at all. It’s a formula that gets calculated on the fly, the instant a visual needs it, based on whatever filters are currently active. Click a slicer, drill into a category, change a date range, and every measure on the report recalculates in that instant.

Here’s the rule I give every analyst I mentor: if the answer needs to change when someone interacts with the report, it’s a measure. If you need a fixed, stored value on every row for grouping, sorting, or slicing, something like an age bracket, a customer segment label, or a year flag, that’s a calculated column. Total sales, year over year growth, percent of total, running totals: all measures. A “high value customer” flag you want to filter by: calculated column.

Get this backwards often enough, like that client did, and your model balloons in size while your report crawls.

### Row context and filter context, the idea that trips up almost everyone

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nL6fqzl0ICYj_z2Zsrrj7A.png)

If there’s one concept that separates people who fight with DAX from people who write it comfortably, it’s this one.

Filter context is the set of filters currently applied to your calculation. It comes from slicers, from rows and columns in a table or matrix visual, from filters on the page, and from any **CALCULATE** statement in your formula. When you’re looking at a total in a visual, that number only reflects rows that survive the current filter context.

Row context is different. It shows up when a formula moves through a table one row at a time, which happens inside calculated columns and inside iterator functions like **SUMX**. Picture walking down a spreadsheet, row by row, doing the same calculation on each one. That’s row context. There’s no filtering happening. There’s just the current row.

The part that confuses people: these two contexts don’t automatically talk to each other. A row context, on its own, doesn’t filter anything. This is exactly why a calculated column referencing another table’s aggregated value can behave strangely unless something bridges the two. That something is CALCULATE.

### CALCULATE, the one function that runs the whole show

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*F27jzzHq_aLVoWHVilrOxw.png)

If you only deeply learn one DAX function, make it **CALCULATE**. Almost every advanced technique in Power BI, from year over year comparisons to dynamic top-N rankings, is CALCULATE wearing a different hat.

What CALCULATE does is simple to say and slightly tricky to feel: it takes an expression and evaluates it inside a modified filter context. You hand it filters, add a region, remove a year, force a specific category, and it computes your formula as if those were the only filters in the world.

Total Revenue Lagos = CALCULATE(\[Total Revenue\], Customers\[City\] = “Lagos”)

That measure ignores whatever the report is currently filtered to and forces the calculation to only look at Lagos, always. This is the pattern behind almost every compare X to Y measure you’ll ever write.

There’s a subtler trick worth knowing too: context transition. Any time CALCULATE runs inside a row context, say inside a calculated column, or inside SUMX, it converts that row into an equivalent filter, one row acting exactly like a one row filter. This is why a measure reference inside an iterator behaves the way it does, and it’s also the reason context transition can get expensive on huge tables. Each row effectively triggers its own mini filter operation.

**VAR**, the underrated habit that saves you hours

Early on, I wrote DAX the way most people do: long, nested expressions with the same calculation repeated three or four times inside one formula. It worked. It was also nearly impossible to debug, and slower than it needed to be, because DAX kept recalculating the same thing over and over.

VAR fixes both problems. It lets you calculate something once, store it under a name, and reuse that name as many times as you want inside the same measure.

> YoY Growth % = VAR CurrentSales = \[Total Sales\] VAR PriorSales = CALCULATE(\[Total Sales\], SAMEPERIODLASTYEAR(‘Calendar’\[Date\])) RETURN DIVIDE(CurrentSales — PriorSales, PriorSales)

Read that back next to a version without variables, everything nested inside one DIVIDE call, and the difference is obvious. Variables read like a sentence. Nested expressions read like a puzzle. When you come back to your own report six months later, or a colleague opens your file for the first time, that difference is the gap between understanding it in ten seconds and needing thirty minutes and a coffee.

### The DAX functions that quietly save the most time

A handful of functions do most of the heavy lifting in day to day Power BI work. Here’s the shortlist I actually reach for on almost every project.

![](https://miro.medium.com/v2/resize:fit:1378/format:webp/1*dB6yqLT2l9Z9odz85p0SUg.png)

**DIVIDE** handles division safely, returning blank or zero instead of an error when the denominator is zero. Skip this and one empty category can crash your entire visual.

**SUMX, AVERAGEX**, and their siblings are iterators. They walk through a table row by row and apply a calculation to each row before aggregating. Use these when the calculation itself needs to happen per row, like multiplying quantity by unit price row by row before adding it all up, something a plain SUM can’t do.

**ALL** and **ALLSELECTED** remove filters. ALL wipes out every filter on a table or column, which is how you build percent of total measures. ALLSELECTED keeps filters from slicers outside the current visual while ignoring the visual’s own context, which is the trick behind subtotal rows that still show 100%.

**RELATED** pulls a value from a related table into the current row, useful in calculated columns when you need a field that lives in a different table connected by a relationship.

**SWITCH** replaces long chains of nested IF statements with something you can actually read at a glance. Anyone who has tried to debug five nested IFs understands why this belongs on the list.

**SAMEPERIODLASTYEAR** and **DATESYTD**, along with **DATEADD**, **TOTALYTD**, and **TOTALQTD**, handle the time comparisons that used to take people hours to hand build with date logic. Build one calendar table, mark it as a date table, and these functions do the rest.

**RANKX** gives you dynamic ranking that updates as filters change, exactly what you want for a top 5 products visual that needs to stay accurate no matter what the user filters by.

Learn these eight well and you’ll cover most of what shows up in real Power BI work.

### The mistakes I still see most often

Building calculated columns for things that should be measures, which we’ve already covered. Writing the same sub-calculation three times inside one formula instead of using a variable. Nesting nine IFs instead of reaching for SWITCH. Forgetting DIVIDE and letting a single zero break a whole report. And the big one: not building a proper date table, then wondering why SAMEPERIODLASTYEAR gives wrong or blank results. Time intelligence functions in DAX only work correctly against a marked, continuous date table. Skip that step and nothing downstream behaves the way the documentation says it should.

### Where this actually gets you

None of this is about memorizing syntax. DAX rewards people who understand what’s being filtered and when, not people who’ve memorized fifty function names. Once row context, filter context, and CALCULATE actually click, the rest of the language starts to feel less like magic and more like a small set of tools you already know how to combine.

That client’s 400MB file, once we swapped the calculated columns for measures and cleaned up the model, dropped to under 60MB and refreshed in under a minute. Same data. Same visuals. The only thing that changed was understanding what DAX was actually doing under the hood.

That’s the whole game.