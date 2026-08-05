---
created: 2026-08-01
updated: 2026-08-02
source: "The DAX concepts that actually save you time in Power BI.md"
note_type: atomic
tags: [dax, measures, calculated-columns, fundamentals, beginner]
---

# Measures vs Calculated Columns: When to Use Each

The fork that separates working models from bloated ones. Same data — 400MB down to 60MB.

## Calculated Column

- Computed **once per row** at data load or refresh
- Result **stored physically** in the table — takes memory
- **Does not recalculate** when user interacts with the report
- Sits like a printed label

```c
// Stored value: Customer Lifetime Value per row
Customer Lifetime Value = Sales[Amount] * 0.1
```

## Measure

- **No stored value**: formula computed on the fly
- Recalculates **instantly** whenever filter context changes
- Click a slicer, drill into a category, change date range → measure recalculates
- Takes zero memory in the model

```c
// Computed when visual needs it, based on current filters
Total Sales = SUM(Sales[Amount])
```

## The Decision Rule

| Question | Answer | Use |
|----------|--------|-----|
| Does the value need to **change** when someone interacts with the report? | Yes | **Measure** |
| Do you need a **fixed, stored value** on every row for grouping, sorting, or filtering? | Yes | **Calculated column** |

**Examples — Measure:**
- Total sales
- Year-over-year growth
- Percent of total
- Running totals

**Examples — Calculated column:**
- Customer age bracket (fixed label)
- Customer segment flag (for filtering/slicing)
- Year flag (categorical)

## The 400MB→60MB Case Study

Building calculated columns for things that should be measures:
- Bloat: adds physical rows to the model
- Slows refresh: recalculates at load time unnecessarily
- Doesn't respond to filters: wrong tool for interactive values

Fix: swap for measures → model shrinks, refresh time drops, report responds to filters.

## Related

- [[row-vs-filter-context-core]] — why measures need filter context to work
- [[calculate-context-transition-core]] — how CALCULATE bridges contexts
- [[dax-common-mistakes-beginners]] — calc column anti-patterns
