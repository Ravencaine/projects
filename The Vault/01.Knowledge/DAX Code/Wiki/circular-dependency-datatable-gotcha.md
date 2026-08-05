---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: gotcha
tags: [dax, gotcha, circular-dependency, sort-column, datatable, calculated-column]
---

# Circular Dependency — DATATABLE Sort Column Gotcha

When building a disconnected `Selector` table for the baseline highlight pattern, adding a Sort Order column as a **separate calculated column** on the `Selector` table (reading `Selector[Category]` in a SWITCH) causes a circular dependency error.

## The Problem

Power BI detects this dependency cycle:

```
Selector[Sort Order] formula reads Selector[Category]
Selector[Category] sort order depends on Selector[Sort Order]
→ Cycle detected → Error
```

## The Fix

Put **both columns in the same `DATATABLE` call** as literal data pairs:

```dax
Selector =
DATATABLE (
    "Category", STRING,
    "Sort Order", INTEGER,
    {
        { "Value A", 1 },
        { "Value B", 2 },
        { "Value C", 3 }
    }
)
```

Neither column is a formula that reads the other — both are literal values, so no dependency cycle exists. Set the sort via **Column tools → Sort by column** on the Category column.

## Why It Happens

Any calculated column that appears in a `Sort By Column` configuration must not have a formula dependency on the column it sorts. A separate `SWITCH`-based calculated column reads `Category` in its formula, creating the cycle. Literal columns in `DATATABLE` have no formula — they are static data.

## Related

- [[selector-datatable-disconnected-table]] — `function`
- [[sort-column-pq-vs-dax]] — `pattern`
- [[stacked-chart-baseline-highlight-pattern]] — `pattern`
