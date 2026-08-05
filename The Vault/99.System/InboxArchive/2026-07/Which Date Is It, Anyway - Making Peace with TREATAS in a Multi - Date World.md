---
title: "🧠 “Which Date Is It, Anyway?” — Making Peace with TREATAS in a Multi-Date World"
source: "https://medium.com/@markchen69/which-date-is-it-anyway-making-peace-with-treatas-in-a-multi-date-world-4f1400d4e6d1"
author:
  - "[[Mark Chen]]"
published: 2025-05-28
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
> “All dates are equal, but some are more equal than others.” — George Orwell, probably not talking about Power BI

## 📆 When One Date Just Isn’t Enough

Let’s paint a scene familiar to many of us in data analytics: you’re in Finance or Supply Chain, you open a dataset called `CustomerTransactions`, and it looks something like this:

*TransactionID Customer Product OrderDate ShipDate DueDate PaymentDate 1001 Contoso WidgetX 2024–12–01 2024–12–03 2024–12–10 2024–12–09  
1002 Northwind WidgetY 2024–12–02 2024–12–04 2024–12–12 2024–12–10*

Each of these dates is important in its own right. But in Power BI, relationships are **monogamous** by default: only *one* active relationship can exist between `Date` and `CustomerTransactions`. That means when you want to analyze by `ShipDate` instead of `OrderDate`, you either:

1. Create a bunch of inactive relationships and activate them using `USERELATIONSHIP()` in every DAX measure
2. Duplicate the `Date` table multiple times, creating a Cartesian Date Circus
3. Start crying softly into your keyboard

But what if I told you there was a better way? A way to **summon a relationship just in time**, use it, and vanish like Batman at a crime scene?

## 🦸 Meet TREATAS: The Dynamic Relationship Whisperer

In short, `TREATAS` allows you to **project values from one column as if they belonged to another table’s column** — effectively *creating a virtual relationship on the fly*.

Let’s say you want to analyze shipped quantities *by* ***ShipDate***, but your model’s active relationship is on `OrderDate`.

Instead of flipping relationships or duplicating date tables, do this:

```c
Ship Qty by Date = 
CALCULATE(
    SUM(CustomerTransactions[Quantity]),
    TREATAS(
        VALUES('Date'[Date]),
        CustomerTransactions[ShipDate]
    )
)
```

Boom. This tells Power BI:

> *“Hey, for the duration of this measure, treat the values in* `*CustomerTransactions[ShipDate]*` *as if they were part of the* `*'Date'[Date]*` *column.”*

It’s like temporary cosplay for your data model. No permanent commitments, no side effects.

## ⚔️ Real-World Scenario: The Multi-Date Metrics Battle

Your CFO wants the following KPIs in one visual:

- Orders by Order Date
- Shipments by Ship Date
- Overdue payments by Due Date
- Cash received by Payment Date

All of these should slice/filter by a single `Date` slicer.

**Your data model?**

Just one `Date` table.  
Just one active relationship (let's say on `OrderDate`).  
Everything else: **handled by** `**TREATAS**`.

```c
Shipped Qty by Date = 
CALCULATE(
    SUM(CustomerTransactions[Quantity]),
    TREATAS(VALUES('Date'[Date]), CustomerTransactions[ShipDate])
)
```
```c
Overdue Payments by Date = 
CALCULATE(
    SUM(CustomerTransactions[OutstandingAmount]),
    TREATAS(VALUES('Date'[Date]), CustomerTransactions[DueDate])
)Cash Received by Date = 
CALCULATE(
    SUM(CustomerTransactions[PaidAmount]),
    TREATAS(VALUES('Date'[Date]), CustomerTransactions[PaymentDate])
)
```

Each measure now responds to the same `Date` slicer, even though it’s pulling from different date columns. Clean. Powerful. Zero extra relationships.

## 🎨 Visual Model

Here’s what the model looks like:

- One `Date` table with a single active relationship to `CustomerTransactions[OrderDate]`
![](99.System/Attachments/1!x29UB8tg9EGviipT-MZJTg.png.webp)

- Other date fields? Left alone
- All complexity handled in the measure logic

## 🤯 Wait, Why Not Just Use USERELATIONSHIP?

`USERELATIONSHIP` works — but only if you’ve already defined the inactive relationship. With `TREATAS`, you don’t need **any** relationship in the model. That’s huge in complex data models where adding one more relationship could create ambiguity or circular references.

Also, `TREATAS` is more flexible when projecting multiple fields — say, if you want to simulate a multi-column relationship or join based on transformed data.

## 🚫 Common Pitfalls

- `**TREATAS**` **is strict** — The column you map to must match the data type and ideally the granularity of your `Date` table. You might need to use `FORMAT()`, `TRUNC()`, or even add calculated columns to ensure alignment.
- **No automatic blank handling** — If your `ShipDate` has blanks, `TREATAS` might lead to unexpected results.
- **Not a magic wand** — `TREATAS` is powerful, but if you're constantly using it everywhere, it might be a sign your model needs refactoring.

## 🎯 When to Use TREATAS Like a Pro

- When you need **time intelligence across multiple date types** from the same fact table
- When creating extra date tables is overkill or pollutes your model
- When you’re building dynamic visuals with a universal date slicer

## 🧘 Final Thoughts: Zen and the Art of Relationships

`TREATAS` isn’t just a function — it’s a **mindset**. It lets you move past the rigidity of static data models and into a world where context is fluid, flexible, and well… *treatable*.

So the next time someone asks you:

> *“Can we analyze that by Ship Date instead?”*

You won’t break a sweat. You’ll smile, open DAX, and TREATAS yourself to a clean, elegant solution.

## 🧪 Want to Try It?

Drop your own multi-date challenge in the comments, and I’ll show you how to `TREATAS` it into submission.