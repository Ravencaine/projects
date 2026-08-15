---
created: 2026-08-10
updated: 2026-08-10
source: 10 Power Automate Flows That Actually Save Hours — Not Just Demos
source_url: https://medium.com/@kaklotarrahul79/10-power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3
note_type: pattern
tags: [power-automate, ai-builder, pdf, sharepoint, excel, automation]
---

# PDF Form Processing to SharePoint/Excel

Automatically extract data from PDF invoices or application forms using AI Builder and write structured records to Excel or a SharePoint List.

## Purpose

Eliminates manual data entry from PDF documents. Instead of opening each PDF, copying fields (Vendor, Total Amount, Date), and pasting into Excel, the flow does it automatically.

## Components

1. **Trigger:** File created in a SharePoint/OneDrive folder OR email with PDF attachment received
2. **Action:** Pass document through **AI Builder — Form Processing** model to extract key fields (e.g., Vendor, Total Amount, Date)
3. **Action:** Add a new row to an Excel table (stored in OneDrive/SharePoint) or a SharePoint List with the extracted values

## Structure

```
Trigger:  When a file is created (SharePoint/OneDrive) OR
          When an email with attachment arrives

     ↓
Action:  AI Builder — Process and extract data from forms
         (pre-trained or custom Form Processing model)
         Output: Vendor, Amount, Date, etc.

     ↓
Action:  Create a new row in an Excel table
         OR  Create an item in a SharePoint List
         Field mapping: extracted value → column
```

## Key Details

- Requires a trained **AI Builder Form Processing model** — use the pre-built receipt/invoice model or train a custom one for your form layout
- Excel table must be formatted as a proper Excel Table (Insert → Table) for the "Add a row into a table" action to work
- The flow processes every PDF it sees; filter by folder path or attachment type to limit scope

## Hours Saved

~4–6 hours/week on manual data entry.

## Related

- [[Email-Attachment-Archiver-to-SharePoint]]
- [[Multi-Level-Document-Approval-Engine]]
