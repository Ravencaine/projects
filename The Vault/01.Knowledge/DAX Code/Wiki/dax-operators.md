---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: reference
tags: [dax, reference, operators]
---

# DAX Operators: Arithmetic, Comparison, Logical, and Text

Complete reference for all operator types available in DAX formulas.

## Quick Reference

### Arithmetic Operators

| Operator | Operation | Example |
|----------|-----------|---------|
| `+` | Addition | `[TotalSales] + [TotalCost]` |
| `-` | Subtraction | `[StoreSales2009] - [StoreSales2008]` |
| `*` | Multiplication | `[UnitPrice] * [SalesQuantity]` |
| `/` | Division | `[TotalProfit] / [TotalSales]` |
| `^` | Exponentiation | `2 ^ 10` |

### Comparison Operators

| Operator | Operation |
|----------|-----------|
| `=` | Equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `<>` | Not equal to |

### Logical Operators

| Operator | Operation | Description |
|----------|-----------|-------------|
| `&&` | AND | Both conditions must be true |
| `|` | OR | Either condition must be true |

### Text Concatenation Operator

| Operator | Operation | Example |
|----------|-----------|---------|
| `&` | Concatenation | `"Product: " & [ProductName]` |

## Notes

- When filtering in `CALCULATE()`, use `=` for text comparisons: `ChannelName = "Store"` (no quotes around the table/column, quotes around the value)
- Multiple `CALCULATE()` filter arguments are combined with AND — use `|` for OR within a single filter expression
- The division operator `/` returns a decimal — format the result cell as Percentage for profit/sales ratios
- Identifiers (calculated field names) must be enclosed in square brackets: `[StoreSales]`

## Related

- [[dax-calculate-function]] — using comparison operators in filter arguments
- [[dax-year-over-year]] — arithmetic and comparison operators in practice
- [[dax-left-function]] — LEFT for text extraction before comparison
