---
created: 2026-08-09
updated: 2026-08-09
source: "Document Power BI Dataflows Gen1 with Copilot Cowork (Before You Migrate).md"
note_type: workflow
tags: [power-bi, dataflows-gen1, documentation, copilot-cowork, export-json, skill, workflow]
---

# Document Dataflows Gen1 with CoWork Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[Source-Document-Dataflows-Gen1-CoWork]]

Use Microsoft Copilot CoWork to generate reusable technical documentation for Power BI Dataflows Gen1 before migrating to Gen2 or another platform.

## When to use

Before migrating Dataflows Gen1 (legacy). Want structured, repeatable documentation for any dataflow.

## Step 1 — Export export.json

In Power BI Service:
1. Navigate to your Dataflow Gen1 workspace
2. Click the three dots next to the dataflow
3. Select **Export JSON**
4. Download the file

The export.json contains everything CoWork needs: table catalog, column names, data types, Power Query M code, source/target table relationships, primary keys, foreign keys, refresh information.

## Step 2 — Create a reference Word template

1. Open a new Word document
2. Define the exact structure you want for each table:
   - Table name and description
   - Source system (server, database, schema)
   - Source objects
   - Granularity
   - Primary key / foreign key
   - Business purpose
   - Special transformation logic
   - Usage notes
   - Technical structure (column list with data types)
3. This template becomes the reference for CoWork

## Step 3 — Generate initial documentation with Copilot

1. Open Word document
2. Use Copilot: "Please generate a full documentation of all tables in the dataflow based on the attached export.json"
3. Attach export.json
4. Request: for each table — table name, source names, granularity, business description; tabular section with all columns, data types, descriptions
5. Review output; correct formatting (column widths, alignment)
6. Save this as your reference template

## Step 4 — Create the CoWork Skill

1. Open Microsoft Copilot → CoWork
2. Customize → Skills → Add → Create new
3. Select **Document template** (not generic writing)
4. Attach: export.json (sample input) + reference Word document (desired output)
5. Instruction: "Transform the information in the JSON file always into a Word document that matches exactly the structure in the attached document"
6. Let CoWork draft the skill — it queues if you send more inputs while thinking
7. Review the generated skill.md file

## Step 5 — Quality check

CoWork generates a quality report (0–100 score):
- Publish bar: 70 (skills below 70 should not be published)
- Risk: medium/low/high
- Criteria: timing, lanes, surprise handling
- This workflow's skill scored 96/100

## Step 6 — Test the skill

1. Run the skill against the same export.json
2. CoWork validates the output against the reference structure
3. If validation fails: iterate on the skill instructions
4. If validation passes: skill is ready for production use

## Step 7 — Store and reuse

Skills are stored in OneDrive → Documents → CoWork folder → Skills.
Maximum 50 skills per tenant.

## Cost

CoWork is pay-as-you-go. Skill creation cost ~341 credits (~$0.03 USD). Running the skill costs <1 credit. One-time creation cost amortized over all future dataflows.

## Key files in export.json

| Section | Contents |
|---------|----------|
| Table catalog | Table name, classification, description, load enabled |
| Query definitions | Source objects, server, database, schema |
| Column definitions | Column names, data types |
| M code | Power Query transformations |
| Refresh metadata | Last refresh date |
| Relationships | Primary key, foreign key |

## Related

- [[CoWork-Skill-from-Input-Output-Samples]] — generalizable principle
- [[CoWork-Skill-Guardrails]] — what to include in skill guardrails
- [[Skill-Guardrails-Design-Workflow]] — designing effective guardrails
