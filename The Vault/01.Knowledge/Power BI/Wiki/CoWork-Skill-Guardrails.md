---
created: 2026-08-09
updated: 2026-08-09
source: "Document Power BI Dataflows Gen1 with Copilot Cowork (Before You Migrate).md"
note_type: atomic
tags: [power-bi, copilot-cowork, skill, guardrails, reliability, atomic]
---

# CoWork Skill Guardrails

**Type:** Atomic · **KB:** Power BI · **Source:** [[Source-Document-Dataflows-Gen1-CoWork]]

Guardrails in a CoWork skill define what the skill must NOT do. They are the boundary conditions that prevent hallucinations, off-target output, and false success declarations.

## What guardrails prevent

| Guardrail type | Prevents |
|---------------|---------|
| Never fabricate facts | Making up column names, table descriptions, data types |
| Retrieve before asking | Asking for information the user already attached |
| Confirm file exists before announcing completion | Reporting success when the output was not created |
| Fail honestly | Reporting a failure instead of generating placeholder data |
| Match reference structure exactly | Deviating from the expected output format |

## Example guardrails from the Dataflow Documentation skill

```
match the reference structure exactly
never fabricate fact
retrieve before asking — locate and pass the JSON yourself
ask the user only if no dataflow JSON can be found
fail honestly if the JSON cannot be read — say so and ask for reattach
do not produce a document from placeholder or sample data
confirm the file exists in output before announcing completion
```

## Guardrails and quality score

Guardrails contribute to the "surprise handling" criterion in the quality report. Skills with explicit guardrails score higher because they handle edge cases predictably rather than hallucinating or asking unnecessary questions.

## Where to put guardrails

In the skill.md file, under a `## Guardrails` or `### Guardrails` section. Place after core instructions. Keep each guardrail as a single imperative statement.

## Related

- [[Skill-Guardrails-Design-Workflow]] — how to design effective guardrails
- [[CoWork-Skill-Quality-Report]] — how guardrails affect the quality score
- [[CoWork-vs-Copilot-Agent]] — why built-in guardrails beat manual correction
