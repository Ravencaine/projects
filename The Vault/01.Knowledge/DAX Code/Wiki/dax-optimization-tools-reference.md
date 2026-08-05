---
created: 2026-07-30
updated: 2026-08-02
source: "dax4humans_ch15_dax_studio.txt"
note_type: reference
tags: [dax-studio, optimization, tools, performance, benchmark]
---

# DAX Optimization Tools — Quick Reference

Overview of the three primary tools for analyzing and improving DAX query performance in Power BI.

## Quick Reference

| Tool | Type | Cost | Best For |
|------|------|------|----------|
| Performance Analyzer | Built-in pane (Power BI Desktop) | Free | Quick visual-level timings |
| DAX Studio | Standalone application | Free | Detailed SE/FE breakdown, benchmark |
| Power Optimizer (TruViz) | External tool | Free/AI-powered | Full semantic model audit + AI suggestions |

---

### Performance Analyzer (Built-in)

**Access:** View → Performance Analyzer → Start recording → Refresh visuals

Breaks each visual's render time into:
- **DAX query**: time to execute the DAX query (the only part developers can optimize)
- **Visual display**: rendering time for the visual itself
- **Other**: query preparation, waiting on other visuals, background tasks
- **Evaluated parameters**: time spent on field parameters (if enabled)

Click **Run in DAX query view** to export the raw DAX query for use in DAX Studio.

---

### DAX Studio

**Download:** https://daxstudio.org/downloads/

Free, open-source. Key features:
- **Server Timing** tab — shows time spent in Storage Engine (SE) vs Formula Engine (FE)
- **Benchmark**: run the same query multiple times to get consistent timings
- **Query History**: captures all queries executed against the model
- **Export Query** from Performance Analyzer → paste into DAX Studio for analysis

Typical benchmark output:

| Metric | Value |
|--------|-------|
| Total (FE) | ~100% |
| SE | ~0% (fast) or >0% (slower) |

---

### Power Optimizer by TruViz

**Download:** https://thepowertools.ai/

AI-powered. Features:
- Performance analysis of all DAX calculations
- Identifies unused tables, columns, and measures
- Visualizes relationships between measures, calculated columns, visuals, and pages
- **Suggests fixes**: not just identifies problems

Also useful: **Powerops** (https://powerops.app/) — best practices checker for DAX code.

---

## Key Workflow

1. Identify slow visual in **Performance Analyzer**
2. Export DAX query via "Run in DAX query view"
3. Paste into **DAX Studio**
4. Run benchmark to confirm time split (SE vs FE)
5. Apply optimization techniques
6. Re-run benchmark to measure improvement

## Notes

- Power Optimizer requires an internet connection (cloud AI).
- DAX Studio requires the `.pbix` to be open (it connects to the running Power BI Desktop instance via the External Tools tab, or opens a `.pbip` model directly).
- Alex Nolock's VERTIPAQ analyzer in DAX Studio is also valuable for seeing column cardinality and compression ratios.

## Related

- [[dax-optimization-9-iteration-case-study]] — worked example of optimizing a slow measure
- [[storage-engine-vs-formula-engine-in-dax]] — understanding SE vs FE
