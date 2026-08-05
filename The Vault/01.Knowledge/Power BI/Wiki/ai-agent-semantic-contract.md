---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: pattern
tags: [power-bi, pattern, ai-agent, semantic-contract, governance, rbac]
---

# AI Agent Semantic Contract

A semantic contract defines what an AI agent is permitted to read, write, and execute against an ontology — serving as a governance layer that prevents unauthorized or destructive actions by autonomous agents operating on business data.

## Purpose

Without a semantic contract, an AI agent querying a business ontology can:
- Read any entity and property
- Write or modify any field
- Execute any action (e.g., reroute shipments, approve refunds, close accounts)

A semantic contract restricts all three dimensions based on the agent's assigned role and the business rules encoded in the ontology.

## Contract Structure

```python
contract = builder.build_contract(
    agent_name="SupplyChainMonitor",
    permissions={
        "read": ["Shipment", "Customer", "Warehouse", "IoTSensor"],
        "write": ["Shipment.Status", "Alert"],
        "execute": ["RerouteShipment", "NotifyCustomer", "EscalateToManager"],
        "role": "Operations_Manager"
    }
)
```

## Permission Dimensions

| Dimension | Scope | Example |
|---|---|---|
| `read` | Entity types the agent can query | Shipment, Customer |
| `write` | Specific properties the agent can modify | Shipment.Status, Alert |
| `execute` | Actions the agent can trigger | RerouteShipment, NotifyCustomer |
| `role` | Required authorization role | Operations_Manager |

## Generated Contract Metadata

```json
{
  "agentName": "SupplyChainMonitor",
  "ontologyVersion": "SupplyChain_v1.0",
  "permissions": {
    "readEntities": ["Shipment", "Customer", "Warehouse", "IoTSensor"],
    "writeProperties": ["Shipment.Status", "Alert"],
    "executableActions": ["RerouteShipment", "NotifyCustomer", "EscalateToManager"],
    "requiredRole": "Operations_Manager"
  },
  "businessRulesEnforced": 7,
  "validationConstraints": 15
}
```

## Enforcement Points

1. **Read enforcement**: Agent query is validated against `read` entity list before execution
2. **Write enforcement**: Property updates checked against `write` property list
3. **Action execution**: `execute` list checked before triggering business actions
4. **Role verification**: Agent identity confirmed against `requiredRole`
5. **Business rule validation**: All writes and actions validated against ontology business rules

## Operational Rules in the Contract

The contract enforces rules the business analyst added:

```json
{
  "name": "RerouteApprovalRequired",
  "condition": "RiskScore > 80 AND Status = 'In Transit'",
  "requiredApproval": "Operations_Manager",
  "validation": {
    "preconditions": [
      "Destination.Status = 'Active'",
      "Destination.CapacityUtilization < 90%"
    ]
  },
  "triggeredEvents": ["NotifyCustomer", "LogAudit", "UpdateETA"]
}
```

## Notes

- Semantic contracts are generated from the ontology after the business analyst completes the 30% review
- They represent the OPERATIONAL layer — what the agent can actually do — as opposed to the ANALYTICAL layer (what the data means)
- Contracts should be versioned alongside the ontology

## Related

- [[power-bi-formal-ontology-extraction-pipeline]] — `pattern`
- [[ontology-auto-generation-70-30-split]] — `atomic`
- [[schema-drift-detection-pattern]] — `pattern`
