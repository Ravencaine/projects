---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, technique, Power BI]
---

# Splat operators in Dash callbacks enable a single generic callback to handle any number of cards

<!-- Using *[Output(f'c{i}-inner', 'className') for i in range(1, len(CARDS)+1)] and the same pattern for Input adapts the callback automatically to len(CARDS) without per-card code. -->

## Claim

Using *[Output(f'c{i}-inner', 'className') for i in range(1, len(CARDS)+1)] and the same pattern for Input adapts the callback automatically to len(CARDS) without per-card code.

## Evidence

- Stated in [[Data-Driven-UI-Card-Tuples]] — Structure
