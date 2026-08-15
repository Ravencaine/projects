---
created: 2026-08-02
updated: 2026-08-02
source: Power BI: Elevating Data Visualization with Custom Measure Sorting
note_type: snippet
tags: [dax, snippet, unichar, unicode, sorting, space, rept]
---

# REPT(UNICHAR(8203), N) — Invisible Zero-Width Space Prefix

Prepends N zero-width space (ZWSP) characters to a string. Invisible in rendered visuals but treated as characters by Power BI's sort engine.

```
UNICHAR(8203)  →            (zero-width space, U+200B)
REPT(UNICHAR(8203), N)  →   repeated N times
```

**Applications:**
- Custom sort order in SWITCH branches (see `custom-measure-sort-unichar-rept.md`)
- Blank value cleanup (captured separately as `blank-values-unichar-8209.md`)

**Contrast:**
- `UNICHAR(8209)` (non-breaking hyphen) — prevents orphan words, not for sorting
- `UNICHAR(8203)` (ZWSP) — counted as a space by sort; use for ordering
