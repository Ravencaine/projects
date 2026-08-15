---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
note_type: atomic
tags: [normalization, database-design, schema, flat-rows, atomic]
---

# Normalized Tables vs Flat Rows Atomic

**Type:** Atomic · **KB:** Data Modeling · **Source:** [[source-excel-postgres-weekend-yadullah]]

Designing normalized tables before migration exposes the true state of denormalized data. Sketching customers, orders, and payments as separate tables revealed years of accumulated duplicate and inconsistent entries that flat-row spreadsheets had hidden.

## What normalization reveals

When you map a flat spreadsheet to normalized tables:

- **Duplicate records:** same entity entered multiple times (different spellings, trailing spaces)
- **Inconsistent fields:** same field with different formats across rows ("yes"/"Y"/"true", "N"/"no"/"false")
- **Missing relationships:** orders with no matching customer record
- **Orphaned entries:** records with no foreign key relationship

## The schema-first insight

The act of sketching tables (customers, orders, payments) is itself the first data quality audit. Before writing any migration script, the schema design surfaces problems that were invisible in flat rows.

## Example: flat rows hiding duplicates

In a flat spreadsheet, the same company might appear as:
- `Acme Corp`
- `Acme Corp `
- `ACME CORP`
- `acme corp`

These are four rows in Excel but represent one entity. Normalization forces this collision to be resolved.

## Related

- [[database-schema-first-migration]] — schema design as migration step 1
- [[postgres-constraint-enforcement]] — constraints catch duplicates after design
- [[excel-to-postgres-migration-workflow]] — full migration process
