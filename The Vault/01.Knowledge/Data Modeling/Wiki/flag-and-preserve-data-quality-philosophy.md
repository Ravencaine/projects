---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: atomic
tags: [data-warehouse, data-quality, etl, elt, philosophy, flag-preserve]
---

# Flag and Preserve — Data Quality Philosophy

Never silently discard non-matching or suspicious source values. Preserve them in raw form with an `is_matched` flag column. This transforms data quality from a one-time cleanup into a continuously improving, observable process.

## Definition

For every column being matched against a reference table: if the match succeeds, store the standardized value; if it fails, keep the original raw value and add an `is_matched` boolean column alongside it.

## Key Points

- **The delete-or-assume trap:** silently deleting bad records or labeling them "Unknown" makes reports look clean but destroys the evidence of what went wrong
- **Flag-and-preserve keeps data loss visible:** a query filtering `is_matched = false` instantly surfaces every non-matching value, turning quality improvement into an ongoing process
- **Business users can distinguish** between definitively verified records and raw/unverified ones
- The principle extends beyond matching: explicitly document placeholder/test values in code rather than silently grouping them with real data

## Examples

```sql
-- Instead of:
UPDATE staging_location
SET location = 'Unknown'
WHERE location NOT IN (SELECT code FROM ref_location);

-- Do this:
ALTER TABLE staging_location
ADD COLUMN is_matched BOOLEAN;

UPDATE staging_location
SET is_matched = (location IN (SELECT code FROM ref_location));
-- Keep raw value; let downstream consumers decide how to handle unmatched rows
```

## General Rule

> When making a data quality decision, ask: "Six months from now, if someone asks why this decision was made, can the code and the data give them the answer?" If no — you are hiding the problem, not solving it.

## Related

- [[same-code-different-meanings-code-column-reliability]] — a specific case this philosophy applies to
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
