---
created: 2026-08-13
source: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
source_url: https://www.youtube.com/watch?v=QXMMpabHPS4
note_type: pattern
tags: [html-visual, dynamic-theme, rgb, named-color, gradient, bookmarks]
---

# Dynamic Color Themes via HTML + RGB

Use the HTML custom visual's CSS color support to let users drive theme colors via numeric parameters (R/G/B), named color strings, or a gradient blend.

## Purpose

Power BI's native theme can be replaced per report, but not per visual at runtime. HTML visuals can read a CSS color string from a DAX measure — so three numeric parameters (R, G, B) plus a calculation group for solid / RGB / named / gradient modes gives users live control over text, borders, backgrounds, and icons.

## Inputs

| Input | Type | Range / Source |
|-------|------|----------------|
| R numeric parameter | integer | 0–255 |
| G numeric parameter | integer | 0–255 |
| B numeric parameter | integer | 0–255 |
| Named color table | table | Browser-recognized HTML color names (manually pasted) |
| Color-mode bookmarks | bookmarks | Toggle between RGB and named-color input |
| Color percentage parameter | integer 0–100 | Blend ratio between two gradient colors |
| Hue parameter | integer | Lighten/darken offset |

## Structure

```dax
ColorText =
VAR _R = SELECTEDVALUE('RParam'[RParam Value], 0)
VAR _G = SELECTEDVALUE('GParam'[GParam Value], 0)
VAR _B = SELECTEDVALUE('BParam'[BParam Value], 0)
RETURN
"rgb(" & _R & ", " & _G & ", " & _B & ")"
```

### Dual-Mode Switch

A small helper table with two rows (`RGB`, `Name`) controls which color path renders:

```dax
ColorChoice =
SWITCH(
    TRUE(),
    SELECTEDVALUE('ColorMode'[Mode]) = "RGB", ColorText_RGB(),
    SELECTEDVALUE('ColorMode'[Mode]) = "Name", SELECTEDVALUE('NamedColors'[ColorName], "black"),
    "black"
)
```

The mode is selected by which bookmark is active — `+` bookmark shows the RGB sliders, `–` bookmark shows the named-color picker.

### Gradient Calculation Item

```dax
Gradient =
"linear-gradient(90deg, " & [Color1] & " " & [Pct1] & "%, " & [Color2] & " " & [Pct2] & "%)"
```

The `<Pct>` numeric parameter (0–100) controls how much of color one vs color two is shown.

### Border via Overlay Trick

The colored border on the demo isn't a CSS border. It's a full-bleed HTML visual with one color, then a smaller HTML visual layered on top with a different color. The "border" is just the visible ring of the larger visual.

## Example

Flavio Meneses' original idea: three R/G/B numeric sliders. Injae Park's extension adds named colors, gradient blends, and a Hue control that lightens one color against another. Combined, that's a complete dynamic theming system for HTML visuals — no JSON theme reloads.

## Limitations

- Three separate colors for foreground, gradient, and background = **9 parameters**. With named colors also selectable = **3 reference tables**. Approach "more effort than it's worth for most people."
- Hue and gradient maths are sensitive to parameter independence; users can pick combinations that look bad. There is no design constraints layer.

## Related

- [[dynamic-html-text-via-calculation-groups]] — same approach applied to text properties
- [[google-fonts-api-power-bi]] — for sourcing the font driving the text
