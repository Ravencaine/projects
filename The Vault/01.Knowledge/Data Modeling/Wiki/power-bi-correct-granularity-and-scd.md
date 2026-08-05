---
created: 2026-07-27
updated: 2026-08-02
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: atomic
tags: [granularity, scd, slowly-changing-dimension, power-bi, performance]
---

# Correct Granularity and SCD Performance

Joining a fact table to a slowly changing dimension (SCD) table at the wrong granularity causes Power BI to recalculate the entire fact table in memory — one of the most expensive performance mistakes possible.

## Definition

An SCD Type 2 stores multiple versions of a dimension row (with effective date ranges). The fact table must join to the dimension at the correct point-in-time key — not to the current-version dimension row if the fact records historical transactions.

Joining at the wrong granularity forces the engine to evaluate SCD version logic for every fact row on every query.

## Key Points

**The problem:** A client joined fact_sales to a SCD product dimension using a product key. The dimension had type-2 rows with date ranges. A MAXX measure was added to find the "current" version per key — but this forced the entire fact table to be recalculated in memory on every query, because no surrogate key on the fact pointed to the correct SCD version.

**The fix:** Assign a surrogate key to every SCD row (including inactive versions). Fact rows join to the specific SCD version that was active at transaction time. Inactive rows are never in the fact table → never queried.

**Query time went from seconds to milliseconds** after the fix.

## Why It Happens

- Type-2 SCD rows accumulate: each version of a dimension member is a separate row
- Without a fact-table surrogate key pointing to the correct version, the engine must evaluate the date range for every row on every query
- MAXX/HISTORY functions iterate the entire dimension looking for the correct version — extremely expensive on large fact tables

## Prevention

- Always assign a surrogate key to every row in a SCD table (active and inactive)
- Store the appropriate surrogate key on the fact table at ETL time (point-in-time correct key)
- Never join a fact table to a dimension using a business key that requires MAXX/HISTORY to resolve the correct version at query time

## Related

- [[surrogate-keys-vs-composite-keys]] — the key design pattern that enables correct granularity
- [[scd-type-1-price-changes]] — SCD Type 1 (overwrite) vs Type 2 (history)
