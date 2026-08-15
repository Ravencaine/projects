---
created: 2026-08-08
updated: 2026-08-08
source: Calculating Geometric Mean in Power BI
source_url: https://www.sqlservercentral.com/articles/calculating-geometric-mean-in-power-bi
author:
  - name: Dinesh Asanka
url: https://www.sqlservercentral.com/
note_type: source
tags: [power-bi, geometric-mean, power-query, mean, statistics]
---

# Geometric Mean in Power BI (SQLServerCentral)

> **Type:** article (SQLServerCentral)
> **Author:** Dinesh Asanka
> **Published:** 2026-07-06
> **URL:** https://www.sqlservercentral.com/articles/calculating-geometric-mean-in-power-bi
> **Routed to:** Power BI

## Summary

No built-in geometric mean function in Power BI. Two-step Power Query approach: (1) multiply all values in a group with `List.Product`, then (2) raise to power `1/n` with `Number.Power`. Works for ranking scenarios where multiple reviewers score the same subjects — geometric mean reduces the influence of extreme outliers compared to arithmetic mean.

## Key Points

- Geometric mean decreases faster than harmonic mean as value spread increases
- Use case: multi-reviewer/multi-judge ranking scenarios
- **Limitation:** breaks with zero or negative values
- Three embedded screenshots in article showing: sample data table, Group By step, custom column step

## Extracted Notes

Links to notes derived from this source:

- [[Geometric-Mean-Formula]] — `atomic` — definition, formula, behaviour across spread values
- [[Geometric-Mean-Power-Query]] — `pattern` — two-step Power Query implementation (List.Product + Number.Power)
- [[Geometric-Mean-Zero-Negative-Limitation]] — `atomic` — zero and negative values break geometric mean
- [[Geometric-Mean-Multi-Reviewer-Rankings]] — `pattern` — use case: judges ranking players

## Metadata

| Field | Value |
|-------|-------|
| Screenshots | 99.System/Attachments/Geometric-Mean-Power-BI/ |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-08 |
| Word count | ~750 |
