---
created: 2026-08-02
updated: 2026-08-02
source: From Power BI Dashboard to AI Agent in 30 Minutes I Built the Tool That Unlocks 20 Million Hidden Ontologies.md
note_type: reference
tags: [cursor, ai, reference, prompts, tool-building, llm-coding]
---

# Cursor AI Prompts for Tool Building

Specific, high-context Cursor AI prompts used to build the PowerBI-Ontology-Extractor in 48 hours. The quality of the generated code was directly driven by prompt specificity and real-world context.

## Prompt 1: PBIX Reader

```
Create a PBIXReader class that:
- Unzips .pbix files (they're ZIP archives)
- Reads model.bim JSON
- Extracts tables, relationships, measures
- Uses context manager for cleanup
- Handles errors gracefully
```

**What it generated**: Core extraction class — ZIP handling, JSON parsing, entity extraction.

## Prompt 2: DAX Parser

```
Create a DAXParser that converts DAX formulas to business rules:
- Parse CALCULATE with filters → business rule
- Extract IF/SWITCH logic → conditional rules
- Identify dependencies (tables/columns used)
- Handle complex nested formulas
```

**What it generated**: DAX → business rule extraction logic with ~92% accuracy on standard patterns.

## Prompt 3: Schema Drift Detection

```
Create schema drift detection that prevents the $4.6M mistake:
- Compare expected vs actual columns
- Detect renames, deletions, additions
- Estimate impact (cost of failure)
- Suggest fixes
- Provide fail-safe mode for agents
```

**What it generated**: The schema drift detection module — the most critical safety component of the tool.

## Prompt Design Principles

| Principle | Example |
|---|---|
| Specific, not vague | "Unzips .pbix files (they're ZIP archives)" not "handle PBIX files" |
| Include the real-world failure | "$4.6M mistake" context drove the safety features |
| State the output format | "business rule" not "parsed formula" |
| Include error handling | "Handles errors gracefully" |
| Describe the user goal | "prevents the $4.6M mistake" not "adds validation" |

## Note on Build Timeline

- 0–8 hours: Core extraction (PBIX reader, model.bim parser, entity extraction)
- 8–16 hours: DAX parsing and business rule extraction
- 16–24 hours: Ontology generation (entity mapping, relationship mapping, constraints)
- 24–32 hours: Schema validation and drift detection
- 32–40 hours: Export formats (Fabric IQ, OntoGuard, OWL)
- 40–48 hours: Testing and documentation

## Related

- [[powerbi-ontology-extractor-workflow]] — `pattern`
- [[schema-drift-detection-pattern]] — `pattern`
