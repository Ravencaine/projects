---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: atomic
tags: [power-bi, data-modeling, date-table, best-practice]
---

# Auto Date Time Disable

Turn off Power BI's automatic hidden date tables to take control of your data model.

## Definition

When a date column is added to a Power BI model, Power BI auto-creates hidden date tables behind the scenes. Each date column gets its own auto-generated table. For quick reports this is convenient, but in a real semantic model this creates bloat — multiple hidden tables that impact performance and obscure your intentional data model.

## Key Points

- Auto Date Time creates **hidden, separate date tables** for every date column — not a shared calendar
- Multiple date columns in a single model = multiple hidden date tables (one per column)
- DAX Studio shows the bloat: a model with 5 date columns creates 5 hidden date tables
- **Global setting** (File → Options → Data Load): turns off Auto Date Time for all future `.pbix` files
- **Current file setting**: turns it off only for the active file
- **Mark as Date Table**: designates a central date table, reducing the hidden table count by 1 per date column connected to it
- Switching relationships from integer keys to actual date columns further reduces hidden tables
- **Warning**: disabling after building visuals with auto hierarchies will break those visuals — test before flipping

## Examples

**Global disable:**
File → Options → Data Load → Auto Date Time → uncheck

**Mark as Date Table:**
Right-click a date column → Calendar Options → Mark as Date Table → choose the full date column → Save

**Switch relationships:**
Change relationship from integer key to full date column → reduces hidden tables

## Related

- [[Measure-Table-Dedicated]] — another model hygiene pattern
- [[auto-date-time-hidden-bloat]] — existing note on the bloat problem
