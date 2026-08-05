---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: pattern
tags: [power-bi, pattern, pbix, zip, model-bim, semantic-model]
---

# PBIX as ZIP Archive — model.bim Structure

A Power BI `.pbix` file is a ZIP archive containing the complete semantic model and report definition. Understanding this structure is the foundation for programmatic extraction and ontology generation.

## Archive Structure

```
my_report.pbix (ZIP)
├── Report/                    # Report layout (visuals, pages)
│   └── ...
├── DataMashup                 # Mashup query definitions
├── DataModel/
│   └── DataModel (some path)  # Binary AS database
├── SecurityBindings           # RLS / row-level security
└── [Content_Types].xml
```

For Analysis Services Tabular models saved as `.pbix`:
- The semantic model lives inside the DataModel folder as a binary AS database

For datasets connected to external sources:
- The `.pbix` contains `DataMashup` (Power Query definitions) and remote connection metadata

## The model.bim File

When exported as a `.bim` file (from Analysis Services or Power BI Dataset workflows), the model is stored as JSON:

### Key Sections

```json
{
  "model": {
    "tables": [
      {
        "name": "SHIPMENTS",
        "columns": [
          { "name": "ShipmentID", "dataType": "string", "isKey": true },
          { "name": "CustomerID", "dataType": "string" },
          { "name": "Temperature", "dataType": "decimal" },
          { "name": "Status", "dataType": "string" }
        ],
        "measures": [
          {
            "name": "High Risk Shipments",
            "expression": "CALCULATE(COUNTROWS(...), Temp > 25 OR ...)"
          }
        ],
        "partitions": [...]
      }
    ],
    "relationships": [
      {
        "name": "ShipmentsCustomer",
        "fromTable": "SHIPMENTS",
        "fromColumn": "CustomerID",
        "toTable": "CUSTOMERS",
        "toColumn": "CustomerID",
        "crossFilteringBehavior": "bothDirections"
      }
    ]
  }
}
```

## Extraction Workflow

1. **Unzip** the `.pbix` file
2. **Locate** `model.bim` or `DataModel` folder
3. **Parse** the JSON semantic model
4. **Extract** tables, columns, relationships, measures
5. **Transform** into ontology format (entities, properties, relationships, rules)

## Note on .pbix vs .bim

| Format | Contents | Extraction |
|---|---|---|
| `.pbix` | ZIP with report + model | Unzip first |
| `.bim` | Direct JSON semantic model | Parse directly |

Power BI datasets (published to service) store the model as a binary Analysis Services database — not directly readable as JSON. The `.bim` export from SSMS or Tabular Editor provides the JSON equivalent.

## Related

- [[power-bi-formal-ontology-extraction-pipeline]] — `pattern`
- [[dax-measure-to-business-rule-extraction]] — `function`
- [[powerbi-ontology-extractor-workflow]] — `pattern`
