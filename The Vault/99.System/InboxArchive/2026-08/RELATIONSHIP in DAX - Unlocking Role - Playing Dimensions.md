---
title: "RELATIONSHIP in DAX — Unlocking Role-Playing Dimensions"
source: "https://medium.com/write-your-world/relationship-in-dax-unlocking-role-playing-dimensions-ac67667d2618"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2025-12-07
created: 2026-07-27
description: "The day two date columns broke my Power BI model."
Processed: "Unprocessed"
---
## The day two date columns broke my Power BI model.

## Act 1 — The Dashboard That Betrayed Me

It started like any other Power BI project.  
A client from the logistics sector wanted to analyze **Sales by Invoice Date** and **Sales by Ship Date**.

Simple request, right?

I built a clean star schema:

- **Sales** fact table
- **Date** dimension (a standard date table)
- Relationship: `Sales[InvoiceDate] → Date[Date]`

The visuals worked perfectly.  
Until the client clicked a slicer and asked:

> *“Why doesn’t this change when I switch to* Ship Date*?”*

That’s when my model betrayed me.

Power BI relationships can only have **one active relationship** between two tables at a time.  
I had two:

- `Sales[InvoiceDate] → Date[Date]` ✅ (Active)
- `Sales[ShipDate] → Date[Date]` ❌ (Inactive)

Suddenly, my slicer became useless for half of the analysis.

![](99.System/Attachments/1!x7r4UGht0CLeaEbwOvC5wg.png.webp)

One active (solid line) and one inactive (dotted line) relationship between Sales and Date.

## Act 2 — The Pain of Inactive Relationships

I tried everything — duplicate visuals, new tables, even calculated columns.  
Each workaround either broke performance or created data mismatches.

Finally, a colleague messaged:

> *“Just use USERELATIONSHIP(). It activates the inactive relationship when needed.”*

At first, I thought it sounded too magical.  
But once I used it, it felt like discovering a secret DAX portal.

## Act 3 — The Fix That Changed Everything

I created two measures:

```c
Sales by Invoice Date = SUM ( Sales[SalesAmount] )

Sales by Ship Date =
CALCULATE (
 SUM ( Sales[SalesAmount] ),
 USERELATIONSHIP ( Sales[ShipDate], ‘Date’[Date] )
)
```

And boom 💥 — it worked like a charm.  
When I plotted both measures on the same chart, the results aligned perfectly with business logic.

![](99.System/Attachments/1!r7Y-_g1PtWjGo-AlqMaCPg.png.webp)

A dual-line chart showing “Sales by Invoice Date” vs “Sales by Ship Date” — each line controlled by different relationships

## Act 4 — How USERELATIONSHIP Really Works

USERELATIONSHIP doesn’t create a relationship —  
it **activates** an existing *inactive* one **temporarily** for that measure.

Think of it as a “relationship switcher” that CALCULATE can control:

- Only one relationship can be active globally
- But CALCULATE + USERELATIONSHIP allows you to **use the inactive one contextually**

Example:

```c
CALCULATE (
 [Total Sales],
 USERELATIONSHIP ( Sales[ShipDate], Date[Date] )
)
```

So inside this CALCULATE, Power BI uses the Ship Date relationship —  
but everywhere else, Invoice Date remains active.

![](99.System/Attachments/1!WPD7Rra9v4Es2paNlYg0jg.png.webp)

CALCULATE turning on “Ship Date” link temporarily.

## Act 5 — Why You Shouldn’t Duplicate Your Date Table (Most of the Time)

Before learning USERELATIONSHIP, I used to duplicate the Date table like this:

- `Date_Invoice` for InvoiceDate
- `Date_Ship` for ShipDate

That worked… until the client asked for a single timeline comparing both.  
Suddenly, the slicers became disconnected and filters didn’t sync.

USERELATIONSHIP saved me by letting both metrics use **the same Date dimension** —  
keeping the model clean and filters unified.

![](99.System/Attachments/1!RMZ4y5S0ScXUjCEf1ySSdA.png.webp)

one diagram with duplicated Date tables (messy), one with single Date + USERELATIONSHIP (clean)

## Act 6 — Real-World Example: Comparing Shipping Delays

A week later, the client asked:

> *“Can we see the average delay between Invoice Date and Ship Date?”*

Absolutely.

Using the same relationships, I wrote:

```c
Average Shipping Delay =
AVERAGEX (
 Sales,
 DATEDIFF ( Sales[InvoiceDate], Sales[ShipDate], DAY )
)
```

Then I used my two measures side-by-side:

- `Sales by Invoice Date`
- `Sales by Ship Date`

The report showed a 3.4-day average delay — and they used that metric in every weekly meeting after.

## Act 7 — Common Mistakes to Avoid

Even though USERELATIONSHIP is powerful, many analysts misuse it.

Here are the top mistakes I’ve seen (and made):

![](99.System/Attachments/1!HGECDo0bj4aFSRPWYlz9-g.png.webp)

## Act 8 — Going Further: Dynamic Switching Between Dates

Once I mastered USERELATIONSHIP, I pushed it further.

I created a **parameter table** called `DateType`:

![](99.System/Attachments/1!LJEmkBpd3Avmk2jkJmOSPg.png.webp)

Then I wrote:

```c
Dynamic Sales =
SWITCH (
 SELECTEDVALUE ( DateType[Date Type] ),
 “Invoice Date”, [Sales by Invoice Date],
 “Ship Date”, [Sales by Ship Date]
)
```

Now users could switch between Invoice vs Ship Date using a slicer —  
and the chart dynamically updated.

![](99.System/Attachments/1!Td6cRgOv31GrLv0wbYmF6w.png.webp)

“Invoice Date / Ship Date” toggle changing the chart line.

## Act 9 — The Client’s Reaction

When I demoed this, the client literally said:

> *“You just saved us from duplicating 12 visuals and 2 extra date tables.”*

For me, that’s when USERELATIONSHIP became more than a function —  
it became a mindset for **clean modeling and flexible storytelling**.

## Act 10 — Best Practices for USERELATIONSHIP

✅ Keep one Date table only — don’t duplicate unless absolutely needed.  
✅ Use CALCULATE + USERELATIONSHIP for alternate time perspectives.  
✅ Combine it with SWITCH + SELECTEDVALUE for dynamic analysis.  
✅ Always document inactive relationships clearly in your model.  
✅ Test your measures carefully — inactive links can cause unexpected blanks.

## 💡 Key Takeaway

> Inactive doesn’t mean useless — it just needs the right DAX to wake it up.