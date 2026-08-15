---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
note_type: workflow
tags: [excel, conditional-formatting, rule-priority, manage-rules, overlapping-rules, priority-order]
---

# Rule Priority in CF Manager

When multiple conditional formatting rules apply to the same range, the order they appear in CF Manager determines which format wins. Stricter rules must be above more general ones.

## The Priority Principle

- Rules at the **top** of the list have higher priority
- When a row satisfies multiple rules, the **first matching rule** in the list wins
- CF stops evaluating after the first match (unlike DAX's CALCULATE which continues)

## Practical Priority Order

When using multiple alert levels, strict rules must be above gentler ones:

```
1. Overdue (red)    ← most urgent, top position
2. Due in 7 days (yellow)
3. Due in 30 days (light yellow)
4. General row format (lowest priority, bottom)
```

## How to Set Priority

1. Select the range → Conditional Formatting → Manage Rules
2. Rules appear in evaluation order (top = highest priority)
3. Use "Move Up" / "Move Down" to reorder
4. Apply → OK

## Common Mistake

Putting a general rule above a specific one. Example: a general "highlight all rows" rule above a "highlight overdue" rule means overdue rows never get their specific format — the general rule fires first and CF stops.

## Related

- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
- [[TODAY-for-Dynamic-Date-Alerts]] — example of priority with date thresholds
