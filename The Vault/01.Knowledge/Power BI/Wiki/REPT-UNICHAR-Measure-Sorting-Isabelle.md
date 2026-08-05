---
created: 2026-08-05
updated: 2026-08-05
source: Analyzing Survey Comments in Power BI Using AI (Isabelle Bittar)
note_type: reference
tags: [power-bi, svg, measure-sort, unichar, custom-sort, conditional-formatting]
---

# REPT/UNICHAR Measure Sorting — Isabelle Bittar (Medium)

Isabelle Bittar's Medium article explaining the `REPT(UNICHAR(8203))` zero-width space technique for sorting non-numeric text categories in Power BI by an underlying numeric measure.

> **URL:** https://medium.com/microsoft-power-bi/power-bi-elevating-data-visualization-with-custom-measure-sorting-b368fd382917
> **Author:** Isabelle Bittar
> **Published:** 2025
> **Referenced from:** [[Analyzing-Survey-Comments-AI-Power-BI-Isabelle-Bittar-source]]

## Summary

Covers the full technique: using `REPT(UNICHAR(8203), n)` to prepend zero-width space characters to text labels, enabling Power BI's alphabetical sort to produce a custom numeric order. Includes worked examples and the logic behind choosing UNICHAR(8203) specifically.

## Related

- [[SWITCH-REPT-UNICHAR-Custom-Sorting]] — `atomic` — DAX implementation of the same technique
- [[Survey-Sentiment-Scorecard]] — real-world usage of the pattern
