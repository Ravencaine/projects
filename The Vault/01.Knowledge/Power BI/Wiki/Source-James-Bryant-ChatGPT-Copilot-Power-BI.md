---
created: 2026-08-10
updated: 2026-08-10
source: ChatGPT + Copilot for Power BI
source_url: https://medium.com/@Jamesabryant/
author: James Bryant
published: 2026-05-12 / 2026-05-19
note_type: source
tags: [power-bi, ai, chatgpt, copilot, workflow, dashboard-design, dax, prompt-engineering]
---

# Source: Bryant — ChatGPT + Copilot for Power BI

> **Type:** opinion / methodology
> **Author:** James Bryant
> **Published:** 2026-05-12 ("ChatGPT Thinks. Copilot Builds. Power BI Proves.") and 2026-05-19 ("The Two-Layer Workflow That Actually Works")
> **URL:** https://medium.com/@Jamesabryant/
> **Routed to:** Power BI (workflows), DAX Code (pattern)
> **Category:** Power BI, AI Workflows, Prompt Engineering, Dashboard Design, DAX

## Summary

Two articles presenting the same core argument: ChatGPT and Copilot play different roles in Power BI development and should not be used interchangeably. Layer 1 = ChatGPT for upstream design (defining purpose, KPIs, decision logic, alerting thresholds). Layer 2 = Copilot for in-platform execution (drafting DAX, building visuals, Q&A). A sports performance dashboard (athlete speed/strength/endurance) is used as the working example to demonstrate the workflow. Key DAX example: Endurance Improvement via FIRSTDATE/LASTDATE with percentage change. Key design principle: every KPI card hides something — pair it with context (trend line, comparison, target, detail view).

## Key Claims / Components

1. **Two-layer AI workflow:** Layer 1 = ChatGPT before Power BI (thinking/design layer); Layer 2 = Copilot inside Power BI (building/execution layer)
2. **ChatGPT is strongest as planning partner:** helps frame the dashboard, identify leading vs lagging indicators, challenge each KPI's assumptions, define alerting thresholds
3. **Copilot is acceleration, not direction:** can draft DAX, suggest visuals, build Q&A — but cannot rescue a weak model or invent framing
4. **Five-step loop:** (1) ChatGPT define purpose, (2) ChatGPT challenge design, (3) Copilot build first version, (4) Power BI validate model, (5) ChatGPT refine story
5. **M&A as the sharpest use case:** acquisition dashboards show the gap between reporting and decision support; signals scattered across sentiment, regulatory, timeline
6. **KPI cards hide distribution:** "Average Speed: 8.30 m/s" hides consistency, trend, and outliers; always pair with context
7. **Endurance Improvement DAX:** FIRSTDATE + LASTDATE + AVERAGE + DIVIDE — percentage improvement from first to last record
8. **ChatGPT review prompt for DAX:** "Explain this formula. What assumptions does it make? How could it produce misleading results?"
9. **Copilot review checklist:** right fields, correct aggregation, filter behavior, DAX logic, performance at scale
10. **The shift:** dashboards from static reports → intelligent decision systems; analysts from button-clickers → question framers

## DAX Pattern Extracted

`Endurance Improvement (%)` — `CALCULATE(AVERAGE(...), FIRSTDATE(...))` / `CALCULATE(AVERAGE(...), LASTDATE(...))` with `DIVIDE` for percentage. Blind spots: per-entity vs all-records, lifetime vs filter period, blank values.

## Value: Power BI KB

New author (James Bryant). Two-layer AI workflow, KPI context principle, and M&A decision-support framing are all new. No existing coverage in the Power BI KB.

## Extracted Notes

- [[Two-Layer-AI-Workflow-ChatGPT-Copilot-Power-BI]] — `workflow` — Layer 1 ChatGPT for design before Power BI; Layer 2 Copilot for in-platform execution; five-step loop
- [[KPI-Card-Context-Principle]] — `atomic` — every KPI hides distribution/trend/outliers; always pair with context (trend line, comparison, target, detail view)
- [[Endurance-Improvement-FIRSTDATE-LASTDATE-Pattern]] — `pattern` — FIRSTDATE + LASTDATE + AVERAGE + DIVIDE for first-to-last percentage improvement; blind spots for per-entity and blank values
- [[Source-James-Bryant-ChatGPT-Copilot-Power-BI]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | ChatGPT + Copilot for Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Notes count | 3 (workflow ×1, atomic ×1, pattern ×1) |
