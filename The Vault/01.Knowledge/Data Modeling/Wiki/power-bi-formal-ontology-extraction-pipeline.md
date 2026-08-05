---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: pattern
tags: [power-bi, data-modeling, ontology, extraction, pipeline]
---

# Power BI → Formal Ontology Extraction Pipeline

A four-step pipeline that converts a Power BI `.pbix` semantic model into a formal ontology ready for AI agent consumption, Fabric IQ import, or OntoGuard validation.

## Pipeline Overview

```
.pbix file
  └─ Step 1: Extract semantic model
        └─ Step 2: Generate ontology (70% auto)
              └─ Step 3: Business analyst review (30%)
                    └─ Step 4: Export to target format
```

## Step 1: Extract from Power BI

A `.pbix` file is a ZIP archive. The key artifact inside is `model.bim` — a JSON file containing the complete semantic model.

### Extracted Components

| PBIX Component | Ontology Equivalent |
|---|---|
| Tables (fact + dimension) | Entities |
| Columns | Properties (with data types) |
| Relationships | Semantic links (with cardinality) |
| Hierarchies | Property hierarchies |
| DAX measures | Business rules (analytical) |
| Row-level security | Access control constraints |

### Python Pattern

```python
from powerbi_ontology import PowerBIExtractor

extractor = PowerBIExtractor("Supply_Chain_Operations.pbix")
semantic_model = extractor.extract()

print(f"Tables: {len(semantic_model.entities)}")
print(f"Relationships: {len(semantic_model.relationships)}")
print(f"DAX Measures: {len(semantic_model.measures)}")
```

## Step 2: Generate the Ontology (70% Auto)

The generator maps each semantic model component to its ontology equivalent.

### Auto-Generated Elements

- **Entities**: one per table, with source reference
- **Properties**: one per column, typed (GUID, String, Decimal, Enum)
- **Relationships**: foreign key → semantic link (belongs_to, originates_from)
- **Constraints**: data type ranges, enum values, uniqueness, referential integrity
- **Business Rules**: CALCULATE/IF/SWITCH DAX patterns → structured rules

### Python Pattern

```python
from powerbi_ontology import OntologyGenerator

generator = OntologyGenerator(semantic_model)
ontology = generator.generate()

print(f"Entities: {len(ontology.entities)}")
print(f"Properties: {sum(len(e.properties) for e in ontology.entities)}")
print(f"Business Rules: {len(ontology.business_rules)}")
print(f"Constraints: {sum(len(e.constraints) for e in ontology.entities)}")
```

## Step 3: Business Analyst Review (30%)

The analyst reviews auto-generated elements and adds the missing operational and governance rules.

### What the Analyst Adds

- Approval requirements (which actions need human sign-off)
- Role-based access constraints
- Cross-entity operational rules
- Semantic reconciliation when definitions conflict

### Python Pattern

```python
ontology.add_business_rule({
    "name": "RerouteApprovalRequired",
    "entity": "Shipment",
    "condition": "RiskScore > 80 AND Status = 'In Transit'",
    "requiredApproval": "Operations_Manager",
    "allowedActions": ["RerouteShipment"],
    "triggeredEvents": ["NotifyCustomer", "LogAudit", "UpdateETA"]
})
```

## Step 4: Export

```python
from powerbi_ontology.export import FabricIQExporter

exporter = FabricIQExporter(ontology)
fabric_json = exporter.export()

with open("supply_chain_ontology.json", "w") as f:
    json.dump(fabric_json, f, indent=2)
```

## Related

- [[power-bi-informal-ontologies]] — `atomic`
- [[ontology-auto-generation-70-30-split]] — `atomic`
- [[dax-measure-to-business-rule-extraction]] — `function`
- [[ontology-fabric-iq-export]] — `pattern`
- [[schema-drift-detection-pattern]] — `pattern`
- [[multi-dashboard-semantic-debt-analysis]] — `pattern`
