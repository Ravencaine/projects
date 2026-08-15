---
created: 2026-08-09
updated: 2026-08-09
source: "5 Boring Excel Functions That Are Secretly Brilliant • My Online Training Hub"
note_type: atomic
tags: [excel, functions, rept, in-cell-charts, visualization, dashboards, kpi]
---

# REPT: In-Cell Bar Charts

`REPT(text, number_of_times)` repeats text a specified number of times. Combined with number columns, it creates bar charts directly inside worksheet cells — no chart objects needed.

## Syntax

```
=REPT(text, number_of_times)
```

Example: `=REPT("●", 5)` → `●●●●●`

## Use Case: In-Cell Bar Chart

```
=REPT("█", Sales)
```
Repeats the block character `█` once per unit of Sales — creates a horizontal bar proportional to the value.

## Why It's Powerful

- No chart object to insert or resize
- Bars resize automatically when data changes
- Works inside any cell — can be embedded in tables, dashboards, KPI reports
- Characters are fully customisable: `●`, `█`, `★`, shaded symbols

## Best Uses

- Dashboards
- KPI reports and scorecards
- Heat maps (using colour via conditional formatting)
- Executive summaries
- Any report where a visual bar adds context without a full chart

## Related

- [[Source-5-Boring-Excel-Functions-Mynda-Treacy]] — source
