---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

note_type: pattern
tags: [excel, pivot-table, pattern]
---

-----|--------|
| Do Not Show Subtotals | Removes all subtotals |
| Show all Subtotals at Bottom | Default — subtotals at bottom of each group |
| Show all Subtotals at Top | Subtotals appear before the rows they summarize |

## Grand Totals

Access via: `Pivot Table Tools → Design → Grand Totals`

| Option | Result |
|--------|--------|
| Off for Rows and Columns | No grand total row or column |
| On for Rows and Columns | Total of all rows AND all columns |
| On for Rows Only | Total column only |
| On for Columns Only | Total row only |

## Practical Implications

- **Remove subtotals** when there are many hierarchical levels — reduces visual noise
- **Remove Grand Total column** when you only need row totals (often the case)
- **Subtotals at top** works better for left-to-right hierarchies (geography > product > color)

## Source Reference

Chapter 3, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
