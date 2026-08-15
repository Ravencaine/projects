---
created: 2026-08-10
updated: 2026-08-10
source: Designing Lightweight Workflows with Power BI and Power Automate
source_url: https://medium.com/@jmwestendorp/designing-lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906
note_type: gotcha
tags: [power-automate, power-bi, json, parse-json, schema, validation, gotcha]
---

# Parse JSON Schema: Validate Before Wiring Up Downstream Actions

When Power Automate receives a dataset from Power BI, the raw JSON array is technically usable but cumbersome and fragile. The `Parse JSON` step converts it to structured objects — but schema errors are a common source of silent failures in Power Automate flows.

## The Discipline

1. **Shape the dataset correctly in DAX first** — `SELECTCOLUMNS` projects only the fields needed, creating flat, predictable objects
2. **Generate schema from a representative sample** — run the Power BI action once, capture the returned array, use the Parse JSON "Generate from sample" option
3. **Validate the parsed output before moving on** — scan the generated schema and confirm it matches the SELECTCOLUMNS output one-to-one

## Common Schema Problems

- Power Automate introduces additional nesting that wasn't in the raw JSON
- Bracketed property names (`[ContractID]` vs `ContractID`) can appear in the schema
- Nested arrays vs flat records — mismatches cause downstream Apply to Each loops to fail silently
- The schema can drift if the DAX query changes and you re-run the sample

## The Debugging Shift

Moving from DAX/M/measures to JSON schema precision is nontrivial. Even with a well-shaped dataset, Power Automate expects structure to be explicit. This shift in mindset — from implicit to explicit — is where most struggles happen.

## Why Generate from Sample Beats Hand-Authoring

Hand-authoring a JSON schema is error-prone. Generating from a real sample payload:
- Captures the actual data types returned
- Validates that the DAX query output is what you expect
- Is faster and more reliable than guessing schema syntax

## Rule

> Let DAX define the rows and columns. Let Power Automate infer the schema from a representative sample. Confirm the parsed output exposes exactly the fields you expect before wiring up any downstream actions.

## Related

- [[Scoped-DAX-EVALUATE-SELECTCOLUMNS-Query-Pattern]] — upstream: DAX shapes the dataset before it reaches Power Automate
- [[SharePoint-List-Sync-Orchestration-Pattern]] — downstream: the Apply to Each loop that uses the parsed fields
