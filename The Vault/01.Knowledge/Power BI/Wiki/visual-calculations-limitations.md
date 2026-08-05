---
created: 2026-08-01
updated: 2026-08-02
source: "Visual Calculations Just Went GA. They'll Save You Hours — and Quietly Fragment Your Model If You Let Them.md"
note_type: atomic
tags: [power-bi, visual-calculations, limitations, exports, governance]
---

# Visual Calculations — Limitations That Bite

## Core Limitation: No Reuse

- Cannot copy to another visual
- Cannot reference from another visual
- Cannot promote to the model
- Same running sum on 5 visuals → write it 5 times → copies drift independently

**This is the heart of the governance problem.**

## Exports Exclude Them

Data exports do **not** include visual calculation results.

```
User sees:  $1,234,567 running total in matrix
User exports to Excel → running total column NOT in file
```

Users see a number and it vanishes when they export. Support ticket follows. (Underlying-data exports show hidden fields, but the calculation results themselves don't export.)

## They Don't Travel

| Feature | Visual Calc Support |
|---------|---------------------|
| Pin to dashboard | ❌ No |
| Publish to web | ❌ Limited |
| Embedded scenarios | ❌ Limited / no IntelliSense |
| Copilot / AI grounding | ❌ Copilot reasons over the model; visual calcs aren't there |

## Visual Coverage Gaps

Not available in:
- Slicers (expected)
- Key influencers
- Decomposition trees
- Small multiples
- Q&A
- **Custom visuals** (notable)

## Model Features Don't Reach Them

- No dynamic format strings
- No drill-through to records
- No "show items with no data"
- No personalization
- `RELATED()`, `USERELATIONSHIP()` not available (on visual matrix, not model graph)

## Why These Are Architecture, Not Bugs

All limitations follow from the design: calculation lives on a visual → anything that happens away from that visual (exports, dashboards, other visuals, AI) doesn't know it exists.
