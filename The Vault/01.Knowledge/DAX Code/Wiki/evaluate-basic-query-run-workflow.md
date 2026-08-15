---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring the New DAX Query View in Power BI.md"
note_type: workflow
tags: [power-bi, dax, dax-query-view, evaluate, query, workflow]
---

# EVALUATE Basic Query Run Workflow

**Type:** Workflow · **KB:** DAX Code · **Source:** [[source-dax-query-view-power-bi]]

Write and run a basic DAX query using EVALUATE in the DAX Query View.

## Step 1 — Open DAX Query View

1. Click the DAX Query View tab (left side, fourth icon)
2. A default Query Page opens with an example query

## Step 2 — Write an EVALUATE query

```dax
EVALUATE
'Products'
```

Or with row limit:

```dax
EVALUATE
TOPN(100, 'Products')
```

Or with filter:

```dax
EVALUATE
FILTER(
    'Products',
    'Products'[Category] = "Bikes"
)
```

## Step 3 — Run the query

1. Click **Run** at the top of the Query Editor
2. Observe results in the **Results** pane (bottom)

## Step 4 — Save the query

1. Rename the Query Page tab (double-click or right-click → Rename)
2. The query is saved inside the .pbix model

## Common EVALUATE patterns

| Pattern | DAX |
|---------|-----|
| All rows from table | `EVALUATE 'Table'` |
| Top N rows | `EVALUATE TOPN(N, 'Table')` |
| With filter | `EVALUATE FILTER('Table', 'Table'[Col] = "Value")` |
| With sort | `EVALUATE ORDERBY('Table'[Col], ASC)` |

## Related

- [[dax-query-view-ui-components]] — Query Editor and Results pane
- [[format-comment-search-workflow]] — formatting and editing tools
- [[quick-queries-workflow]] — Quick Queries templates for common exploration
