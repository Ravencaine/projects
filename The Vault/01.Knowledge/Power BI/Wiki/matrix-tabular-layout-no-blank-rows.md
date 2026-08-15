---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring New Matrix Visual Layouts in Power BI.md"
note_type: atomic
tags: [power-bi, matrix-visual, tabular-layout, compact, outline, atomic]
---

# Matrix Tabular Layout No Blank Rows Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-new-matrix-visual-layouts-power-bi]]

Tabular layout is like Outline layout (hierarchical data in separate columns) but removes the blank rows that normally appear between category groups. Produces a cleaner, more compact table — ideal when report space is at a premium.

## Key characteristics

- **Column-based**: Each hierarchy level in its own column (same as Outline)
- **No blank rows**: Category groups have no separator gaps — rows are continuous
- **Space efficient**: Most compact of the three layouts
- **Clean look**: Preferred for final reports and dashboards

## Blank row comparison

| Layout | Blank rows between groups? |
|--------|---------------------------|
| Compact | Yes (with indentation) |
| Outline | Yes |
| Tabular | No |

## When to use Tabular

- Reports where visual space is limited
- P&L and cash flow statements where continuous rows read better
- Exporting to Excel where blank rows cause import complications

## Related

- [[matrix-compact-layout-default]] — indented default
- [[matrix-outline-layout-column-based]] — column layout with gaps
- [[matrix-cash-flow-pl-report-workflow]] — practical use in financial reports
