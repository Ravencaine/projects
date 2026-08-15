---
created: 2026-08-11
updated: 2026-08-11
source: "Document-Dataflows-Gen1-CoWork-Transcript.md"
note_type: workflow
tags: [power-bi, dataflows-gen1, documentation, cowork]
---

# Document Dataflows Gen1 with CoWork

Use Microsoft CoWork (Microsoft 365 Copilot) to create a reusable skill that transforms Dataflows Gen1 JSON exports into Word documentation automatically.

## Steps

### 1. Export JSON from Power BI Service

1. Go to Power BI Service → Dataflow Gen1
2. Click the three dots → **Export JSON**
3. JSON contains: table names, column names, data types, M query code, source/target tables, refresh metadata

### 2. Create a Documentation Template in Word

1. Open Word → create a template with sections: TOC, overview, source system, table catalog, column tables, refresh info
2. Open the Word doc with Copilot → attach the exported JSON → prompt: *"Generate a full documentation of all tables. For each table: section with source table name, granularity, business description, primary key, foreign key, business purpose, usage notes, technical structure (column names, data types), and refresh info."*
3. Copilot drafts the documentation — review and correct formatting

### 3. Create a CoWork Skill

1. Go to CoWork → Customize → Skills → Add
2. Attach the exported JSON (input) + the Word doc (template output)
3. Prompt: *"The skill should transform the information in the JSON export into a Word document matching exactly the structure in the attached reference document."*
4. CoWork drafts the Skill.md and a quality report (scored out of 100, publish bar at 70)
5. Review guardrails: never fabricate facts, retrieve JSON before asking, confirm file exists before announcing completion
6. Publish the skill

### 4. Reuse

Run the skill on any new Dataflows Gen1 JSON export → CoWork generates documentation automatically matching the reference structure.

## Guardrails to Set in the Skill

```
- Match the reference structure exactly. No other structure.
- Never fabricate facts.
- Retrieve the JSON before asking.
- Ask the user only if no JSON can be found.
- Fail honestly if JSON cannot be read — do not produce a document from placeholder or sample data.
- Confirm the file exists in output before announcing completion.
```

## Cost

CoWork uses credits (pay-as-you-go). ~341 credits ≈ $0.03 USD per skill run. Reusable across all future exports.

## Skills Location

OneDrive → Documents → CoWork → skills → [skill-name]

## Related

- [[power-bi-dataflows-gen1-export-json]] — what the JSON export contains
