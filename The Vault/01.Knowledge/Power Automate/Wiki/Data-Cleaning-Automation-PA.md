---
created: 2026-08-11
source: How I Use Power Automate as a Finance Analyst to Prepare Management Reports.md
note_type: workflow
tags: [power-automate, data-cleaning, automation, finance, data-quality]
---

# Data Cleaning Automation (Power Automate)

Automated workflow that removes duplicates and standardises date formats in transaction data using Power Automate's built-in data operations.

## Prerequisites

- Source data in a SharePoint List, Excel table, or SQL Database accessible to the flow
- SharePoint List or Excel table with write permissions
- Consistent column naming across source data

## Steps

1. **Trigger** — Recurrence (daily/weekly/monthly) or SharePoint list item Created/Modified
2. **Get data** — List rows present in a table (SharePoint List, Excel, SQL)
3. **Remove duplicates** — use Power Automate's **Remove duplicate items** action on the dataset; deduplication key = transaction ID or composite key (date + amount + description)
4. **Compose — Date standardisation** — apply `formatDateTime(item()?['Date'], 'yyyy-MM-dd')` to every date field to produce ISO 8601 consistency
5. **Parse JSON** — structure the cleaned output as an array for downstream steps
6. **Create table** / **Update table rows** — write cleaned data back to SharePoint List or Excel
7. **Log** — create an entry in a cleaning log table (SharePoint List or SQL) recording rows processed, duplicates removed, date format applied
8. **Notify** — send a Teams message or email confirming clean data is ready

## Variations

- **Multi-source merge first:** add a **Join** step before deduplication to consolidate data from multiple regions before cleaning
- **Conditional cleaning:** add a **Condition** step to flag or remove records where a required field is blank before deduplication
- **AI anomaly detection:** insert **Detect anomalies using AI Builder** after cleaning to flag unusual transaction amounts

## Common Errors

- **Null date fields** — the formatDateTime expression fails if the field is null; guard with `if(empty(...), null, formatDateTime(...))`
- **Composite duplicate key** — deduplicating on a single column (e.g., date alone) can remove valid records; use a composite key or Power Automate's built-in duplicate detection with the right key

## Related

- [[PA-Finance-Report-Pipeline]] — pipeline that includes this step
- [[Source-Kaklotar-10-Power-Automate-Flows]] — broader PA flow patterns
