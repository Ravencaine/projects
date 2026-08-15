---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: atomic
tags: [dax, removefilters, allselected, per-level, conditional-formatting, slicer-context, atomic]
---

# REMOVEFILTERS vs ALLSELECTED for Per-Level Rules

**Type:** Atomic · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

Inside each level branch of a per-level conditional formatting measure, the CALCULATE modifier determines **which totals to compare against**. REMOVEFILTERS and ALLSELECTED produce different results when the visual has date slicers.

## REMOVEFILTERS — full model totals

```dax
CALCULATE([Sales Amount], REMOVEFILTERS('Date'))
```

Ignores all filters from the Date table — compares against the **entire model's** total for all time. Use when the comparison should be against absolute historical totals.

**Result:** Does NOT respect slicers on the Date table.

## ALLSELECTED — visual totals

```dax
CALCULATE([Sales Amount], ALLSELECTED('Date'))
```

Respects the date range currently selected in the visual — compares against the **displayed** total. Use when the comparison should be relative to what the user is currently viewing.

**Result:** DOES respect slicers on the Date table.

## Decision rule

| If you want comparison against... | Use |
|-----------------------------------|-----|
| Full model total (all time) | REMOVEFILTERS |
| Visual's visible range only | ALLSELECTED |

## In ISATLEVEL visual calculations

ISATLEVEL measures use COLLAPSE/COLLAPSEALL, which operate on the visual rowset — equivalent to ALLSELECTED behavior by default. COLLAPSE always navigates within what the visual currently shows.

## Practical example

Year-level shading: is this year > 40% of the grand total?

- **REMOVEFILTERS:** compares against all years in the model (e.g., 2020–2026). If viewing only 2024–2025, those two years might each represent 50% of the displayed range but only 15% of the full model — different colors.
- **ALLSELECTED:** compares against the visible range (2024–2025 only). Each year at 50% of displayed = SteelBlue regardless of earlier/later years.

## Related

- [[ISINSCOPE-Per-Level-Conditional-Formatting]] — measure implementation using both
- [[REMOVEFILTERS-vs-ALL-ALLSELECTED-ALLEXCEPT]] — broader comparison
