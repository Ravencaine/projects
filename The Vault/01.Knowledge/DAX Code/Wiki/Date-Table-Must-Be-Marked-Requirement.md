---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Where Everything You've Learned About Context Finally Pays Off
source_url: https://medium.com/@jeseenaparveenk/dax-time-intelligence-where-everything-youve-learned-about-context-finally-pays-off-8de1bb67adcb
note_type: atomic
tags: [dax, date-table, prerequisite, mark-as-date-table, best-practice]
---

# A Proper Marked Date Table Is a Prerequisite for All Time Intelligence Functions

Every DAX time intelligence function requires a dedicated, correctly marked Date table. Auto date/time in Power BI is not sufficient.

## Requirements for a Valid Date Table

- One row per date, no gaps, covering the full range of your data (and ideally a bit beyond)
- A single, clean Date column connected to fact tables
- Marked as a Date Table in Power BI: right-click the table → Mark as date table
- If not set up correctly, every time intelligence function will break or return wrong results silently

## Mark as Date Table — Why It Matters

Marking the table does two things:
1. Enables the time intelligence functions to work correctly against that column
2. Allows Power BI to use it for auto-exists filtering between the date column and the fact table

Without marking, DAX may evaluate time functions against the wrong date context, especially when combining multiple date columns in a model.

## Related

- [[Time-Shift-Functions-DATEADD-SAMEPERIODLASTYEAR-PARALLELPERIOD]] — DATEADD, SAMEPERIODLASTYEAR, PARALLELPERIOD
- [[Running-Total-Functions-TOTALMTD-TOTALQTD-TOTALYTD]] — TOTALMTD/QTD/YTD and their DATES counterparts
- [[Rolling-Window-Functions-DATESINPERIOD]] — DATESINPERIOD with LASTDATE for rolling trailing windows
- [[Custom-Date-Range-DATESBETWEEN]] — DATESBETWEEN for precise fixed date windows
- [[Time-Intelligence-Is-CALCULATE-With-Date-Table]] — every time intelligence function is CALCULATE with a date table filter modifier
