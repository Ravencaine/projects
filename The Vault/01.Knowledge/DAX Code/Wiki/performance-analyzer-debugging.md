---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, performance, debugging, performance-analyzer, power-bi]
note_type: pattern

---

# Performance Analyzer Debugging in DAX

Using Power BI Performance Analyzer to identify slow visuals and DAX bottlenecks.

## Reading Performance Analyzer Output

1. Open View > Performance Analyzer
2. Click Start Recording
3. Interact with the visual
4. Click Refresh visual
5. Expand the visual to see DAX query times

## Key Metrics

| Metric | Meaning |
|--------|---------|
| DAX Query | Time to execute the DAX query |
| Visual Display | Time to render after data arrives |
| Overhead | Other processing time |

## Common Fixes

| Problem | Solution |
|---------|----------|
| Slow DAX query | Simplify measure, reduce cross-joins |
| High SE time | Pre-aggregate data, reduce model size |
| Visual display slow | Simplify visual, reduce data points |

## Notes

- DAX Studio Server Timings provide deeper analysis
- The Performance Analyzer shows which visuals are slow, not why

## Related

- [[dax-performance-optimization-techniques]]
- [[storage-engine-vs-formula-engine-in-dax]]
