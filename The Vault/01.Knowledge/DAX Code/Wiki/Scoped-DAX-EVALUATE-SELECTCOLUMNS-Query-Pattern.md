---
created: 2026-08-10
updated: 2026-08-10
source: Designing Lightweight Workflows with Power BI and Power Automate
source_url: https://medium.com/@jmwestendorp/designing-lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906
note_type: pattern
tags: [dax, evaluate, selectcolumns, filter, power-automate, query, scoping, json, active-contracts]
---

# Scoped Dataset Pattern: EVALUATE + SELECTCOLUMNS + FILTER

Before any Power Automate logic runs, the contract population is constrained using a DAX `EVALUATE` + `SELECTCOLUMNS` + `FILTER` statement. This does two things: defines what qualifies as in scope, and shapes the output so the resulting JSON is predictable for Power Automate.

## The Pattern

```dax
EVALUATE
SELECTCOLUMNS (
    FILTER (
        'Contracts',
        'Contracts'[Active Canceled] IN { "Active", "Lapsed" }
    ),
    "ContractID",       'Contracts'[ContractID],
    "ContractUniqueID", 'Contracts'[ContractUniqueID],
    "Contract Status",  'Contracts'[Active Canceled],
    "Contract Start",   'Contracts'[ContractStart],
    "Contract End",     'Contracts'[ContractEnd]
)
```

## How Each Function Contributes

| Function | Role |
|----------|------|
| `FILTER` | Defines the active population — returns only rows where status is Active or Lapsed |
| `SELECTCOLUMNS` | Shapes the output — projects only the fields needed downstream; renames them for Power Automate readability |
| `EVALUATE` | Returns the result as a table for Power BI / Power Automate consumption |

## Why Scope Aggressively

Working with the full historical contract table means:
- More SharePoint list items to manage
- Longer, less predictable flow runtimes
- Users interacting with stale records they don't care about

Scoping to active/lapsed contracts keeps the SharePoint list focused, runtime predictable, and the user mental model clean.

## Design for Automation Upstream

`SELECTCOLUMNS` projects only the fields required downstream. This allows the JSON output to be structured with Power Automate in mind — flat, predictable objects — not just whatever shape the source table happens to have.

## Testing the Query

Use DAX query view in Power BI Desktop to validate the EVALUATE statement for completeness and efficiency before passing it into the Power Automate action. Once finalized, the same query goes directly into the Power BI action in the flow.

## Related

- [[Lightweight-Workflows-Power-BI-Automate-Conceptual-Model]] — how this query fits the layered system architecture
- [[Power-Automate-Parse-JSON-Schematization-Discipline]] — why parsing the JSON output matters
- [[Date-Table-Must-Be-Marked-Requirement]] — date table prerequisite for time intelligence functions (separate concern but related model hygiene)
