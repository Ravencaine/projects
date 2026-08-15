---
created: 2026-08-11
updated: 2026-08-11
source: "Document-Dataflows-Gen1-CoWork-Transcript.md"
note_type: source
tags: [power-bi, dataflows, cowork, documentation, video]
---

# Document Dataflows Gen1 — CoWork — Source

CoWork presenter demonstrates exporting Dataflows Gen1 JSON from Power BI Service and creating a CoWork skill that transforms the export into Word documentation automatically.

> **Type:** video
> **Author:** CoWork (video presenter)
> **Published:** 2025
> **URL:** https://www.youtube.com/watch?v=MfENXZxHoN4
> **Routed to:** Power BI

## Summary

Dataflows Gen1 are legacy but still usable. Export the full JSON from Power BI Service (table catalog, column metadata, M code, source info). Create a reference Word document with the desired documentation structure. Build a CoWork skill that maps JSON → Word using the reference as a template. Guardrails ensure accuracy: never fabricate, retrieve before asking, confirm output file exists. Skill quality scored 96/100, cost ~$0.03 per run. Reusable across all future Dataflows exports.

## Key Claims

- Dataflows Gen1 = legacy but not deprecated yet — no new features, still functional
- Export JSON contains everything needed for full documentation
- Specific, precise documentation → CoWork outperforms generic Copilot (less back-and-forth)
- Skills are reusable: create once, run on any future export
- Test skills on multiple different JSON exports to validate robustness

## Extracted Notes

- [[document-dataflows-gen1-cowork-workflow]] — workflow — full step-by-step
- [[power-bi-dataflows-gen1-export-json]] — pattern — what the JSON export contains
- [[cowork-skill-structure-quality]] — pattern — skill components, guardrails, quality scoring

## Metadata

| Field | Value |
|-------|-------|
| Source file | Document-Dataflows-Gen1-CoWork-Transcript.md |
| Ingestion date | 2026-08-11 |
| Duration | 20:38 |
| Attachments | [[Attachments/Video/Document-Dataflows-Gen1-CoWork.mp4]] |
