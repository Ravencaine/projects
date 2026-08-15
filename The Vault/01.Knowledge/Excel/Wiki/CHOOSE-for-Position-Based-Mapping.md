---
created: 2026-08-09
updated: 2026-08-09
source: "6 Better Alternatives to the Excel IF Function • My Online Training Hub"
note_type: atomic
tags: [excel, formulas, choose, position-mapping, month, quarter, financial-year, index]
---

# CHOOSE for Position-Based Mapping

`CHOOSE` maps a number (1–12) to a result based on its position in a list. The number represents a position, not a logical condition — making it ideal for month→quarter mappings, fiscal year calendars, and any indexed-label conversion.

## CHOOSE Syntax

```
=CHOOSE(index, value1, value2, ..., valueN)
```

Returns `value[index]`. If `index = 3`, returns the 3rd value.

## Example: Month Number → Financial Year Quarter

Financial year starts July. Month mapping:

| Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Q3  | Q3  | Q3  | Q4  | Q4  | Q4  | Q1  | Q1  | Q1  | Q2  | Q2  | Q2  |

Nested IF alternative:
```
=IF(D6<=3,"Q3",IF(D6<=6,"Q4",IF(D6<=9,"Q1","Q2")))
```

CHOOSE version:
```
="Q"&CHOOSE(D6, 3,3,3, 4,4,4, 1,1,1, 2,2,2)
```
D6 is the index (month number). The 12 arguments are the quarter values for positions 1–12. Prepend "Q" for display.

## Why CHOOSE Fits

The input is already a position number (1–12). Each position has exactly one result. CHOOSE is purpose-built for this — no conditional logic needed.

## When to Use CHOOSE

- Input is a number representing a position (1–12, 1–7, etc.)
- Each position maps to a known result
- Compact replacement for multiple IF statements
- Month-to-quarter, day-to-shift, index-to-label conversions
- Scenarios where a small fixed list needs to be mapped

## Related

- [[Source-6-Better-Alternatives-to-IF-Mynda-Treacy]] — source
