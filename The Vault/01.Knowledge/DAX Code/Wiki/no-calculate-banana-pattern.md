---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [no-calculate, pattern, beginner]
---

# No CALCULATE Banana Pattern

The foundational DAX pattern: `FILTER` a table into a variable, then aggregate it with an X aggregator — no `CALCULATE` required.

## Purpose

This pattern is the cornerstone of Deckler's "No CALCULATE" philosophy. It provides a consistent, readable, and debuggable structure for nearly any DAX calculation by decomposing the problem into three discrete steps: **exclude**, **filter**, and **aggregate**. Each step is stored in a named `VAR` so the logic is transparent at every layer.

Use this pattern whenever you need to filter rows before aggregating — e.g. summing costs excluding a category, finding the min/max subject to a condition, or any aggregation that is not simply "all rows."

## Components

1. **`VAR __ExcludeItem`**: define the exclusion/filter criterion (any scalar value)
2. **`VAR __Table`**: `FILTER()` the source table by the criterion
3. **`VAR __Result`**: an X aggregator (`SUMX`, `MINX`, `MAXX`, `AVERAGEX`, etc.) over the table variable

## Structure

```dax
Sum Total Cost No Pickle =
VAR __ExcludeItem = "Pickle"
VAR __Table = FILTER( 'Table', 'Table'[Item] <> __ExcludeItem )
VAR __Result = SUMX( __Table, [Total Cost] )
RETURN
    __Result
```

## Example

Summing the `Total Cost` column for all rows where the `Item` is **not** "Pickle":

```dax
Sum Total Cost No Pickle =
VAR __ExcludeItem = "Pickle"
VAR __Table = FILTER( 'Table', 'Table'[Item] <> __ExcludeItem )
VAR __Result = SUMX( __Table, [Total Cost] )
RETURN
    __Result
```

Result: **38.89** (sum of all non-Pickle rows)

The same 3-step structure applies for min, max, count, etc. — just swap the X aggregator.

## How It Differs from CALCULATE

| Aspect | No CALCULATE (Banana Pattern) | CALCULATE |
|--------|-------------------------------|-----------|
| Philosophy | Explicitly build a filtered table, then aggregate | Implicitly change the filter context |
| Debugging | Each `VAR` is independently inspectable | Acts as a "black box" — no intermediate steps |
| Learning curve | Predictable, compositional structure | Requires understanding context transition, filter arguments, and modifier order |
| Complexity ceiling | Can scale to dozens of lines but stays readable | Can become deeply opaque at scale |

Deckler's thesis: `CALCULATE` is a "fancy FILTER." It does the same job but hides the intermediate table logic, making it much harder to reason about and debug. The Banana Pattern makes the filtering step first-class and visible.

## Variations

- **MINX variant**: find minimum cost excluding an item:
  ```dax
  Min Total Cost Not Pickle =
  VAR __ExcludeItem = "Pickle"
  VAR __Table = FILTER( 'Table', 'Table'[Item] <> __ExcludeItem )
  VAR __Result = MINX( __Table, [Total Cost] )
  RETURN
      __Result
  ```
- **Compound filter**: exclude multiple items using `|`:
  ```dax
  VAR __Table = FILTER( 'Table',
      'Table'[Item] <> "Pickle" && 'Table'[Item] <> "Grapefruit"
  )
  ```
- **Nested lookups**: `FILTER` → `MAXX` to "look up" a value by finding the max row meeting criteria.

## Related

- [No CALCULATE vs CALCULATE](/wiki/no-calculate-vs-calculate-deckler.md) — direct comparison of both approaches
- [DAX Variables (VAR/RETURN)](/wiki/dax-variables-var-return.md) — the variable conventions that power this pattern
- [X Aggregators (SUMX/MINX/MAXX)](/wiki/x-aggregators-sumx-minx-maxx.md) — the aggregation half of the pattern
- [FILTER](/wiki/filter.md) — the filtering function
- [TOCSV Debugging Pattern](/wiki/dax-debugging-tocsv.md) — how to inspect table variables mid-formula
