---
created: 2026-08-09
updated: 2026-08-09
source: "Elevating Power BI Reports with HTML & CSS Joining Forces 💪.md"
note_type: pattern
tags: [power-bi, html, css, shapes, dax, substitute, pattern]
---

# HTML Shape Measure Template Pattern

**Type:** Pattern · **KB:** Power BI · **Source:** [[source-html-css-joining-forces-fp20]]

Create a reusable HTML shape template in DAX with placeholders. Use SUBSTITUTE to replace placeholders with dynamic values (color, font, text, icon) computed from the data model. One template → many conditional variants.

## When to use

When you need custom shapes (ovals, badges, pills) that display data-driven content with dynamic colors, text, and icons. Rather than separate measures per variant, one template + SUBSTITUTE handles all variations.

## Template structure

```dax
Oval Set Up =
"<head>
<meta name=""viewport"" content=""width=device-width, initial-scale=1"">
<style>
.oval {
  height: 18px;
  width: 48px;
  background-color: {BACKGROUND_COLOR};
  border-radius: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: {FONT_COLOR};
  font-size: 10px;
}
</style>
<body>
<div class=""oval"">
    <span>&nbsp;{TEXT}</span>
</div>
</body>"
```

Three placeholders: `{BACKGROUND_COLOR}`, `{FONT_COLOR}`, `{TEXT}`.

## Substitution chain

```dax
VAR _Shape =
SUBSTITUTE(
    SUBSTITUTE(
        SUBSTITUTE(
            [Oval Set Up],
            "{BACKGROUND_COLOR}", _BackgroundColor
        ),
        "{FONT_COLOR}", _FontColor
    ),
    "{TEXT}", _Text
)
RETURN IF([Score] <> BLANK(), _Shape)
```

Three nested SUBSTITUTE calls: one per placeholder.

## Use cases

- KPI variation badges (green/red with arrow + percentage)
- Status pills (positive/negative/neutral)
- Category labels with dynamic colors
- Trend indicators with conditional icons

## Why not built-in shapes

Power BI built-in shapes cannot include dynamic text or icons inside them. HTML shapes can contain `<span>` elements with DAX-computed values and Font Awesome icon codes, making them fully dynamic.

## Related

- [[html-measure-integration-pattern]] — underlying mechanism
- [[substitute-placeholder-chaining]] — nested SUBSTITUTE pattern
- [[font-awesome-dax-icon-measure]] — icon + SUBSTITUTE
