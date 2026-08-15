---
created: 2026-08-09
updated: 2026-08-09
source: "Build an Automated Excel Database • My Online Training Hub"
note_type: reference
tags: [excel, forms, data-validation, dropdown, today, worksheet-protection, locked-cells, tab-order]
---

# Data Entry Form Best Practices

Key design decisions for a professional Excel data entry form: input cells are unlocked, everything else is protected, only input cells can be edited.

## Form Field Setup

| Field | Technique |
|-------|-----------|
| Text input | Unlocked cell, input cell |
| Dropdown selection | Data Validation → List (referencing a named range or UNIQUE spill range) |
| Date field | `=TODAY()` — auto-inserts current date; can be locked |
| Notes | Free-text unlocked cell |

## Data Validation Dropdown

For list fields (Industry, Service, etc.):
1. Create a source list (can be UNIQUE-based for dynamic updates)
2. Data → Data Validation → Allow: List → Source: `=IndustryList`

## Locking and Protection

1. Select the input cells → Ctrl+1 → Protection tab → **Uncheck Locked**
2. Go to **Review → Protect Sheet**
3. Tick **Select unlocked cells only**
4. Apply

Result: users can tab between input cells freely, but cannot edit any other cell.

## Tab Order

Tab order follows the left-to-right, top-to-bottom order of cells. Arrange input fields in logical entry order for smooth workflow.

## Shape Formatting

- Use rounded rectangles for visual grouping
- Turn off gridlines for a cleaner form appearance
- Use shapes/icons to make the form look like a real application

## Related

- [[Source-Automated-Excel-Database-Mynda-Treacy]] — source
- [[Form-Database-Automation-Architecture]] — the full system this form is part of
