---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: pattern
tags: [data-modeling, pattern, ontology, fabric, export, microsoft-fabric]
---

# Ontology → Fabric IQ Export

Exporting a formal ontology (generated from Power BI) to Microsoft Fabric IQ format, ready for direct import into a Fabric workspace as a semantic item.

## Fabric IQ Format

The Fabric IQ JSON export encodes the complete ontology: entities, properties, relationships, business rules, constraints, and data bindings in a structured format that Fabric IQ can consume.

### Export Pattern

```python
from powerbi_ontology.export import FabricIQExporter

exporter = FabricIQExporter(ontology)
fabric_json = exporter.export()

with open("supply_chain_ontology.json", "w") as f:
    json.dump(fabric_json, f, indent=2)
```

### Fabric IQ JSON Structure

```json
{
  "ontologyItem": "SupplyChain_Ontology_v1",
  "version": "1.0.0",
  "source": "Power BI: Supply_Chain_Operations.pbix",
  "extractedDate": "2025-01-31T10:00:00Z",
  "metadata": {
    "extractionTool": "PowerBI-Ontology-Extractor v0.1.0",
    "originalDashboard": "Supply_Chain_Operations.pbix",
    "analyst": "Operations Team"
  },
  "entities": [
    {
      "name": "Shipment",
      "description": "A delivery of goods with environmental monitoring and tracking",
      "sourceTable": "SHIPMENTS",
      "properties": [
        {
          "name": "ShipmentID",
          "type": "GUID",
          "required": true,
          "unique": true,
          "description": "Unique identifier for shipment"
        },
        {
          "name": "Temperature",
          "type": "Decimal",
          "unit": "Celsius",
          "validRange": { "min": -20, "max": 40 },
          "description": "Real-time IoT temperature reading"
        },
        {
          "name": "Status",
          "type": "Enum",
          "values": ["In Transit", "Delivered", "Delayed", "Cancelled"],
          "required": true
        }
      ],
      "relationships": [
        {
          "type": "belongs_to",
          "target": "Customer",
          "foreignKey": "CustomerID",
          "cardinality": "many-to-one"
        },
        {
          "type": "originates_from",
          "target": "Warehouse",
          "foreignKey": "OriginWarehouse",
          "cardinality": "many-to-one"
        }
      ],
      "constraints": [
        {
          "type": "range",
          "property": "Temperature",
          "min": -20,
          "max": 40,
          "errorMessage": "Temperature must be between -20°C and 40°C"
        }
      ]
    }
  ],
  "businessRules": [
    {
      "name": "HighRiskShipmentDetection",
      "source": "DAX: High Risk Shipments",
      "entity": "Shipment",
      "condition": "Temperature > 25 OR VibrationLevel > 5 OR Status = 'Delayed'",
      "action": "classify_as_high_risk",
      "priority": "high",
      "triggeredEvents": ["NotifyOperationsTeam", "LogIncident"]
    }
  ],
  "dataBindings": {
    "Shipment": {
      "source": "OneLake.supply_chain_db.shipments",
      "schema": "dbo",
      "mapping": {
        "ShipmentID": "shipment_id",
        "Temperature": "iot_temperature"
      },
      "refreshPolicy": "real-time"
    }
  }
}
```

## Import into Fabric

1. Open Fabric workspace
2. Create new "Ontology Item"
3. Upload the generated JSON
4. Deploy to OneLake
5. Connect AI agents via semantic contract

## Related

- [[power-bi-formal-ontology-extraction-pipeline]] — `pattern`
- [[ai-agent-semantic-contract]] — `pattern`
- [[schema-drift-detection-pattern]] — `pattern`
