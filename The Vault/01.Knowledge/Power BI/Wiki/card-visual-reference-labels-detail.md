---
created: 2026-08-02
source: Next-Level Dashboard Design With Power BI's New Card Visual With Reference Labels
note_type: pattern
tags: [powerbi, pattern, card-visual, reference-labels, detail, conditional-formatting]
---

# Card Visual: Reference Labels with Detail Sub-Values

Reference labels display a title string below each callout value. The `Detail` sub-tab on a reference label lets you attach a second DAX measure whose result renders beside the title.

**Example use case:** `Vacancy Rate LY` (title) + `Vacancy Rate Variation` (Detail) → shows `Vacancy Rate LY   2%`

**Conditional formatting on Detail:** apply `fx` conditional color to the Detail measure itself (DAX-level IF returning hex strings), not to the reference label's color field. The card's color `fx` does not propagate into the Detail sub-value — the measure must carry the color.

**Blank detail cleanup:** when a reference label has no Detail, it shows `—`. Fix: assign `UNICHAR(8209)` (zero-width space) via a dedicated "Blank values" measure in the detail's `fx` field.
