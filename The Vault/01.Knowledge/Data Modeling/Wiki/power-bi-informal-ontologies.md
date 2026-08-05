---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: atomic
tags: [power-bi, ontology, data-modeling, semantic-model, ai-agents]
---

# Power BI Models as Informal Ontologies

Power BI semantic models contain rich domain knowledge — tables, relationships, hierarchies, DAX measures, business rules — that collectively form an informal ontology of the business domain. They are not labeled as such, but the semantic structure is present and machine-readable.

## Definition

An ontology is a formal specification of the concepts, properties, relationships, and constraints in a domain. A Power BI `.pbix` file encodes all of these:

| Ontology Component | Power BI Equivalent |
|---|---|
| Entities / Classes | Tables (fact + dimensions) |
| Properties / Attributes | Columns |
| Relationships | Model relationships (1:1, many-to-one) |
| Business Logic | DAX measures |
| Constraints | Column types, PK/FK relationships |
| Hierarchies | Explicit hierarchies in the model |

## Key Claims

- Microsoft has ~20 million Power BI semantic models deployed globally
- Each model encodes a domain expert's understanding of their business in table/column/measure form
- These are "informal ontologies" — the knowledge is there but not in a machine-consumable format
- Formalizing them (extracting into ontology formats like OWL, JSON-LD, or Fabric IQ) unlocks the trapped semantic intelligence
- The extraction is 70% automatable; the remaining 30% requires business analyst review

## Implications

- Power BI is the world's largest deployed knowledge base of informal business ontologies
- Extracting and formalizing these models enables AI agents to understand business semantics before querying data
- Organizations already have the semantic layer — they just need the tool to extract it

## Related

- [[power-bi-formal-ontology-extraction-pipeline]] — `pattern`
- [[ontology-auto-generation-70-30-split]] — `atomic`
- [[schema-drift-column-rename-loss]] — `gotcha`
- [[dax-measure-to-business-rule-extraction]] — `function`
