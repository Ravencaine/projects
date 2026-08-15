---
created: 2026-08-10
updated: 2026-08-10
source: "Excel REPT Function In Cell Charts • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
note_type: function
tags: [excel, function, text, visualisation]
---

# REPT — Repeat Text

Repeats a text string a specified number of times. Used to build formula-driven in-cell bar charts, progress bars, and star ratings.

## Signature

```excel
=REPT(text, number_times)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | string | The text or Unicode character to repeat |
| `number_times` | number | How many times to repeat; decimals are rounded down to integer |

## Returns

A text string containing `text` repeated `number_times` times. Returns empty string if `number_times` is 0.

## Examples

```excel
=REPT("-", 10)
→ "----------"

=REPT("█", 3.9)
→ "███"   (rounds 3.9 down to 3)

=REPT("★", 4) & REPT("☆", 5-4)
→ "★★★★☆"
```

## Notes

**REPT truncates decimals, it does not round.** `=REPT("█",3.9)` returns 3 blocks, not 4. Always wrap with ROUND, ROUNDDOWN, or ROUNDUP when using percentage or ratio values that may have decimal components.

See [[REPT-Rounds-Decimals-Down]] for the full gotcha.

Works in all Excel versions — no Microsoft 365 required.

## Related

- [[In-Cell-Bar-Chart-REPT]] — pattern
- [[Progress-Bar-REPT-LET]] — pattern
- [[Star-Rating-REPT]] — pattern
- [[REPT-vs-Conditional-Formatting-Data-Bars]] — comparison
