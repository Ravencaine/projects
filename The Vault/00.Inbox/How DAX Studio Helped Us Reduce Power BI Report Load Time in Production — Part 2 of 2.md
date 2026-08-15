---
title: "How DAX Studio Helped Us Reduce Power BI Report Load Time in Production — Part 2 of 2"
source: "https://medium.com/@dashakashkumar636/how-dax-studio-helped-us-reduce-power-bi-report-load-time-in-production-part-2-of-2-9fc1cdc3573e"
author:
  - "[[Akash Dash]]"
published: 2026-08-09
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
A Real Example: Bad DAX, Server Timings, and the Fix

In [Part 1](https://medium.com/@dashakashkumar636/how-dax-studio-helped-us-reduce-power-bi-report-load-time-in-production-part-1-of-2-c57b8c1138e0?sharedUserId=dashakashkumar636), we covered the basics — connecting DAX Studio to a report, and understanding the Storage Engine (SE) vs Formula Engine (FE) split using a simple analogy: SE as a team of workers counting pages in parallel, FE as the single reviewer who has to compare all those counts one at a time.

Now let’s put that into practice with a real measure, a real 1.29-million-row table, and real Server Timings output.

**The scenario**

We’re working with Microsoft’s public [Employee Hiring History sample](https://learn.microsoft.com/en-us/power-bi/create-reports/sample-employee-hiring-history) — specifically the Employee table, which holds 1,290,259 rows with columns like Age, BadHires, EmplID, HireDate, TenureDays, and more.

Say we want a measure that shows, for each employee’s age, what share of that age group’s “bad hires” a given row represents — a Bad Hire Ratio. It sounds like a simple ratio calculation. Here’s a version that gets the right answer, but does it in a very expensive way.

***The bad measure***

```c
Bad Hire Ratio (SLOW) = 
SUMX(
    Employee,
    VAR CurrentAge = Employee[Age]
    VAR TotalBadHiresForSameAge =
        CALCULATE(
            SUM ( Employee[BadHires] ),
            FILTER(
                ALL ( Employee ),
                Employee[Age] = CurrentAge
            )
        )
    RETURN
        DIVIDE ( Employee[BadHires], TotalBadHiresForSameAge )
)
```

Why this is a problem, in plain terms:

- SUMX(Employee, …) iterates the table one row at a time — row context.
- Inside that loop, CALCULATE triggers context transition on every single row, and FILTER(ALL(Employee), …) asks the engine to rebuild a filtered table from scratch, every time, just to find rows matching CurrentAge.
- In the worst case, that’s the kind of pattern that scales as rows × rows instead of a single pass — exactly the FILTER(ALL())-inside-CALCULATE anti-pattern this series is built around.
- It gets worse if this measure is referenced by, or nested inside, another measure that also uses ALL() or a similar full-table filter — each layer adds its own re-scan on top of the one below it, effectively creating a nested loop. What looks like two “simple” measures combined can multiply into far more engine work than either one shows on its own.

**Reading the Server Timings on the bad measure**

Here’s what running this actually produced in DAX Studio:

The visual we captured this from is a simple table: AgeGroup and Bad Hire Ratio (SLOW) in Columns, with a Grand Total row turned on. Following the [Part 1](https://medium.com/@dashakashkumar636/how-dax-studio-helped-us-reduce-power-bi-report-load-time-in-production-part-1-of-2-c57b8c1138e0?sharedUserId=dashakashkumar636) workflow — Performance Analyzer → Copy query → paste into DAX Studio — captures the real query Power BI generated for that exact visual.

*Total Duration: 110ms — SE 100ms (90.9%), FE 10ms (9.1%), Storage Engine CPU 94ms, Total CPU 109ms, 7 Storage Engine queries.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ycwTu-IcV7WDY5jXaFxzCg.png)

Bad DAX Server Timings

![](https://miro.medium.com/v2/format:webp/1*nFcBEjyhIAboPS1JHqWNyQ.png)

SE & FE Workflow for Bad DAX

The first thing worth noticing: even though the underlying Employee table has 1.29 million rows, the actual scans here work with far smaller row counts — 430, 86, sometimes just 6 or 1. VertiPaq is columnar, so it only touches the columns the measure references (Age, BadHires), and Age has just 86 distinct values. Instead of a literal row-by-row scan, the Storage Engine collapses the work down to the distinct combinations that actually exist. This is VertiPaq quietly optimizing around low cardinality — it’s not proof the pattern is safe, just proof this particular column let the engine cheat.

> DAX Studio auto-flags two lines here as HighlightQuery — its way of marking the queries it considers most significant to the total cost. Both are the same expensive CallbackDataID pattern: the Formula Engine calling back into the Storage Engine separately to resolve the DIVIDE, because context transition inside the iterator forced that per-row (here, per-group) handoff. FE is single-threaded, so every one of those callbacks happens serially, one after another — which is why these two lines dominate duration even though they return almost no rows.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wXcSg_j1dW560a88b3hKCg.png)

CallbackDataID Marker (Different Run Image)

> Notice they fire twice: once to compute the ratio for the AgeGroup subtotal rows (line 8, 50ms), and again, independently, to compute it for the single Grand Total row (line 14, 61ms). Combined, these two lines account for 111ms of the 130ms total — about 85% of the entire query, just from the same per-row callback machinery being triggered once per rollup level the visual displays.

**The important lesson here:** this anti-pattern would look far worse on a high-cardinality column. Age has only 86 distinct values, so VertiPaq’s collapse kept the row counts low throughout. Key it on something like EmplID (1.29M distinct values) or TenureDays, and there’s no collapsing left to do — the callback pattern would fire proportionally more often, and both SE Queries count and total duration would climb sharply. The takeaway isn’t “this measure is fine because it only touched a few hundred rows” — it’s “this measure has a structural cost that scales with cardinality and with how many rollup levels a visual shows, and we got lucky on both counts here.”

**The fix**

```c
Bad Hire Ratio (FAST) = 
SUMX(
    ADDCOLUMNS(
        SUMMARIZE ( Employee, Employee[Age] ),
        "@BadHiresForAge", CALCULATE ( SUM ( Employee[BadHires] ) )
    ),
    VAR CurrentTotal = [@BadHiresForAge]
    RETURN
        DIVIDE ( CurrentTotal, CurrentTotal )
)
```

What changed:

- SUMMARIZE(Employee, Employee\[Age\]) builds the distinct list of ages once — a single set-based operation, not a per-row iteration over 1.29M rows.
- ADDCOLUMNS + CALCULATE(SUM(…)) computes the total BadHires per age group — CALCULATE still triggers context transition, but now only once per distinct age (86 times), not once per row.
- No FILTER(ALL(Employee)) anywhere. We never ask the engine to rebuild a filtered copy of the whole table to find matching rows — the grouping step already did that job, natively, using VertiPaq’s own strengths.
- The outer SUMX now iterates an 86-row summary table, not the 1.29M-row base table.

**Reading the Server Timings on the fast measure**

*Total Duration: 20ms — SE 11ms, FE 9ms, Storage Engine CPU 16ms, Total CPU 16ms, 4 Storage Engine queries.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IEnRRssMZXgYNK7LjQw3Bw.png)

Fast DAX Server Timings

**Total: 110ms → 20ms.** That’s a **5.5x reduction**, and the shape of the trace tells the real story:

- No CallbackDataID line anywhere. Zero. That’s the single clearest proof the fix worked — there’s no per-group callback left to trigger, because SUMMARIZE/ADDCOLUMNS built the grouped table once instead of asking CALCULATE to re-derive it per row.
- No HighlightQuery flags this time either — DAX Studio isn’t singling out any one line as disproportionately expensive, because nothing here is disproportionately expensive. The cost is spread evenly across four ordinary scans.
- SE Queries dropped from 7 to 4. The bad version needed extra passes to resolve the join for both the AgeGroup subtotal and the Grand Total separately, the fast version resolves both from the same handful of scans.
- Line 4 is worth a second look: 3ms duration but 16ms CPU time. That’s not a red flag — it’s the opposite. A CPU time higher than wall-clock duration means the Storage Engine split the work across multiple threads running in parallel, several cores did 16ms of combined work in just 3ms of real time. Compare that to the bad version’s CallbackDataID lines, where CPU time roughly equaled duration — the sign of single-threaded, serial FE work with no parallelism to lean on.
- FE time is still 9ms — not literally zero — because the Formula Engine still has to do some final assembly and return the result set. But as a share of total time, FE went from 9.1% of 110ms to 45% of a much smaller 20ms pie. In absolute terms, FE barely changed and what disappeared was the repeated back-and-forth calling into FE that the bad version was doing per group, per rollup level.
![](https://miro.medium.com/v2/resize:fit:1328/format:webp/1*P-PV--AdOmJwV0Mg6UyIuQ.png)

SE & FE Workflow for Fast DAX

**Before vs. after, side by side**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JT3faj7Swj8_vSLRYabpwg.png)

Fast and Bad DAX Comparison

**Takeaways**

- **Low cardinality can hide a bad pattern.** Our bad measure “only” scanned 430 rows because Age has 86 distinct values — but the structural cost (a callback per group) would scale badly on a high-cardinality column. Don't let a small Server Timings number on a test column convince you a pattern is safe.
- **Push work into the Storage Engine, keep the Formula Engine’s job small.** The fast version isn’t a different answer — it’s the same math, computed once at the right grain instead of repeatedly inside a row context.
- The CallbackDataID line in Server Timings is a specific, learnable red flag. If you see it consuming a large share of your query’s duration, look for CALCULATE/context transition sitting inside a row-by-row iterator, and consider whether a SUMMARIZE/ADDCOLUMNS pattern could compute the same result at a coarser grain.

If you’re debugging your own slow Power BI report, the workflow is the same one we used here: capture the query from Performance Analyzer, run it in DAX Studio with Server Timings and Query Plan on, look for FE time and CallbackDataID lines dominating duration, and check whether a FILTER(ALL())-inside-CALCULATE pattern is hiding inside a row-by-row iterator.

That’s the full loop — from “this report feels slow” to knowing exactly why, and exactly what to change.

Follow me for more of such content. Happy Coding:)