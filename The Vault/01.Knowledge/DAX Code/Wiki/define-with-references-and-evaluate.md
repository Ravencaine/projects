---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring the New DAX Query View in Power BI.md"
note_type: atomic
tags: [power-bi, dax, dax-query-view, measure-dependencies, define-with-references, atomic]
---

# Define With References And Evaluate Atomic

**Type:** Atomic · **KB:** DAX Code · **Source:** [[source-dax-query-view-power-bi]]

Define with References and Evaluate is an advanced DAX Query View action that shows not just a measure's formula and result, but the full chain of all measures it references. Essential for auditing and debugging complex measure hierarchies.

## How to use

1. In the Data Pane, right-click any **measure**
2. Select **Define with References and Evaluate**
3. Results pane expands to show the entire dependency tree

## What it shows

| Output | What it shows |
|--------|--------------|
| Target measure | The measure you right-clicked |
| Referenced measure 1 | Formula and value |
| Referenced measure 2 | Formula and value |
| ... | Full chain, recursively |

## Why it matters

In a well-structured measures model:
- `Total Sales = SUM(Sales[Amount])`
- `Sales YTD = TOTALYTD([Total Sales], Calendar[Date])`
- `Sales YoY = DIVIDE([Sales YTD], [Sales LYTD]) - 1`

Define with References and Evaluate on `Sales YoY` reveals all three — the measure itself plus `Total Sales`, `Sales YTD`, and `Sales LYTD` — with formulas and current values.

## When to use

- Tracing unexpected results in a measure chain
- Auditing measure dependencies before deleting a measure
- Documenting what a complex measure actually depends on

## Related

- [[define-evaluate-measures-in-place]] — single measure evaluation
- [[format-comment-search-workflow]] — reading complex generated output
