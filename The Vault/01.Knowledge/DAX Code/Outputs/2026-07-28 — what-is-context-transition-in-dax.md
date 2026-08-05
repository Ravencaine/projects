---
type: vault-query
question: "what is context transition in DAX"
date: 2026-07-28T21:11:56
kb: DAX Code
---

# what is context transition in DAX



# Context Transition in DAX

**Context transition** is the mechanism by which CALCULATE converts an active **row context** into an equivalent **filter context**.

## Definition

When CALCULATE runs inside a row context (inside a calculated column or inside an iterator like SUMX), each active row context is converted into a filter on the corresponding table — effectively one row acting as a one-row filter. This allows measures to behave differently when called from different contexts. [01.Knowledge/DAX Code/Wiki/context-transition-with-calculate.md]

## Key Points

| Aspect | Description |
|--------|-------------|
| **Trigger** | CALCULATE function |
| **Source context** | Row context (from calculated columns or iterators) |
| **Result** | Equivalent filter context |
| **Effect** | One row acts as a one-row filter |

## How It Works

Row context iterates over rows and exists in:
- **Calculated columns** — each row is evaluated with its own context
- **Iterator functions** (SUMX, MAXX, etc.) — explicitly loop over rows [01.Knowledge/DAX Code/Wiki/dax-context.md]

When CALCULATE is evaluated within either of these row contexts, it performs the transition — transforming the current row's values into filters on the table. This is the key behavior that makes CALCULATE powerful inside iterators and calculated columns. [01.Knowledge/DAX Code/Wiki/context-transition-with-calculate.md]

## Example Pattern

```dax
-- Calculated Column with context transition
TotalPrice = CALCULATE(SUM(Sales[Price]), Sales[Quantity] > 0)
```

In a calculated column, CALCULATE wraps the expression, and the row context for the current row becomes a filter context for the evaluation.

## Sources

  1. [[01.Knowledge/DAX Code/Wiki/Power BI Demystified Row Context vs. Context Transition Explained with Examples.md|Power BI Demystified Row Context vs. Context Transition Explained with Examples]] — score 0.033  2. [[01.Knowledge/DAX Code/Wiki/context-transition-with-calculate.md|Context Transition with CALCULATE]] — score 0.031  3. [[01.Knowledge/DAX Code/Wiki/dax-context.md|DAX Context]] — score 0.030  4. [[01.Knowledge/DAX Code/Wiki/filter-context-vs-row-context.md|Filter Context vs Row Context]] — score 0.030  5. [[01.Knowledge/DAX Code/Wiki/dax-is-column-oriented.md|DAX Is Column-Oriented — Unlike Excel Cell Formulas]] — score 0.027

## Query Log

- **Date:** 2026-07-28 21:11
- **Top results:** 35 notes ranked
- **Dominant KB:** DAX Code
