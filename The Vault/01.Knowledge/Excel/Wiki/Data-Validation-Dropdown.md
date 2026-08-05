---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, data-validation, dropdown, prevent-error, list, input, restrict]
---

# Data Validation: Prevent Bad Inputs

Data → Data Validation → Allow: List creates a dropdown menu in a cell, restricting inputs to a predefined list of values — eliminating typos, inconsistent spellings, and custom entries before they enter the data.

## The Problem Without It

A "Status" column without validation accumulates variants:

`Approved`, `approved`, `aproved`, `Approved!`, `Approve` — five entries for the same status, each treated as different by Pivot Tables.

## Steps

1. Select the column or range
2. Go to **Data → Data Validation**
3. Under **Allow:** select **List**
4. Enter the options: `Pending, Approved, Rejected`
   - Or reference a cell range: `=$E$1:$E$3`
   - Or reference a named range
5. Enable **In-cell dropdown** (checked by default)
6. Click **OK**

## Input Message (Optional)

Set an input message that appears when the user selects the cell:

**Input Message → Title:** "Status" → **Input message:** "Select Pending, Approved, or Rejected."

## Error Alert (Optional)

Set a stop/warning/information alert when invalid data is entered:

**Error Alert → Style:** Stop → **Title:** "Invalid Entry" → **Error message:** "Please select from the list."

## Common Use Cases

| Column type | Validation options |
|------------|-------------------|
| Status | `Pending, Approved, Rejected` |
| Region | `North, South, East, West` |
| Priority | `Low, Medium, High` |
| Department | Reference named range of departments |

## Limitation

Data Validation is advisory — a user can copy-paste a value that bypasses the dropdown. To fully enforce: protect the sheet and lock the cells.

## Related

- [[Find-Replace-Ctrl-H]] — clean up existing typo variants first, then apply Data Validation
- [[Highlight-Duplicates-Conditional-Formatting]] — review duplicates before applying validation rules
