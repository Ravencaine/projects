---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, technique, Power BI]
---

# Dash n_clicks can toggle flip card state with no animation logic in Python

<!-- Dash tracks only n_clicks on the card inner container. Odd clicks set className to 'flip-card-inner flipped'; even clicks reset it. The class toggle is the only Dash responsibility; the animation is pure CSS. -->

## Claim

Dash tracks only n_clicks on the card inner container. Odd clicks set className to 'flip-card-inner flipped'; even clicks reset it. The class toggle is the only Dash responsibility; the animation is pure CSS.

## Evidence

- Stated in [[CSS-Flip-Card-Dash]] — Dash (state only)
