---
created: 2026-07-27
updated: 2026-08-02
source: "Why I Stopped Writing 'Best Practice' DAX Posts (And What I Write Instead)"
source_url: "https://medium.com/write-your-world/why-i-stopped-writing-best-practice-dax-posts-and-what-i-write-instead-8e0ee0c8a6ae"
note_type: source
tags: [dax, documentation, pattern-philosophy, dax-writing]
---

# Why I Stopped Writing "Best Practice" DAX Posts

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-06-30
> **URL:** https://medium.com/write-your-world/why-i-stopped-writing-best-practice-dax-posts-and-what-i-write-instead-8e0ee0c8a6ae
> **Routed to:** DAX Code

## Summary

The author shifted from publishing generic "best practice" DAX advice to documenting specific patterns, their trade-offs, and the conditions under which each applies. The article is a meta-document about DAX documentation philosophy — arguing that pattern documentation should be conditional, not prescriptive.

## Key Claims

- "Best practice" without context is misleading — the same pattern that is best in one scenario is worst in another
- DAX pattern documentation should include: the scenario, the trade-offs, the performance characteristics, and the failure modes
- The author now writes "Pattern + Condition" documentation instead of "Best Practice" posts
- Example: SAMEPERIODLASTYEAR is "best practice" for time intelligence ONLY when the date table is continuous; otherwise it is wrong

## Notable Details

- Documentation anti-pattern: "always use VAR" — true in complex measures, false in simple ones where it adds noise
- Documentation anti-pattern: "never nest CALCULATEs" — sometimes necessary when different CALCULATEs serve different purposes
- The author now uses a template: "Pattern Name — Scenario — Trade-offs — When to Use — When NOT to Use"

## Extracted Notes

- [[dax-documentation-philosophy]] — atomic — Pattern + Condition documentation approach

## Metadata

| Field | Value |
|-------|-------|
| Source file | Why I Stopped Writing "Best Practice" DAX Posts (And What I Write Instead).md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~3,438 |
