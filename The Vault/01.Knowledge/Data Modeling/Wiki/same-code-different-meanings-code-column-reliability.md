---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: atomic
tags: [data-warehouse, data-quality, dimension-table, code-column, conformance]
---

# Same Code, Different Meanings — Code Column Reliability

A code or type column does not always mean the same thing across the source system's lifetime or across modules. Using it directly as a dimension table key produces silent misclassifications — the query runs, it just returns wrong results.

## Definition

Code columns (status codes, type codes) can accumulate inconsistent meanings over time as different modules start using the same numeric or string value to represent different business concepts.

## Key Points

- Source systems evolve: a code value that originally meant one thing gains additional meanings as the system grows
- The query does not error — it silently returns wrong counts, wrong groupings, wrong aggregations
- **Workaround:** exclude the unreliable code column; use the cleaned text value as the natural key instead
- Text comparison carries a small performance cost, but is significantly more reliable

## Examples

A status code column (`status_id`) had multiple different `status_text` values mapped to the same numeric code. Using `status_id` as the dimension table key would group records with genuinely different statuses together.

Resolution: use `status_text` (the actual text) as the natural key, mapping each unique text string to a dimension row.

## Related

- [[unique-key-that-isnt-primary-key-verification]] — another source system assumption to verify
- [[flag-and-preserve-data-quality-philosophy]] — general philosophy for handling unreliable source data
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
