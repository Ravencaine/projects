---
title: "Understanding EARLIER in DAX: The Time Machine You Didn’t Know You Had"
source: "https://medium.com/write-your-world/understanding-earlier-in-dax-the-time-machine-you-didnt-know-you-had-c969fa5eea46"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2025-11-12
created: 2026-07-27
description: "The function everyone feared… until variables (VAR) came to the rescue."
Processed: "Unprocessed"
---
## The function everyone feared… until variables (VAR) came to the rescue.

## Act 1 — The Day I Met EARLIER (and Got Confused)

It was a regular Tuesday afternoon.  
My student Riya pinged me on Teams, panic in her message:

> *“Sir, my running total works for one customer but not for all! And Power BI says:  
> *‘EARLIER/EARLIEST refers to an earlier row context which doesn’t exist’. *😭”*

Ah, the classic DAX heartbreak.  
If you’ve written DAX for even a few months, you’ve seen that error.

So I opened her model, took a sip of coffee, and smiled.  
This was going to be *another EARLIER adventure*.

## Act 2 — Why EARLIER Exists

Before `VAR`, DAX needed a way to look *back* into a previous row context —  
a bit like a time machine.

Let’s break that down.

Imagine you have a simple **Sales** table:

![](99.System/Attachments/1!ROlBlMXpdYGdzmljjRklVA.png.webp)

Now, you want to create a **Running Total** by customer.

At first, Riya wrote this:

```c
Running Total =
CALCULATE(
 SUM(Sales[Sales]),
 FILTER(Sales, Sales[Month] <= EARLIER(Sales[Month]))
)
```

…and that’s when she got the error.

## Act 3 — The Hidden Rule: EARLIER Needs a Parent Row Context

The key thing about `EARLIER` is this:

> *It only works when you already have* ***two nested row contexts*** *—  
> one inside the other.*

Think of it as a *conversation between two loops.*

Let’s visualize:

![](99.System/Attachments/1!Vr0vRj2CKVfDkMN_3D5WgA.png.webp)

**“Two Row Context Loops”**

- Outer loop → iterates over each Customer
- Inner loop → iterates over Sales rows for that customer
- EARLIER → allows the inner loop to “look up” to the current value in the outer loop

In Riya’s case, the measure didn’t have that outer loop —  
so `EARLIER` didn’t know what “earlier” meant.

It’s like asking, *“Earlier than what?”*

## Act 4 — The Proper Example

When you create a **calculated column** (not a measure),  
each row gets its own “row context” —  
and that’s when `EARLIER` can shine.

Let’s build a column that shows a **Running Total by Customer**:

```c
Running Total =
CALCULATE(
 SUM(Sales[Sales]),
 FILTER(
 Sales,
 Sales[Customer] = EARLIER(Sales[Customer]) &&
 Sales[Month] <= EARLIER(Sales[Month])
 )
)
```

Now it works!

Why? Because:  
1️⃣ The **outer context** is the calculated column (one row at a time).  
2️⃣ The **inner context** is the FILTER iterator.  
3️⃣ `EARLIER()` lets the inner loop access the value of `Sales[Customer]` and `Sales[Month]` from the current row of the outer loop.

![](99.System/Attachments/1!jby1XxaQh2Vlpyj4HefWUg.png.webp)

A two-level diagram showing: “Outer Row (Customer=A, Month=Feb)” → Inner Filter context looping over all rows where Customer=A and Month ≤ Feb.

## Act 5 — Why It Feels Like Magic (but Isn’t)

When people first discover `EARLIER`, they think it’s *telepathic* —  
like it just knows the previous value automatically.

But it’s really just **context transition** in disguise:

- Each new iterator (like FILTER, ADDCOLUMNS, or SUMX) creates a *new row context*.
- EARLIER helps you refer to the one above that.

Think of it as:

> *“Go one step up the context ladder and fetch that value.”*

You can even use multiple EARLIER calls if you have 3+ nested loops:  
`EARLIER()` → one level up  
`EARLIEST()` → the top-most one

![](99.System/Attachments/1!W42nxCNmcj1OT9v6j44wkg.png.webp)

A “context ladder” diagram — three boxes labeled Row Context 1, Row Context 2, Row Context 3 with arrows showing EARLIER climbing upward.

## Act 6 — The Problem: EARLIER Makes Code Hard to Read

When Riya looked at her formula again, she sighed:

> *“Sir, this is so hard to read.”*

And she was right.

Here’s the truth:

- EARLIER works only in calculated columns.
- It breaks easily when you move to measures.
- It’s not beginner-friendly.

That’s why DAX introduced **VAR** —  
to replace most of these patterns with clean, readable code.

## Act 7 — Rewriting the Same Logic Using VAR

Let’s compare both approaches.

With EARLIER:

```c
Running Total =
CALCULATE(
 SUM(Sales[Sales]),
 FILTER(
 Sales,
 Sales[Customer] = EARLIER(Sales[Customer]) &&
 Sales[Month] <= EARLIER(Sales[Month])
 )
)
```

**With VAR:**

```c
Running Total =
VAR Cust = Sales[Customer]
VAR Mo = Sales[Month]
RETURN
CALCULATE(
    SUM(Sales[Sales]),
    FILTER(Sales, Sales[Customer] = Cust && Sales[Month] <= Mo)
)
```

Clean, clear, and measure-compatible.

![](99.System/Attachments/1!j8REKJSED_kX3vZvsBNmOA.png.webp)

Side-by-side “EARLIER vs VAR” example highlighting readability difference.

## Act 8 — Real Project Example: Ranking Sales per Customer

A client once asked me to create a ranking column for each customer’s purchases.

Using `EARLIER`, it looked like this:

```c
Rank by Customer =
RANKX(
 FILTER(Sales, Sales[Customer] = EARLIER(Sales[Customer])),
 Sales[Sales],
 ,
 DESC
)
```

It worked!  
But once we needed it as a **measure**, it failed.  
So we rewrote it using `VAR` and `RANKX` inside `CALCULATE`.

## Act 9 — The Rule of Thumb

![](99.System/Attachments/1!IR0PX9XHena3pikKR2tf5w.png.webp)

![](99.System/Attachments/1!8vF2H8xLdam4WZqK88uzUg.png.webp)

A summary infographic: “EARLIER = Old Time Machine 🕰️ | VAR = Modern Jetpack 🚀

## Act 10 — Riya’s Realization

A few days later, Riya texted again:

> *“Sir, I replaced all my EARLIERs with VARs.  
> The formulas are shorter. My model is faster. And I finally understand DAX!”*

I laughed and replied,

> *“See? You don’t need to travel to the past to understand your data anymore.”*

Because that’s what EARLIER really was —  
a way to **peek back in time** before variables existed.  
It taught us how DAX thinks.

And once you understand that,  
you can write DAX that’s not just correct — it’s *beautiful*.

## Key Takeaways

✅ **EARLIER** lets you access outer row context — useful in calculated columns.  
✅ **VAR** does the same thing more elegantly and works in measures.  
✅ Use **EARLIER** only when you’re dealing with nested row contexts.  
✅ Use **VAR** for clarity, flexibility, and speed.  
✅ The future of DAX is **readable, reusable, and context-smart**.