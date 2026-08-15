---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Drop-Down Lists in Excel • My Online Training Hub"
note_type: atomic
tags: [excel, xlookup, auto-fill, dropdown, related-data, structured-reference, interactive-form, lookup]
---

# XLOOKUP for Auto-Filling Related Data from Dropdown

When a user selects an item from a dropdown, XLOOKUP can automatically populate other fields with related data from a lookup table — transforming a dropdown into an interactive form.

## Formula

```
=XLOOKUP([@[Employee Name]], EmployeeDatabaseTable[Employee Name], EmployeeDatabaseTable[Department], "")
```

## How It Works

| Step | Expression | Meaning |
|------|-----------|---------|
| 1 | `[@[Employee Name]]` | Current row's Employee Name cell (structured ref) |
| 2 | `EmployeeDatabaseTable[Employee Name]` | Lookup column |
| 3 | `EmployeeDatabaseTable[Department]` | Return column (Department) |
| 4 | `""` | If not found, return empty string |

Copy the formula across to additional columns (e.g. Hourly Rate) — change the return column to `EmployeeDatabaseTable[Hourly Rate]`.

## Use Cases

- Employee form: name → department + rate
- Product form: product → category + price
- Client form: client → account manager + contract value

## Why XLOOKUP

| | XLOOKUP | VLOOKUP / INDEX+MATCH |
|--|---------|----------------------|
| Direction | Left or right | Right only (VLOOKUP) |
| Exact match default | Yes | No (needs 4th arg = 0) |
| Clean syntax | Single function | Two functions |

## Related

- [[Source-Dynamic-Drop-Down-Lists-Mynda-Treacy]] — source
- [[Cascading-Dropdowns-SORT-FILTER-XLOOKUP]] — XLOOKUP also used to expose spill range to DV for cascading dropdowns
