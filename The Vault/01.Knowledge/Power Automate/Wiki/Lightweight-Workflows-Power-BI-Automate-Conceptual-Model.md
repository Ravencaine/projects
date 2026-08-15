---
created: 2026-08-10
updated: 2026-08-10
source: Designing Lightweight Workflows with Power BI and Power Automate
source_url: https://medium.com/@jmwestendorp/designing-lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906
note_type: pattern
tags: [power-automate, power-bi, sharepoint, architecture, system-of-record, boundary]
---

# Power BI + Power Automate + SharePoint: Layered System Architecture

Each tool has a clear, single job. Power BI defines the authoritative population and anchors facts. Power Automate reconciles state between systems. SharePoint captures human/process-driven operational context. No system does more than it is well suited for.

## The Layered Model

```
Power BI        → Source of truth for facts (contracts, dates, amounts)
                  Defines the population. Anchors what exists.

Power Automate  → Reconciliation layer. Keeps SharePoint in sync with Power BI.
                  Reacts to changes. Does not own data.

SharePoint      → Operational surface. User-managed context (status, ownership, notes).
                  Evolves independently of source data.
```

## Core Principle: Additive, Not Overwriting

SharePoint never overwrites source contract data. The integration is intentionally additive. Power BI represents the authoritative state; SharePoint contributes a layer of context that would otherwise be invisible in traditional reporting.

## What Can and Cannot Change

**Fixed (Power BI source of truth):**
- Vendor names, contract dates, descriptions, identifiers
- Anything that defines what a record *is*

**Mutable (SharePoint — user-managed):**
- Status, responsible owner, in-process flags, notes
- Anything that reflects what is *happening* to a record

This distinction allows Power BI to remain reliable and stable while still reflecting operational reality.

## Why This Pattern Works

| Problem it solves | How |
|---|---|
| Power BI treated as read-only | SharePoint acts as write-back surface for operational context |
| Upstream changes required for every status update | Power Automate bridges the gap |
| SharePoint list diverges from Power BI population | Reconciliation loop keeps them in sync |
| Hard deletes lose potentially useful context | Flagging + views preserves history |

## Related

- [[Scoped-DAX-EVALUATE-SELECTCOLUMNS-Query-Pattern]] — how DAX defines and scopes the active population
- [[SharePoint-List-Sync-Orchestration-Pattern]] — the Power Automate loop that syncs SharePoint to the scoped dataset
- [[Inactive-Record-Flag-Instead-of-Delete]] — flagging fallen-out-of-scope records rather than hard deleting
