---
title: "From 59 Copy Pasted Measures to One Library: What Migrating to GA DAX UDFs Actually Taught Me"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/From-59-Copy-Pasted-Measures-to-One-Library-What-Migrating-to-GA/ba-p/5259384?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-07-01
created: 2026-08-08
description: "A field report from rebuilding a production UDF library the week DAX User-Defined Functions went GA in Power BI's June 2026 release. THE PROBLEM"
Processed: "Unprocessed"
---
**A field report from rebuilding a production UDF library the week DAX User-Defined Functions went GA in Power BI's June 2026 release.**

**THE PROBLEM EVERY DAX DEVELOPER KNOWS BUT NOBODY TALKS ABOUT**

Open any semantic model that's been alive for more than six months and you'll find the same crime scene: three measures that all compute "safe division," each written slightly differently. A YoY% formula copy-pasted into eleven visuals, one of which still has last quarter's bug because nobody remembered to fix it there too. A currency-conversion snippet that exists in four models because nobody wanted to rebuild it from scratch.

This isn't sloppiness. It's what happens when a language has no functions. Until recently, DAX gave us measures, calculated columns, and calculation groups- but no clean way to package a piece of logic once and call it everywhere with parameters, the way SQL, Python, or M have always let us. Every "reusable" pattern was really just disciplined copy-paste with a naming convention on top.

I hit this wall hard while building a shared logic layer for one of my tutorial models- a "NovaMart Global" demo I use to teach advanced DAX patterns. Over several months it grew to 59 functions covering things like safe division, dynamic banding, ABC classification, and currency-aware growth calculations, all namespaced under dwp.\*. Every one of them was a measure, because that was the only unit of reuse DAX had. It worked, but it wasn't a library. It was a folder of measures pretending to be one.

Then DAX User-Defined Functions moved from preview to generally available in the June 2026 release of Power BI Desktop, and I spent a week rebuilding that library the right way. Here's what actually changed, what broke, and what I'd tell any developer sitting on their own pile of duplicated logic.

**WHAT A UDF ACTUALLY IS (AND WHY IT'S NOT A CALCULATION GROUP)**

A DAX UDF is a first-class model object - visible in Model Explorer, storable in TMDL, and callable from measures, calculated columns, visual calculations, and even other UDFs. You define it once inside a DEFINE block using the FUNCTION keyword, give it typed parameters, and call it exactly like a native DAX function.

*DEFINE*

*/// Returns SalesAmount safely divided, avoiding divide-by-zero errors*

*/// [@param](https://community.fabric.microsoft.com/t5/user/viewprofilepage/user-id/69498) {NUMERIC} Numerator - the value to divide*

*/// [@param](https://community.fabric.microsoft.com/t5/user/viewprofilepage/user-id/69498) {NUMERIC} Denominator - the value to divide by*

*/// @returns the division result, or BLANK if denominator is zero*

*FUNCTION dwp.SafeDivide = (*

*Numerator: NUMERIC,*

*Denominator: NUMERIC*

*) =>*

*IF ( Denominator = 0, BLANK(), DIVIDE ( Numerator, Denominator ) )*

*EVALUATE*

*{ dwp.SafeDivide ( \[Total Sales\], \[Total Cost\] ) }*

Two things separate this from what most of us were doing with calculation groups or "template measures":

Typed parameters with two passing modes. Value types (Scalar, Table, AnyVal) evaluate eagerly the moment the function is called. Expression types (AnyRef, CalendarRef) pass an unevaluated expression that the function controls the evaluation context for- which is exactly what you need when a function has to reference a measure and force its own CALCULATE context transition. Get this wrong and your "reusable" function behaves differently depending on where it's called from, which is the single most common bug I saw while rebuilding my library.

Documentation that IntelliSense actually reads. The /// comment block above the function isn't decoration- type the function name anywhere in the model and IntelliSense surfaces that description, parameter list, and return type. For a 59-function library, this is the difference between a tool people actually adopt and a wiki page nobody opens.

THE DAY-TO-DAY PROBLEM THIS SOLVES

If you maintain more than one semantic model- client work, internal reporting, a tutorial library, whatever- you've lived this cycle:

1. Write a clever piece of logic in Model A.
2. Need it again in Model B. Copy-paste it, rename a column reference.
3. Find a bug in the logic three weeks later. Fix it in Model A.
4. Forget Model B exists. Model B ships the bug to a client.

UDFs don't just save typing- they collapse steps 3 and 4 into one place. Because functions live in TMDL as text, you can check a functions.tmdl file into Git, and every model that pulls from the same source of truth gets the fix automatically instead of drifting apart.

**REBUILDING dwp.\*: THREE REAL REFACTORS**

1. Safe division, everywhere. I had six near-identical "safe divide" measures across models. All six collapsed into one dwp.SafeDivide function. Every measure that used to contain IF(Denominator=0, BLANK(), DIVIDE(...)) now just calls the function.
2. ABC classification, parameterized. My old ABC-banding logic hardcoded the 80/15/5 thresholds inside the measure. As a UDF, the thresholds became parameters:

F *UNCTION dwp.ABCBand = (*

*CumulativePercent: NUMERIC,*

*TierA: NUMERIC = 0.8,*

*TierB: NUMERIC = 0.95*

*) =>*

*SWITCH (*

*TRUE,*

*CumulativePercent <= TierA, "A",*

*CumulativePercent <= TierB, "B",*

*"C"*

*)*

Default parameter values meant existing calls didn't break, but any model that needed a stricter 70/90 split could now override the thresholds at the call site instead of forking the measure.

3. Currency-aware growth, using expression parameters. This was the one that taught me the most. My original growth% measure needed to reference a different measure depending on the calling context- sometimes gross sales, sometimes net. Passing that measure as a value parameter evaluated it too early and silently returned the wrong filter context. Switching the parameter to an AnyRef expression type and wrapping the internal call in an explicit CALCULATE fixed it. That single detail- value vs. expression parameters- is worth understanding before you migrate anything, not after you've debugged a mismatched total for two hours like I did.

WHERE TO ACTUALLY BUILD THESE

You've got five entry points, and they're not interchangeable for every workflow:

\- DAX Query View- best for interactive testing; right-click a function for Quick Queries like "Define and evaluate."

\- TMDL View- code-first editing, and where you'll live if you're versioning functions in Git.

\- Model Explorer- create or edit a function directly through the formula bar; existing functions sit under the Functions node.

\- XMLA endpoint / SSMS 22.5+- for programmatic or DevOps-style deployment.

\- Semantic Link Labs- if you're on Fabric notebooks, sempy\_labs.tom.connect\_semantic\_model combined with set\_user\_defined\_function lets you script an entire function library into a model in one notebook cell, which is how I now redeploy all 59 dwp.\* functions to a fresh demo model in seconds instead of rebuilding by hand.

One practical gate: UDFs require database compatibility level 1702 or higher. If you're migrating an older model, check this first- it's the silent blocker that will make your FUNCTION block fail with no obvious explanation.

**A FIVE-MINUTE AUDIT FOR YOUR OWN MODELS**

Before you write a single UDF, open your model and count:

\- How many measures share an identical IF(... = 0, BLANK(), DIVIDE(...)) pattern?

\- How many banding/tiering SWITCH statements exist with hardcoded thresholds?

\- How many measures would break identically if a business rule changed tomorrow?

Every "yes" on that list is a candidate function. In my case, 59 measures across models collapsed into roughly 20 genuinely distinct functions once I stopped treating "different table name" as "different logic."

**THE HONEST LIMITATIONS**

UDFs aren't a replacement for calculation groups- they solve different problems. A calculation group changes which measure gets calculated based on a slicer selection; a UDF changes how a piece of logic is computed wherever it's called. You'll likely use both in a mature model. And because functions can call other functions, it's easy to build a dependency chain that's elegant to write and painful to performance-tune later- writing efficient function bodies isn't a footnote, it's a warning worth taking seriously from the start.

**WHY THIS MATTERS BEYOND YOUR OWN MODEL**

The thing that changed my mind about UDFs wasn't the syntax- it was realizing they're not just a personal productivity feature. A typed, documented function is something both humans and AI assistants can pick up and use correctly on the first try, instead of having to reverse-engineer a wall of nested DAX to figure out what it's supposed to do. If junior teammates or AI copilots are ever going to query your models safely, a well-documented function library is what makes that possible.

If you're still on measures-with-naming-conventions pretending to be a library, GA is the moment to stop pretending. Audit your model, find your dwp.SafeDivide equivalent, and write it once.

Have you rebuilt a measure library with DAX UDFs yet? I'd genuinely like to see what functions other developers have found worth extracting- drop them in the comments.

[dax-udf-before-after.png](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/From-59-Copy-Pasted-Measures-to-One-Library-What-Migrating-to-GA/ba-p/5259384?attachment-id=113998&utm_campaign=newsletter&utm_medium=email&utm_source=powerbiweekly)

Top Kudoed Posts

| Subject | Kudos |
| --- | --- |
| ## Data Days \| Create | 58 |
| ## Data Days \| Connect | 47 |
| ## Power BI Dataviz World Champs \| Round 3 | 29 |
| ## Power BI Dataviz World Champs Barcelona \| Round 2 | 26 |
| ## Power BI Dataviz World Champs Barcelona \| Round 1... | 23 |

[View All](https://community.fabric.microsoft.com/t5/forums/kudosleaderboardpage/board-id/community_blog/timerange/one_month/page/1/tab/posts)

Latest Articles

- [Need a Running Total for Just One Chart? Power BI'...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Need-a-Running-Total-for-Just-One-Chart-Power-BI-s-Visual/ba-p/5342327)
- [Data Days Contests | Announcing SQL + AI Promptath...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Data-Days-Contests-Announcing-SQL-AI-Promptathon-Winners/ba-p/5341906)
- [The Hidden Architecture of Power BI Publishing Exp...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/The-Hidden-Architecture-of-Power-BI-Publishing-Explained/ba-p/5333695)
- [Power BI Dataviz World Champs Barcelona | Round 2...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Barcelona-Round-2-Winners/ba-p/5332826)
- [Power BI Copilot Custom Instructions: Prep Data fo...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Copilot-Custom-Instructions-Prep-Data-for-AI/ba-p/5332193)
- [Power BI Dataviz World Champs | Round 3](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Round-3/ba-p/5323477)
- [Community Sticker Challenge Barcelona 2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Community-Sticker-Challenge-Barcelona-2026/ba-p/5311346)
- [Power BI Copilot Set Limits](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Copilot-Set-Limits/ba-p/5321290)
- [Tired of Viewers Clicking "+" on Every Row? Power...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Tired-of-Viewers-Clicking-quot-quot-on-Every-Row-Power-BI-s/ba-p/5322597)
- [Power Bi Alerts with DAX at Power Automate](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-Bi-Alerts-with-DAX-at-Power-Automate/ba-p/5314017)

Archives

- [08-02-2026 - 08-08-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/8-2-2026%2012%3A00%20AM)
- [07-26-2026 - 08-01-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-26-2026%2012%3A00%20AM)
- [07-19-2026 - 07-25-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-19-2026%2012%3A00%20AM)
- [07-12-2026 - 07-18-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-12-2026%2012%3A00%20AM)
- [07-05-2026 - 07-11-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-5-2026%2012%3A00%20AM)
- [06-28-2026 - 07-04-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-28-2026%2012%3A00%20AM)
- [06-21-2026 - 06-27-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-21-2026%2012%3A00%20AM)
- [06-14-2026 - 06-20-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-14-2026%2012%3A00%20AM)
- [06-07-2026 - 06-13-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-7-2026%2012%3A00%20AM)
- [05-31-2026 - 06-06-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-31-2026%2012%3A00%20AM)
- [05-24-2026 - 05-30-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-24-2026%2012%3A00%20AM)
- [05-17-2026 - 05-23-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-17-2026%2012%3A00%20AM)
- [05-10-2026 - 05-16-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-10-2026%2012%3A00%20AM)
- [View Complete Archives](https://community.fabric.microsoft.com/t5/blogs/blogarchivespage/blog-id/community_blog)