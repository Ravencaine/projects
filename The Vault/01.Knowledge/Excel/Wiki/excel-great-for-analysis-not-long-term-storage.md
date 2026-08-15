---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
note_type: atomic
tags: [excel, analysis, data-sharing, system-of-record, limitation, atomic]
---

# Excel Great for Analysis Not Long Term Storage Atomic

**Type:** Atomic · **KB:** Excel · **Source:** [[source-excel-postgres-weekend-yadullah]]

Excel is the right tool for ad-hoc analysis and data sharing with non-SQL users. It is the wrong tool for long-term systems of record where data integrity, relationships, and auditability matter.

## When Excel is right

| Use case | Why Excel works |
|----------|---------------|
| Ad-hoc analysis | Fast iteration, no schema required |
| Data sharing with non-SQL users | Recipients just open the file |
| One-off reporting | No infrastructure needed |
| Prototyping | Quick to build, quick to throw away |
| Visualization for presentation | Native charting, conditional formatting |

## When Excel breaks down

| Use case | Why Excel fails |
|----------|----------------|
| Long-term data storage | No enforced integrity, easy to corrupt |
| Multi-user data entry | No concurrent locking, no audit trail |
| Cross-reference across datasets | VLOOKUP fragility, no foreign keys |
| Data requiring relationships | Power Pivot optional, easily overridden |
| Query-based reporting | No SQL; complex queries require complex formulas |

## The mental model shift

Excel is a **personal tool:** one person, one file, one version of truth (if disciplined). A database is a **system:** multiple users, enforced rules, queryable by any tool, backed up reliably.

## Author's conclusion

"Excel isn't useless, and I still use it for sharing data with people who aren't going to run SQL queries. But as a system of record, it was never built for the job I was asking it to do."

## Related

- [[excel-vlookup-fragility]] — specific failure modes at scale
- [[excel-optional-safeguards]] — why safeguards don't scale
- [[excel-to-postgres-migration-workflow]] — when and how to migrate
