---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

note_type: pattern
tags: [excel, pattern]
---

-----|----------|
| New | Add a blank record |
| Delete | Remove the current record |
| Restore | Undo changes |
| Find Prev/Next | Navigate records |
| **Criteria** | Enter filter conditions |

## Criteria Mode

Click **Criteria** to enter filter conditions — then use **Find Next** / **Find Prev** to navigate only matching records.

### Example Criteria
```
City: Oakland
```
Shows only records where City = Oakland.

## When to Use

- Single table, simple filter — no Pivot Table overhead
- Data entry form without creating a UserForm
- Quick lookups in small-to-medium tables

## Source Reference

Chapter 2, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
