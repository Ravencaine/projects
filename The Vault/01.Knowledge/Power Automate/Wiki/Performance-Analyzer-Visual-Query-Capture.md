---
created: 2026-08-10
updated: 2026-08-10
source: Automate Data Validation in Power BI Reports using Power Automate
source_url: https://medium.com/@guna24x7/automate-data-validation-in-power-bi-reports-using-power-automate-6deea7b04dbb
note_type: reference
tags: [power-bi, performance-analyzer, dax-query, dax-query-view, reference]
---

# Performance Analyzer — Visual Query (DAX) Capture

Power BI Desktop's Performance Analyzer can export the DAX query that a visual generates internally. This query is the exact DAX code that Power BI sends to the analysis engine — usable in DAX Query View, Power Automate's "Run a Query against Dataset" action, and external tools.

## How to Capture

1. Open the `.pbix` file in Power BI Desktop
2. Wait for all report visuals to load
3. Go to the **View** ribbon → **Performance Analyzer** pane
4. Click **Start recording**
5. Click **Refresh visuals** on each visual you want to capture
6. Expand the visual's entry in the Performance Analyzer
7. Click **Copy query** — the full DAX query is on the clipboard

## What the Query Contains

The captured query uses the DAX Query View syntax:

```dax
DEFINE
    VAR __DS0FilterTable = TREATAS({...}, 'Table'[Column])
    VAR __DS0Core = SUMMARIZECOLUMNS(...)
EVALUATE
    __DS0PrimaryWindowed
ORDER BY
    [SumAmount] DESC
```

| Clause | Purpose |
|--------|---------|
| `DEFINE` | Declares filter variables, measures, and aggregations |
| `EVALUATE` | Returns the result set (equivalent to SELECT in SQL) |
| `ORDER BY` | Sort order of the returned rows |

## Why This Matters

The visual query reflects all applied filters, row-level security, relationships, and measure logic — exactly what the user sees in the visual. Capturing it lets you:

- **Automate validation** — run the same query in Power Automate on a schedule
- **Test in DAX Query View** — validate results before deploying
- **Use in external tools** — DAX Studio, SSDT, or any tool that accepts DAX EVALUATE queries

## Validating in DAX Query View

After capturing the query:

1. Open Power BI Desktop → **External Tools** → **DAX Query View** (or open via the modeling ribbon)
2. Paste the captured query
3. Press **Run** to see the exact tabular output the visual produces
4. Use this to define what "passing" validation looks like

## Key Functions in Captured Queries

| Function | Role |
|---------|------|
| `TREATAS` | Applies filter values as a table filter |
| `SUMMARIZECOLUMNS` | Produces the output table (aggregations + groupings) |
| `IGNORE` | Marks columns as non-aggregating (for ranking, topN) |
| `TOPN` | Limits result rows (often set to 1001) |
| `CALCULATE` | Applies context modification for measures |

## Related

- [[Power-BI-DAX-Query-Data-Validation-Flow]] — Power Automate workflow that uses the captured query
- [[DAX-Query-View-Reference]] — DAX Query View tool reference
