---
created: 2026-08-05
source: Blank Values in Power BI Reports (Boniface Muchendu)
source_url: https://databear.com/blank-values-in-power-bi-reports/
note_type: source
tags: [power-bi, dax, blank, isblank, card-visual, measure]
---

# Blank Values in Power BI Reports (Boniface Muchendu)

Three strategies for handling blank/missing values in Power BI: `+ 0` in measures, the New Card Visual's built-in option, and DAX `IF` with implicit/explicit blank checking.

> **Type:** article
> **Author:** Boniface Muchendu (DataBear)
> **Published:** 2024-03-03
> **URL:** https://databear.com/blank-values-in-power-bi-reports/
> **Routed to:** Power BI (card visual), DAX Code (IF patterns)

## Summary

Boniface Muchendu (DataBear) addresses blank value display in Power BI card visuals. Blank values arise legitimately when no data exists for a filter combination. Three solutions: appending `+ 0` to a measure, using the New Card Visual's "Show blank value as" toggle, or writing an explicit DAX `IF` measure with custom display text.

## Key Claims

- `+ 0` appended to any measure forces a numeric return instead of blank — works universally but forces zero display in charts
- New Card Visual has a native "Show blank value as" setting — no DAX needed
- `IF(ISBLANK([Measure]), "N/A", [Measure])` is the explicit form
- `IF([Measure], [Measure], "N/A")` is the implicit form — IF short-circuits on blank
- `+ 0` is quick but has a chart-side effect: it converts blanks to zeros in visuals

## Extracted Notes

Links to notes derived from this source:

- [[Plus-Zero-Blanks-Atomic]] — `atomic` — the `+ 0` fix: how it works, when to use, when to avoid
- [[New-Card-Visual-Blank-Setting]] — `atomic` — the New Card Visual's "Show blank value as" built-in option
- [[IF-Implicit-Blank-Check-Pattern]] — `pattern` — `IF([Measure], [Measure], "N/A")` — implicit blank check without ISBLANK
- [[Choosing-Blank-Value-Strategy]] — `comparison` — comparing `+ 0`, Card Visual, and IF approaches
- [[Author-Boniface-Muchendu]] — `author` — Boniface Muchendu, DataBear (3 sources)

## Metadata

| Field | Value |
|-------|-------|
| Source file | 3 Ways of dealing with Blank Values in Power BI Reports.md |
| Archived at | — |
| Ingestion date | 2026-08-05 |
| Word count | ~350 |
