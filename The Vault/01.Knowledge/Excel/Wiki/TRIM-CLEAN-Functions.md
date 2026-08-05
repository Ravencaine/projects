---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, formula, trim, clean, spaces, non-printable, text-cleaning]
---

# TRIM and CLEAN Functions

`TRIM()` removes leading/trailing spaces and normalises internal multiple spaces to one. `CLEAN()` removes non-printable ASCII characters (0–31). `CLEAN(TRIM())` is the combination for fully cleaning imported text.

## TRIM

```excel
=TRIM(A2)
```

- Removes all leading and trailing spaces
- Collapses multiple internal spaces to a single space
- Does NOT remove non-breaking spaces (CHAR(160 / &nbsp;)
- Use for: copy-pasted data, imported CSVs, data from PDFs

## CLEAN

```excel
=CLEAN(A2)
```

- Removes non-printable ASCII characters (CHAR(0) through CHAR(31))
- Does NOT remove normal spaces or non-breaking spaces
- Use for: data imported from legacy systems, emails, PDFs with embedded control characters

## CLEAN(TRIM) — The Combo

```excel
=CLEAN(TRIM(A2))
```

Apply TRIM first (removes spaces), then CLEAN (removes remaining invisible characters). This is the standard order for imported text that may contain both.

## Limitation: Non-Breaking Spaces

`CLEAN()` does not remove CHAR(160) — the non-breaking space that appears when copying from websites. To handle this:

```excel
=SUBSTITUTE(CLEAN(TRIM(A2)), CHAR(160), "")
```

Or in Power Query: use `Text.Clean(Text.Trim(...))` — `Text.Clean` in M does handle CHAR(160).

## Why It Matters

Invisible spaces silently break:
- VLOOKUP / XLOOKUP → #N/A errors
- Pivot Table groupings → duplicate or missing entries
- Duplicate checks → false positives
- Power Query merges → mismatched joins

## The Rule

> Make TRIM your first step before any lookup, merge, or duplicate check.

## Related

- [[Text-Transform-M-Power-Query]] — `Text.Trim`, `Text.Clean` in Power Query
- [[Inconsistent-Categories-Normalisation]] (Data Modeling) — Text.Trim for category normalisation
