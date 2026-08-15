---
created: 2026-08-10
updated: 2026-08-10
source: Build a Smart Approval System with Prediction Model in Power Automate
source_url: https://medium.com/@tamilarasu-arunachalam/smart-approval-system-with-prediction-model-in-power-automate-e6ec7995d50b
note_type: source
tags: [power-automate, ai-builder, dataverse, approval, prediction, machine-learning]
---

# Source: Arunachalam — AI Builder Prediction Approval System

> **Type:** prototype walkthrough
> **Author:** Tamilarasu Arunachalam
> **Published:** 2026-06-15
> **URL:** https://medium.com/@tamilarasu-arunachalam/smart-approval-system-with-prediction-model-in-power-automate-e6ec7995d50b
> **Routed to:** Power Automate
> **Category:** Power Automate, AI Builder, Dataverse, Approval Automation, Machine Learning

## Summary

Prototype that replaces traditional manual approval with AI-driven conditional routing. When a new `ApprovalRequests` Dataverse record is created, an AI Builder prediction model scores the likelihood of approval. Three thresholds drive routing: >0.7 → auto-approved; 0.4–0.7 → manager approval; <0.4 → senior manager escalation. Uses Dataverse as both data store and trigger source.

## Key Claims / Components

1. **Dataverse table:** `ApprovalRequests` — fields: Amount, Department, Priority, Request Type, AI Decision
2. **AI Builder prediction model:** trained on historical approval outcomes; uses Amount, Department, Priority, Request Type as features
3. **Power Automate flow:** Dataverse trigger → AI Builder Predict → Condition branches (3 thresholds)
4. **Confidence thresholds:** 0.7 (auto-approve), 0.4–0.7 (manager), <0.4 (escalate)
5. **Limitations:** prototype only; no error handling, logging, or notification steps shown; requires AI Builder license

## Limitations

- No error handling or retry logic in the flow
- No email/Teams notifications documented
- No monitoring or logging after routing
- Requires AI Builder (Premium) license
- Dataverse required — not available on standard Power Automate plans

## Value: Power Automate KB

Core contribution: the confidence-threshold routing pattern using AI Builder + Dataverse. No existing notes cover AI Builder prediction in Power Automate flows.

## Extracted Notes

- [[AI-Builder-Prediction-Approval-Routing]] — `workflow` — AI Builder Predict + Dataverse trigger + 3-threshold confidence routing (auto-approve / manager / escalate)
- [[Source-Arunachalam-AI-Builder-Approval]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | Build a Smart Approval System with Prediction Model in Power Automate.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~51 |
