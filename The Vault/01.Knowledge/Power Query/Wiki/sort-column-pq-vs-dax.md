---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: pattern
tags: [power-query, pattern, sort-column, conditional-column, circular-dependency, m, power-bi]
---

# Sort Column — Power Query vs DAX

When a category column needs a custom sort order (S/M/L/XL/XXL, Low/Medium/High), the sort column must be added in Power Query (M), not as a DAX calculated column — or a circular dependency error blocks the sort-by configuration.

## The Circular Dependency Problem

A DAX calculated column that reads `Dim[Category]` in its formula and is then set as `Category`'s Sort By Column creates a dependency cycle:
- `Sort Column` formula depends on `Category`
- `Category` sort order depends on `Sort Column`

Power BI detects this and raises: **"a circular dependency was detected."**

## Two Scenarios

### Scenario 1: Disconnected Selector DATATABLE

For the `Selector` disconnected table, the fix is simple: put **both columns in the same `DATATABLE` call** as literal data pairs. Neither column is a formula that reads the other — both are literal values, so no dependency cycle exists:

```dax
Selector =
DATATABLE (
    "Category", STRING,
    "Sort Order", INTEGER,
    {
        { "S",   1 },
        { "M",   2 },
        { "L",   3 },
        { "XL",  4 },
        { "XXL", 5 }
    }
)
```

### Scenario 2: Real Imported Dimension Table

For `Dim[Category]` loaded from a real source (CSV, SQL, etc.), the DATATABLE trick does not apply — the table is not authored in DAX. The sort column must be added in **Power Query (M)** instead:

```m
if [Category] = "S"   then 1
else if [Category] = "M"  then 2
else if [Category] = "L"  then 3
else if [Category] = "XL" then 4
else if [Category] = "XXL" then 5
else null
```

Added via **Power Query Editor → Add Column → Custom Column**.

## Why M Works Where DAX Doesn't

A column added in M loads as a plain Data column with **no DAX expression:** nothing in the model dependency graph links it back to `Category`, even though it was obviously derived from it upstream in the query. DAX sees it as a static data column, so no cycle is detected.

## Steps (Real Dimension Table)

1. Power Query Editor → select table → Add Column → Custom Column → paste M expression
2. Close & Apply
3. Hide the new sort column
4. Set `Category → Column tools → Sort by column → Category Sort Order`

## Related

- [[circular-dependency-datatable-gotcha]] — `gotcha`
- [[selector-datatable-disconnected-table]] — `function`
- [[stacked-chart-baseline-highlight-pattern]] — `pattern`
