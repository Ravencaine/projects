---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, performance, storage-engine, formula-engine, optimization]
note_type: pattern

---

# Storage Engine vs Formula Engine in DAX

Understanding the two processing engines that execute DAX queries.

## Overview

```
DAX Query
    --> Formula Engine (FE)  -->  Storage Engine (SE)  -->  Data Cache
         (orchestration)          (data retrieval)
```

## Storage Engine (SE)

- Fast, highly parallelized
- Reads data from the VertiPaq engine
- Handles: simple aggregations, column scans, basic filters
- Returns compressed data to the Formula Engine
- Can cache results in the Data Cache

## Formula Engine (FE)

- Slow, single-threaded (for a given query)
- Handles: complex logic, iterators, cross-joins, complex filters
- Calls the Storage Engine for data
- The bottleneck in most slow DAX

## Optimization Strategy

1. Push as much work as possible to the SE
2. Minimize FE complexity (fewer IFs, simpler iterators)
3. Reduce the number of SE calls (combine filters)

## Fast SE Operations

- SUM, COUNT, MIN, MAX, AVERAGE
- Simple column references
- FILTER with simple conditions
- CALCULATE with simple filters

## Slow FE Operations

- Complex nested IF/SWITCH
- Multi-column CROSSJOIN
- Complex iterator expressions
- SUBSTITUTE with large strings

## Related

- [[dax-performance-optimization-techniques]]
- [[performance-analyzer-debugging]]
