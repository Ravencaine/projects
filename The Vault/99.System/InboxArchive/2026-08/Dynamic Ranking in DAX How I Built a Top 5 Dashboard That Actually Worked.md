---
title: "Dynamic Ranking in DAX: How I Built a Top 5 Dashboard That Actually Worked"
source: "https://medium.com/towards-artificial-intelligence/dynamic-ranking-in-dax-how-i-built-a-top-5-dashboard-that-actually-worked-9080ae713da4"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2025-11-20
created: 2026-07-27
description: "Because “Top 5 Customers” shouldn’t break when you click a slicer."
Processed: "Unprocessed"
---
## Because “Top 5 Customers” shouldn’t break when you click a slicer.

## Act 1 — The Client Request That Sounded Simple (But Wasn’t)

A retail analytics client once called me and said,

> *“We just need a simple Top 5 Customers dashboard. How hard can that be?”*

If you’ve ever worked with Power BI, you already know what’s coming.

I opened the report.  
The model was clean — `Sales`, `Products`, `Date`, and `Customers` tables all perfectly related.

I created a quick table visual:

```c
Total Sales = SUM ( Sales[Revenue] )
```

Then I added:

```c
Rank = RANKX ( ALL ( Customers[CustomerName] ), [Total Sales], , DESC )
```

…and BOOM 💥 — a nice ranking appeared.

I proudly showed it to the client, clicked a slicer for **“Electronics”**, and suddenly the top 5 changed completely.

“Wait,” the client said.

> *“Why is Customer A gone? They’re one of our biggest clients overall!”*

Uh-oh.  
Welcome to **dynamic ranking hell**.

## Act 2 — The Core Problem: Static vs Dynamic Context

At first, I thought the formula was fine.  
But DAX doesn’t just rank values — it ranks **within the current filter context**.

So when you use a slicer, the “universe” of customers changes.  
Power BI doesn’t know whether you want a **global** Top 5 or a **filtered** Top 5.

![](99.System/Attachments/1!WV1PFRELoM2N_SXmPU_mOA.png.webp)

Global vs Filtered Top 5 — comparing how ranking shifts when filter context (like product category) is applied

The trick is to control **what ALL() removes** — and **where CALCULATE() restores filters.**

## Act 3 — Building the Correct Ranking Logic

Here’s the classic pattern that works for almost any scenario:

```c
Customer Rank =
RANKX (
 ALL ( Customers[CustomerName] ),
 [Total Sales],
 ,
 DESC
)
```

Then you can add a measure for dynamic Top N:

```c
Top Customers Sales =
IF (
    [Customer Rank] <= 5,
    [Total Sales],
    BLANK ()
)
```

Now, when you put this measure in a visual, only the top 5 appear — regardless of slicer filters.

![](99.System/Attachments/1!LC4L1hyBLRmtekNV2OjASQ.png.webp)

Dynamic ranking output — Top 5 customers highlighted based on total sales.

## Act 4 — The Client’s Twist: “Can I Choose N?”

Just when I thought we were done, the client smiled:

> *“Actually, can we make Top N dynamic — so users can pick 5 or 10 from a slicer?”*

Of course. Because why not make life harder?

So I created a **“Top N Parameter” table:**

![](99.System/Attachments/1!-ptmR7pjYNcjCO1TVjItIA.png.webp)

Then added a measure to capture selection:

```c
Selected TopN = SELECTEDVALUE ( TopN[TopN], 5 )
```

…and modified the earlier measure:

```c
Top Customers Sales =
IF (
    [Customer Rank] <= [Selected TopN],
    [Total Sales],
    BLANK ()
)
```

Boom 💥 — now the dashboard reacted instantly.  
Switching from Top 5 → Top 10 → Top 15 updated the visuals dynamically.

![](99.System/Attachments/1!1zui_wXjCE_y6EEaYcAzCA.png.webp)

Interactive bar chart where users can adjust Top N dynamically using a slicer

## Act 5 — Performance Problem: The Slow Dashboard

A week later the client called again:

> *“It’s working, but switching filters takes forever!”*

Ah, the cost of beauty.

`RANKX + ALL()` on a large dataset can be expensive, because DAX re-evaluates ranking for every context.

So I rewrote it using **variables (VAR)** to store intermediate results — a trick from our previous post.

```c
Customer Rank =
VAR BaseTable = ALL ( Customers[CustomerName] )
VAR SalesValue = [Total Sales]
RETURN
RANKX ( BaseTable, [Total Sales], SalesValue, DESC )
```

It became **30 % faster** instantly.

![](99.System/Attachments/1!CRIE-e6OxuWJolyo-j6-jA.png.webp)

Performance boost: using VAR in RANKX calculations reduces query time.

## Act 6 — Making It Visual: Ranking on Cards and Charts

Once the logic was solid, I built two visuals:  
1️⃣ **Horizontal Bar Chart** — Top N Customers by Sales  
2️⃣ **Card** — Shows the highest ranked customer

And to make it shine:

- Added **Data Labels** for ranks (1 → 5)
- Used a gradient color — darker bars = higher rank
- Created a toggle: “Show Top N by Sales / Profit / Orders”

Now the client could explore **multiple leaderboards** on the same report.

![](99.System/Attachments/1!Xppxa8MEBTS_WadCjG4fkQ.png.webp)

Including ‘Others’ category — combining Top N customers with the rest for complete visibility.

## Act 7 — Adding the “Others” Category

Clients love totals.  
They asked,

> *“Can you add an ‘Others’ bar showing all customers outside the Top N?”*

Sure.

```c
Sales Top N vs Others =
VAR TopN Sales =
 CALCULATE ( [Total Sales], 
FILTER ( Customers, [Customer Rank] <= [Selected TopN] ) )
VAR All Sales = [Total Sales (All Customers)]
RETURN
UNION (
 ROW ( “Customer”, “Top N”, “Sales”, TopN Sales ),
 ROW ( “Customer”, “Others”, “Sales”, All Sales — TopN Sales )
)
```

Now the bar chart showed **Top N Customers + ‘Others’** neatly.

## Act 8 — Client Reaction: “This Feels Like Magic!”

When I demoed the new dashboard, the client played with slicers, changed N values, and grinned:

> *“This is exactly what we wanted — simple, fast, and flexible.”*

That’s when I realized:

> *Dynamic ranking is not just about Top 5s —  
> it’s about* ***letting users explore data freely without breaking logic.***

## Act 9 — Best Practices Cheat Sheet

![](99.System/Attachments/1!Sejy6rk-rqG_RK1ClpY02A.png.webp)

## Act 10 — Key Takeaways

✅ Dynamic ranking is one of the most powerful ways to create interactive dashboards.  
✅ Always decide **what filters to remove** before ranking.  
✅ Use **VAR** for speed and readability.  
✅ Add a Top N parameter to empower users.  
✅ Visualize it beautifully — people love leaderboards.