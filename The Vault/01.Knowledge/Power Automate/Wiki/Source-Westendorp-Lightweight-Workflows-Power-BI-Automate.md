---
created: 2026-08-10
updated: 2026-08-10
source: Designing Lightweight Workflows with Power BI and Power Automate
source_url: https://medium.com/@jmwestendorp/designing-lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906
note_type: source
tags: [power-automate, power-bi, sharepoint, dax, evaluate, parse-json, reconciliation, upsert, lightweight]
---

# Source: Westendorp — Designing Lightweight Workflows with Power BI and Power Automate

> **Type:** architecture / pattern / workflow
> **Author:** Jacob Westendorp
> **Published:** 2026-08-04
> **URL:** https://medium.com/@jmwestendorp/designing-lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906
> **Routed to:** Power Automate (5 notes) + DAX Code (1 note)
> **Category:** Power BI, Power Automate, SharePoint Integration, DAX Query, Workflow Architecture

## Summary

Extends the Power BI → Power Automate single-datapoint trigger pattern to full population synchronization with SharePoint. Power BI defines and scopes the active contract population via DAX EVALUATE/SELECTCOLUMNS. Power Automate parses the JSON, loops through records, upserts matching SharePoint items, and flags fallen-out-of-scope records rather than deleting them. SharePoint acts as a lightweight operational write-back surface; Power BI ingests it as a secondary dataset to create a unified semantic model.

## Key Claims / Components

1. **Conceptual model:** each tool has one clear job — Power BI anchors facts, Power Automate reconciles, SharePoint captures operational context
2. **Fixed vs mutable fields:** core contract details (vendor, dates, descriptions) are immutable; status/ownership/flags are mutable and user-managed
3. **Scoped dataset via DAX:** EVALUATE + SELECTCOLUMNS + FILTER constrains to active/lapsed contracts; shapes JSON output for Power Automate
4. **JSON schema discipline:** generate schema from a real sample payload; validate one-to-one match before wiring downstream actions; common pitfalls are nesting and bracketed property names
5. **SharePoint sync orchestration:** Get items → Apply to Each → upsert (update if exists, create if not); idempotent across repeat runs
6. **Dedicated SharePoint view for Get items:** efficiency trade-off; exposes only ContractID or small field subset; governance risk if users can change the view
7. **Flag instead of delete:** fallen-out-of-scope records are marked rather than removed; curated views separate active from inactive; human reviews decide retention
8. **Bring data back into Power BI:** SharePoint ingested as secondary dataset; joined to core model on ContractID; additive, never overwrites source data
9. **AI writing note:** Westendorp's reflection on AI as training wheels and the shift toward more authentic independent writing

## Extracted Notes

- [[Lightweight-Workflows-Power-BI-Automate-Conceptual-Model]] — `pattern` — layered system: Power BI anchors facts, Power Automate reconciles, SharePoint captures mutable context; additive integration; fixed vs mutable field distinction
- [[Scoped-DAX-EVALUATE-SELECTCOLUMNS-Query-Pattern]] — `reference` — EVALUATE + SELECTCOLUMNS + FILTER scoping pattern; design JSON output for Power Automate upstream
- [[Power-Automate-Parse-JSON-Schematization-Discipline]] — `gotcha` — generate schema from sample payload; validate before wiring downstream; common schema pitfalls
- [[SharePoint-List-Sync-Orchestration-Pattern]] — `pattern` — upsert loop: Get items → Apply to Each → update/create; idempotent; dedicated SharePoint view efficiency
- [[Inactive-Record-Flag-Instead-of-Delete]] — `pattern` — flag fallen-out-of-scope records; curated views; human reviews retention decisions
- [[Source-Westendorp-Lightweight-Workflows-Power-BI-Automate]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | Designing Lightweight Workflows with Power BI and Power Automate.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Notes count | 5 (pattern ×3, gotcha ×1, source ×1) |
