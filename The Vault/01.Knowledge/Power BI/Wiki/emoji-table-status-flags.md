---
created: 2026-08-02
updated: 2026-08-05
source: 10 Ways to Use Emojis in Power BI
note_type: pattern
tags: [power-bi, emoji, table, status, formatting, dax]
---

# Emoji Table Status Flags — Progress, Risk, Completion

Add emoji status columns to tables so they remain scannable even in export mode — no conditional formatting dependency.

## Status Emoji DAX Pattern

```c
Status Emoji :=
SWITCH(
    TRUE(),
    [Progress %] = 1,   "✅",   // Complete
    [Progress %] > 0.5, "⚠️",   // In Progress
    "❌"                   // Overdue / Not Started
)
```

## Extended Status Set

| Status | Emoji | Condition |
|--------|-------|-----------|
| Complete | ✅ | `Progress = 1` |
| In Progress | 🔄 | `0 < Progress < 1` |
| On Hold | ⏸️ | `Status = "Hold"` |
| Overdue | ⛔ | `DueDate < TODAY() AND Progress < 1` |
| Not Started | ⬜ | `Progress = 0` |

## Why It Works in Exports

Emojis are Unicode text — they survive CSV export, Excel paste, and PowerPoint copy without losing formatting. Conditional formatting (colors, icons) does not.

## Related

- [[emoji-data-label-pattern]] — emoji in labels
- [[emoji-axis-category-labels]] — emoji on axis categories
