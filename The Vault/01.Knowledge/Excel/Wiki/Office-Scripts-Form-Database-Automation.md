---
created: 2026-08-09
updated: 2026-08-09
source: "Build an Automated Excel Database • My Online Training Hub"
note_type: workflow
tags: [excel, office-scripts, automation, forms, vba, macros, form-to-table, copy-paste, record-actions]
---

# Office Scripts for Form-Database Automation

Office Scripts automate the form → database step: copy form field values into the Excel Table. Recorded via Automate → Record Actions, then edited for conditional logic (first-row empty check, append, form clear). Available in Excel Online and Desktop.

## Why Office Scripts (Not VBA)

| | Office Scripts | VBA/Macros |
|--|--------------|------------|
| Excel Online | ✓ | ✗ |
| Excel Desktop | ✓ | ✓ |
| Cross-platform | ✓ | ✗ |
| Browser-accessible | ✓ | ✗ |

## The Recording Step

1. Go to **Automate → Record Actions**
2. Fill in the form fields
3. Select the first empty row in the database table
4. Paste values
5. Stop recording

## The Edit Step (Required Logic)

The raw recording pastes to a fixed location. Edit the script to add:

1. **Check if first row is empty:** if so, paste there; otherwise find the last row
2. **Append to last row:** determine the actual last row of the table dynamically
3. **Clear the form:** after saving, clear all input cells except the Date field (TODAY() resets)

## ChatGPT Tip

Record part of the script, then use ChatGPT to rewrite and optimize it — particularly useful for writing the dynamic last-row logic and form-clearing loops. This avoids manually coding sheet names and cell references.

## Adding the Button

After editing, go to **Code Editor → + Add in workbook** to create a button that runs the script with one click from the form sheet.

## Related

- [[Source-Automated-Excel-Database-Mynda-Treacy]] — source
- [[Form-Database-Automation-Architecture]] — where this step fits in the system
- [[Data-Entry-Form-Best-Practices]] — the form this script populates
