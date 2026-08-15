---
created: 2026-08-10
updated: 2026-08-10
source: "Excel REPT Function In Cell Charts • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
note_type: pattern
tags: [excel, pattern, visualisation, chart, dashboard]
---

# In-Cell Bar Chart with REPT

Creates a proportional bar chart inside a cell using the block character `█` repeated relative to a maximum value.

## Purpose

Compare values across rows without inserting chart objects. Bars update automatically when underlying data changes. Can be combined with conditional formatting for colour-coded thresholds.

## Components

- `REPT` — repeats the block character
- `MAX` — normalises values to 0–1 range
- Excel Table structured references (e.g. `[@Sales]`)
- Monospaced font (Consolas) for alignment

## Structure

```excel
=REPT("█", [@Sales] / MAX([Sales]) * 20)
```

Set the bar width with `* N` where N is the maximum character count (e.g. `* 20` for a 20-character bar).

## Example

Data in an Excel Table column named `Sales`:

```excel
=REPT("█", [@Sales] / MAX([Sales]) * 20)
```

The product with the highest sales gets a full 20-character bar. All other products are proportional.

**Font:** Format the cell with Consolas (or Courier New).

**Conditional formatting colour:**
```
=$D7>9000   → green
=$D7>7000   → yellow
=$D7>6000   → orange
=$D7<=6000  → red
```

Row reference must be relative (`$D7`, not `$D$7`) so Excel checks each row.

## Variations

- Change bar width: `* 50` for higher precision (each character = 2%)
- Narrow bars: use pipe `|` (SHIFT+\\) instead of `█`
- Colour-coded: apply conditional formatting rules based on the underlying cell value

## Related

- [[REPT-Function]] — function
- [[Progress-Bar-REPT-LET]] — pattern with filled + remaining sections
- [[Monospaced-Font-for-REPT-Bars]] — atomic — why Consolas is required
