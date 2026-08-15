---
created: 2026-08-09
updated: 2026-08-09
source: "Excel File Protection Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, very-hidden, vba-editor, visible-property, xlSheetVeryHidden, hide-sheets, backend-sheets, vba, clutter-reduction]
---

# Very Hidden Sheets via VBA Editor

Make a sheet disappear from the Unhide menu using the VBA Editor's Visible property. The sheet is not deleted — it runs in the background, formulas still reference it, but it is invisible to casual users and absent from the right-click Unhide list.

## How to Make a Sheet Very Hidden

**No VBA code required:** just the Properties window:

1. Alt+F11 → Open VBA Editor
2. Find your workbook in the Project window
3. Expand **Microsoft Excel Objects**
4. Select the sheet you want to hide
5. In the Properties window, find **Visible**
6. Change from **-1 - xlSheetVisible** to **2 - xlSheetVeryHidden**
7. Close VBA Editor

The sheet is now very hidden.

## How to Unhide

1. Alt+F11 → Open VBA Editor
2. Select the very hidden sheet
3. Properties window → Visible → **-1 - xlSheetVisible**
4. Return to Excel

## What Very Hidden Means

| Visibility state | Right-click Unhide | VBA Editor |
|-----------------|-------------------|-----------|
| Normal | ✓ | Visible |
| Hidden | In Unhide list | Visible |
| Very Hidden | Not in Unhide list | Visible |

Users can unhide via VBA Editor — this is not true security.

## Use Cases

- Lookup tables / parameter sheets
- Source data sheets
- Helper calculations
- Validation lists
- Back-end sheets that must exist but should not be visible

## Security Note

Anyone with intermediate Excel knowledge can open the VBA Editor and make the sheet visible. Do not use Very Hidden for genuinely sensitive data (salary data, client financials, M&A information). Use encryption instead.

## Related

- [[Source-Excel-File-Protection-Tricks-Mynda-Treacy]] — source
- [[Encrypt-Workbook-with-Password]] — for sensitive data, encryption is the real security layer
