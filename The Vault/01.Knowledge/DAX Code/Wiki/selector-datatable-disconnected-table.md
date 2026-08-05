---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: function
tags: [dax, function, datatable, disconnected-table, selector, slicer, sort-order]
---

# Selector DATATABLE (Disconnected Helper Table)

A small disconnected table that powers the category slicer for the baseline highlight pattern. It holds all category values as literal strings and optionally a sort order column — it has no relationship to the data model.

## Core Formula

```dax
Selector =
DATATABLE (
    "Category", STRING,
    {
        { "Value A" },
        { "Value B" },
        { "Value C" }
        -- one row per distinct value of Dim[Category]
    }
)
```

Created via **Modeling → New table** in Power BI Desktop.

## With Sort Order (for S/M/L/XL/XXL and similar non-alphabetical sequences)

```dax
Selector =
DATATABLE (
    "Category", STRING,
    "Sort Order", INTEGER,
    {
        { "S",     1 },
        { "M",     2 },
        { "L",     3 },
        { "XL",    4 },
        { "XXL",   5 }
    }
)
```

Then set **Category → Column tools → Sort by column → Sort Order**.

## Key Rules

- **Disconnected:** no relationship to any other table. It only feeds `SELECTEDVALUE()` in the Position measures.
- **Both columns must be in the same DATATABLE:** adding Sort Order as a separate calculated column creates a circular dependency.
- **One row per distinct category value:** match the values exactly to `Dim[Category]`.

## Default Selection

By default, all positions return blank when nothing is selected (no `SELECTEDVALUE` fallback). To set a sensible default:

```dax
Position 1 =
VAR Sel = SELECTEDVALUE ( Selector[Category], "Value A" )
RETURN
    IF ( NOT ISBLANK ( Sel ), CALCULATE ( [Your Measure], Dim[Category] = Sel ) )
```

## Related

- [[stacked-chart-baseline-highlight-pattern]] — `pattern`
- [[circular-dependency-datatable-gotcha]] — `gotcha`
- [[sort-column-pq-vs-dax]] — `pattern`
