---
created: 2026-08-03
source: New Power BI Style Presets.md
note_type: gotcha
tags: [power-bi, theme, json, style-presets]
---

# Style Preset Dropdown Does Not Appear

The **Format > Style preset** dropdown is missing from the visual's formatting pane — even though the JSON theme has been loaded.

## Expected Behaviour

After loading a JSON theme with custom presets, the Style preset dropdown appears in the Format pane for each visual that has matching preset definitions.

## Actual Behaviour

The Style preset dropdown does not appear at all. The visual still renders with the base theme formatting.

## Why It Happens

The Style preset dropdown is conditionally rendered by Power BI Desktop — it only appears when at least one custom preset has been defined in the JSON theme for that specific visual type. If the preset definitions are absent or malformed, the dropdown is not shown.

## How to Handle It

1. **Verify the `$schema` is present** and pointing to a valid URL — the March 2025 schema (version 2.141) or later is required for style presets.
2. **Check the preset is defined under the correct visual type key.** The preset definition must be a sibling of the `"*"` block, not nested inside it. Correct structure:
   ```json
   "clusteredColumnChart": {
     "*": {
       "stylePreset": [{ "name": "ColumnDetailedChartLabels" }]
     },
     "ColumnDetailedChartLabels": {
       // preset config here
     }
   }
   ```
   Incorrect (preset config nested inside `"*"`):
   ```json
   "clusteredColumnChart": {
     "*": {
       "stylePreset": [{ "name": "ColumnDetailedChartLabels" }],
       "ColumnDetailedChartLabels": { /* won't be recognised */ }
     }
   }
   ```
3. **Reload the theme:** after editing the JSON, use **View > Themes > Browse for themes** to reapply the updated file.
4. **Confirm Power BI version:** style presets require the March 2025 update or later. Check via **Help > About Microsoft Power BI Desktop**.

## Related Gotchas

- (No other gotchas for style presets yet)
