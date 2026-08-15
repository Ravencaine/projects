---
created: 2026-08-11
updated: 2026-08-11
source: "11-Power-BI-Tips-Guy-in-a-Cube-Transcript.md"
note_type: gotcha
tags: [power-bi, auto-date-time, gotcha]
---

# Gotcha: Auto Date/Time Hidden Table Bloat

Power BI auto-creates hidden date tables for every date column. In models with multiple date columns (booking date, satisfaction date, etc.), this creates 3-5 hidden date tables per date column — model bloat with no visibility.

## Expected Behaviour

Auto Date/Time creates useful date hierarchies quickly for ad-hoc reports.

## Actual Behaviour

Each date column spawns a hidden date table. Connect to DAX Studio or Tabular Editor and you see 4+ hidden date tables consuming memory. Switching the relationship from integer key to actual date reduces them but doesn't eliminate all.

## Why It Happens

Power BI creates Auto Date/Time tables automatically for any column marked as a date type. No explicit action required.

## How to Handle It

1. **Global setting:** File → Options → Data Load → uncheck Auto Date/Time (applies to all future files)
2. **Per-file setting:** File → Options → Current File → Data Load → uncheck Auto Date/Time
3. **For existing hidden tables:** Mark the correct date table as date table (Modeling → Mark as date table) → switch the relationship from integer key to actual date → hidden table disappears
4. **Warning:** If a visual uses the auto date hierarchy, switching off breaks that visual — test first

## Related

- [[dim-date-dax-calendar]] — building a proper date dimension
- [[auto-date-time-hidden-bloat]] — deeper analysis of the bloat mechanism
