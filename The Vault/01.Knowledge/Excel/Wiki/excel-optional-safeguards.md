---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
note_type: atomic
tags: [excel, data-validation, power-pivot, optional, safeguards, atomic]
---

# Excel Optional Safeguards Atomic

**Type:** Atomic · **KB:** Excel · **Source:** [[source-excel-postgres-weekend-yadullah]]

Excel's data integrity features — data validation, Power Pivot relationships — are all optional and can be overridden at any time. There is no enforced referential integrity. Every safeguard depends on user discipline, which breaks under deadline pressure.

## What Excel offers (but doesn't enforce)

| Feature | What it does | Enforced? |
|---------|-------------|-----------|
| Data Validation | Restricts cell input to defined rules | No — can be bypassed |
| Power Pivot relationships | Models relationships between tables | No — can be overridden |
| Named ranges | Stable references across sheets | No — deleted ranges break formulas |
| Workbook protection | Prevents sheet edits | No — easily turned off |

## The core problem

Excel assumes the user is the safeguard. A database enforces constraints regardless of who is using it. When deadlines pressure shortcuts, optional safeguards become theoretical ones.

## Contrast with database constraints

Postgres foreign key, NOT NULL, UNIQUE, and CHECK constraints are enforced by the engine — they cannot be overridden by the user entering data. The system replaces the habit.

## Related

- [[excel-vlookup-fragility]] — what breaks when safeguards fail
- [[excel-great-for-analysis-not-long-term-storage]] — appropriate scope for Excel
