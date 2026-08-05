---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: function
tags: [dax, power-bi, business-rule, measure, ontology, extraction]
---

# DAX Measure → Business Rule Extraction

Converting a DAX measure into a formal business rule that AI agents and semantic systems can consume. The extraction maps CALCULATE filter conditions and IF/SWITCH logic to structured rule definitions.

## Extraction Pattern

### Simple CALCULATE Filter → Business Rule

```dax
-- DAX measure in Power BI:
"High Risk Shipments" =
CALCULATE(
    COUNTROWS(Shipments),
    Shipments[Temperature] > 25
        || Shipments[VibrationLevel] > 5
        || Shipments[Status] = "Delayed"
)
```

Extracted as:

```json
{
  "name": "HighRiskShipmentDetection",
  "entity": "Shipment",
  "source": "DAX: High Risk Shipments",
  "condition": "Temperature > 25 OR VibrationLevel > 5 OR Status = 'Delayed'",
  "action": "classify_as_high_risk",
  "triggeredEvents": ["NotifyOperationsTeam", "LogIncident"],
  "priority": "high"
}
```

### IF/SWITCH Logic → Conditional Rules

```dax
"Customer Risk Classification" =
IF(
    Customer[RiskScore] > 80,
    "High Risk",
    IF(Customer[RiskScore] > 50, "Medium Risk", "Low Risk")
)
```

Extracted as:

```json
[
  { "condition": "RiskScore > 80", "action": "classify_as_high_risk" },
  { "condition": "RiskScore > 50", "action": "classify_as_medium_risk" },
  { "condition": "RiskScore <= 50", "action": "classify_as_low_risk" }
]
```

### DISTINCTCOUNT with Filter → At-Risk Entity Detection

```dax
"At-Risk Customers" =
CALCULATE(
    DISTINCTCOUNT(Customer[CustomerID]),
    Customer[RiskScore] > 80
)
```

Extracted as:

```json
{
  "name": "CustomerImpactAssessment",
  "entity": "Customer",
  "source": "DAX: At-Risk Customers",
  "condition": "Customer.RiskScore > 80",
  "action": "flag_customer_at_risk"
}
```

## Extraction Pipeline

1. **Parse DAX measure text** → extract CALCULATE arguments, FILTER conditions, aggregation function
2. **Map column references** → entity + property names from the semantic model
3. **Convert operators** → `>` → greater than, `||` → OR, `&&` → AND
4. **Identify aggregation** → COUNTROWS → row count, SUM → total, DISTINCTCOUNT → distinct entities
5. **Format as business rule JSON** → entity, condition, action, source measure

## Notes

- Extraction handles standard CALCULATE patterns reliably (~92% accuracy)
- Nested formulas and complex context transitions require manual analyst review
- The extracted rule captures what the measure DEFINES (analytical rules); business analysts add what the agent should DO (operational rules)

## Related

- [[ontology-auto-generation-70-30-split]] — `atomic`
- [[power-bi-informal-ontologies]] — `atomic`
- [[power-bi-formal-ontology-extraction-pipeline]] — `pattern`
