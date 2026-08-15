---
created: 2026-08-04
updated: 2026-08-05
source: "Stop Copy-Pasting DAX: The Power of Measure Branching in Power BI"
note_type: atomic
tags: [dax, measure-branching, naming-conventions, best-practices, beginner]
---

# Measure Branching Naming Conventions

Consistent naming makes the measure hierarchy scannable at a glance. Naming conventions communicate the layer and purpose of each measure without needing to open the formula editor.

## Layer Naming Patterns

| Layer | Prefix / Suffix | Example |
|-------|----------------|---------|
| Layer 1 (Base) | `Base` or `Core` | `Base Sales`, `Core Revenue` |
| Layer 2 (Derived) | Verb or descriptor | `Gross Profit`, `Profit %` |
| Layer 3 (Advanced) | Context or modifier | `YTD Sales`, `LY Profit` |

## Display Folder Structure

Group measures visually using Tabular Editor or Power BI's Display Folder property:

```
📁 0.Base
    Base Sales
    Base Cost
    Base Qty
📁 1.Derived
    Gross Profit
    Profit %
📁 2.Advanced
    YTD Sales
    YoY Growth %
```

## Naming Rules

1. **Use `[Brackets]` for measure references:** never forget the brackets inside CALCULATE, CALCULATETABLE, or any expression that references another measure.
2. **Omit table qualifiers:** `SUM(Sales[Revenue])` not `SUM('Sales'[Revenue])` unless the column name is ambiguous.
3. **Keep names short:** 1–3 words. `Sales YTD` beats `Year to Date Total Sales`.
4. **Use Title Case:** `Gross Profit %` not `gross_profit_pct`.
5. **Indicate direction for delta measures:** `Sales vs LY %`, `Margin Delta`.

## Anti-Pattern: Underscores and Abbreviations

```dax
-- Avoid: underscores and cryptic abbreviations
Total_Sales_Qty_YTD_LY
TSQ

-- Prefer: readable Title Case
Total Sales YTD vs LY %
```

## Related

- [[measure-branching-pattern]] — the full three-layer branching structure
- [[base-measure-design]] — Layer 1 base measure principles
- [[measure-branching-calculate-composition]] — extending branched measures with CALCULATE
