---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: atomic
tags: [dax-concepts, row-context, filter-context, context-transition]
---

# DAX Context: Row Context and Filter Context

DAX context is simply the set of **filters** that determine which rows are available for a calculation. Understanding context is the key to thinking in DAX.

## Definition

**Row context** means "the current row" — used when DAX evaluates a calculated column. When you reference `[Price]`, row context means it reads the `Price` value for whichever row is currently being computed.

**Filter context** means "the active filters from visuals, slicers, and DAX expressions" — used by measures. When a visual shows "Banana", the filter context restricts all calculations to only Banana rows.

## Key Points

- **Calculated columns use row context.** A column definition like `[Price] * [Quantity]` is evaluated once per row, with row context automatically pointing to the current row.
- **Aggregators in calculated columns break row context.** Writing `AVERAGE( [Price] )` in a calculated column returns the same value for every row because aggregators operate over the full table with no filters — row context does not apply inside the aggregation.
- **Measures use filter context.** The value of a measure changes depending on what the visual is filtering. A Card visual with no filters shows the overall average; when a Table visual shows "Banana" on a row, that Banana filter propagates to the Card and the measure recalculates.
- **Context flows from visuals to measures.** Selecting a column in a clustered column chart changes the filter context for every measure in other visuals on the page. This can be seen via the funnel icon when hovering over a visual.
- **Context can also come from inside DAX.** The `FILTER` function creates explicit filter context as part of a DAX expression, independent of visual filters.

## Examples

**Calculated column — row context:**
```dax
Total Cost = [Price] * [Quantity]
```
Row context makes `[Price]` and `[Quantity]` resolve to the current row's values automatically.

**Calculated column — aggregation breaks row context:**
```dax
Average Price = AVERAGE( [Price] )
```
Every row shows the same value (3.79) because the aggregator ignores row context and operates over the full table.

**Measure — Banana row in a Table visual:**
The Banana row filters the data to just Banana rows (8.97 and 14.95). The `Average Total Cost` measure computes `(8.97 + 14.95) / 2 = 11.96` for that row. For Pickle, it shows the single Pickle row's cost. For the Grand Total row (no filter), it averages all rows.

**External filter context:**
Selecting "Banana" in a clustered column chart creates a filter that propagates to the Card visual showing `Average Total Cost` — the Card now shows only the Banana average, not the overall average.

## Related

- [No CALCULATE Banana Pattern](/wiki/no-calculate-banana-pattern.md) — FILTER creates filter context within the pattern
- [X Aggregators](/wiki/x-aggregators-sumx-minx-maxx.md) — iterators that establish row context while respecting filter context
- [CALCULATE](/wiki/calculate.md) — context transition (row → filter) is a core CALCULATE behavior
- [HASONEVALUE](/wiki/hasonevalue.md) — detecting whether a filter has collapsed to a single value (vs. a total row)
