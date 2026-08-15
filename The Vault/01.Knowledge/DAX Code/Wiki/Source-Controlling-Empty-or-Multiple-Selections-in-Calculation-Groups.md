---
created: 2026-08-06
updated: 2026-08-06
source: Controlling empty or multiple selections in calculation groups
source_url: https://www.sqlbi.com/articles/controlling-empty-or-multiple-selections-in-calculation-groups/
note_type: source
tags: [calculation-groups, dax, tabular, multiple-selection, empty-selection, sqlbi, marco-russo, alberto-ferrari]
---

# Controlling Empty or Multiple Selections in Calculation Groups (Russo & Ferrari / SQLBI)

A SQLBI article by Marco Russo & Alberto Ferrari on two new calculation group properties — `multipleOrEmptySelectionExpression` and `noSelectionExpression` — that intercept DAX execution when a calculation group has zero, one, or multiple active calculation items.

> **Type:** article
> **Authors:** Marco Russo & Alberto Ferrari (SQLBI)
> **Published:** 2025-06-02
> **URL:** https://www.sqlbi.com/articles/controlling-empty-or-multiple-selections-in-calculation-groups/
> **Routed to:** DAX Code

## Summary

Calculation groups execute only when exactly one item is active in a visual's filter context. When the CG column is absent from the visual, multiple selections in a slicer, empty selections (e.g., item renamed after report saved), or no selection all silently fall back to the original measure value. Two new TMDL-editable properties address this gap: `multipleOrEmptySelectionExpression` intercepts 0 or ≥2 active items; `noSelectionExpression` intercepts when no CG filters are active at all. Both require compatibility level 1605 and are in preview as of May 2025. The article covers four worked examples: error-raising strict mode, highest-ordinal fallback, Time Intelligence item combination via INTERSECT/SWITCH, and a currency conversion no-selection default. Key insight: "empty selection" ≠ "no selection" — empty means filter active but zero rows; no selection means no filter at all.

## Key Claims

- CG silently ignores all items when ≥2 are active or when 0 are selected outside the visual — both return raw measure values
- `multipleOrEmptySelectionExpression` intercepts both zero AND multiple items (same event)
- `noSelectionExpression` fires only when the CG column has zero filters — different from empty selection
- Empty selection scenario: item renamed in the model after report was saved → report filter references non-existent item → zero rows visible
- All three conditions can now be intercepted and handled programmatically
- Both properties require CL ≥ 1605; Tabular Editor hides them if CL < 1605
- Performance note: these properties add DAX engine overhead — always test before releasing (SQLBI recommends the Optimizing DAX video course)
- Currency conversion no-selection pattern: applies conversion automatically unless user selects "No conversion" calculation item

## Notable Details

- No downloads — all 3 URLs are SQLBI/Tabular Editor/Power BI article/tool links (skip)
- [[Author-Marco-Russo-Alberto-Ferrari]] — new author note created
- [[Controlling-Calculation-Group-Selection]] — atomic concept note
- [[Calculation-Group-Multiple-Selection-Pattern]] — pattern note with 4 worked examples
- [[Calculation-Group-No-Selection-Default-Pattern]] — no-selection pattern with currency conversion example
- [[TMDL-Syntax-Calculation-Group-Properties]] — TMDL syntax reference

## Extracted Notes

Links to notes derived from this source:

- [[Controlling-Calculation-Group-Selection]] — `atomic` — concept overview
- [[Calculation-Group-Multiple-Selection-Pattern]] — `pattern` — multiple selection DAX patterns
- [[Calculation-Group-No-Selection-Default-Pattern]] — `pattern` — no-selection default patterns
- [[TMDL-Syntax-Calculation-Group-Properties]] — `reference` — TMDL syntax reference

## Metadata

| Field | Value |
|-------|-------|
| Source file | Controlling empty or multiple selections in calculation groups.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-06 |
| Word count | ~3,200 |
