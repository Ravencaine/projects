---
created: 2026-08-05
updated: 2026-08-05
source: 4 Tips Work Efficiently Power BI (Isabelle Bittar)
note_type: atomic
tags: [power-bi, workflow, asset-library, github, dax, m-code, template, productivity]
---

# Reusable Project Assets: Don't Start From Scratch

Maintaining a library of reusable assets — DAX measures, M functions, HTML setup code, and visualization templates — instead of rebuilding common elements from scratch on each project.

## Definition

Building up a personal or team library of proven, tested assets that can be copied into new projects. The library grows over time and covers the most common patterns: KPI cards, conditional formatting, date dimension setup, HTML tooltips, and M transforms.

## Asset Types to Build

| Asset type | Examples |
|-----------|----------|
| **DAX measures** | Running totals, SAMEPERIODLASTYEAR, complex conditional formatting |
| **M / Power Query** | Date dimension generator, calendar table, standard cleans |
| **HTML setup measures** | HTML/CSS for custom tooltips, cards, headers |
| **Visual templates** | Configured KPI card, gauge, table with specific settings |
| **Parameter files** | Standard threshold/benchmark Excel sheets |
| **Color measure sets** | Named hex palettes for conditional formatting |

## Storage Approaches

### Master PBIX (current approach — limitations)

Isabelle stores most assets in "Master" Power BI files. Problem: a master PBIX grows over time, becomes hard to navigate, and doesn't version-control the assets.

### GitHub (preferred — Isabelle is transitioning)

Storing DAX, M, and HTML snippets in a GitHub repository:
- Individual files per asset — easy to search
- Git history — track changes and rollback
- Collaboration — team members contribute via pull requests
- Readme per asset — document the use case and parameters

Reference: `PowerBI-tips/DAX-Templates` on GitHub (community library).

## Practical Tips

- Build one asset at a time — add to the library immediately after solving a problem cleanly
- Write a brief comment or README alongside each asset explaining when to use it
- Review the library quarterly — prune obsolete patterns

## Related

- [[Organizing-Measures-Display-Folders]]
- [[DAX-Measure-Centralization-via-GitHub]]
