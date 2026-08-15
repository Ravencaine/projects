---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring New Matrix Visual Layouts in Power BI.md"
note_type: atomic
tags: [power-bi, matrix-visual, outline-layout, columns, subtotals, atomic]
---

# Matrix Outline Layout Column Based Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-new-matrix-visual-layouts-power-bi]]

Outline layout displays hierarchical data in separate columns — one column per hierarchy level. Similar to early Power BI Matrix visuals. Allows subtotals to be positioned at top or bottom of each group.

## Key characteristics

- **Separate columns**: Each hierarchy level gets its own column (e.g., Category, Product, Year)
- **Subtotal toggle**: Row subtotals can be placed at top or bottom of each group
- **No indentation**: Cleaner column-based structure vs compact's indentation
- **Legacy feel**: Resembles older Matrix visual behavior

## Compact vs Outline vs Tabular

| Feature | Compact | Outline | Tabular |
|---------|---------|---------|---------|
| Indentation | Yes | No | No |
| Separate columns | No | Yes | Yes |
| Blank rows between groups | Yes | Yes | No |
| Subtotal position | Bottom | Top or Bottom | Top or Bottom |

## When to use Outline

Use Outline when stakeholders need to see each hierarchy level clearly in its own column — especially when exporting or sharing the matrix in tabular form.

## Related

- [[matrix-compact-layout-default]] — indented default layout
- [[matrix-tabular-layout-no-blank-rows]] — column layout minus gaps
- [[matrix-cash-flow-pl-report-workflow]] — practical use case with subtotals
