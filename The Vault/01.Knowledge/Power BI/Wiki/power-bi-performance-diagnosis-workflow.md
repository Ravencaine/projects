---
created: 2026-08-01
updated: 2026-08-02
source: "How I Reduced a Power BI Visual from 23 Seconds to 8 Seconds A Real Performance Tuning Case Study.md"
note_type: pattern
tags: [power-bi, performance-tuning, performance-analyzer, dax-studio, diagnosis, workflow]
---

# Power BI Performance Diagnosis Workflow

A structured 5-step approach to identifying the true root cause of slow Power BI reports — rather than guessing at DAX, SQL, or data model issues.

## The 5 Steps

### 1. Measure — Performance Analyzer

Start in **Power BI Desktop → Performance Analyzer** (View → Performance Analyzer). Refresh the target visual and record:
- Total visual load time
- DAX query time vs visual rendering time

If DAX query dominates → investigate the DAX and data model. If rendering dominates → investigate the visual configuration and volume.

### 2. Isolate — Narrow the Scope

Confirm the bottleneck is isolated to the specific visual (not the entire report). If only one visual is slow while the rest are responsive, the issue is visual-specific, not model-wide.

### 3. Analyse — DAX Studio Server Timings

Extract the generated DAX query and run it in **DAX Studio** with:
- **Clear cache** (to simulate cold query)
- **Server Timings enabled** (shows Formula Engine vs Storage Engine split)
- **Query Plan captured** (shows physical/logical query plan)

Key ratios to look for:
- High Formula Engine % (>80%) with low row count returned → likely unnecessary iteration or cross-joins
- High Storage Engine query count (1,000+) with low row count → repeated small scans (cardinality issue)
- High Storage Engine % with slow scan times → large table scans needing optimization

### 4. Identify — Read the Generated DAX

Read the full generated DAX query (not just Server Timings). Look for:
- `__DS0PrimaryShowAllCompat` → "Show items with no data" enabled
- Nested `GENERATEALL` → cross-joins
- Excessive `FILTER` or `CALCULATE` wrapping → over-filtering
- `SUMMARIZECOLUMNS` with many grouping columns → high cardinality

### 5. Validate — Repeat Diagnostics After Fix

After making changes, repeat the full diagnostic sequence to confirm the improvement is real and not cached.

## Quick Reference Table

| Step | Tool | Output |
|------|------|--------|
| 1. Measure | Performance Analyzer | Timing breakdown per visual |
| 2. Isolate | Visual-by-visual test | Confirms visual vs model scope |
| 3. Analyse | DAX Studio Server Timings | FE vs SE distribution, SE query count |
| 4. Identify | DAX Studio Query Text | Auto-generated DAX patterns |
| 5. Validate | Repeat steps 1–3 | Confirmed improvement |

## Common Findings by Step

| Symptom | Likely Cause | Tool to Confirm |
|---------|-------------|-----------------|
| High DAX time, low rendering | DAX complexity or cross-joins | DAX Studio |
| 1,000+ SE queries for few rows | "Show items with no data" | Generated DAX |
| High FE% | Inefficient DAX, row-by-row iteration | Query Plan |
| Slow SE scan | Large fact tables, missing relationships | VertiPaq Analyzer |
| Slow rendering | Too many visuals, large data volumes | Performance Analyzer |

## Related

- [[show-items-with-no-data-performance-impact]] — common finding from Step 4
- [[ds0-primary-showallcompat-auto-generated-dax]] — the specific pattern to look for in Step 4
- [[performance-tuning-assumption-gotcha]] — why assumptions fail and data must guide investigation
