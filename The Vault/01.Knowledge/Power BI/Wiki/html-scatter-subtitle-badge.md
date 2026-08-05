---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: pattern
tags: [powerbi, dax, html, correlation, tooltip, dynamic-text]
---

# HTML Scatter Subtitle with Correlation Badge

A DAX measure that produces an HTML-formatted subtitle for a scatter chart tooltip page. The subtitle contains a colored badge showing the correlation strength and a plain-language explanation of the relationship direction.

## Formula

```c
Scatter Subtitle (HTML) =
VAR _x    = [Selected X Name]
VAR _y    = [Selected Y Name]
VAR _r    = [Correlation]
VAR _abs  = IF ( ISBLANK ( _r ), BLANK(), ABS ( _r ) )

-- Label bucket
VAR _labelRaw =
    SWITCH(
        TRUE(),
        _r <= -0.70, "high negative",
        _r <= -0.50, "medium negative",
        _r <= -0.30, "low negative",
        _r >=  0.70, "high positive",
        _r >=  0.50, "medium positive",
        _r >=  0.30, "low positive",
        "very weak/none"
    )
VAR _labelText = UPPER(LEFT(_labelRaw,1)) & MID(_labelRaw,2,LEN(_labelRaw)-1)

-- Background color by label bucket
VAR _bg_base =
    SWITCH(
        _labelRaw,
        "high negative",    [_Color Dark Orange],
        "medium negative",  [_Color Mid Orange],
        "low negative",     [_Color Light Orange],
        "high positive",    [_Color Dark Green],
        "medium positive",  [_Color Mid Green],
        "low positive",     [_Color Light Green],
        BLANK()
    )
VAR _bg = IF( _labelRaw = "very weak/none" || _abs < 0.10, [_Color White], _bg_base )

-- Font color: white on high/medium, dark on low
VAR _fg =
    SWITCH(
        TRUE(),
        _labelRaw IN { "high negative", "high positive", "medium negative", "medium positive" }, "#FFFFFF",
        [_Color dark grey]
    )

-- Badge: "<Label> correlation, r = 0.84"
VAR _badgeFull =
    "<span style='background-color:" & _bg &
    "; color:" & _fg &
    "; padding:1px 6px; font-size:12px; font-family:Segoe UI Light; font-weight:600; display:inline-block; white-space:nowrap'>" &
    _labelText & " correlation</span>"
VAR _headline = _badgeFull & ", <b>r = " & FORMAT( _r, "0.00" ) & "</b>"

-- Sentence: "Y tends to increase/decrease as X increases/decreases"
VAR _sentenceRaw = _y & " tends to increase as " & _x & " increases"
VAR _sentenceBold =
    SUBSTITUTE(
        SUBSTITUTE(
            SUBSTITUTE( _sentenceRaw, "increases", "<b>increases</b>" ),
            "decreases", "<b>decreases</b>"
        ),
        "increase", "<b>increase</b>"
    )
VAR _sentenceFinal =
    IF( _r > 0,
        _sentenceBold,
        SUBSTITUTE( _sentenceBold, "<b>increase</b>", "<b>decrease</b>" )
    )

RETURN
IF(
    ISBLANK(_r) || ISBLANK(_x) || ISBLANK(_y),
    BLANK(),
    "<div style='color:" & [_Color dark grey] & "; font-family:Segoe UI Light; font-size:12px; line-height:1.4'>" &
        _headline & "<br/>" & _sentenceFinal &
    "</div>"
)
```

## Output Example

For a cell where engagement is negatively correlated with overtime (r = -0.71):

```
[HIGH NEGATIVE CORRELATION], r = -0.71
Engagement Survey Score tends to **decrease** as Overtime Hours **increases**.
```

## Key Techniques

| Technique | Purpose |
|-----------|---------|
| `_labelRaw` | Buckets r into one of 7 strength labels |
| `_labelText` | Capitalizes the first letter for display ("high negative" → "High negative") |
| `_bg` / `_fg` | Selects background and font color per bucket |
| `<span>` | Inline badge styled with CSS inline attributes |
| `SUBSTITUTE` chain | Bolds "increases"/"decreases" in the sentence |
| `IF(_r > 0, ...)` | Flips sentence direction for negative correlations |

## Notes

- Requires HTML/text box with Web URL content enabled in Power BI.
- Uses `_Color dark grey` from the correlation color palette defined in [[correlation-color-buckets]].
- Requires `Selected X Name`, `Selected Y Name`, and `Correlation` measures from [[scatter-tooltip-x-y-value-measures]] and [[pearson-correlation-measure]].

## Related

- [[correlation-color-buckets]]
- [[scatter-tooltip-x-y-value-measures]]
- [[pearson-correlation-measure]]
