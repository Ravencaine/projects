---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, technique, Power BI]
---

# CSS 3D transforms can implement flip card interactions without JavaScript

<!-- The flip card interaction is driven entirely by CSS: rotateY(180deg) on .flip-card-inner toggled via class name; backface-visibility: hidden prevents mirror-image artefacts. Dash only toggles the class name, handling zero animation logic. -->

## Claim

The flip card interaction is driven entirely by CSS: rotateY(180deg) on .flip-card-inner toggled via class name; backface-visibility: hidden prevents mirror-image artefacts. Dash only toggles the class name, handling zero animation logic.

## Evidence

- Stated in [[CSS-Flip-Card-Dash]] — CSS (3D stage)
