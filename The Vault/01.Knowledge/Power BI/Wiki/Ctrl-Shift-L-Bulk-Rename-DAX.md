---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: atomic
tags: [dax, productivity, shortcut, power-bi-desktop]
---

# Ctrl+Shift+L: Bulk Rename in DAX Editor

Use Ctrl+Shift+L in the DAX formula bar to select all occurrences of highlighted text across all measures in the TMDL view, then apply a rename in one step.

## Definition

When you highlight a text string in the DAX formula bar and press Ctrl+Shift+L, Power BI Desktop selects every identical occurrence of that text string in the current measure. You can then rename or change them all simultaneously, then Apply — avoiding repetitive per-measure edits.

## Key Points

- Available in **TMDL View** (Tabular Model Definition Language) in Power BI Desktop
- Selects **all occurrences** of the highlighted text across the current measure's formula
- Useful for renaming abbreviated prefixes (e.g., `AVG` → `Average`, `TOT` → `Total`)
- **Caution**: if the selected text appears in unintended names, those will also be renamed — verify selection carefully before applying
- Works within a single measure's formula at a time
- One of the highest-leverage productivity shortcuts for models with many similarly-prefixed measures

## Example

**Rename AVG → Average across 4 measures:**
1. Go to TMDL View
2. Double-click a measure containing `AVG Revenue`, `AVG Occupancy`, `AVG ADR`, `AVG RevPAR`
3. Highlight `AVG` text
4. Press **Ctrl+Shift+L** → all 4 `AVG` occurrences highlight
5. Type `Average`
6. Click Apply → all 4 measures update

## Related

- [[Bulk-Edit-Measure-Properties-Model-View]] — bulk editing measure properties
- [[Measure-Table-Dedicated]] — organizing measures before bulk rename
