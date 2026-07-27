---
created: 2026-07-27
source: "Why Totals Look Wrong in DAX (and How to Fix Them)"
source_url: https://medium.com/write-your-world/why-totals-look-wrong-in-dax-and-how-to-fix-them-8b0506129c30
note_type: source
tags: [dax-code]
---

## If you’ve ever seen a Power BI total that made no sense, you’re not alone. Let’s explore why totals behave differently in DAX — and how to fix them with the right techniques.

## Act 1 — The Frustration Every Analyst Feels

It always starts the same way.

You build a beautiful Power BI report.  
You write a simple DAX measure:

```c
Profit = SUM(Sales[Revenue]) — SUM(Sales[Cost])
```

Everything looks fine in the detail rows.

But then you look at the **Total row**.

Expected total = 120 + 250 + 180 = **550**.  
But Power BI shows something completely different — maybe **600**, maybe **540**.

😡 You double-check your math.  
😡 You re-check your DAX.  
😡 You even export to Excel to confirm.

And yet, the total in Power BI doesn’t add up.

Sound familiar? You’re not alone. This “wrong totals” issue is one of the most common frustrations in DAX.

## Act 2 — Why Totals Look Wrong (The Hidden Rule of DAX)

Here’s the secret most beginners don’t realize:

👉 **Totals in DAX are not the sum of visible rows.**

Instead:

- A DAX measure is always **recalculated in the current filter context**.
- For detail rows → context = one customer, one product, one region.
- For totals → context = *all customers, all products, all regions*.

So when you see a total row in Power BI, it’s not “adding up rows.” It’s **running the same formula again, but with a bigger filter context**.

Let’s break it down.

## Example: Profit Margin %

Imagine this measure:

```c
Profit Margin % = 
DIVIDE(
 SUM(Sales[Revenue]) — SUM(Sales[Cost]),
 SUM(Sales[Revenue])
)
```

At row level:

- Customer A → (120 / 300) = 40%
- Customer B → (250 / 500) = 50%
- Customer C → (180 / 400) = 45%

Now, you might expect the total to be:  
(40% + 50% + 45%) / 3 = 45%.

But Power BI shows:  
(120 + 250 + 180) / (300 + 500 + 400) = 550 / 1200 = **45.8%**.

The total isn’t the “average of percentages.” It’s the **percentage for the entire context**.

And that’s the golden rule:  
👉 Totals are **re-evaluations**, not additions.


The total isn’t the average of percentages — it’s the margin recalculated for the entire context.

## Act 3 — The Investigator’s Toolkit (Fixing Wrong Totals)

So how do we fix this?  
There are three main strategies, depending on your scenario.

## 🛠️ Fix 1: Use Iterators (SUMX instead of SUM)

Sometimes the problem is that you’re using an aggregator when you need an iterator.

Bad:

```c
Profit = SUM(Sales[Revenue]) — SUM(Sales[Cost])
```

Better:

```c
Profit = 
SUMX(
 Sales,
 Sales[Revenue] — Sales[Cost]
)
```

Why this works:

- `SUM` adds up columns in the current filter context.
- `SUMX` evaluates each row with its own row context, then sums up the results.
- At the total level, SUMX ensures row-by-row logic is preserved.

SUM totals can mislead because they just add columns, while SUMX recalculates row by row, giving the correct total.

📊 *Visual:* Table showing “wrong total” with SUM vs corrected total with SUMX.

## 🛠️ Fix 2: Conditional Logic with HASONEVALUE

Sometimes you want **totals to behave differently** than detail rows.

Example: Weighted average price.

```c
Weighted Avg Price = 
IF(
   HASONEVALUE(Product[ProductName]),
   DIVIDE(SUM(Sales[Revenue]), SUM(Sales[Quantity])),
   DIVIDE(SUM(Sales[Revenue]), SUM(Sales[Quantity]))
)
```

Wait — that looks the same, right?  
But here’s the trick:

- Inside row context (per product) → works as expected.
- At the total row → same formula, but over the entire dataset.

If you want a different behavior, you can adjust the logic in the `IF` block.


HASONEVALUE lets you apply one formula for rows and a different one for totals

## 🛠️ Fix 3: Debug with ISFILTERED / HASONEFILTER

Sometimes the total looks wrong because your formula assumes row-level filters that don’t exist at total level.

Example:

```c
Sales Check = 
IF(
 ISFILTERED(Customer[CustomerName]),
 SUM(Sales[Revenue]),
 BLANK()
)
```

This ensures the measure only returns values when a filter exists (i.e., not at the grand total).


Table showing totals replaced with BLANK until explicitly defined.

## Act 4 — A Detective Story in Practice

Let’s tell the story of **Maya, a data analyst**.

She was asked to build a dashboard showing **Average Order Value (AOV)** per customer.

Her first DAX measure was:

```c
AOV = DIVIDE( SUM(Sales[Revenue]), COUNT(Sales[OrderID]) )
```

At the customer level, the numbers made sense.  
But the total row showed a completely different value than what the business expected.

The business wanted:

- Average of all customers’ AOVs.  
	But DAX gave:
- Total revenue ÷ total orders.

Maya fixed it with:

```c
AOV Fixed = 
AVERAGEX(
 VALUES(Customer[CustomerName]),
 DIVIDE(SUM(Sales[Revenue]), COUNT(Sales[OrderID]))
)
```

Result: The total now matched the business expectation.

Moral of the story: **Know what the business means by “total.”**  
Because DAX will always apply its own rule: recalculate, not add.


Totals for Average Order Value can be misleading unless you use AVERAGEX to calculate per customer and then average them correctly

## Act 5 — Best Practices for Totals

- ✅ Always test your measure at detail and total level.
- ✅ Ask stakeholders: *“Should totals be recalculated, or should they be sum of rows?”*
- ✅ Use **SUMX** when per-row logic matters.
- ✅ Use **AVERAGEX** for weighted averages.
- ✅ Use **HASONEVALUE** or **ISFILTERED** to control behavior.
- ✅ Educate users: totals aren’t wrong, they’re just **different math**.

Totals in DAX are not added-up rows — they are recalculated in a new filter context.

## Act 6 — Key Takeaways

- Totals in DAX are **re-evaluated**, not just “sums of rows.”
- Wrong totals happen when your logic behaves differently at higher filter contexts.
- Fixes include:

Using iterators like SUMX, AVERAGEX.

Conditional logic with HASONEVALUE.

Clarifying business definition of totals.

- Once you understand this, totals stop being scary — they become predictable.

## Closing Thought

Every analyst who learns DAX eventually faces the “wrong totals” problem.  
The trick isn’t just fixing it — it’s understanding **why**.

So the next time someone says *“the totals are wrong”*, you can smile and say:  
👉 *“They’re not wrong. They’re just DAX being DAX. Let me show you why — and fix it.”*

> See also [[all]] for reference.


> See also [[averagex]] for reference.


> See also [[calculate]] for reference.


> See also [[filter-context-vs-row-context]] for reference.


> See also [[sumx]] for reference.


> See also [[sales-to-budget-variance-percent]] for reference.


> See also [[measures-vs-calculated-columns]] for reference.
