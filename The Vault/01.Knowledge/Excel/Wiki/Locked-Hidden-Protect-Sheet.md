---
created: 2026-08-09
updated: 2026-08-09
source: "Excel File Protection Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, protection, locked, hidden, formula-bar, worksheet-protection, conceal, proprietary]
---

# Locked + Hidden + Protect Sheet

The Protection tab in Format Cells has two independent checkboxes: **Locked** (prevents editing) and **Hidden** (prevents formula bar visibility). Both must be active AND the sheet must be protected for either to work.

## Two Separate Settings

| Setting | Location | Effect |
|---------|----------|--------|
| **Locked** | Ctrl+1 → Protection tab | Cell cannot be edited when sheet is protected |
| **Hidden** | Ctrl+1 → Protection tab | Formula bar shows nothing when cell is selected and sheet is protected |

Both settings are **ignored** until Review → Protect Sheet is applied.

## The Pattern

```
1. Ctrl+1 → Protection tab
2. Check both: ✓ Locked  ✓ Hidden
3. Review → Protect Sheet
```

## Why Both

| Scenario | Locked alone | Locked + Hidden |
|----------|-------------|----------------|
| User clicks a formula cell | Warning: cell protected | Warning: cell protected |
| User navigates via Name Box to formula cell | Can see formula in formula bar | Formula bar is blank |
| User edits locked cell | Prevented | Prevented |

Users can still navigate to formula cells via Name Box. Locked alone still reveals the formula in the formula bar. Locked + Hidden conceals both.

## Use Cases

- Proprietary formulas (commercial logic)
- Commission rates you don't want visible
- Hidden business calculations
- Any formula you don't want copied or shared

## Important Limitation

Hidden is **not encryption**. A determined user can unprotect the sheet and see everything. Use encryption for genuine security.

## Related

- [[Source-Excel-File-Protection-Tricks-Mynda-Treacy]] — source
- [[Unlock-Input-Cells-Protect-Sheet-Workflow]] — unlock input cells first, then protect
