---
created: 2026-08-01
updated: 2026-08-02
source: "From Messy to Masterpiece The Ultimate Power BI Dashboard Checklist .md"
note_type: atomic
tags: [dashboard-design, labels, data-formatting, power-bi]
---

# Label Formatting — Units, Truncation, Tooltips

Format axis labels and data labels with appropriate units, truncate only when necessary, and defer full detail to tooltips.

## Three Rules

### 1. Attach the Right Unit

Labels must include units so readers understand the scale without doing mental math:
- Currency: `$1,234` or `€` — not `1234`
- Percentages: `12.5%` — not `0.125`
- Large numbers: `1.2M` or `1,234K` — not `1234567`

### 2. Truncate with Ellipsis, Not with Meaning

Long category names on axes or in legends should be truncated with `…` rather than cut off mid-word. The full label belongs in the tooltip on hover — never sacrifice meaning for space.

### 3. Tooltips Carry the Detail

The tooltip is the right place for extended context: full label text, exact values, comparisons, annotations. Keep labels themselves lean.

## Related

- [[enhancing-data-narratives-power-bi-tooltips]] — tooltips as narrative devices
- [[power-bi-dashboard-checklist]] — visual design: labels readable without hovering
- [[accessibility-for-charts]] — tooltips as an accessibility channel
