---
created: 2026-08-01
updated: 2026-08-02
source: "Multiple-Criteria Lookups in Excel Five Methods to Master.md"
note_type: atomic
tags: [excel, let, xmatch, index, lookup, multi-criteria, intermediate, 365]
---

# LET + XMATCH + INDEX: Named Sub-Expressions for Clarity and Speed

LET names intermediate calculations inside a formula. Combined with XMATCH and INDEX, it produces a clean, efficient, self-documenting multi-criteria lookup.

## Formula

```c
=LET(
  custMatch, Table1[Customer]=F1,
  prodMatch, Table1[Product]=G1,
  bothMatch, custMatch * prodMatch,
  idx,       XMATCH(1, bothMatch, 0),
  result,    INDEX(Table1[Sales], idx),
  IFNA(result, "Not found")
)
```

## How It Works

1. **LET** declares named sub-expressions — each is calculated once
2. `custMatch` — TRUE/FALSE array for customer match
3. `prodMatch` — TRUE/FALSE array for product match
4. `bothMatch` — the AND of both (same multiplication trick)
5. `XMATCH(1, bothMatch, 0)` — finds the first position where bothMatch = 1 (XMATCH is XLOOKUP's sister; returns position, not value)
6. `INDEX(Table1[Sales], idx)` — returns the value
7. `IFNA(…, "Not found")` — handles the no-match case cleanly

## Why LET Matters Here

Without LET, the same boolean arrays get calculated multiple times as the formula evaluates:

```
INDEX(Table1[Sales], XMATCH(1, (Table1[Customer]=F1) * (Table1[Product]=G1), 0))
```

With large tables and complex conditions, those repeated array calculations add up. LET calculates each array once.

## XMATCH vs MATCH

| Function | Excel Version | Features |
|----------|-------------|----------|
| MATCH | All | Exact, approximate, wildcard |
| XMATCH | 365 only | Exact, approximate, wildcard + binary search mode |

XMATCH supports binary search mode for extra speed on sorted data (`XMATCH(1, array, 0, -1)` for descending).

## When to Use

- Large datasets where repeated array calculations cause slowdown
- Formulas that need to be audited or maintained by others (self-documenting)
- 365-only environments (always check version requirements)
- When combining many criteria (each named step makes the formula readable)

## When NOT to Use

- Pre-365 Excel (LET and XMATCH unavailable)
- One-off simple lookups where readability overhead isn't worth it
- Very simple criteria where INDEX/MATCH array works fine

## Related

- [[index-match-multi-criteria-array]] — same logic without LET; requires Ctrl+Shift+Enter in older Excel
- [[xlookup-multi-criteria-concatenation]] — concatenation approach; no array formulas
- [[filter-function-multi-match]] — return all matches instead of just the first
