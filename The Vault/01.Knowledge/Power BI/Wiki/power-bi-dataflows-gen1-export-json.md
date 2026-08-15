---
created: 2026-08-11
updated: 2026-08-11
source: "Document-Dataflows-Gen1-CoWork-Transcript.md"
note_type: pattern
tags: [power-bi, dataflows-gen1, export]
---

# Dataflows Gen1 Export JSON — Contents

Power BI Service → Dataflow Gen1 → Export JSON produces a file containing the complete metadata of the dataflow.

## Contents

| Section | Details |
|---------|---------|
| Table catalog | Table names, descriptions, query IDs |
| Column metadata | Column names, data types |
| M query code | Power Query expressions for each table |
| Source information | Server, database, schema, source objects |
| Refresh metadata | Last refresh date, load enabled status |
| Output format | Version, structure |

## File Location

After export: Three dots → Export JSON → downloads to local machine.

## Why Export

- Dataflows Gen1 are legacy (no new features being developed) but still in use
- Export JSON = complete record of the dataflow's structure before migration or decommissioning
- The JSON is the input for CoWork documentation skills

## Related

- [[document-dataflows-gen1-cowork-workflow]] — CoWork skill to document the export
