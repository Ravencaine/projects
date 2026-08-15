---
created: 2026-08-13
source: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
source_url: https://www.youtube.com/watch?v=QXMMpabHPS4
note_type: pattern
tags: [calculation-group, kpi-card, selectedmeasure, format-string-expression, sameperiodlastyear]
---

# KPI Context Cards with Calculation Groups

Build KPI cards that show current value, last-period value, growth %, and a directional triangle in one Calculation Group — using the calculation-group-only functions `SELECTEDMEASURE()` and `SELECTEDMEASUREFORMATSTRING()`.

## Purpose

A single calculation item produces a card text like:

```
$1.2M ▲ +12.3%
```

…where the value is the current measure and the percent + triangle is computed from `SAMEPERIODLASTYEAR()`. Without a Calculation Group you'd need three measures and a custom visual per KPI.

## Components

| Variable | Expression | Purpose |
|----------|-----------|---------|
| `Current` | `SELECTEDMEASURE()` | The value of whatever measure is in the visual's Values field |
| `LastYear` | `CALCULATE( SELECTEDMEASURE(), SAMEPERIODLASTYEAR('Date'[Date]) )` | Same period, prior year |
| `Growth` | `DIVIDE( Current - LastYear, LastYear )` | Percentage change |
| `FormatString` | `SELECTEDMEASUREFORMATSTRING()` | The format string of the underlying measure |

## Structure (Tabular Editor — Calculation Item)

```dax
KPI =
VAR _Value      = SELECTEDMEASURE()
VAR _LastYear   = CALCULATE( SELECTEDMEASURE(), SAMEPERIODLASTYEAR('Date'[Date]) )
VAR _Growth     = DIVIDE( _Value - _LastYear, _LastYear )
VAR _FmtString  = SELECTEDMEASUREFORMATSTRING()
VAR _Arrow      = IF( _Growth > 0, "▲", IF( _Growth < 0, "▼", "■" ) )
VAR _PctString  = FORMAT( ABS(_Growth), "+0.0%;-0.0%;0.0%" )
RETURN
    FORMAT( _Value, _FmtString ) & " " & _Arrow & " " & _PctString
```

If a `Date` table isn't named that way, adjust `SAMEPERIODLASTYEAR()` to reference the actual date column and table.

## Format String Expression (Tabular Editor)

Calculation groups expose a **Format String Expression** property directly in Tabular Editor (the empty box at the calculation-item level). Use it to keep numbers readable instead of raw text:

```dax
// Format String Expression — shortens large numbers without using logarithms
// Credit: Kane Snyder (Agile Analytics)
VAR _Value      = SELECTEDMEASURE()
VAR _IntPart    = INT( ABS(_Value) )
VAR _DigitCount = LEN( _IntPart )
VAR _Scaled =
    SWITCH(
        TRUE(),
        _DigitCount <= 3, FORMAT(_Value, "#,##0"),
        _DigitCount <= 6, FORMAT(_Value / 1000, "#,##0.0") & "K",
        _DigitCount <= 9, FORMAT(_Value / 1000000, "#,##0.0") & "M",
        FORMAT(_Value / 1000000000, "#,##0.0") & "B"
    )
RETURN _Scaled
```

Without an explicit format string expression, Power BI treats the calculation item's output as text and the user loses all numeric formatting.

## Variations

- **Show Δ (delta) instead of %** — replace `_PctString` with `FORMAT(_Value - _LastYear, "+#,##0;-#,##0;0")`. Combine with percent for compactness.
- **Multiple card sizes** — apply the calculation group filter to one card (e.g. a small KPI strip) but not another (a large headline card). The filter only affects visuals that have the calculation-group column in their filter context.
- **Cross-measure by category** — `SELECTEDMEASURE()` resolves whichever measure the visual binds to, so swapping measures on the page (Sales, Profit, Units) works without changing the calculation item.

## Gotchas

- **Without a Format String Expression, the output reads as text** — that's the most common "why doesn't this format right?" failure mode for calculation items.
- **Logarithms are slow** — original approaches used `LOG10()` for magnitude scaling; an integer-length switch is significantly faster per Kane Snyder's published work.

## Related

- [[dynamic-html-text-via-calculation-groups]] — the same Calculation Group pattern, applied to text/font/color
- [[advanced-kpi-cards]] — card design and `UNICHAR()` arrow approach (alternative)
