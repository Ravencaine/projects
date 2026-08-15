---
created: 2026-08-08
updated: 2026-08-08
source: ABC Analysis in Power BI The Chart That Shows Your 8020 Instantly
note_type: pattern
tags: [power-bi, visual-calculations, abc-analysis, pareto, chart]
---

# ABC Classification Chart with Visual Calculations

Build a Pareto/ABC analysis chart in Power BI that shows which products/clients drive 80% of revenue — using only visual calculations, no model-level measures.

## Goal

Visualise the Pareto principle (80/20 rule) as an ABC classification:
- **A bucket:** top products contributing up to 40% of total
- **B bucket:** products from 40% to 80%
- **C bucket:** remaining products (tail)

## Chart Structure

**Base:** Line and clustered column chart

| Axis | Element | Source |
|------|---------|--------|
| X-axis | Breakdown dimension (ProductId, CustomerId, etc.) | Data field on Rows |
| Column Y-axis | TotalSales (hidden → moved to Tooltips to enable sorting) | Data field |
| Column Y-axis | Group A / Group B / Group C (stacked columns) | Visual calculations |
| Line Y-axis | % of Total + Running Sum (Pareto line) | Visual calculations |
| Data labels | A / B / C on last item per bucket | Visual calculations |

## Step-by-Step

### Step 1 — Percent of Total (visual calculation)

```
% of Total =
  COLLAPSESUM(SUM(Sales[SalesAmount]))
  / COLLAPSESUM(SUM(Sales[SalesAmount]), ALL)
```

> Uses `ROWS` implicitly (not hard-coded ProductId) — swaps to any dimension without editing.

### Step 2 — Running Sum (visual calculation)

```
Running Sum =
  RUNNINGSUM(
    [% of Total],
    ORDER BY [Total Sales] DESC,
    ROWS
  )
```

### Step 3 — Stacked ABC columns (visual calculations)

```
Group A = IF([Running Sum] <= 0.4, 0.4, BLANK())
Group B = IF([Running Sum] > 0.4 && [Running Sum] <= 0.8, 0.8, BLANK())
Group C = IF([Running Sum] > 0.8, 1.0, BLANK())
```

### Step 4 — Stack and overlap

1. Put Group A, B, C all on Column Y-axis → they stack automatically
2. In **Format → Columns → Layout**: set **Overlap** = 100%, **Space between categories** = 0%
3. Use **Flip overlap** button to separate into three bands
4. Assign distinct colours: green (A), light blue (B), orange (C)

### Step 5 — ABC labels (last item per bucket)

Use `NEXT` to find the last product in each group, then show a data label only on that dot:

```
Next Running Sum =
  NEXT(
    [Running Sum],
    ORDER BY [Total Sales] DESC,
    ROWS
  )

// Group B label condition:
= IF([Group B] - [Next Running Sum] > 0, [Group B], BLANK())
```

Then: data label → value ON, title ON, label text = "B"; marker hidden for all other points.

## Formatting Details

- Visual calculation data formats must be set in **Properties → Data format** (not the main format pane)
- Set % of Total and Running Sum as **decimal number → percentage, 0 decimals**
- Line colour: black; width: 2px; markers: on for Pareto line only
- Grid lines: off

## Key Insight

> For visual calculations, you can only reference values that are **on the visual:** even if hidden. Use the data pane visibility (eye icon) to hide without removing from the visual's accessible fields.

## Related

- [[Visual-Calculations-COLLAPSESUM]] — COLLAPSESUM / COLLAPSE ALL
- [[Visual-Calculations-RUNNINGSUM-ORDER-BY]] — RUNNINGSUM with ORDER BY
- [[Visual-Calculations-NEXT]] — NEXT function for last-in-group detection
- [[ABC-Group-Thresholds-Stacked-Columns]] — threshold stacking technique
