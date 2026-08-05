---
created: 2026-08-01
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md"
note_type: atomic
tags: [power-bi, performance, dax, optimization, beginner, measurement]
---

# Performance Analyzer Workflow

Before fixing anything, measure. Performance Analyzer ships with Power BI and tells you exactly where time goes per visual.

## How to Use It

1. Go to **View → Performance Analyzer** → click **Start recording**
2. Refresh the visuals on your report
3. Click **Refresh visuals** in the Performance Analyzer pane
4. Expand each visual to see the breakdown

## The Three Numbers

Each visual breaks into three components:

| Component | What It Means | If It's High |
|-----------|--------------|-------------|
| **DAX query** | Time to fetch data from the model | Fix the model or measures |
| **Visual display** | Time to render the result on screen | Simplify the visual |
| **Other** | Background overhead | Usually acceptable |

**Rule:** If DAX query is the long bar, the problem is the model — not the visual. Swapping visual types won't help.

## Case Study Numbers

- Slow matrix: 9,240 ms total → 8,900 ms was DAX query
- Fix: don't swap the matrix for a "lighter" visual; fix the model underneath

## When to Go Deeper

Performance Analyzer shows client-side execution. For engine-level diagnostics:
- **DAX Studio**: query plan and Server Timings
- **VertiPaq Analyzer**: column sizes and model inefficiencies at a glance

Performance Analyzer is enough to find the biggest bottlenecks. Use DAX Studio when you need to drill into specific slow measures.

## Related

- [[star-schema-performance-impact]] — fix DAX query time at the model level
- [[dax-measure-optimization-patterns]] — fix slow DAX measures
