---
created: 2026-08-06
updated: 2026-08-06
source: Controlling Format Strings in Calculation Groups
source_url: https://www.sqlbi.com/articles/controlling-format-strings-in-calculation-groups/
note_type: source
tags: [calculation-groups, dax, format-string, tabular, Marco-Russo, sqlbi]
---

# Controlling Format Strings in Calculation Groups (Russo / SQLBI)

A SQLBI article by Marco Russo on the *Format String Expression* property of calculation items — how to dynamically override a measure's display format from within a calculation group using [[SELECTEDMEASUREFORMATSTRING]] and [[SELECTEDMEASURENAME]].

> **Type:** article
> **Author:** Marco Russo (SQLBI)
> **Published:** 2021-10-21 (updated)
> **URL:** https://www.sqlbi.com/articles/controlling-format-strings-in-calculation-groups/
> **Routed to:** DAX Code

## Summary

Calculation items have two DAX properties: the Expression (value) and the Format String Expression (display format). The article explains how to use Format String Expression to control formatting dynamically — for example, applying a percentage format to a YOY% calculation item regardless of the underlying measure's format. Includes a full currency conversion example where the format string is looked up from a Currency table based on the selected currency, while preserving original formats for ratio and count measures. Key insight: `SELECTEDMEASUREFORMATSTRING()` reads the format after any higher-precedence CG has already modified it — the precedence chain matters for format strings just as it does for values. Two updates note: Power BI custom visuals may not fully support custom format strings (Microsoft announced a fix but it was not resolved by 2021); precedence order for Time Intelligence vs Currency Conversion CGs was corrected in a 2021 update.

## Key Claims

- Format String Expression controls display format independently of the measure's defined format
- `SELECTEDMEASUREFORMATSTRING()` returns the current measure's format, including any format already modified by a higher-precedence CG
- Currency Conversion CG example: format string comes from Currency table, but ratio/count measures (containing "#" or "%") are skipped via `SELECTEDMEASURENAME()`
- Precedence: highest value applies first — both Expression and Format String Expression respect precedence order
- Highest-precedence CG's Format String Expression runs while lower-precedence CG columns are still in filter context — enabling cross-CG context inspection
- Custom visuals in Power BI may not honour Format String Expression (outstanding issue as of 2021)
- Article is part of a 9-article SQLBI Calculation Groups series

## Notable Details

- All 9 URLs are SQLBI article links — skip (direct_file type, sqlbi.com)
- [[Author-Marco-Russo-Alberto-Ferrari]] — Russo solo on this article; Ferrari may be co-author on the series but this specific article is Marco Russo
- [[Format-String-Expression-in-Calculation-Groups]] — atomic concept note
- [[Currency-Conversion-Format-String-Pattern]] — pattern note with full DAX
- Related to [[Controlling-Calculation-Group-Selection]] — separate SQLBI article on the newer selection properties

## Extracted Notes

Links to notes derived from this source:

- [[Format-String-Expression-in-Calculation-Groups]] — `atomic` — concept overview
- [[Currency-Conversion-Format-String-Pattern]] — `pattern` — currency conversion format string pattern with full DAX

## Metadata

| Field | Value |
|-------|-------|
| Source file | Controlling Format Strings in Calculation Groups.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-06 |
| Word count | ~1,200 |
