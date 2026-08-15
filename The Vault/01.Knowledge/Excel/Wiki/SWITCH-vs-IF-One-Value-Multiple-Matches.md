---
created: 2026-08-09
updated: 2026-08-09
source: "6 Better Alternatives to the Excel IF Function • My Online Training Hub"
note_type: atomic
tags: [excel, formulas, switch, dropdown, dynamic-calculation, if, dashboards]
---

# SWITCH vs IF: One Value, Multiple Matches

`SWITCH` tests one value once and returns different results — including different calculations — for each possible option. Unlike XLOOKUP (which returns values from a table), SWITCH can return entirely different formulas per option.

## SWITCH Syntax

```
=SWITCH(
  expression,
  option1, result1,
  option2, result2,
  ...
  default_result
)
```

The expression is tested once. Each option is compared to it. The matching option's result is returned.

## Example: Dropdown-Driven Report

User selects a metric from a dropdown: Total Sales, Total Profit, Profit Margin, Average Selling Price.

SWITCH handles each option with its own calculation:
```
=SWITCH(
  C15,
  "Total Sales",         SUM(D6:D9),
  "Total Profit",        SUM(G6:G9),
  "Profit Margin",       SUM(G6:G9)/SUM(D6:D9),
  "Average Selling Price", SUM(D6:D9)/SUM(F6:F9),
  "Select a valid metric"
)
```
C15 is tested once. Each option triggers a different formula. The final default string handles unexpected input.

## SWITCH vs XLOOKUP

| | SWITCH | XLOOKUP |
|--|--------|---------|
| Returns | Different formulas per option | Values from a table |
| Use case | Each option needs different logic | Same lookup against a table |
| Example | Dropdown → different calculations | Region code → commission rate |

SWITCH: when each option triggers a different calculation.
XLOOKUP: when all options retrieve from the same column.

## When to Use SWITCH

- One value tested against several options
- Each option returns a different result or calculation
- The same cell is repeated in a nested IF
- Dropdown-driven reports, dashboards, KPI selectors
- Reports where the user selects the calculation type

## Related

- [[Source-6-Better-Alternatives-to-IF-Mynda-Treacy]] — source
- [[XLOOKUP-vs-IF-for-Lookup-Tables]] — XLOOKUP retrieves from table; SWITCH returns different calculations
