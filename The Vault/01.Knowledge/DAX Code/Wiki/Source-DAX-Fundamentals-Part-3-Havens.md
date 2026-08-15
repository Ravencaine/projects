---
created: 2026-08-09
updated: 2026-08-09
source: "DAX Fundamentals Part 3 The Patterns That Make Reports Work.md"
source_url: https://www.youtube.com/watch?v=_McUlXEyWyg
creator: Havens Consulting
note_type: source
tags: [dax, time-intelligence, variables, switch, selectedvalue, userelationship, calculation-groups, storage-engine, formula-engine, havens-consulting]
---

# DAX Fundamentals Part 3: The Patterns That Make Reports Work (Havens Consulting)

> **Type:** video (YouTube, ~19 min)
> **Creator:** Reid Havens / Havens Consulting
> **Published:** 2026-06-30
> **URL:** https://www.youtube.com/watch?v=_McUlXEyWyg
> **Guide:** https://go-ae.org/hc-yt-dax-guide-part-3
> **Routed to:** DAX Code

## Summary

Part 3 of the DAX Fundamentals series — patterns built on filter context and CALCULATE foundations. Covers: time intelligence functions, SWITCH/SELECTEDVALUE for dynamic reports, variables, inactive relationships via USERELATIONSHIP, calculation groups as the ultimate deduplication pattern, and how the Storage Engine and Formula Engine divide query work.

## Key Claims

### Time Intelligence
- Prerequisite: proper date table (contiguous dates, no gaps; mark as date table)
- Sources: Power Query, Bravo, DAX, SQL, Tabular Editor
- DATESYTD / DATESQTD / DATESMTD: same pattern, different reset points (year / quarter / month)
- DATEADD: shifts entire date range forward or backward by specified intervals
- These functions return **tables of dates**, not scalar values — CALCULATE uses them as filter arguments internally

### SWITCH + SELECTEDVALUE
- SWITCH = better nested IF (SQL CASE equivalent)
- `SWITCH(TRUE(), condition1, result1, condition2, result2, ...)` — returns first match
- SELECTEDVALUE: returns column value when exactly one value filtered; fallback on multi/no selection
- Common uses: dynamic titles, measure switching, what-if parameters
- Field parameters can replace some SWITCH patterns (user selects which measure appears in a visual)

### Variables
- Capture context at definition time — evaluated once, referenced many times
- Benefits: performance (declared once, not recalculated per condition), readability, debuggability
- Swap RETURN for a variable name to smoke-test intermediate values
- Tabular Editor 3 DAX debugger for step-through evaluation
- DAX Query View also provides debugging capabilities

### USERELATIONSHIP
- One active relationship per table pair; second relationship must be inactive
- USERELATIONSHIP activates an inactive path inside CALCULATE
- Automatically deactivates conflicting relationships — no NOT-USERELATIONSHIP needed
- Use case: fact table with two date columns (Trade Date, Delivery Date) both pointing to Calendar table

### Calculation Groups
- Modifier wrapping around any measure — report/page/visual level
- Write base measures once; calc group applies YTD, Prior Cycle, YoY%, etc.
- Without: 9 measures (base × 3 time calcs × 3 scenarios)
- With: 3 base measures + 1 calc group
- SELECTEDMEASURE: applies calc group to any measure in the visual (not just one named measure)
- Pattern: default item (no modification) + items with time intelligence modifiers
- UDFs covered in Part 4 (planned follow-up)

### Engine Architecture
- DAX runs a two-stage query process
- **Storage Engine (VertiPaq):** in-memory columnar compression, parallelised, very fast; retrieves and constructs data
- **Formula Engine:** evaluates DAX expressions (CALCULATE, iterators, variables), single-threaded, slower
- **Rule:** push as much work to Storage Engine as possible

### Fast Patterns (Storage Engine-Friendly)
- Simple aggregations: SUM, COUNT, MIN, MAX on direct column references
- Star schema with clean foreign keys
- Basic CALCULATE with table filters

### Slow Patterns (Formula Engine-Heavy)
- Complex iterators (SUMX with nested logic)
- Nested CALCULATE inside CALCULATE
- Row-by-row processing
- X/iterator functions
- Many-to-many relationships without bridge tables (no dictionary/mapping; real-time path lookup)

### Many-to-Many Note
- One-to-many and one-to-one relationships have dictionaries (saved row-by-row mappings)
- Many-to-many relationships lack dictionaries — paths must be resolved at query time
- Historically called "weak relationships" — avoid unless bridge tables are impractical

### Key Takeaways
1. Time intelligence functions return tables, not scalars
2. Variables capture context at definition; cannot add filters after declaration
3. USERELATIONSHIP implicitly deactivates conflicting relationships
4. Calculation groups eliminate measure duplication
5. Push work to Storage Engine via model design (star schema + simple aggregations)
6. All patterns build on filter context + CALCULATE foundations

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX Fundamentals Part 3 The Patterns That Make Reports Work.md |
| Transcript | Full YouTube transcript included in source file |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
