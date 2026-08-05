---
created: 2026-08-01
updated: 2026-08-02
source: "Multiple-Criteria Lookups in Excel Five Methods to Master.md"
note_type: atomic
tags: [excel, index, match, lookup, multi-criteria, array-formula, intermediate]
---

# INDEX/MATCH with Boolean Array Multiplication

INDEX/MATCH with array multiplication handles multiple criteria without helper columns or 365-only functions.

## Formula

```c
=INDEX(
  Table1[Sales],
  MATCH(
    1,
    (Table1[Customer]=F1) * (Table1[Product]=G1),
    0
  )
)
```

## How It Works

1. `(Table1[Customer]=F1)` — produces TRUE/FALSE array
2. `(Table1[Product]=G1)` — produces TRUE/FALSE array
3. `*` multiplies them → 1 where **both** are TRUE, 0 otherwise
4. `MATCH(1, …, 0)` — finds the row number where the product is 1
5. `INDEX(Table1[Sales], …)` — returns the value at that row

## Entry Method

| Excel Version | How to Enter |
|---------------|-------------|
| Excel 365 / 2021 | Normal formula (dynamic arrays handle it) |
| Excel 2019 and earlier | **Ctrl+Shift+Enter** (enter as array formula) |

In older Excel, the formula appears wrapped in `{curly braces}` after confirming with Ctrl+Shift+Enter.

## Comparison Table

| Aspect | Helper Column | INDEX/MATCH Array |
|--------|-------------|-------------------|
| Extra column needed | Yes | No |
| Version support | All | All (with CSE in older) |
| Performance | Excellent | Good on small-mid tables |
| Auditability | Easy (visible column) | Harder (hidden logic) |
| Readability | ★★★★★ | ★★★☆☆ |

## When to Use

- Small to mid-sized tables where performance is acceptable
- When you don't want to modify the source table structure
- When helper columns are not an option (shared workbook, read-only source)

## Related

- [[xlookup-multi-criteria-concatenation]] — alternative without array formulas
- [[filter-function-multi-match]] — return multiple matching rows
- [[let-xmatch-index-lookup]] — LET avoids recalculating arrays; 365-only
