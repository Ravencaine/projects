---
created: 2026-08-10
updated: 2026-08-10
source: "Excel REPT Function In Cell Charts • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
note_type: pattern
tags: [excel, pattern, visualisation, progress, dashboard, let]
---

# Progress Bar with REPT + LET

Creates a two-section progress bar inside a cell: filled blocks for completed portion, shade blocks for the remainder.

## Purpose

Shows both completion and remaining portions simultaneously. Used for project progress, goal tracking, budget usage, and target achievement. Updates dynamically with formula-driven data.

## Components

- `LET` — names intermediate calculations for readability
- `ROUND` — converts percentage to whole character count (required because REPT truncates)
- `REPT` — repeats filled and remainder characters
- `&` — concatenates filled and remainder sections
- Unicode symbols: `█` (filled) and `▒` (shade/remaining)

## Structure

```excel
=LET(
  width, 20,
  filled, ROUND([@[Completion Rate]] * width, 0),
  REPT("█", filled) & REPT("▒", width - filled)
)
```

`width` sets the total bar length in characters. `filled` converts the percentage to whole characters using ROUND.

## Example

For 90% completion, width = 20:

```excel
filled = ROUND(90% * 20, 0)  →  18
REPT("█", 18) & REPT("▒", 2)  →  "██████████████████▒▒"
```

For 23%, width = 50 (higher precision):

```excel
filled = ROUND(23% * 50, 0)  →  12
REPT("█", 12) & REPT("▒", 38)  →  "████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░"
```

## Precision

| Width | Per-character % |
|-------|-----------------|
| 20 | 5% |
| 50 | 2% |
| 100 | 1% |

Higher width = more precision. Values like 93% and 95% round to the same character count at width=20.

## Variations

- Use pipe `|` (SHIFT+\\) instead of `▒` for narrower remaining indicators
- Replace `▒` with a space `" "` for a gap before the remaining section
- Combine with conditional formatting on the underlying cell for colour coding

## Related

- [[REPT-Function]] — function
- [[In-Cell-Bar-Chart-REPT]] — pattern without remainder section
- [[Star-Rating-REPT]] — pattern using filled/unfilled symbols
