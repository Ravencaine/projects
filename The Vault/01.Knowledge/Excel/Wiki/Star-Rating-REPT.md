---
created: 2026-08-10
updated: 2026-08-10
source: "Excel REPT Function In Cell Charts • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
note_type: pattern
tags: [excel, pattern, visualisation, rating, stars]
---

# Star Rating with REPT

Creates a filled/unfilled star rating inside a cell from a numeric score.

## Purpose

Display ratings (product reviews, performance scores, service quality) as visual stars without chart objects. Updates automatically with data changes.

## Components

- `REPT` — repeats filled and unfilled stars
- `ROUNDDOWN` — rounds the score to whole number for star count
- Unicode stars: `★` (filled) and `☆` (unfilled)

## Structure

```excel
=REPT("★", [@Score]) & REPT("☆", 5 - ROUNDDOWN([@Score], 0))
```

For a score of 4: 4 filled stars + 1 unfilled star.

## Generating Stars with UNICHAR

Can also generate stars dynamically:

```excel
=REPT(UNICHAR(9733), [@Score]) & REPT(UNICHAR(9734), 5 - ROUNDDOWN([@Score], 0))
```

- UNICHAR(9733) = ★ (filled star)
- UNICHAR(9734) = ☆ (unfilled star)

## Half Stars

**Not reliably supported.** Excel cannot shade half of a character. Options:

1. Round to nearest whole star (simplest, most portable)
2. Round down — show 4 stars for 4.5
3. Round up — show 5 stars for 4.5

Whole stars are recommended for consistency across Excel versions and fonts.

## Variations

- Scale to 10: `5 - ROUNDDOWN([@Score], 0)` becomes `10 - ROUNDDOWN([@Score], 0)`
- Three-state: use a different symbol (e.g. half-filled star via conditional formatting — unreliable)

## Related

- [[REPT-Function]] — function
- [[In-Cell-Bar-Chart-REPT]] — bar chart pattern
- [[Progress-Bar-REPT-LET]] — progress bar pattern
