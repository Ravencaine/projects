---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, pattern, Power BI]
---

# Thematic coding of survey comments requires a two-pass approach: extract themes first, then classify

<!-- First-pass: one LLM call over the full corpus extracts a closed set of 12-15 themes. Second-pass: per-comment calls classify each comment against the closed theme list. This prevents unbounded cardinality and inconsistent labels from free tagging. -->

## Claim

First-pass: one LLM call over the full corpus extracts a closed set of 12-15 themes. Second-pass: per-comment calls classify each comment against the closed theme list. This prevents unbounded cardinality and inconsistent labels from free tagging.

## Evidence

- Stated in [[GPT-4-Thematic-Coding]] — Purpose
