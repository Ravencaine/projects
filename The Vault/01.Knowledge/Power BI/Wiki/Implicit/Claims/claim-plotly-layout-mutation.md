---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, gotcha, Power BI]
---

# Plotly update_layout() mutates input dicts in place

<!-- Plotly's `fig.update_layout(**layout)` mutates the Python dict passed to it, rather than defensively copying. Reusing the same dict across multiple figures compounds changes silently, causing layout drift in later renders. -->

## Claim

Plotly's `fig.update_layout(**layout)` mutates the Python dict passed to it, rather than defensively copying. Reusing the same dict across multiple figures compounds changes silently, causing layout drift in later renders.

## Evidence

- Stated in [[plotly-layout-mutation-gotcha]] — Why It Happens
