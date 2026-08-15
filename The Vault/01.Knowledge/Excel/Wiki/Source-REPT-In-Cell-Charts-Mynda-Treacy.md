---
created: 2026-08-10
updated: 2026-08-10
source: "Excel REPT Function In Cell Charts • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
note_type: source
tags: [excel, functions, visualisation, dashboard, charts]
---

# Excel REPT Function In Cell Charts — My Online Training Hub / Mynda Treacy

Source: My Online Training Hub. Published 2026-06-23. Author: Mynda Treacy — 11th source.

## Summary

The REPT function repeats text a specified number of times. Combined with Unicode block characters and font formatting, it creates formula-driven in-cell visuals — bar charts, progress bars, and star ratings — that update automatically when underlying data changes. Works entirely inside cells without inserting chart objects.

## Key Claims

- REPT repeats text a given number of times; accepts any character or Unicode symbol
- REPT always rounds decimal inputs down to the nearest integer
- In-cell bar charts: `=REPT("█",[@Sales]/MAX([Sales])*20)` with Consolas font
- Progress bars: `=LET(width,20, filled,ROUND([@[Completion Rate]]*width,0), REPT("█",filled)&REPT("▒",width-filled))`
- Star ratings: `=REPT("★",[@Score])&REPT("☆",5-ROUNDDOWN([@Score],0))`
- Half stars not reliably supported via Unicode
- REPT bar charts combine with conditional formatting for colour control
- Monospaced font (Consolas) required for bar alignment

## Notable Details

- UNICHAR(9733) = filled star (★), UNICHAR(9734) = unfilled star (☆)
- Block character inserted via Insert > Symbol > Arial > Block Elements
- Pipe symbol `|` via SHIFT+\\ gives narrower bar increments for higher precision
- Conditional formatting formulas on REPT bars must use relative row references (e.g. `$D7` not `$D$7`)
- Progress bar width of 20 = 5% per character; width of 50 = 2% per character

## Extracted Notes

Links to notes derived from this source:

- [[REPT-Function]] — `function` — text repeat with signature, parameters, gotcha
- [[In-Cell-Bar-Chart-REPT]] — `pattern` — proportional bar chart inside cells
- [[Progress-Bar-REPT-LET]] — `pattern` — two-symbol progress bar with filled/remaining sections
- [[Star-Rating-REPT]] — `pattern` — filled/unfilled star rating from numeric score
- [[REPT-Rounds-Decimals-Down]] — `gotcha` — decimal truncation behaviour
- [[REPT-vs-Conditional-Formatting-Data-Bars]] — `comparison` — when to use each approach
- [[Monospaced-Font-for-REPT-Bars]] — `atomic` — Consolas required for alignment
- [[REPT-Function]] — `function` — text repeat with signature, parameters, gotcha
- [[Author-Mynda-Treacy]] — `author` — Mynda Treacy / MyOnlineTrainingHub

## Metadata

| Field | Value |
|-------|-------|
| Source file | Inbox |
| Archived at | pending |
| Ingestion date | 2026-08-10 |
| Word count | ~700 |
