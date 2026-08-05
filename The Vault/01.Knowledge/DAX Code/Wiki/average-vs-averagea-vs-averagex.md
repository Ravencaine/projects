---
created: 2026-08-01
updated: 2026-08-02
source: "Unraveling DAX Functions The Mystery Behind AVERAGE, AVERAGEA, and AVERAGEX.md"
note_type: atomic
tags: [dax, average, averagea, averagex, BLANK, boolean, text, beginner]
---

# AVERAGE vs AVERAGEA vs AVERAGEX

## Three Variants

| Function | Scope | Non-Numeric Values |
|----------|-------|--------------------|
| `AVERAGE` | Column | Ignored (BLANK returned if all non-numeric) |
| `AVERAGEA` | Column | Included: TRUE=1, FALSE=0, numeric-text converted |
| `AVERAGEX` | Expression per row | Depends on expression result |

## AVERAGE

Simple arithmetic mean of numeric values only.

```c
AVERAGE(Sales[Price])
```

- Ignores BLANK, text, and Boolean values
- Returns BLANK if column has zero numeric values
- Use for clean numeric columns only

## AVERAGEA — Include All Value Types

**"A" = includes All value types** (text, Boolean, numeric-text).

```c
AVERAGEA(Sales[Value])
```

Example: values `10, 15, TRUE, "5", FALSE`

| Function | Calculation | Result |
|----------|-------------|--------|
| `AVERAGE` | (10+15)/2 | 12.5 |
| `AVERAGEA` | (10+15+1+5+0)/5 | 6.2 |

Rules: TRUE=1, FALSE=0, numeric-text converted, text="0" treated as 0.

**When to use AVERAGEA:** Columns with mixed data types where you want Booleans and text-numbers counted.

## AVERAGEX — Iterator with Expression

**"X" = iterates over table, evaluates expression per row, then averages the results.**

```c
AVERAGEX(Sales, Sales[Quantity] * Sales[Price])
```

Example: Product table

| Product | Quantity | Price |
|--------|----------|-------|
| Apple | 3 | 2.5 |
| Banana | 2 | 1.5 |
| Orange | 5 | 3.0 |

- Row expressions: 3×2.5=7.5, 2×1.5=3.0, 5×3.0=15.0
- Average: (7.5+3.0+15.0)/3 = **8.5**

## Quick Decision Tree

```
Is your data a simple numeric column?
├── YES → AVERAGE (ignore non-numeric)
└── NO  → Does the column have mixed types you want counted?
    ├── YES → AVERAGEA
    └── NO  → Do you need row-level expression?
        ├── YES → AVERAGEX
        └── NO  → AVERAGE
```

## Gotchas

- `AVERAGEA` treats `"5"` as 5, but `"abc"` is still ignored (only numeric-text converts)
- `AVERAGE` returns BLANK (not an error) when all values are non-numeric
- `AVERAGEX` creates a row context — context transition applies to any nested CALCULATE calls
- AVERAGEX with a simple column reference is slower than AVERAGE (use AVERAGE for flat columns)
