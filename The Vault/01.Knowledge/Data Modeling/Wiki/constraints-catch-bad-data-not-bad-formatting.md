---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
note_type: atomic
tags: [postgres, constraints, data-quality, type-safety, formatting, atomic]
---

# Constraints Catch Bad Data Not Bad Formatting Atomic

**Type:** Atomic · **KB:** Data Modeling · **Source:** [[source-excel-postgres-weekend-yadullah]]

Postgres constraints enforce type and referential integrity — they reject wrong types, missing required values, and orphaned foreign keys. They do NOT normalize inconsistent text formatting. Understanding this boundary prevents misusing constraints as a formatting tool.

## What constraints catch

| Constraint | Catches | Example |
|------------|---------|---------|
| Type constraint | Wrong data type | "paid in full" in amount column (numeric expected) |
| NOT NULL | Missing required value | Order with no order date |
| UNIQUE | Duplicate value | Same email entered twice |
| FOREIGN KEY | Orphaned reference | Order referencing non-existent customer |
| CHECK | Custom rule violation | Amount < 0 when balance should never go negative |

## What constraints do NOT catch

| Problem | Why constraints miss it | Solution |
|---------|------------------------|----------|
| Inconsistent boolean values | `"yes"`, `"Y"`, `"true"`, `"N"` all valid text | Normalize before insert (pandas `.str.lower()`) |
| Trailing/leading spaces | Spaces are valid characters in text | `.str.strip()` before insert |
| Case inconsistency | `"Acme Corp"` vs `"acme corp"` | Normalize to lowercase before insert |
| Misspelled names | Still valid text | Not caught; requires external validation |

## Postgres boolean parsing

Postgres does parse common boolean representations: `yes/no`, `true/false`, `on/off`, `1/0`. An invoice column with `yes/no/true/N` was mostly accepted. But this is type parsing, not constraint enforcement — it's a convenience, not a guarantee.

## Practical implication

Before migration: clean the data (strip spaces, normalize case, standardize booleans). After migration: constraints catch type violations automatically.

## Related

- [[postgres-constraint-enforcement]] — what constraints catch
- [[excel-to-postgres-migration-workflow]] — cleaning data before insert
- [[normalized-tables-vs-flat-rows]] — why inconsistencies surface at schema design
