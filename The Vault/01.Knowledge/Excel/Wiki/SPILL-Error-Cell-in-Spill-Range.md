---
created: 2026-08-09
updated: 2026-08-09
source: "Build a Dynamic Excel Report with Just 4 Formulas • My Online Training Hub"
note_type: gotcha
tags: [excel, dynamic-arrays, spill, spill-error, spill, troubleshooting, blocking-cells]
---

# #SPILL! Error — Cell in Spill Range

When a dynamic array formula spills its results into adjacent cells and any of those cells contains data, Excel returns #SPILL!. The formula has no room to expand.

## Cause

```
C8: =FILTER(SalesData, ...)
```
C8 spills to C8:C100. If cell C9 contains an "x", the spill is blocked → #SPILL!.

## Fix

1. Select the formula cell
2. Excel shows a faint dotted border around the intended spill range
3. Clear any data within that range
4. The formula recalculates and fills the range

## Prevention

Keep the spill range clear. Don't use cells adjacent to dynamic array outputs for manual data entry.

## Related

- [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy]] — source
- [[No-Dynamic-Arrays-Inside-Formatted-Tables]] — related: don't nest dynamic arrays inside tables either
