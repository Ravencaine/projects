---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: atomic
tags: [ontology, data-modeling, automation, business-analyst]
---

# 70/30 Ontology Auto-Generation Split

Ontology extraction from Power BI models is approximately 70% automatable via parsing; the remaining 30% requires business analyst input to capture operational rules, governance constraints, and domain-specific definitions that cannot be inferred from the data model alone.

## The Split

### 70% — Auto-Generated from Power BI Model

| Source | Extracted As |
|---|---|
| Table name | Entity name |
| Column names + types | Properties with data types |
| Column descriptions | Property descriptions |
| Primary key columns | Unique constraints |
| Foreign key relationships | Entity relationships (belongs_to, originates_from) |
| Enum / fixed-value columns | Property enumerations (allowed values) |
| DAX measures (CALCULATE patterns) | Business rules (conditions + actions) |
| Column min/max from data | Range constraints |
| Row counts | Cardinality hints |

### 30% — Business Analyst Input Required

| What | Why |
|---|---|
| Operational rules | What CAN the agent DO? (not just what is "high risk") |
| Governance constraints | Approval requirements, role-based access |
| Cross-entity business logic | End-to-end process rules spanning multiple entities |
| Semantic reconciliation | When two dashboards define "Active Customer" differently |
| Domain exceptions | Edge cases not captured in existing formulas |
| Canonical definitions | Establishing a single authoritative definition for conflicting concepts |

## The Pattern

```
Power BI Model
  → 70% auto-extracted by parser (entities, properties, relationships, constraints)
  → Business Analyst reviews + adds the missing 30% (operational rules, governance)
  → Validated Ontology → Fabric IQ / OntoGuard / AI Agent
```

## Measured Quality

- 92% of DAX business rules extracted correctly from measures
- 8% needed manual clarification from the analyst
- The 30% is not a weakness — it is where human expertise lives

## Related

- [[power-bi-informal-ontologies]] — `atomic`
- [[power-bi-formal-ontology-extraction-pipeline]] — `pattern`
- [[dax-measure-to-business-rule-extraction]] — `function`
