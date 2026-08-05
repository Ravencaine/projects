---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [debugging, tocsv, no-calculate, troubleshooting]
---

# TOCSV Debugging Pattern

A No CALCULATE debugging technique: use `TOCSV()` in the `RETURN` statement to visualize a table variable as CSV text inside a Card visual, revealing exactly which rows are in any intermediate `VAR`.

## Purpose

When a DAX measure returns an unexpected result (often BLANK), you need to inspect the intermediate table variables to understand why. `TOCSV` converts any table variable into comma-separated text that a Card visual can display — making table contents visible without leaving Power BI.

This is the primary debugging tool in the No CALCULATE workflow. It has no equivalent in the CALCULATE approach, where intermediate tables are opaque.

## Structure

```dax
<Debug Measure> =
VAR __Table = <some filtered table>
RETURN
    TOCSV( __Table )           -- default: 10 rows, comma-delimited, with headers
    -- or with options:
    TOCSV( __Table, 5 )        -- limit to 5 rows
    TOCSV( __Table, 10, "|" )  -- pipe delimiter
    TOCSV( __Table, 10, ",", FALSE )  -- no headers
```

## Example

```dax
Sum Total Cost Grapefruit and also Pickle =
VAR __Item1 = "Grapefruit"
VAR __Item2 = "Pickle"
VAR __Table = FILTER( 'Table', 'Table'[Item] = __Item1 )
VAR __Table1 = FILTER( __Table, 'Table'[Item] = __Item2 )
VAR __Result = SUMX( __Table1, [Total Cost] )
RETURN
    __Result   -- returns BLANK
```

**Debugging steps:**

1. Swap `RETURN __Result` → `RETURN COUNTROWS(__Table)` → Card shows `1`
2. Swap `RETURN __Result` → `RETURN COUNTROWS(__Table1)` → Card shows `(Blank)` — the empty table is the problem
3. Swap `RETURN __Result` → `RETURN TOCSV(__Table)` → Card shows the single Grapefruit row, confirming the filter logic

**Formatting tip (Henrik Vestergaard):** Use a Table visual instead of a Card for left-aligned output. Use the Consolas monospace font.

## TOCSV Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Table` | Table expression | Required | The table, VAR, or expression to convert |
| `MaxRows` | Integer | 10 | Maximum rows to display |
| `Delimiter` | Text | `,` | Column separator |
| `IncludeHeaders` | Boolean | TRUE | Whether to show column headers |

## Why This Only Works with No CALCULATE

With CALCULATE, there are no named intermediate table variables. The equivalent CALCULATE formula:
```dax
Sum Total Cost Grapefruit and also Pickle C =
CALCULATE(
    CALCULATE(
        SUM( 'Table'[Total Cost] ),
        'Table'[Item] = "Grapefruit"
    ),
    'Table'[Item] = "Pickle"
)
```
...has no native way to inspect the inner `CALCULATE`'s table. The function is a "black box."

## Related

- [No CALCULATE vs CALCULATE](/wiki/no-calculate-vs-calculate-deckler.md) — why debuggability is a core argument for No CALCULATE
- [No CALCULATE Banana Pattern](/wiki/no-calculate-banana-pattern.md) — the pattern that makes TOCSV debugging possible
- [EVALUATEANDLOG](/wiki/evaluateandlog.md) — server-side DAX query debugging
- [DAX Studio](/wiki/dax-studio.md) — external debugging tooling
