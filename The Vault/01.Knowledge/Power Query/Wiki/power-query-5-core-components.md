---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Transforming Data with Power Query Editor.md"
note_type: atomic
tags: [power-bi, power-query, beginner, ui, ribbon, applied-steps]
---

# Power Query Editor: 5 Core Components

Power Query Editor has five UI components that work together. Understanding each one makes the tool intuitive.

## 1. The Ribbon

Four tabs:

| Tab | Purpose |
|-----|---------|
| **Home** | Connect to data, basic transformations, close & apply |
| **Transform** | Advanced reshaping: unpivot, transpose, merge columns, data type changes |
| **Add Column** | Create new calculated columns, custom formulas, duplicate columns |
| **View** | Toggle Column Quality, Column Profile, Formula Bar; manage dependencies |

## 2. Queries Pane (Left Side)

Lists all data connections and queries — each query is one table. From here you can:
- Rename queries for clarity
- Organise related queries into groups
- See query dependencies

## 3. Data Preview (Centre)

Live preview of the current query's data — up to 1,000 rows by default. Changes from Applied Steps update the preview instantly.

**Key tip:** Enable Column Quality (View → Column Quality) to see error rates per column. Enable Column Profile (View → Column Profile) for distribution histograms.

## 4. Applied Steps (Right Side) ⭐

The game-changer. Every transformation you apply is recorded as a named step. You can:
- See exactly what you've done
- Click any step to see the data at that point
- Delete or reorder steps
- Edit any step's settings

Steps are named by default (Source, Navigation, Changed Type, etc.). Rename them for clarity.

## 5. Formula Bar

Shows the M code (Power Query's language) for the selected step. You don't need to write M manually, but seeing it helps with troubleshooting complex transformations.

**Toggle visibility:** View → Formula Bar

## Related

- [[power-query-applied-steps-repeatability]] — the key benefit of Applied Steps
- [[power-query-workflow-process]] — the workflow that uses all 5 components
