---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
note_type: atomic
tags: [excel, vlookup, fragility, data-quality, risk, atomic]
---

# Excel VLOOKUP Fragility Atomic

**Type:** Atomic · **KB:** Excel · **Source:** [[source-excel-postgres-weekend-yadullah]]

Excel VLOOKUP-based data models degrade silently under scale. Three specific failure modes: cross-referencing multiple sheets, deleted-cell formula drift, and accidental filter deletion. All three caused real data loss in the author's experience.

## Failure mode 1 — multi-sheet cross-reference

When a question requires cross-referencing three separate spreadsheets, VLOOKUP chains become fragile. Each lookup is a point of failure; if one sheet's row order changes, all downstream VLOOKUPs return wrong values silently.

## Failure mode 2 — deleted cell formula drift

Formulas pointing at cells that were later deleted silently break or return errors. Over years of edits, these accumulate invisibly until a critical query reveals the gap.

## Failure mode 3 — filter fat-finger

Accidentally applying a filter can hide half the rows. If the user doesn't notice before saving, the hidden data is effectively lost.

## Why this matters

Each failure mode requires manual vigilance to prevent. There is no enforced referential integrity — no foreign key equivalent — to catch these at the source.

## Related

- [[excel-optional-safeguards]] — validation and Power Pivot are optional, not enforced
- [[excel-great-for-analysis-not-long-term-storage]] — Excel appropriate for ad-hoc, not systems of record
