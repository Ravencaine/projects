---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [auto-date-time, power-bi, date-hierarchy, calendar-table]
---

# Auto Date/Time in Power BI

Power BI automatically creates hidden date tables when this option is enabled, enabling time-intelligent DAX and date hierarchies without manual calendar table creation.

## Definition

When **Auto Date/Time** is enabled (default), Power BI creates a hidden date table for every date column in your model. This enables:

- Automatic date hierarchies in visuals (Year → Quarter → Month → Day)
- Time-intelligence DAX functions (TOTALYTD, SAMEPERIODLASTYEAR, etc.)
- Correct date sorting without explicit calendar tables

## Key Points

- Enabled per-file under File → Options → Data Load → Auto Date/Time
- Best for simple date hierarchies — for complex fiscal calendars or custom date logic, create explicit date tables
- Hidden tables are automatically managed; they don't appear in the Fields pane
- Can be disabled to improve import speed for large models

## Related

- [[dim-date-dax-calendar]]
- [[time-series-data-requirements]]
