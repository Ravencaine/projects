---
created: 2026-08-09
updated: 2026-08-09
source: "Filters in Power BI Everything You Need to Know.md"
note_type: workflow
tags: [power-bi, filters, visual-level, page-level, report-level, workflow]
---

# Apply Filters to Visuals Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-filters-in-power-bi-everything-you-need-to-know]]

Add a field as a filter to a specific visual, page, or the entire report. Four-step workflow.

## Steps

1. **Select the visual:** click the visualization on the report canvas
2. **Open the Filters pane:** the Filters pane is on the right side of Power BI Desktop (may need to click the funnel icon)
3. **Drag the field:** drag any field from the Fields pane into the desired section:
   - Visual-level filters (top of pane)
   - Page-level filters (middle)
   - Report-level filters (bottom)
4. **Set the filter criteria:** choose filter type and specify conditions (Basic / Advanced / Top N / Relative Date)

## Filter type selection

After dragging the field in, use the dropdown at the top of the filter card to switch type:

- **Basic filtering:** check/uncheck individual values
- **Advanced filtering:** build AND/OR/NOT condition chains
- **Top N:** enter N and select a measure to rank by
- **Relative date:** choose period type and duration

## Tips

- Include blank values option is in the filter card (three dots → "Select all")
- Lock/Unlock toggle in the filter card header controls whether authors can change it in Publishing
- Add multiple fields to the same filter level — they stack (AND logic between them)

## Related

- [[filter-levels-in-power-bi]] — visual vs page vs report vs drillthrough
- [[filter-types-overview]] — basic, advanced, Top N, relative date
- [[filter-best-practices]] — model understanding before filtering
