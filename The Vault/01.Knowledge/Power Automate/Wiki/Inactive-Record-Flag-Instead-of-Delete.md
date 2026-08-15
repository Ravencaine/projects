---
created: 2026-08-10
updated: 2026-08-10
source: Designing Lightweight Workflows with Power BI and Power Automate
source_url: https://medium.com/@jmwestendorp/designing-lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906
note_type: pattern
tags: [power-automate, sharepoint, reconciliation, flag, retention, archival, inactive-records]
---

# Flag Fallen-Out-of-Scope Records Instead of Deleting Them

When the Power BI dataset is scoped to active contracts, some SharePoint items will eventually represent records that have dropped out of scope. The reconciliation logic flags those records rather than deleting them, introducing a deliberate pause before any data is discarded.

## Why Flag, Not Delete

Records that fall out of the active scope may still carry value:
- **Historical follow-up** — a contract may have lapsed but follow-up actions are still needed
- **Audit trail** — deleted records are gone; flagged records can still be reviewed
- **Downstream dependencies** — other processes or teams may still reference the record
- **Intentional separation** — teams need a clean active working set, not a polluted list, but they also need access to historical state

## The Pattern

```
Fallen-out-of-scope ContractID detected in reconciliation loop
    ↓
Flag the SharePoint item (set Inactive = true, or add a status tag)
    ↓
Surface via curated SharePoint view (filtered to show only active records by default)
    ↓
Human reviews flagged records and decides: archive, re-activate, or delete
```

Curated SharePoint views separate inactive/obsolete contracts from the active working set without immediately discarding information.

## Why This Matters for Reporting

The SharePoint list feeds back into Power BI as a secondary dataset joined on ContractID. A clean, flag-based approach means:
- Active reports show only active context
- Inactive records are accessible but not cluttering daily use
- Decisions about long-term retention stay with the team, not the automation

## Rule

> Keep the interaction surface focused and current. Leave decisions about archival or deletion exactly where they belong — with the humans who understand the business context.

## Related

- [[SharePoint-List-Sync-Orchestration-Pattern]] — the reconciliation loop that detects fallen-out-of-scope items
- [[Lightweight-Workflows-Power-BI-Automate-Conceptual-Model]] — the additive integration model that makes this flagging pattern safe
