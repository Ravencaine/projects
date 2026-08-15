---
created: 2026-08-11
source: How I Use Power Automate as a Finance Analyst to Prepare Management Reports.md
note_type: pattern
tags: [power-automate, powerpoint, charts, data-visualization, finance]
---

# Dynamic PowerPoint Chart Updates via Power Automate

Power Automate pattern that updates charts in a live PowerPoint presentation with the latest financial data before distribution — keeping presentations current without manual editing.

## Purpose

Static charts go stale quickly. This pattern fetches the latest data and refreshes chart data points in a PowerPoint file before sending or publishing the presentation, ensuring every stakeholder sees current numbers.

## Components

1. **Get file content** — downloads the source PowerPoint from SharePoint / OneDrive
2. **Get data** — retrieves latest figures (Excel, SharePoint List, SQL)
3. **Compose / Parse JSON** — structures data for chart injection
4. **Create a PowerPoint with updated charts** — replaces chart data in the deck
5. **Create file** — saves the updated presentation
6. **Send an Email (V2)** — distributes to management team

## Structure

```
Trigger: Recurrence (monthly / quarterly)
  │
  ├── Get file content — PowerPoint template
  ├── Get rows from a table — latest financial data
  ├── Calculate / Compose — derive metrics
  └── Create a PowerPoint with updated charts
        Create file — save with date-stamped name
              Send an Email (V2) — attach updated presentation
```

## Key Insight

Charts embedded in a linked Excel object within PowerPoint update automatically when the source Excel data changes. Power Automate can refresh the underlying data source before distributing the file — the chart updates without needing to touch the PowerPoint directly.

## Variations

- **Linked Excel data:** keep chart data in a separate Excel file; update the Excel via PA, then distribute the PowerPoint (chart refreshes on open)
- **AI Builder summarisation:** add a **Summarise text using AI Builder** step to generate an executive summary slide before distribution

## Related

- [[Template-Based-Report-Generation-PA-Excel]] — complementary text/number reporting
- [[PA-Finance-Report-Pipeline]] — full pipeline this pattern extends
