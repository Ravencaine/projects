---


title: "DAX Logical Operators (AND, OR)"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, logical]
note_type: function
description: "DAX logical operators — && (AND), | (OR), AND(), OR(). Used in FILTER, IF, and CALCULATE. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# DAX Logical Operators

## Operators

| Operator | Name | Description |
|----------|------|-------------|
| `&&` | AND | Both conditions must be true |
| `|` | OR | At least one condition must be true |
| `=` | Equal | Value matches |
| `<>` | Not equal | Value does not match |
| `>` | Greater than | — |
| `<` | Less than | — |
| `>=` | Greater or equal | — |
| `<=` | Less or equal | — |

## && (AND)

```dax
-- Both conditions must be true
Sales[Quantity] > 10 && Sales[Amount] > 1000
```

## | (OR)

```dax
-- Either condition (or both) must be true
Sales[Category] = "Electronics" | Sales[Category] = "Appliances"
```

## AND() and OR() Functions

These functions exist but are **less common** than the `&&` and `|` operators:

```dax
-- AND() equivalent:
AND( Sales[Qty] > 10, Sales[Amount] > 1000 )

-- OR() equivalent:
OR( Sales[Category] = "A", Sales[Category] = "B" )
```

Prefer `&&` and `|` — they are more readable and idiomatic DAX.

## In CALCULATE / FILTER Context

```dax
-- CALCULATE with AND
HighValueOnlineSales :=
CALCULATE(
    SUM( Sales[Amount] ),
    Sales[Amount] > 1000,
    Sales[Channel] = "Online"
)
```

## Source Reference

Chapter 7, DAX Operators section, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
