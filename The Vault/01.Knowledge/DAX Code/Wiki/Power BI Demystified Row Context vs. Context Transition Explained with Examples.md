---
created: 2026-07-27
updated: 2026-08-02
source: "Power BI Demystified: Row Context vs. Context Transition Explained with Examples"
source_url: https://medium.com/write-your-world/power-bi-demystified-row-context-vs-context-transition-explained-with-examples-d43576a74f22
note_type: source
tags: [dax-code]
---

## Most learners get stuck on DAX because of context. Here’s an easy, visual guide to Row Context and Context Transition with code and examples.

## Introduction: Why Context Confuses Everyone

If you’ve ever written DAX in Power BI, you’ve probably hit this wall:

- Why does my calculated column give one result, but the same formula in a measure gives another?
- What does “row context” even mean?
- And why does CALCULATE suddenly change everything?

The answer lies in **context**: specifically, **Row Context** and **Context Transition**.

These two ideas are at the heart of DAX. Once you master them, the rest of Power BI feels far less confusing.

## What Is Row Context?

Think of **row context** as Power BI’s ability to “look at one row at a time.”

- When you create a **calculated column**, Power BI evaluates the formula *for each row separately*.
- Example:
```c
Sales[Profit] = Sales[Revenue] — Sales[Cost]
```

👉 Here, Power BI loops over each row in the `Sales` table and calculates `Revenue - Cost` for that row.


Row context means: evaluate the formula for each row individually

## What Is Context Transition?

**Context transition** happens when row context turns into **filter context**.

- The key function that triggers this: **CALCULATE**.
```c
Total Profit :=
CALCULATE( SUM(Sales[Profit]) )
```
- Here, CALCULATE takes the row context (if any) and **converts it into a filter**.
- This is why measures behave differently than calculated columns — because CALCULATE changes the way context is applied.

CALCULATE is the bridge that turns row context into filter context

**Example 1: Calculated Column vs. Measure**

```c
— Calculated Column
Sales[Profit] = Sales[Revenue] — Sales[Cost]

 — Measure
Total Profit = SUM(Sales[Revenue]) — SUM(Sales[Cost])
```
- **Calculated Column:** Each row shows its own profit.
- **Measure:** Ignores rows, shows aggregate based on filter context (like region, product, date).

👉 This is why a column works row by row, but a measure changes when you slice by region.


## Example 2: Context Transition in Action

Let’s say you create a measure:

```c
Profit by Row :=
SUMX(Sales, Sales[Revenue] — Sales[Cost])
```

What happens here?

- SUMX iterates each row (row context).
- Inside SUMX, CALCULATE is implied → row context becomes filter context for each row.

That’s context transition at work.


## Why This Matters

- **Row Context** explains why calculated columns behave differently.
- **Context Transition** explains why measures change with filters.
- Together, they explain 90% of “Why does my DAX give a different result?”

## Key Takeaways (Scannable Section)

- ✅ Row Context = “Evaluate formula per row.”
- ✅ CALCULATE introduces Context Transition.
- ✅ Measures ≠ Columns because measures use filter context.
- ✅ SUMX, AVERAGEX, etc. use row context + context transition under the hood.

## Closing Thought

Once you understand Row Context and Context Transition, DAX becomes far less mysterious.  
Instead of memorizing formulas, you can reason through why a measure gives the result it does.

👉 Next time your DAX confuses you, ask: *“Am I in row context, filter context, or both?”*

Power BI,Data Science,Analytics,Business Intelligence,DAX

> See also [[all]] for reference.


> See also [[averagex]] for reference.


> See also [[calculate]] for reference.


> See also [[context-transition-with-calculate]] for reference.


> See also [[dax-context]] for reference.


> See also [[filter-context-vs-row-context]] for reference.


> See also [[sumx]] for reference.


> See also [[measures-vs-calculated-columns]] for reference.
