---
created: 2026-08-01
updated: 2026-08-02
source: "Unlocking Python Inside Power BI How I Solved the Cumulative Value Challenge (and What I Learned Along the Way).md"
source_url: "https://medium.com/@markchen69/unlocking-python-inside-power-bi-how-i-solved-the-cumulative-value-challenge-and-what-i-learned-25c984e0a940"
note_type: source
tags: [power-bi, power-query, python, pandas, cumsum, formula-firewall, intermediate]
---

# Python in Power Query — Mark Chen

> **Type:** practical guide / intermediate
> **Author:** Mark Chen
> **Published:** 2026-05-21
> **Routed to:** Power Query (primary); Power BI (setup)
> **KB:** Power Query

## Summary

Running Python scripts directly inside Power Query to solve iterative calculations that M language handles poorly at scale. Key example: cumulative revenue by version and enterprise unit using `pandas` `cumsum()`. Four hard-won lessons: (1) Python scripts only work on direct source queries — referenced queries are blocked by Formula Firewall; (2) Python libraries must be installed outside Power BI (pip/conda), and Power BI must point to the same Python installation; (3) pandas data types (`astype()`) do not carry into Power Query after expansion — always add a `Table.TransformColumnTypes` step; (4) `cumsum()` with `groupby()` solves Power Query's O(n²) `List.FirstN()` cumulative sum problem.

## Extracted Notes

- [[pandas-cumsum-vs-list-firstn]] — `atomic` — pandas `cumsum()` O(n) vs M `List.FirstN()` O(n²); `groupby()` resets per group; vectorised vs row-by-row
- [[python-script-in-power-query]] — `atomic` — Transform → Run Python Script; dataset passed as pandas DataFrame; expand output; full M code example
- [[formula-firewall-python-blocked]] — `atomic` — Python scripts only on direct queries; Formula Firewall blocks referenced queries; run on source table instead
- [[python-data-types-power-query]] — `atomic` — pandas `astype()` does not carry into PQ; Table.TransformColumnTypes step required after expanding Python output
- [[python-in-power-bi-setup]] — `atomic` — Install via pip/conda; verify Power BI Python path; restart after install; `python -c "import..."` test

## Metadata

| Field | Value |
|-------|-------|
| Source file | Unlocking Python Inside Power BI How I Solved the Cumulative Value Challenge (and What I Learned Along the Way).md |
| Ingestion date | 2026-08-01 |
| Word count | ~1,400 |
| Level | Intermediate |
| Category | Power Query / Python |
