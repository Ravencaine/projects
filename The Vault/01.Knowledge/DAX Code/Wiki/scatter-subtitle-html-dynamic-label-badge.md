---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, html, tooltip, dynamic-label, correlation]
---

# Scatter Subtitle (HTML) — Dynamic Label Badge for Correlation Tooltip

Generates an HTML text box content for the scatter chart tooltip subtitle: a color-coded badge showing the correlation strength and direction, plus a plain-language sentence explaining the relationship.

## Signature

```dax
Scatter Subtitle (HTML) :=
VAR _x    = [Selected X Name]
VAR _y    = [Selected Y Name]
VAR _r    = [Correlation]
VAR _abs  = IF ( ISBLANK ( _r ), BLANK(), ABS ( _r ) )

VAR _labelRaw =
    SWITCH( TRUE(),
        _r <= -0.70, "high negative",
        _r <= -0.50, "medium negative",
        _r <= -0.30, "low negative",
        _r >=  0.70, "high positive",
        _r >=  0.50, "medium positive",
        _r >=  0.30, "low positive",
        "very weak/none"
    )
VAR _labelText = UPPER(LEFT(_labelRaw,1)) & MID(_labelRaw,2,LEN(_labelRaw)-1)

VAR _bg =
    IF( _labelRaw = "very weak/none" || _abs < 0.10, [_Color White],
        SWITCH( _labelRaw,
            "high negative",   [_Color Dark Orange],
            "medium negative", [_Color Mid Orange],
            "low negative",    [_Color Light Orange],
            "high positive",   [_Color Dark Green],
            "medium positive", [_Color Mid Green],
            "low positive",    [_Color Light Green]
        )
    )
VAR _fg =
    IF( _labelRaw IN { "high negative", "high positive", "medium negative", "medium positive" },
        "#FFFFFF", [_Color dark grey] )

VAR _badgeFull =
    "<span style='background-color:" & _bg &
    "; color:" & _fg &
    "; padding:1px 6px; font-size:12px; font-family:Segoe UI Light; font-weight:600; display:inline-block; white-space:nowrap'>" &
    _labelText & " correlation</span>"

VAR _headline = _badgeFull & ", <b>r = " & FORMAT( _r, "0.00" ) & "</b>"

VAR _sentenceRaw = _y & " tends to increase as " & _x & " increases"
VAR _sentenceFinal =
    IF( _r > 0,
        SUBSTITUTE( SUBSTITUTE( _sentenceRaw, "increases", "<b>increases</b>" ), "decreases", "<b>decreases</b>" ),
        SUBSTITUTE( SUBSTITUTE( _sentenceRaw, "increases", "<b>decreases</b>" ), "decreases", "<b>increases</b>" )
    )

RETURN
IF( ISBLANK(_r) || ISBLANK(_x) || ISBLANK(_y), BLANK(),
    "<div style='color:" & [_Color dark grey] & "; font-family:Segoe UI Light; font-size:12px; line-height:1.4'>" &
        _headline & "<br/>" & _sentenceFinal &
    "</div>"
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `[Selected X Name]` / `[Selected Y Name]` | measure | Variable display names |
| `[Correlation]` | measure | Pearson r value |
| `_Color *` | measures | Hex color constants |

## Returns

An HTML string that Power BI renders as formatted text in the visual's text box.

Output example: `<div style='...'><span style='...'>Medium negative correlation</span>, <b>r = -0.62</b><br/><b>Overtime Hours</b> tends to <b>decrease</b> as <b>Engagement Survey Score</b> increases</div>`

## Notes

- Assigned to a **Text Box** visual on the tooltip page, not to a DAX measure property
- The HTML requires the report to have HTML rendering enabled (enabled by default in Power BI)
- `_Color dark grey` is referenced as `[Color dark grey]` (note: lowercase `dark grey` — matches the source naming)
- The plain-language sentence flips "increases" → "decreases" when r is negative

## Related

- [[interactive-tooltip-scatter-chart-on-matrix]] — `pattern` — tooltip scatter chart
- [[selected-x-name-selected-y-name]] — `function` — variable name capture
- [[correlation-core-pearson-measure]] — `function` — correlation value source
- [[color-palette-measures-static-hex-strings]] — `function` — color constants
