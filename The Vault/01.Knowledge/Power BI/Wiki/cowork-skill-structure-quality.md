---
created: 2026-08-11
updated: 2026-08-11
source: "Document-Dataflows-Gen1-CoWork-Transcript.md"
note_type: pattern
tags: [power-bi, cowork, documentation, skill]
---

# CoWork Skill — Structure and Quality

Microsoft CoWork (part of Microsoft 365 Copilot) lets you create reusable skills from input/output examples.

## Skill Components

A CoWork skill consists of:

- **Name + description:** what the skill does
- **Instructions:** core logic, step-by-step process
- **Guardrails:** constraints that prevent bad output (never fabricate, always retrieve before asking, confirm file exists)
- **Reference files:** sample input + expected output used as templates
- **Quality report:** CoWork scores the skill 0-100; publish bar is 70

## Quality Scoring

| Score | Meaning |
|-------|---------|
| 96/100 | Excellent — ready to publish |
| 70+ | Publishable |
| <70 | Revise before publishing |

Quality dimensions: does it know what to do, does it stay in its lane, does it handle surprises safely, does it crown (complete successfully)?

## Guardrails Pattern

For documentation skills:
```
- Match the reference structure exactly. No other structure.
- Never fabricate facts.
- Retrieve the JSON before asking.
- Ask the user only if no JSON can be found.
- Fail honestly — do not produce from placeholder data.
- Confirm the file exists in output before announcing completion.
```

## Related

- [[document-dataflows-gen1-cowork-workflow]] — practical application of CoWork skill pattern
