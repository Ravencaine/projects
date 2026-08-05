---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: gotcha
tags: [dax, gotcha, emoji, unicode, string]
---

# Emoji in DAX String Concatenation

DAX string concatenation using `&` handles Unicode emoji characters without any special syntax — but emoji can cause rendering issues in certain Power BI visuals and export contexts.

## Expected Behaviour

Using emoji in DAX string literals should render correctly in card visuals, button slicers, and table/matrix visuals:

```dax
"👥 " & [Count] & " employees exceeded threshold"
```

## Actual Behaviour

In button slicer callout labels and some custom visuals, emoji may not render on all platforms or may cause alignment issues in narrow containers. On some deployments, emoji characters can increase the measure string length enough to affect formatting in compact card designs.

## Why It Happens

DAX stores strings as UTF-16 (like Excel). Emoji are valid Unicode code points in the supplementary planes (U+1F300 and above). DAX handles them correctly at the expression level. The rendering issue is a Power BI visual limitation, not a DAX limitation.

## How to Handle It

- Use emoji in button slicer callout labels and card visuals — they render in the Power BI Desktop and service client in most cases
- For report page tooltips and exported formats (PDF, PPTX), test emoji rendering before deploying
- For cross-platform compatibility, prefer named Unicode characters from the Basic Multilingual Plane via `UNICHAR()` — e.g. `UNICHAR(9658)` for a right-pointing triangle instead of `🔺`
- Keep emoji at the start of the string — trailing emoji can cause unexpected text wrapping in card visuals

## Related

- [[UNICHAR]]
