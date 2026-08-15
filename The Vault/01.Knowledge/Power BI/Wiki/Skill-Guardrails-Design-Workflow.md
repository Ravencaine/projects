---
created: 2026-08-09
updated: 2026-08-09
source: "Document Power BI Dataflows Gen1 with Copilot Cowork (Before You Migrate).md"
note_type: workflow
tags: [power-bi, copilot-cowork, skill, guardrails, design, workflow]
---

# Skill Guardrails Design Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[Source-Document-Dataflows-Gen1-CoWork]]

Design effective guardrails for a CoWork skill. Guardrails prevent hallucinations, out-of-scope behavior, and false success declarations. Write them after core instructions, before testing.

## Step 1 — Identify failure modes

For each skill, ask: what could go wrong?

Common failure modes:
- Making up facts (fabricating data, column names, descriptions)
- Asking for information already provided
- Deviating from the output structure
- Reporting success when the file was not created
- Producing placeholder or sample data instead of real output
- Failing silently instead of reporting the error

## Step 2 — Write a guardrail for each failure mode

Transform each failure mode into a specific imperative guardrail:

| Failure mode | Guardrail |
|-------------|-----------|
| Fabricating facts | "Never fabricate fact. Use only information from the provided input files." |
| Asking for provided info | "Retrieve information from attached files before asking the user." |
| Wrong structure | "Match the reference structure exactly. Do not improvise sections or layouts." |
| False success | "Confirm the output file exists before announcing completion." |
| Silent failure | "Fail honestly — report the error and ask for reattachment rather than generating placeholder data." |
| Placeholder data | "Do not produce a document from placeholder, sample, or fabricated data." |

## Step 3 — Order guardrails by priority

Put the most critical guardrails first. "Never fabricate" and "match reference structure" should appear near the top of the guardrails section.

## Step 4 — Test the guardrails

Run the skill against edge cases:
- Missing input file
- Malformed JSON
- File with no tables
- Reference document with different structure than the input

If the skill passes these tests, the guardrails are strong enough.

## Step 5 — Check the quality report

After running the skill test, review the quality report. Low "surprise handling" scores indicate guardrails need strengthening.

## Guardrail template

```markdown
## Guardrails

- Never fabricate fact. Use only information from the provided input files.
- Retrieve information from attached files before asking the user.
- Ask the user only if the required input files cannot be found.
- Match the reference structure exactly. Do not improvise sections or layouts.
- Do not produce output from placeholder or sample data.
- Fail honestly — report errors rather than generating incomplete output.
- Confirm the output file exists before announcing completion.
```

## Common guardrail mistakes

| Mistake | Fix |
|---------|-----|
| Too vague ("be accurate") | Be specific ("never fabricate column names") |
| No edge case coverage | Test with malformed/missing inputs |
| Contradicts core instructions | Guardrails should reinforce, not contradict |
| Too many guardrails | Focus on the 3–5 most critical failure modes |

## Related

- [[CoWork-Skill-Guardrails]] — the atomic reference
- [[CoWork-Skill-Quality-Report]] — how guardrails affect quality scores
- [[Document-Dataflows-Gen1-with-CoWork-Workflow]] — workflow context
