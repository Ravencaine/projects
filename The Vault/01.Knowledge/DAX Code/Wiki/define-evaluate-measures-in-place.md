---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring the New DAX Query View in Power BI.md"
note_type: atomic
tags: [power-bi, dax, dax-query-view, define-evaluate, measure, atomic]
---

# Define Evaluate Measures In Place Atomic

**Type:** Atomic · **KB:** DAX Code · **Source:** [[source-dax-query-view-power-bi]]

DAX Query View allows evaluating any measure directly from the Data Pane — no need to add it to a visual or write an EVALUATE statement. Right-click a measure → Define and Evaluate → formula and result appear immediately.

## How to use

1. In the Data Pane, right-click any **measure**
2. Select **Define and Evaluate**
3. The Results pane shows:
   - The measure's full DAX formula
   - The measure's output value in the current filter context

## What it replaces

Previously required: add measure to a visual, or write a full EVALUATE with CALCULATE context. Define and Evaluate is a one-click shortcut for rapid measure inspection.

## When to use

- Debugging a measure that returns unexpected values
- Checking if a measure formula is correct before committing it
- Comparing a measure's output under different filter contexts

## Related

- [[define-with-references-and-evaluate]] — full dependency chain view
- [[dax-query-view-ui-components]] — Data Pane location
