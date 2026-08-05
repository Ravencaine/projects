---
created: 2026-08-02
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: function
tags: [dax, measure, date, max]
---

# Maximum Date

Returns the maximum date in the `Date` column — used as the dynamic anchor for current-period measures.

```dax
Maximum Date = MAX('Process Duration'[Date])
```

## Usage

The returned date drives all current-period calculations: it adapts automatically as the dataset refreshes without hard-coding a date.

## See Also

- [[max-date-pattern-rolling-window.md]] — rolling window variant using MAX as anchor
- [[datesinperiod-rolling-12-month-window.md]] — DATESINPERIOD rolling window pattern

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
