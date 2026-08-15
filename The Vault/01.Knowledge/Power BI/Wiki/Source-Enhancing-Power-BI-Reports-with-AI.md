---
created: 2026-08-09
updated: 2026-08-09
source: "Enhancing Power BI Reports with AI A Focus on Accessibility.md"
source_url: https://smart-frames.co.uk/2026/07/01/before-ai-builds-your-power-bi-report-tell-it-this/
note_type: source
tags: [power-bi, ai, accessibility, wcag, prompting, vibe-coding, pbiaudits, juls]
---

# Enhancing Power BI Reports with AI: A Focus on Accessibility (Juls / Smart Frames)

> **Type:** article
> **Author:** Juls (smart-frames.co.uk)
> **Published:** 2026-07-01
> **URL:** https://smart-frames.co.uk/2026/07/01/before-ai-builds-your-power-bi-report-tell-it-this/
> **Routed to:** Power BI

## Summary

AI-assisted report building (vibe coding, Copilot) needs accessibility as a continuous constraint, not a one-time instruction. AI drifts from WCAG criteria across iterations because context window prioritises recent prompts. Solution: embed accessibility criteria into the initial prompt specification; use the Accessibility Prompt Builder tool (pbiaudits.com) to generate structured prompts; pair prompting with post-build auditing.

## Key Claims

### Accessibility Drift Problem
- Repeated accessibility prompts still produce drift: contrast failures, light text, small interactive elements, removed focus indicators
- Cause: LLM optimises for current request; older constraints fade as context window fills
- Drift accumulates incrementally across many small iterations — nothing dramatic in isolation

### Core Prompting Criteria
When prompting AI to generate/modify dashboards, include:
- Colour contrast (WCAG thresholds against chosen background)
- Meaningful + dynamic alt text for visuals and slicers
- Visual density and information hierarchy
- Clear page/visual/axis titles
- Readable, scalable font sizes
- Logical tab order for keyboard navigation
- Appropriately sized interactive elements
- Preference for native Power BI visuals unless custom genuinely required

### Tool
- [PBIX A11y Accessibility Prompt Builder](https://pbiaudits.com/accessibility-prompt-builder) — free tool; inputs: canvas size, layout, contrast, font size, tab order, element sizing → generates ready-to-use accessibility prompt

### Prompting ≠ Proof
- Embedding accessibility in the prompt reduces issues at creation
- Auditing is still required as verification layer
- Both needed: prompt shapes intent, audit confirms execution

## Metadata

| Field | Value |
|-------|-------|
| Source file | Enhancing Power BI Reports with AI A Focus on Accessibility.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
