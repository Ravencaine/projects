---
created: 2026-08-09
updated: 2026-08-09
source: "Excel File Protection Tricks • My Online Training Hub"
note_type: workflow
tags: [excel, protection, worksheet-protection, input-cells, locked-cells, unlock, guide-users, usability]
---

# Unlock-Input-Cells-Protect-Sheet Workflow

Protect formula cells by unlocking only the input cells, then applying sheet protection. Users can only type in designated cells; everything else is locked. This is the foundation of a well-designed shared Excel file.

## When to Use

- Commission trackers, sales reports, budget templates, invoice files, forecast models
- Any workbook shared with non-technical users who might accidentally overwrite formulas

## Step-by-Step

**Step 1: Identify input cells**
Determine which cells users need to edit (date, sales rep, product, units, price, etc.)

**Step 2: Unlock input cells**
1. Select the input cells
2. Ctrl+1 → Protection tab → **Uncheck Locked**
3. OK

**Step 3: Protect the sheet**
1. Review → Protect Sheet
2. Add password (optional)
3. Choose allowed actions (default is usually fine)
4. OK

## What Users Can Do After

- Select and type in unlocked cells normally
- Tab between input cells
- Cannot edit locked cells — Excel shows a warning if they try

## What Users Can Still Do (Configurable)

In the Protect Sheet dialog, allow or disallow:
- Format cells, columns, rows
- Insert/delete rows
- Sort, AutoFilter
- Edit objects, scenarios

## Result

A guided data-entry experience where users cannot accidentally break formulas or change commission rates.

## Related

- [[Source-Excel-File-Protection-Tricks-Mynda-Treacy]] — source
- [[Locked-Hidden-Protect-Sheet]] — the two Protection tab checkboxes (Locked + Hidden)
- [[Data-Entry-Form-Best-Practices]] — this pattern applied to data entry forms specifically
