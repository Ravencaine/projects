---
created: 2026-07-27
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load"
note_type: workflow
tags: [power-bi, performance, troubleshooting, performance-analyzer, dax-studio, vertipaq]
---

# Power BI Performance Troubleshooting Workflow

A systematic 4-step workflow for diagnosing and fixing slow Power BI reports, from 14s to under 2s.

## Prerequisites

- Power BI Desktop (latest version)
- DAX Studio (free, daxstudio.org)
- Performance Analyzer (built into Power BI Desktop)

## Step 1: Measure with Performance Analyzer

1. Open Power BI Desktop > View > Performance Analyzer
2. Click **Start recording**
3. Refresh all visuals on the report
4. Click **Stop recording**
5. Review each visual's time — identify the slowest 2-3 visuals
6. Note: DAX Query time vs. Visual display time

**Target:** Individual visual DAX query time < 100ms.

## Step 2: Profile Slow DAX in DAX Studio

1. Open DAX Studio (External Tools > DAX Studio, or launch standalone)
2. Connect to the Power BI model (localhost)
3. Paste the slow DAX query (from Performance Analyzer > Copy Query)
4. Click **Run**: note the time
5. Click **Server Timings** tab > Run again — shows storage engine vs. formula engine time

**Key metrics:**
- SE (Storage Engine): fast, parallelizable
- FE (Formula Engine): slow, single-threaded
- If FE is high: DAX expression is complex — simplify or pre-compute

## Step 3: Fix DAX Issues (Most Common Cause)

### Remove Unnecessary ALL() Calls

```dax
-- Slow: ALL removes all filters including Date, causing full table scan
Bad =
CALCULATE (
    [Total Sales],
    ALL ( Sales )  -- too broad
)

-- Fast: remove ALL, use specific filter
Good =
CALCULATE (
    [Total Sales],
    REMOVEFILTERS ( Products )  -- only removes Product filter
)
```

### Fix Nested CALCULATEs

See [[nested-calculate-gotcha]] — flatten nested CALCULATEs into a single CALCULATE.

### Use Variables to Cache Intermediate Results

See [[var-in-dax]] — VAR caches expensive sub-expressions.

## Step 4: Fix Model Issues (if DAX is already optimal)

### Run VertiPaq Analyzer in DAX Studio

1. DAX Studio > Advanced > VertiPaq Analyzer
2. Review table sizes — identify oversized tables
3. Check column cardinality — high cardinality columns (unique IDs, free text) slow down the model
4. Hide unnecessary columns to reduce model size

### Fix Relationship Cross-Filter Direction

- In Model view: right-click relationship > Edit
- Set Cross-filter direction to Single (or Both only where needed)
- Bidirectional cross-filtering causes N×M filter propagation

### Add Aggregations

For tables > 1M rows:
1. Create an aggregation table (pre-summarized at month/category level)
2. Right-click table > Aggregations
3. Configure: GroupBy column + Summarize column

## The Order of Operations

1. Performance Analyzer — identify slow visuals (no guessing)
2. DAX Studio — profile the slow DAX query
3. Fix DAX first — most issues are here
4. Fix model only if DAX is already optimal

## Related

- [[power-bi-performance-optimization]] — preventive optimization checklist
- [[nested-calculate-gotcha]] — DAX fix
- [[dax-performance-5000-measures-source]] — DAX anti-patterns
