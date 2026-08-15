---
created: 2026-08-10
updated: 2026-08-10
source: Designing Lightweight Workflows with Power BI and Power Automate
source_url: https://medium.com/@jmwestendorp/designing-lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906
note_type: pattern
tags: [power-automate, sharepoint, get-items, upsert, reconciliation, loop, apply-to-each]
---

# SharePoint List Sync: Power Automate Orchestration Pattern

Once the Power BI dataset is parsed and validated, Power Automate synchronizes it with a SharePoint list using an upsert loop: for each contract, check if a matching item exists, update it if yes, create it if no.

## The Core Loop

```
Power BI action (scoped dataset)
    ↓
Parse JSON (validate schema)
    ↓
Get items (SharePoint — return existing items)
    ↓
Apply to each (contract in parsed dataset)
    ↓
    Check: does SharePoint item with this ContractID exist?
        → YES: Update existing SharePoint item (preserve user context)
        → NO:  Create new SharePoint item
    ↓
Flag fallen-out-of-scope items (see [[Inactive-Record-Flag-Instead-of-Delete]])
```

## Efficiency: Dedicated SharePoint View

When the SharePoint list is large or has many columns, create a dedicated view that exposes only the key column (ContractID) or a small subset of required fields. Pass that view into the "Get items" action.

**Trade-off:** A specific SharePoint view can be changed by end users, which could break the flow if governance is loose. In practice, the performance gain outweighs the risk.

## Idempotent: Repeat Runs Are Safe

The flow handles repeat runs safely:
- Running again will not create duplicate items
- User updates to SharePoint fields are preserved (only mapped Power BI fields are updated)
- The flow only reconciles — it does not undo human work

## Field Mapping Rule

Only fields sourced from Power BI are overwritten. User-managed fields (notes, status, ownership) in SharePoint are preserved across updates. This is what makes the SharePoint layer additive rather than destructive.

## Prerequisites

- ContractID as a stable identifier that exists in both Power BI and SharePoint
- SharePoint list already created with matching column names
- DAX query scoped to active population (see [[Scoped-DAX-EVALUATE-SELECTCOLUMNS-Query-Pattern]])
- JSON schema validated (see [[Power-Automate-Parse-JSON-Schematization-Discipline]])

## Related

- [[Lightweight-Workflows-Power-BI-Automate-Conceptual-Model]] — layered architecture this pattern implements
- [[Scoped-DAX-EVALUATE-SELECTCOLUMNS-Query-Pattern]] — upstream: how DAX defines the dataset
- [[Inactive-Record-Flag-Instead-of-Delete]] — downstream: what to do with items that fall out of scope
