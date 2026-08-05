---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, excel, beginner, mindset, context]
---

# DAX vs Excel: The Mindset Shift

DAX looks like Excel formulas but works completely differently. The biggest mistake beginners make: assuming that knowing Excel means knowing DAX.

## The Excel Mindset

```
=SUM(B2:B100)
```

You reference specific cells. The formula calculates those exact cells. Always the same result regardless of context.

**Result:** 100% predictable, independent of anything else in the spreadsheet.

## The DAX Mindset

```dax
Total Revenue = SUM(Orders[TotalAmount])
```

You reference a column. What gets summed changes based on context — what slicers are selected, what the visual is filtered to, what relationships are active.

**Result:** Changes based on filter context. Same formula, different answer depending on what the user is looking at.

## The Core Difference

| Excel | DAX |
|-------|-----|
| References cells | References columns |
| Always the same result | Result changes with context |
| Independent | Context-aware |
| No relationships | Relationships drive context |
| One formula = one calculation | One measure = many possible results |

## Why This Matters

Excel: `=SUM(B2:B100)` always returns the same value.

DAX: `=SUM(Orders[TotalAmount])` returns:
- All-time total revenue when no filters are active
- Only 2024 revenue when Year = 2024 is selected
- Only Technology category revenue when that filter is active
- Revenue for the specific customer row in a table visual

The same formula produces four different answers. That's not a bug — that's the feature.

## The Mental Model

> **Excel:** "Add up these specific cells."
> **DAX:** "Add up this column, but only the rows that match whatever the user is currently looking at."

DAX formulas don't live in isolation — they live inside a report that has relationships, filters, slicers, and visual-level contexts. The formula responds to all of them.

## Related

- [[row-context-vs-filter-context]] — the two types of context that drive DAX behaviour
- [[calculate-context-modifier]] — how to change the filter context
- [[basic-aggregation-measures]] — the foundational DAX measures that demonstrate context in action
