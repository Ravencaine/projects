---
created: 2026-08-11
source: How I Use Power Automate as a Finance Analyst to Prepare Management Reports.md
note_type: pattern
tags: [power-automate, excel, template, report-generation, finance]
---

# Template-Based Report Generation (PA → Excel Template)

Power Automate pattern that populates a pre-built Excel template with live processed data, producing a consistent, professional management report on a schedule or trigger.

## Purpose

Manual report generation is error-prone and time-consuming. This pattern uses a standardised Excel template as a fixed layout — Power Automate fills the data fields automatically — ensuring consistent formatting every cycle with zero copy-paste.

## Components

1. **Excel Template file** — pre-built with headers, formatting, charts
2. **Get file content** — reads the template from SharePoint / OneDrive
3. **List rows present in a table** — retrieves current data to merge
4. **Compose / Parse JSON** — normalises and structures data
5. **Create table / Update table row** — populates the Excel table
6. **Create file** — saves the filled template to SharePoint / OneDrive

## Structure

```
Trigger: Recurrence (monthly / weekly)
  │
  ├── Get file content — download Excel template
  ├── List rows present in a table — pull latest data
  ├── Compose — normalise / calculate metrics
  └── Create table — write structured data into template
        Create file — save with date-stamped filename
              Send an Email (V2) — attach and send to stakeholders
```

## When to Use

- Monthly or weekly management reports with consistent structure
- Finance dashboards where the layout never changes but the numbers do
- Any scenario where a stakeholder expects the same report format every cycle

## Variations

- **Multi-sheet workbook:** use a separate **Update a row** action per sheet, or loop over sheets
- **Dynamic chart refresh:** Excel charts linked to data tables update automatically when table data changes
- **PDF export:** add a **Convert file** step after saving the Excel file to produce a PDF attachment

## Related

- [[Weekly-Status-Report-Aggregator]] — similar aggregation pattern
- [[PA-Finance-Report-Pipeline]] — full pipeline this pattern sits inside
- [[PDF-Form-Processing-to-SharePoint-Excel]] — reverse pattern: paper → Excel
