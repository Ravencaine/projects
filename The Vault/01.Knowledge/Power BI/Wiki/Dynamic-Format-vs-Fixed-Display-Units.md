---
created: 2026-08-10
updated: 2026-08-10
source: "Give Users Full Control Over KPI Scale with Dynamic Formatting"
source_url: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Give-Users-Full-Control-Over-KPI-Scale-with-Dynamic-Formatting/ba-p/5297206"
note_type: comparison
tags: [power-bi, comparison, dynamic-format, display-units, measure]
---

# Dynamic Format String vs Fixed Display Units

Two approaches to controlling how KPI numbers display in Power BI visuals.

## Summary

Fixed Display Units (visual settings) are quick but inflexible — one setting applies to all users. Dynamic Format Strings with a disconnected table give each user self-service control without measure duplication.

## Dynamic Format String

### Pros
- Users control their own view via slicer
- Single measure handles all scales — no duplication
- Format string handles scaling at display time, not in DAX — calculation stays consistent
- Same measure works across all visuals with different scales
- Extendable to multi-currency, percentages, custom symbols

### Cons
- Requires Measure Tools → Format → Dynamic (modern modelling UI)
- Disconnected table adds a minor semantic model artifact
- Default fallback must be explicitly set or blanks appear when no slicer selection is active

## Fixed Display Units (Visual Settings)

### Pros
- Zero setup — built into every visual's format pane
- Works with any measure immediately
- No semantic model changes needed

### Cons
- One setting applies to all users — no self-service control
- "Auto" is unpredictable and offers no user choice
- To support both executives (Millions) and analysts (Actuals), you need duplicate measures ("Sales (M)" + "Sales")
- Duplicate measures create technical debt and confuse self-service users
- Small values show as `$0.0M` when fixed to Millions — misleading for detailed views

## Comparison Table

| Criteria | Dynamic Format String | Fixed Display Units |
|----------|----------------------|---------------------|
| User self-service control | Yes — slicer | No |
| Measure duplication | None | Required for multiple scales |
| Setup effort | Medium (table + measure) | None |
| Small value display | Shows correctly with Actuals | Shows as $0.0M when fixed high |
| Multi-currency support | Yes — extend with SWITCH | No |
| Works across all visuals | Yes — single measure | Requires consistent setting per visual |
| Requires modern modelling UI | Yes | No |

## When to Use

**Use Dynamic Format Strings when:** multiple user personas need different scales (executives vs analysts), you need multi-currency support, or you want to avoid measure duplication.

**Use Fixed Display Units when:** a single scale is acceptable for all users, the report is for one audience only, or you need a quick solution with no model changes.

## Related

- [[Dynamic-KPI-Scale-Disconnected-Table-SWITCH]] — pattern
- [[Dynamic-Format-String-Implementation]] — workflow
