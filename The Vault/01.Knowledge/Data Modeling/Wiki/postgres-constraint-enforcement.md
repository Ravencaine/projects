---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
note_type: pattern
tags: [postgres, database, constraints, foreign-key, unique, not-null, type-safety, pattern]
---

# Postgres Constraint Enforcement Pattern

**Type:** Pattern · **KB:** Data Modeling · **Source:** [[source-excel-postgres-weekend-yadullah]]

PostgreSQL enforces data quality rules at the engine level through constraints. Unlike Excel, where safeguards are optional and overridable, Postgres constraints cannot be bypassed. This replaces manual vigilance with enforced rules.

## Constraint types

| Constraint | Effect | Excel equivalent |
|------------|--------|------------------|
| `UNIQUE` | No duplicate values in column | Data Validation (optional) |
| `NOT NULL` | Column cannot be empty | Data Validation (optional) |
| `FOREIGN KEY` | Reference must exist in parent table | Power Pivot relationship (optional) |
| `CHECK` | Custom boolean expression | Manual formula check |
| Type constraint | Value must match declared type | None |

## Real migration catches

During the author's migration, Postgres caught three data quality issues that Excel had silently allowed:

1. **Duplicate email**: same company entered twice under same email address → UNIQUE constraint on email refused the duplicate
2. **Missing FK reference**: order referenced a customer email that didn't exist → FOREIGN KEY rejected it
3. **Wrong type**: "paid in full" typed into an amount column → type constraint (numeric) rejected it

## Contrast: VLOOKUP vs FK

| VLOOKUP (Excel) | FOREIGN KEY (Postgres) |
|----------------|----------------------|
| Returns blank if not found | REJECTS INSERT if not found |
| No enforcement | Engine-level rejection |
| Manual check required | Automatic |
| Returns stale data if source changes | Always current |

## Why constraints beat manual checks

- Constraints run regardless of who enters data
- Constraints run regardless of deadline pressure
- Constraints fail loudly — data cannot silently enter wrong
- Constraints document intent in the schema itself

## Related

- [[constraints-catch-bad-data-not-bad-formatting]] — limits of constraints
- [[excel-to-postgres-migration-workflow]] — migration process that uses constraints
- [[database-schema-first-migration]] — schema design as the first step
