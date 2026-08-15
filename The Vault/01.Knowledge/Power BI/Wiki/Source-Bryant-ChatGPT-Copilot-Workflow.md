---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Workflow for Building Better Power BI Dashboards with ChatGPT and Copilot
source_url: https://medium.com/microsoft-power-bi/a-practical-workflow-for-building-better-power-bi-dashboards-with-chatgpt-and-copilot-ad9f2f65a0cd
note_type: source
tags: [powerbi, ai, chatgpt, copilot, dashboard-design, workflow]
---

# Source: Bryant — ChatGPT Copilot Workflow

> **Type:** article
> **Author:** James Bryant
> **Published:** 2026-04-28
> **URL:** https://medium.com/microsoft-power-bi/a-practical-workflow-for-building-better-power-bi-dashboards-with-chatgpt-and-copilot-ad9f2f65a0cd
> **Routed to:** Power BI
> **AI tool used:** ChatGPT, Copilot

## Summary

Divides AI tool responsibilities in a Power BI dashboard project: ChatGPT for reasoning and prototyping before/during data prep; Copilot for execution and iteration inside Power BI. Includes SaaS metrics and rideshare data-cleanup case studies. Core principle — AI accelerates execution; it does not fix weak thinking.

## Key Claims

1. Most dashboards fail before Power BI opens — weak thinking (fuzzy business question, messy data, too many KPIs) not wrong chart choices
2. ChatGPT and Copilot have distinct zones of strength and should not be treated as interchangeable
3. ChatGPT: reasoning, prototyping, clarifying question, structuring data cleanup, drafting DAX for review
4. Copilot: execution inside Power BI — generate visuals, refine DAX, apply PQ transforms, adjust layout
5. Three-phase workflow: ChatGPT (clarify + prepare) → Copilot (build inside PBI) → ChatGPT (review + interpret) → Copilot (refine)
6. The back-and-forth between tools is the real workflow — not asking one tool to do everything
7. ChatGPT can structure messy data cleanup: remove duplicates, impute missing values, correct anomalies, standardize formats
8. A dashboard can look good while the story underneath is wrong — if data prep is skipped
9. After building, use ChatGPT as an external reviewer: "What is this dashboard saying clearly, what is still confusing, and what question would an executive ask next?"
10. The future of dashboard work: better thinking before the build, cleaner execution during, clearer interpretation after — not just faster creation

## Case Studies

### SaaS Metrics
Business question: should the business spend more on acquisition or retention?
ChatGPT prompt: monthly ARR, new customer count, churned customer count — analyze trends, identify churn spikes, compare acquisition vs retention ROI, recommend strategy, flag risk factors.
ChatGPT response: Month 6 churn spike (~8%), acquisition recovered in months 9–12, recommendation to prioritize retention + onboarding + cohort monitoring.
Copilot inside PBI: line chart of monthly ARR, annotations for churn months, bar overlay of churn vs acquisition, supporting ARR growth measure.

### Rideshare Data Cleanup
Dataset: 247 duplicate rides, 18% missing driver ratings, $0 or >$500 fares, mixed date formats.
ChatGPT tasks: remove duplicates, fill blanks using mean/mode imputation, correct anomalies using historical averages, standardize timestamps.
This is not a visualization problem — it is a data-preparation problem that must be solved before building.

## Notable Details

- Book referenced: *Smart Dashboards with Power BI, ChatGPT and Copilot* (Amazon)
- Article level: Intermediate; Category: AI; Tags: Tutorial, AI
- First sentence: "Most dashboard articles start too late. They start with the chart."
- Key quote: "Copilot helps you get to a usable page faster. ChatGPT helps you think more clearly about what the page means."

## Extracted Notes

- [[ChatGPT-Copilot-Dashboard-Build-Workflow]] — `workflow` — three-phase workflow; pre-build ChatGPT, in-PBI Copilot, post-build review
- [[ChatGPT-Equals-Reasoning-Copilot-Equals-Execution]] — `atomic` — tool division; when to use each; table of situations

## Metadata

| Field | Value |
|-------|-------|
| Source file | A Practical Workflow for Building Better Power BI Dashboards with ChatGPT and Copilot.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~175 |
