---
created: 2026-08-09
updated: 2026-08-09
source: "Excel HYPERLINK function • My Online Training Hub"
note_type: gotcha
tags: [excel, hyperlink, ctrl-k, static, dynamic, formula, insert-hyperlink, object, not-a-formula]
---

# Ctrl+K Static vs Formula-Based Dynamic Hyperlink

Ctrl+K (Insert → Hyperlink) creates a static hyperlink object embedded in the cell. The HYPERLINK() formula creates a dynamic formula that updates when its inputs change. They are fundamentally different — confusing them causes unexpected behaviour.

## Two Types of Hyperlinks

| | Ctrl+K / Insert Hyperlink | =HYPERLINK(...) formula |
|--|------------------------|------------------------|
| Type | Static hyperlink object | Dynamic formula |
| Updates when data changes | No | Yes |
| Responds to cell references | No | Yes |
| Can use XLOOKUP/MATCH inside | No | Yes |
| Stored in cell | No (overlay object) | Yes |
| Affected by Copy/Paste | No | Yes |

## The Confusion Point

Both appear as blue clickable text in a cell. Users often assume Ctrl+K inserted something equivalent to a formula — but it is a static object, not a formula. It will not update if the lookup value changes.

## When to Use Each

| Scenario | Use |
|----------|-----|
| Links to fixed URLs, files, or sheets | Ctrl+K (Insert Hyperlink) |
| Links that must update with data changes | =HYPERLINK() formula |
| Dynamic row-jumping based on a dropdown selection | =HYPERLINK() formula |
| Links inside a dynamic array | =HYPERLINK() formula |

## The HYPERLINK Formula Advantage

Only the formula version can:
- Dynamically resolve the target based on a lookup result
- Use XLOOKUP, MATCH, or other formulas to determine the destination
- Update automatically when the underlying data changes

For any navigation system driven by a dropdown or lookup, use the HYPERLINK formula — not Ctrl+K.

## Related

- [[Source-HYPERLINK-Function-Mynda-Treacy]] — source
- [[Dynamic-Hyperlink-XLOOKUP-CELL]] — formula-based dynamic hyperlink that Ctrl+K cannot replicate
- [[Sheet-Navigation-TOC-HYPERLINK]] — formula-based TOC; could also be done statically with Ctrl+K but formula is more maintainable
