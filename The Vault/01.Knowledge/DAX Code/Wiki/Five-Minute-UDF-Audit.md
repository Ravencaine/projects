---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: workflow
tags: [dax, udf, audit, migration, power-bi, inventory]
---

# Five-Minute UDF Audit

Count these three things in your semantic model to find UDF candidates before writing a single line of new code.

## The Audit Checklist

### 1. Duplicate Safe-Division Patterns

Count measures containing:
```
IF ( [Column] = 0, BLANK(), DIVIDE( ... ) )
```
Each distinct variant is a `SafeDivide` UDF candidate.

### 2. Hardcoded Banding / Tiering Thresholds

Count SWITCH statements with numeric thresholds like `0.8`, `0.95`, `80%`, or literal cutoffs that differ across measures.

Each group of similar thresholds is a parameterized banding UDF candidate (e.g., `dwp.ABCBand(pct, TierA:=0.8, TierB:=0.95)`).

### 3. Fragile Business Logic

Ask: if a business rule changed tomorrow, how many measures would need updating identically?

Every "yes" is a single UDF with the rule in one place.

## Expected Finding

Most models with 6+ months of development will find 10–20 candidates. 59 measures often collapse to ~20 distinct functions — many "different" measures are the same logic applied to different columns.

## After the Audit

See [[Measure-Library-to-UDF-Migration]] for the refactoring process.

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[Measure-Library-to-UDF-Migration]] — what to do after auditing
- [[dwp.SafeDivide]] — #1 candidate pattern
- [[dwp.ABCBand]] — #2 candidate pattern
