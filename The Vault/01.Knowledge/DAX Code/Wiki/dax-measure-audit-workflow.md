---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
note_type: workflow
tags: [dax, performance, audit, workflow]
---

# DAX Measure Audit Workflow

A 3-step workflow to identify, diagnose, and fix slow DAX measures using Performance Analyzer and DAX Studio. Based on Tejwani's 4-week study of 5,247 measures.

## Prerequisites

- Power BI Desktop with the report open
- DAX Studio (free tool from daxstudio.org)
- XMLA endpoint access (for enterprise models) or local .pbix file

## Steps

### Step 1 — Identify Slow Measures (10 minutes)

1. In Power BI Desktop: **View → Performance Analyzer → Start Recording**
2. Interact with the report: click slicers, change filters, scroll through pages
3. Click **Stop Recording**
4. Expand each visual to see its DAX queries
5. Flag any measure with duration **> 2 seconds**
6. Export or note the 5 slowest measures

> "Slow" is defined as >2s in Performance Analyzer or >1s in isolated DAX Studio test.

### Step 2 — Check for the 5 Patterns (5 minutes per measure)

For each slow measure, scan for these patterns in order:

**Pattern 1 — Unnecessary Iterators**
Look for: `SUMX`, `AVERAGEX`, `COUNTX`, `MAXX`, `MINX` where the expression is a single column reference.
Fix: Replace with `SUM`, `AVERAGE`, `COUNT`, `MIN`, `MAX`.

**Pattern 2 — Calculated Columns**
Look for: Calculated columns in large fact tables used only for aggregation (not for slicing/filtering).
Fix: Move the calculation to a measure.

**Pattern 3 — RELATED() in Iterators**
Look for: `RELATED()` inside a `SUMX`, `AVERAGEX`, etc.
Fix: Store the related value at transaction time in the fact table.

**Pattern 4 — Nested CALCULATE + FILTER(ALL())**
Look for: `CALCULATE(agg, FILTER(ALL(Tbl), condition))`
Fix: Use direct filter: `CALCULATE(agg, Tbl[Col] = value)` or time intelligence functions.

**Pattern 5 — ALL() when REMOVEFILTERS() suffices**
Look for: `ALL(table)` inside `CALCULATE` where the table is not needed as a return value.
Fix: Replace with `REMOVEFILTERS(table)`.

### Step 3 — Rewrite and Test (10 minutes per measure)

1. Rewrite the measure following the fixes above
2. Open DAX Studio, connect to the model
3. Run the measure in DAX Studio's Query Builder or write an EVALUATE query
4. Run **Server Timings** to confirm SE vs FE time
5. Compare before/after from Performance Analyzer
6. Deploy if the measure is faster; otherwise revert and investigate further

```dax
-- Example EVALUATE query to test a measure in DAX Studio
EVALUATE
SUMMARIZECOLUMNS(
    'Date'[Year],
    "Total Sales", [Total Sales]
)
```

## Variations

**For enterprise models via XMLA:**
1. Connect DAX Studio to the XMLA endpoint: `powerbi://api.powerbi.com/v1.0/<tenant>/<workspace>`
2. Query all measures: `SELECT * FROM $SYSTEM.MDSCHEMA_MEASURES`
3. Export to CSV for batch analysis

**For quick visual check without DAX Studio:**
Use Performance Analyzer's **Copy query** button on each visual to capture the raw DAX.

## Common Errors

- Measure works in DAX Studio but not in Power BI → check for missing model relationships
- Performance improved but totals are wrong → verify the pattern doesn't break grand totals

## Related

- [[5-dax-performance-patterns-reference]] — all 5 patterns with benchmarks
- [[unnecessary-iterator-pattern]] — Pattern 1 fix
- [[calculated-columns-vs-measures-performance]] — Pattern 2 fix
- [[related-in-iterators-performance]] — Pattern 3 fix
- [[nested-calculate-direct-filters-pattern]] — Pattern 4 fix
- [[all-vs-removefilters-performance]] — Pattern 5 fix
