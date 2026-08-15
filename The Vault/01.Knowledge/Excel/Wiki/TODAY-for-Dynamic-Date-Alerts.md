---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, conditional-formatting, today, date, deadline, overdue, alert, dynamic]
---

# TODAY() for Dynamic Date Alerts

`=TODAY()` recalculates on every workbook recalculation. Combined with conditional formatting, it creates self-updating date alerts: overdue contracts, upcoming deadlines, items due within a window.

## Common Patterns

| Alert type | Formula |
|-----------|---------|
| Overdue | `=$G7<=TODAY()` |
| Due within 7 days | `=$G7<=TODAY()+7` |
| Due within 30 days | `=$G7<=TODAY()+30` |
| Future-only threshold | `=$G7>TODAY()+90` |

## Priority Rule

When multiple alert levels exist, order rules in CF Manager:
1. **Overdue (red):** highest priority, most urgent
2. **Due soon (yellow):** secondary
3. **Future (green):** lowest priority

Strict/urgent rules must appear above general rules so they take precedence.

## Key Benefit

No manual updates. Open the workbook tomorrow and TODAY() has shifted by one day — alerts update automatically.

## Related

- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
- [[Rule-Priority-in-CF-Manager]] — priority: overdue rules above upcoming
