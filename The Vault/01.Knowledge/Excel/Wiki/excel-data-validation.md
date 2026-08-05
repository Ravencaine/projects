---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

note_type: pattern
tags: [excel, pattern]
---

---|-------------|
| Whole number | Integer values only |
| Decimal | Numbers within a range |
| List | Dropdown menu |
| Date | Valid dates |
| Time | Valid times |
| Text length | Minimum/maximum characters |
| Custom | Formula-based validation |

## List Validation (Dropdown)

```
Allow: List
Source: =$A$1:$A$10
```

Creates a dropdown arrow in the cell. Ensures consistent values (no typos).

## Error Alerts

When a user enters invalid data:

| Style | Behavior |
|-------|----------|
| Stop | Rejects the entry entirely |
| Warning | Prompts to accept anyway |
| Information | Informational only |

## Common Pattern: In-Column Dropdown

```
Allow: List
Source: =RegionList   ' Named range
```

## Source Reference

Chapter 2, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
