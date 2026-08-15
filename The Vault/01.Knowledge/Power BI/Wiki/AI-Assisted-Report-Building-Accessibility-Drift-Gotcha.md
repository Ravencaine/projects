---
created: 2026-08-09
updated: 2026-08-09
source: "Enhancing Power BI Reports with AI A Focus on Accessibility.md"
note_type: gotcha
tags: [power-bi, ai, accessibility, wcag, gotcha, prompting, drift]
---

# AI-Assisted Report Building — Accessibility Drift Gotcha

> **Type:** gotcha
> **Routed to:** Power BI

## Problem

When building Power BI reports with AI assistance (Copilot, vibe coding, prompting tools), accessibility requirements erode across iterations even when explicitly stated in every prompt.

## Why It Happens

LLMs optimise for the current request. As conversation context grows:
- Earlier instructions lose influence
- New prompts take priority
- Small regressions accumulate (lighter button colours, removed focus indicators, smaller click targets)
- Nothing dramatic in isolation — the drift is incremental

## Evidence

- WCAG-compliant buttons revert to failing contrast ratios
- Focus indicators disappear after redesigns
- Correctly implemented accessibility fixes get undone in later prompts
- Accessibility cannot be a one-time instruction — it must be continuously reinforced

## Mitigation

1. **Embed accessibility into the prompt specification:** not as a one-time note, but as a continuous constraint
2. **Use structured prompting tools:** e.g., [PBIX A11y Accessibility Prompt Builder](https://pbiaudits.com/accessibility-prompt-builder)
3. **Pair prompting with auditing:** prompt shapes intent, audit confirms execution
4. **Native visuals over custom** unless genuinely required — native controls handle accessibility better

## Accessibility Checklist for AI Prompts

- [ ] Colour contrast (WCAG thresholds against chosen background)
- [ ] Meaningful + dynamic alt text for all visuals/slicers
- [ ] Visual density and information hierarchy
- [ ] Clear page/visual/axis titles
- [ ] Readable, scalable font sizes
- [ ] Logical tab order
- [ ] Appropriately sized interactive elements
- [ ] Native Power BI visuals preferred

## See Also

- [[Source-Enhancing-Power-BI-Reports-with-AI]] — source article by Juls / Smart Frames
