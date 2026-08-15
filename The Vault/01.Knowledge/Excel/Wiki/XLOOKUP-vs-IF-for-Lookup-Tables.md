---
created: 2026-08-09
updated: 2026-08-09
source: "6 Better Alternatives to the Excel IF Function • My Online Training Hub"
note_type: atomic
tags: [excel, formulas, xlookup, lookup-table, if, maintainability, hard-coded-values]
---

# XLOOKUP vs IF for Lookup Tables

When a formula maps one value to another (region code → commission rate), it is a lookup problem, not a logic problem. Store the mapping in a table and use XLOOKUP — maintain the table, not the formula.

## The IF Anti-Pattern

Region code → commission rate via nested IF:
```
=IF(D6="N", 5%,
IF(D6="S", 6%,
IF(D6="E", 7%, 0%)))
```
Rules are buried in the formula. Change a rate → edit the formula. Add a region → rewrite the formula.

## The XLOOKUP Pattern

**1. Create a lookup table** (`CommRates` with columns Region Code, Rate).

**2. Use XLOOKUP:**
```
=XLOOKUP(D6, CommRates[Region Code], CommRates[Rate], 0%)
```
- D6: the value to look up
- CommRates[Region Code]: where to search
- CommRates[Rate]: what to return
- 0%: if-not-found result

Now the commission rules are in a table. Change a rate → update the table. Add a region → add a row. If the table is an Excel Table, the formula range expands automatically.

## Comparison

| Nested IF | XLOOKUP |
|-----------|---------|
| Logic inside the formula | Retrieves from a table |
| Harder to update | Easier to maintain |
| Rules buried in formula | Rules visible in a table |
| New items → formula rewrite | New items → table row |

## When to Use XLOOKUP

- Matching one value to another
- Returning a value from a table
- Rules that may change over time
- Clean formula that anyone can update

Rule of thumb: if you're matching one item to another item, use a lookup table.

## Related

- [[Source-6-Better-Alternatives-to-IF-Mynda-Treacy]] — source
- [[IFS-vs-Nested-IF-Order-Matters]] — IFS is for logic; XLOOKUP is for lookup
