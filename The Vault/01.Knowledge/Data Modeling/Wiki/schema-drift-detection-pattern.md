---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: pattern
tags: [data-modeling, pattern, schema-drift, ai-agent, validation, ontoguard]
---

# Schema Drift Detection

Automatically detecting when the actual database schema diverges from the ontology's expected schema — preventing AI agents from making decisions based on stale column mappings.

## The Problem

AI agents bound to an ontology rely on property-to-column mappings to read and write data. When a data engineer renames a column in the source database, the ontology's binding becomes stale:

```
Ontology binding expects: warehouse_location
Actual database column:  facility_id
Agent query result:      NULL
Agent decision:          Invalid warehouse → routing failure
Cost:                    $4.6M recovery operation
```

## Detection Workflow

```python
from powerbi_ontology import SchemaMapper

mapper = SchemaMapper(ontology, data_source="azure_sql")
binding = mapper.create_binding("Warehouse", "dbo.warehouses")
binding.property_mappings = {
    "WarehouseID": "warehouse_id",
    "Location": "warehouse_location",   # ← expected column
    "Status": "status",
    "CapacityUtilization": "capacity_pct"
}

# Get actual schema from the live database
actual_schema = {
    "tables": {
        "warehouses": {
            "columns": [
                "warehouse_id",
                "facility_id",           # ← renamed!
                "status",
                "capacity_pct"
            ]
        }
    }
}

# Validate
result = mapper.validate_binding(binding, actual_schema)

if not result.is_valid:
    drift = mapper.detect_drift(binding, actual_schema)
    print(f"Missing: {drift.missing_columns}")
    print(f"New: {drift.new_columns}")
    print(f"Impact: ${drift.estimated_impact}")
```

## Drift Categories

| Drift Type | Description | Detection Method |
|---|---|---|
| Missing column | Expected column not found | Direct comparison |
| New column | Unexpected column in source | Schema scan |
| Type change | Data type mismatch | Type comparison |
| Renamed column | Semantic match found | Column name similarity + type match |
| Constraint change | NOT NULL / PK change | Constraint metadata |

## Fail-Safe Mode

When drift is detected:
1. **Agent execution is blocked:** no queries execute against stale bindings
2. **Drift report generated:** missing/new columns, estimated cost impact
3. **Fix suggestions provided:** `mapper.update_binding("Warehouse", "Location", "facility_id")`
4. **Approval workflow triggered:** data team verifies the fix before re-activation

## Output Structure

```json
{
  "entityName": "Warehouse",
  "severity": "CRITICAL",
  "missingColumns": ["warehouse_location"],
  "newColumns": ["facility_id"],
  "estimatedImpact": 4600000,
  "failureMode": "Agent received NULL values, routed shipments to invalid warehouses",
  "suggestedFixes": [
    {
      "description": "Update semantic binding to map Location → facility_id",
      "command": "mapper.update_binding('Warehouse', 'Location', 'facility_id')"
    }
  ]
}
```

## Notes

- Tested against column renames, drops, and additions — caught 100% of drift events in evaluation
- Prevents the exact failure mode described in the $4.6M logistics incident
- Forms the "semantic firewall" layer in the OntoGuard integration

## Related

- [[schema-drift-column-rename-loss]] — `gotcha`
- [[ontology-fabric-iq-export]] — `pattern`
- [[ai-agent-semantic-contract]] — `pattern`
