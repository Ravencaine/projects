---
created: 2026-08-13
source: Power Automate UI flows — Automating Microsoft Forms Creation
source_url: https://medium.com/jenzushsu/power-automate-ui-flows-automating-microsoft-forms-creation-f3f5cb4677bc
note_type: pattern
tags: [power-automate, ui-flows, microsoft-forms, automation, rpa]
---

# Automating Microsoft Forms Creation (UI Flows + Selenium)

Automate mass creation of Microsoft Forms by looping over an Excel list and using a Forms template with UI Flows and Selenium IDE.

## Purpose

When thousands of identical Microsoft Forms need to be created (e.g., one per campus location), manual duplication is impractical. This pattern automates the entire process end-to-end: read Excel → duplicate Form → capture URL and QR code → write back to Excel.

## Components

- Excel table (OneDrive) as data source — contains location list with columns: Name, URL (empty), QR Code
- Microsoft Forms template — a pre-built form with consistent structure
- Web UI Flow (Selenium IDE) — records the duplicate-form, extract-URL, extract-QR steps
- Power Automate cloud flow — orchestrates the loop and data updates

## Structure

### Step 1 — Prepare

1. Create one **Microsoft Forms template** with the required fields
2. Create an **Excel sheet** on OneDrive with columns: `LocationName`, `URL` (leave empty for automation to fill), `QRCode`

### Step 2 — Cloud Flow Design

```
List rows present in a table (Excel)
  ↓
Apply to each (output from List rows)
  ↓
Condition: URL is empty
  ├─ No → skip
  └─ Yes → Run a UI flow for web
              ↓
              Update a row (Excel) with URL and QR code
```

### Step 3 — UI Flow Recording (Selenium IDE)

Inside the Selenium IDE, record these steps:
1. Open Forms template
2. Duplicate the form
3. Update the title with the passed location name
4. Extract the new form's URL
5. Extract the QR code image reference

Pass the `LocationName` as an **input** to the UI flow. Return `FormURL` and `QRCodeData` as **outputs**.

## Output

After the flow runs, the Excel sheet is updated with:
- The shareable URL for each location's Microsoft Form
- The QR code (as `data:image` base64)

## Related

- [[What-Are-UI-Flows]]
- [[Creating-a-Web-UI-Flow-Selenium-IDE]]
- [[UI-Flows-Limitations]]
- [[QR-Code-Generation-from-Forms-URL]]
