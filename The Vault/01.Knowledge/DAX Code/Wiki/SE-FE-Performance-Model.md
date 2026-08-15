---
created: 2026-08-11
source: How DAX Studio Helped Us Reduce Power BI Report Load Time in Production — Part 1 of 2.md
note_type: atomic
tags: [dax, performance, storage-engine, formula-engine, mental-model, analogy]
---

# SE/FE Performance Model: The Warehouse Analogy

The Storage Engine (SE) and Formula Engine (FE) have fundamentally different performance characteristics. A simple analogy explains why.

## The Analogy: Counting a Word in a Book

**Setup:** 1,000-page book. Goal: find the page with the most occurrences of the word "Data".

**Step 1 — SE counts (parallel, mechanical):**
Hand the book to 5 workers, each assigned 200 pages. Each worker scans their own pages and writes a single number: *page number → count of "Data"*. No worker needs to know what anyone else found. This is fast and parallel — purely mechanical. This is the Storage Engine scanning columns.

**Step 2 — FE compares (serial, needs the full picture):**
Now you have 1,000 slips of paper, one per page. To find the page with the *maximum* count, one person must read all 1,000 slips sequentially, tracking the highest number. This cannot be split across workers. This is the Formula Engine working on SE's already-summarised results.

## The Punchline

SE did the expensive-looking work (reading every page) but did it fast because it was parallel. FE did comparatively little raw work (scanning 1,000 numbers, not 1,000 pages) but had to do it alone.

**The critical insight:** A badly-written DAX instruction that tells FE *"for every page, re-read the entire book"* forces FE to redo SE's job over and over — turning a fast parallel engine into a slow serial bottleneck.

## Practical Interpretation

- **SE-heavy, FE-light query** = healthy; SE did the heavy lifting in parallel, FE finished with a small dataset
- **FE-heavy query** = danger signal; FE is doing too much work, likely re-scanning data that SE already processed
- **FE repeatedly re-triggering SE** = worst case; each FE row forces a new SE scan — the row-count multiplier effect compounds

## Related

- [[Storage-Engine-vs-Formula-Engine]] — SE vs FE defined
- [[DAX-Studio-Debug-Workflow]] — practical debugging workflow
- [[FILTER-ALL-Inside-CALCULATE-AntiPattern]] — the anti-pattern that forces FE to re-scan
