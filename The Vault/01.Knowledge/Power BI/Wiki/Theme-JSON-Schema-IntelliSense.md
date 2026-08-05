---
created: 2026-08-03
updated: 2026-08-05
source: New Power BI Style Presets.md
note_type: atomic
tags: [power-bi, theme, json, intellisense]
---

# $schema IntelliSense for Power BI JSON Themes

Adding a `$schema` property to a Power BI JSON theme file enables IntelliSense — auto-complete, validation, and inline documentation — in code editors like Visual Studio Code.

## Definition

The `$schema` property is a JSON Schema URL that tells the editor how to validate and auto-complete your theme file. Without it, the editor treats the file as plain JSON with no guidance.

## Key Points

- The `$schema` URL points to Microsoft's official theme schema on GitHub.
- The schema URL embeds a version number (e.g., `reportThemeSchema-2.141.json` for March 2025).
- To find the **latest schema URL**, go to **View > Themes > Customize current theme** in Power BI Desktop and click the "How to create a theme" link at the bottom — it opens Microsoft's documentation with the current GitHub URL.
- Place `$schema` directly under the `name` property at the top of the JSON file.

## Code

```json
{
  "name": "My Theme",
  "$schema": "https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/refs/heads/main/Report%20Theme%20JSON%20Schema/reportThemeSchema-2.141.json",
  ...
}
```

## Related

- [[Style-Presets-Pattern.md]]
- [[Style-Presets-Workflow.md]]
