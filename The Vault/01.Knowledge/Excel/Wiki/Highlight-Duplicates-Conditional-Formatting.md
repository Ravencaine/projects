---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, duplicate, conditional-formatting, inspect, highlight, data-quality]
---

# Highlight Duplicates with Conditional Formatting

Using Home → Conditional Formatting → Duplicate Values to visually inspect duplicate records before deleting — avoiding the mistake of blindly removing rows that are legitimately identical.

## The Risk

Jumping straight to **Remove Duplicates** without inspection can delete valid records. Two customers with the same name who placed identical orders on the same day are not necessarily errors.

## Steps

1. Select the column or range to check
2. Go to **Home → Conditional Formatting → Highlight Cells Rules → Duplicate Values**
3. Excel highlights duplicate values in light red with dark red text
4. Review highlighted rows — confirm whether they are actual errors before taking action

## After Inspection: Remove Duplicates

Once confirmed, remove with:
**Data → Remove Duplicates** (select columns to consider, not all columns)

## When to Inspect vs Remove Directly

| Situation | Action |
|-----------|--------|
| Large transaction dataset, many near-duplicates | Inspect first with Conditional Formatting |
| Small, known-clean dataset | Remove Duplicates directly is fine |
| De-duplicating a dimension table | Always inspect — dimension keys must be unique |
| De-duplicating a fact table | Inspect — fact tables can have legitimately identical rows |

## Limitation

Conditional Formatting highlights any value that appears more than once — it cannot distinguish between "two genuine duplicates" and "one genuine + one error duplicate." Context matters.

## Related

- [[Duplicate-Records-Detection-Removal]] (Data Modeling) — COUNTROWS vs DISTINCTCOUNT DAX check, PQ Remove Duplicates
- [[3-Minute-Data-Cleaning-Checklist]] — duplicate check is step 3 of the 7-step checklist
