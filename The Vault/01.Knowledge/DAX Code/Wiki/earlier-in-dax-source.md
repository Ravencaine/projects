---
created: 2026-07-27
updated: 2026-08-02
source: "Understanding EARLIER in DAX: The Time Machine You Didn't Know You Had"
source_url: "https://medium.com/write-your-world/understanding-earlier-in-dax-the-time-machine-you-didnt-know-you-had-c9ab56c4d8b5"
note_type: source
tags: [dax, earlier, earliest, row-context, nested-context, running-totals]
---

# Understanding EARLIER in DAX: The Time Machine You Didn't Know You Had

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-10-15
> **URL:** https://medium.com/write-your-world/understanding-earlier-in-dax-the-time-machine-you-didnt-know-you-had-c9ab56c4d8b5
> **Routed to:** DAX Code

## Summary

EARLIER() accesses the value of a column from the OUTER row context within nested row iteration contexts — essential for running totals, cumulative sums, and calculations where you need to reference the "previous" row's value. EARLIEST() goes back two or more levels of nesting.

## Key Claims

- EARLIER is needed when a CALCULATE() inside an iterator creates a new row context on top of the existing one
- Running totals, cumulative sums, and "show running total per category" all require EARLIER
- Error "EARLIER/EARLIEST refers to an earlier row context which doesn't exist" occurs when EARLIER is used outside any iterator
- Modern DAX: measure branching + CALCULATE() can replace many EARLIER use cases
- VAR cannot replace EARLIER in all scenarios because VAR captures result, not current row context position

## Notable Details

- EARLIER() defaults to level 1 (immediate outer context); EARLIER(Column, 2) goes back 2 levels
- EARLIEST() always refers to the outermost (level 0) row context
- EARLIER is a table iterator function — it only works inside SUMX, AVERAGEX, FILTER, etc.

## Extracted Notes

- [[earlier-function]] — function
- [[earlier-vs-earliest-gotcha]] — gotcha

## Metadata

| Field | Value |
|-------|-------|
| Source file | Understanding EARLIER in DAX The Time Machine You Didn't Know You Had.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~940 |
