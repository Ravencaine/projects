---
created: 2026-08-01
updated: 2026-08-02
source: "Translytical Task Flows Just Hit GA. They Quietly Change What a Power BI Report Actually Is.md"
note_type: atomic
tags: [power-bi, fabric, Direct-Lake, Data-Agents, MCP, OneLake, AI, strategy, advanced]
---

# Fabric AI Integration: The Broader Story

Translytical Task Flows didn't ship in isolation. They went GA at FabCon 2026 alongside a suite of interlocked capabilities. Understanding the broader direction changes how you plan.

## What Else Shipped at FabCon 2026

| Capability | Status |
|-----------|--------|
| **Direct Lake on OneLake** | GA |
| **Fabric Data Agents** | GA |
| **Fabric Local MCP** | GA |
| **Fabric Remote MCP** | Public Preview |
| **OneLake security model unification** | Shipped |
| **Database Hub in Fabric** | Shipped |
| **Translytical Task Flows** | GA |

## The Integrated Story

Microsoft is deliberately building an interlocking fabric:

```
OneLake (unified storage)
    │
    ├── Direct Lake on OneLake      → analytical layer is dramatically faster
    │                                 (GA at FabCon)
    │
    ├── Translytical Task Flows      → analytical layer is actionable
    │                                 (GA at FabCon)
    │
    ├── Fabric Data Agents           → analytical layer is conversational
    │                                 (GA at FabCon)
    │
    ├── Fabric Local/Remote MCP      → analytical layer is programmable
    │                                 from AI tools (GA + Preview)
    │
    └── OneLake security             → all of the above governable
                                        through a single model
```

## Why This Compounds

The architectural decisions made for Translytical Task Flows also serve the other capabilities:

**Identity:** Same Entra ID inheritance that secures translytical operations secures Fabric Data Agent interactions.

**Data store:** Same Fabric SQL database that stores translytical write-back data is queryable by Data Agents.

**UDF pattern:** Same user-data-function pattern that powers translytical write-back enables AI agents to take actions on your data.

Organizations adopting one will likely want the others within 12–18 months.

## Planning Implication

The decisions made for Translytical Task Flows — where data lives, how identity flows, how governance is structured — compound into the broader Fabric AI estate.

**Start with the decisions, not the features.**

Ask: what data store, identity model, and governance structure do we want to serve all Fabric AI capabilities?

Then evaluate which features to activate first based on current team readiness.

## Tejwani's Four Pieces of Advice

1. **Start with the highest-friction read-then-act workflow**: don't try to build translytical for every report
2. **Get audit logging design right before shipping**: build from day one
3. **Treat UDFs as software, not report features**: code review, version control, testing, error handling
4. **Plan capacity sizing for transactional workload patterns**: OLTP ≠ OLAP capacity assumptions

## Related

- [[translytical-task-flows-overview]] — the feature in context
- [[translytical-architecture]] — decisions that compound
- [[translytical-vs-alternatives]] — fit assessment within the broader Fabric story
