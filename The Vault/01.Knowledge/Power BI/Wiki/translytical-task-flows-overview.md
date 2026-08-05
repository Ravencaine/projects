---
created: 2026-08-01
updated: 2026-08-02
source: "Translytical Task Flows Just Hit GA. They Quietly Change What a Power BI Report Actually Is.md"
note_type: atomic
tags: [power-bi, fabric, translytical, task-flows, UDF, python, write-back, GA, advanced]
---

# Translytical Task Flows: What Actually Shipped

GA at FabCon 2026 (March 2026). Report buttons trigger Python UDFs that read filter context and write back to Fabric. This is bigger than "Power BI now has write-back."

## Verified GA Facts

| Fact | Detail |
|------|--------|
| **Trigger** | Power BI report button → Fabric User Data Function (UDF) |
| **UDF runtime** | Python 3.11.9, public PyPI supported |
| **Parameters** | UDFs read filter context from report as parameters |
| **Write targets** | Fabric SQL databases, Fabric Warehouses, Fabric Lakehouse files |
| **External calls** | External APIs, Teams, Azure OpenAI, workflow systems |
| **Return type** | Must return string to wire to report button |
| **Identity** | Microsoft Entra ID inherited from user — no separate service principal |

## Why It's Bigger Than Write-Back

Traditional write-back has always existed (Power Apps, Power Automate, third-party tools). Three things make Translytical Task Flows architecturally different:

**1. First-party inside Fabric governance**
Write-back through Power Apps/Automate crosses into Power Platform — separate licensing, governance, deployment, and learning curve. Task Flows stay inside Fabric: same workspace, same permissions, same deployment story.

**2. Action surface area is wider than traditional write-back**
The button doesn't have to write to a database — it can call external APIs, post to Teams, generate Azure OpenAI completions, trigger workflows. "Write-back" is the simple case, not the ceiling.

**3. Software development pattern**
UDFs are Python code: code editor, version control, parameters, return types, error handling, testing. Different from configuring Power Apps forms or Power Automate flows. Puts write-back in the hands of code-comfortable teams; forces software engineering practices into a reporting tool.

## Strategic Shift

"Translytical" = transactional + analytical in one environment.

Until now: analyze in one tool, act in another.
With Task Flows: action layer folds back into analytics layer.

Power BI is no longer just a reporting tool — it's becoming an **action layer**.

## Supported Scenarios (from Microsoft GA docs)

| Scenario | Description |
|----------|-------------|
| **Add data** | Insert new records into Fabric tables from inside the report |
| **Edit data** | Update existing records (status, annotations, discount values) |
| **Delete data** | Remove records that shouldn't appear |
| **Call external APIs** | Trigger downstream actions in other systems |

## Related

- [[translytical-use-cases]] — 6 specific workflow categories with implementation patterns
- [[translytical-architecture]] — architectural decisions before deploying
- [[translytical-tradeoffs]] — honest tradeoffs marketing leaves out
