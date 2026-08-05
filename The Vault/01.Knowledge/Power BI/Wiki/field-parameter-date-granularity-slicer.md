---
created: 2026-08-02
source: Power BI Time Hacks: Mastering Dynamic Date Views
note_type: pattern
tags: [powerbi, pattern, field-parameter, dynamic-axis, date-granularity, slicer]
---

# Field Parameter for Date Granularity Selector

A field parameter exposing all columns from a calendar table enables a single slicer to switch the X-axis granularity between Daily, Weekly, and Monthly views.

**Setup:**
1. **Modeling → New parameter → Fields** — select all columns from the Calendar table (e.g. `'Calendar'[Daily]`, `'Calendar'[Weekly]`, `'Calendar'[Monthly]`)
2. Enable **`Add slicer to this page`** in the parameter dialog — creates a native slicer on the canvas
3. Format the slicer (new slicer visual, formatting options) to match the report theme

**Result:** selecting a granularity option in the slicer changes which calendar column appears on the visual axis. Use in bar charts, line charts, and KPI cards with `SELECTEDVALUE('Date Granularity'[Data Granularity Fields])` to branch DAX logic.

> See `dynamic-granularity-aggregation-switch.md` for the DAX measures that respond to this selection.
