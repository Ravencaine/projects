---
created: 2026-08-10
updated: 2026-08-10
source: "Excel REPT Function In Cell Charts • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
note_type: comparison
tags: [excel, comparison, charts, conditional-formatting, visualisation]
---

# REPT vs Conditional Formatting Data Bars

Two ways to add inline bar visuals to cells in Excel — without chart objects.

## Summary

CF Data Bars are faster to set up. REPT bars offer more control over characters, symbols, and formula logic.

## REPT

### Pros
- Fully formula-driven — bar length controlled by a formula
- Combine with any conditional formatting rule on the underlying cell value
- Works with Excel Table structured references
- Characters and font formatting fully customisable
- Can create two-section progress bars (filled + remaining)
- Star ratings possible

### Cons
- Requires knowing the block character or UNICHAR codes
- Must use a monospaced font (Consolas, Courier New) for alignment
- Bar length is fixed to a maximum character count; percentage precision depends on width
- No built-in axis or labels

## Conditional Formatting Data Bars

### Pros
- Built-in — no character knowledge needed
- Axis and label options available
- Gradient and solid fill options
- Fast setup via Home → Conditional Formatting → Data Bars

### Cons
- Bar colour controlled by CF rules, not by the cell value
- Cannot combine with font colour conditional formatting on the same cell
- Less control over character/symbol customisation
- No two-section (filled + remaining) progress bar
- No star ratings

## Comparison Table

| Criteria | REPT | CF Data Bars |
|----------|------|--------------|
| Formula-driven length | Yes | Limited |
| Two-section progress bar | Yes | No |
| Star ratings | Yes | No |
| Font colour from CF rules | Yes | No |
| Monospaced font required | Yes | No |
| Built-in axis/label | No | Yes |
| Setup speed | Medium | Fast |
| Character customisation | High | None |

## When to Use

**Use REPT when you need:** colour-coded thresholds via CF, progress bars, star ratings, or formula-driven character selection.

**Use CF Data Bars when you need:** a quick visual comparison with minimal setup, built-in axis labels, or gradient fills.

## Related

- [[REPT-Function]] — function
- [[In-Cell-Bar-Chart-REPT]] — pattern
- [[Progress-Bar-REPT-LET]] — pattern
