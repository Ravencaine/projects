---
created: 2026-08-09
updated: 2026-08-09
source: "Document Power BI Dataflows Gen1 with Copilot Cowork (Before You Migrate).md"
note_type: pattern
tags: [power-bi, copilot-cowork, skill, documentation, pattern, input-output, reference, reusable]
---

# CoWork Skill from Input-Output Samples Pattern

**Type:** Pattern · **KB:** Power BI · **Source:** [[Source-Document-Dataflows-Gen1-CoWork]]

Create a reusable CoWork skill by providing: (1) a sample input file and (2) a reference output file with the desired structure. CoWork learns the transformation pattern and applies it to any future input.

## The principle

> Give CoWork a sample of what you put in, and a sample of what you want to come out. It learns the transformation and applies it to new inputs.

This is not prompting — it is **sample-driven skill creation**. The skill encodes the relationship between your specific input format and your specific output format.

## Template

1. **Sample input file:** represents the raw data to be transformed (e.g., export.json from Dataflow Gen1)
2. **Reference output file:** shows the exact structure, formatting, and content expected (e.g., a Word document with a specific table layout)
3. **Transform instruction:** one sentence: "Transform the information in [input file] into a document that matches exactly the structure in [reference file]"

## Why this works better than prompting alone

| Prompting alone | Input-output sample pattern |
|-----------------|---------------------------|
| Generic output | Exact structure match |
| Back-and-forth corrections needed | Validates against reference automatically |
| No memory of desired format | Skill remembers format forever |
| Different output each time | Consistent output every time |

## Generalization: any documentation project

This pattern applies to any structured documentation task where you have:
- A known input format (JSON, CSV, export file)
- A known output format (Word doc, PDF, markdown)

CoWork extracts the mapping between input fields and output structure from the samples.

## Example: this workflow

- **Input:** `adventureworks-dataflow-export.json` (table catalog, columns, M code, metadata)
- **Output:** Word document with table-of-contents, overview, source system section, table catalog per table (name, description, granularity, primary key, business purpose, technical structure)
- **Instruction:** "Transform the JSON into a Word matching the reference structure exactly"
- **Result:** 96/100 quality score; passed all validation checks

## CoWork quality report

CoWork generates a quality report scoring the skill on:
1. Timing — operates at the right pace
2. Lanes — stays within its scope
3. Surprise handling — manages unexpected inputs safely
4. Crownling / convergence — completes reliably

Publish bar: 70/100. Skills below 70 should not be published.

## Related

- [[Document-Dataflows-Gen1-with-CoWork-Workflow]] — full workflow using this pattern
- [[CoWork-Skill-Guardrails]] — what guardrails to include
- [[CoWork-vs-Copilot-Agent]] — why CoWork with this pattern beats Copilot Agent
