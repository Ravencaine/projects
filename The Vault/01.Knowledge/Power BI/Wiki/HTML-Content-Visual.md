---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [html-content, font-awesome, custom-visual, icon, dax-html]
related: [UNICHAR, SUBSTITUTE, Process-Tracker-Dynamic-Fill]
---

# HTML Content Visual with Font Awesome

Uses the HTML Content custom visual to render Font Awesome icons and styled HTML text inside Power BI, driven entirely by DAX measures. Enables dynamic icons (checkmarks, spinners, alerts) that cannot be rendered natively.

## Setup

1. Search **HTML Content** in the Power BI visualizations pane and add it.
2. Import from: `https://appsource.microsoft.com/en-us/marketplace/apps`

## Font Awesome CDN Header

Add this as a `const` measure — include it once in the report via a hidden HTML Content visual:

```dax
_const HTML Header =
"<head>"
    & "<link rel=""stylesheet"" href=""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css""/>"
& "</head>"
```

## Icon Constants

```dax
_const Icon Font Awesome Setup =
"<head><link rel=""stylesheet"" href=""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css""/></head>"
& "<div style=""margin:right;""><i style=""color:{COLOR}"" class=""{ICON_CODE} {SIZE}""></i>&nbsp;"

_const Icon Green Check =
SUBSTITUTE(
    SUBSTITUTE(
        SUBSTITUTE([_const Icon Font Awesome Setup], "{ICON_CODE}", "fa-solid fa-circle-check"),
        "{SIZE}", "fa-xl"
    ),
    "{COLOR}", [_const Color Green]
)

_const Icon In Progress =
SUBSTITUTE(
    SUBSTITUTE(
        SUBSTITUTE([_const Icon Font Awesome Setup], "{ICON_CODE}", "fa-solid fa-spinner"),
        "{SIZE}", "fa-xl"
    ),
    "{COLOR}", [_const Color Green]
)
```

## Icon Measure

```dax
Step 1 Icon =
    SWITCH(
        TRUE(),
        [Selected Stage Order] > 1, [_const Icon Green Check],
        [Selected Stage Order] = 1, [_const Icon In Progress]
    )
```

## Alert Icon Example

```dax
_const Icon Alert =
"<i style=""color:#EE6064"" class=""fa-solid fa-circle-exclamation fa-xl""></i>"

_const Icon No Alert =
"<i style=""color:#76E3B4"" class=""fa-solid fa-circle-check fa-xl""></i>"

Alert Icon =
    IF(
        CONTAINSSTRING([Alert Message], "No new alerts"),
        [_const Icon No Alert],
        [_const Icon Alert]
    )
```

## Common Font Awesome Icons

| Icon | Code | Use |
|------|------|-----|
| Checkmark | `fa-solid fa-circle-check` | Completed step |
| Spinner | `fa-solid fa-spinner` | In-progress step |
| Alert | `fa-solid fa-circle-exclamation` | Alert indicator |
| Chart | `fa-solid fa-chart-line` | Analytics |
| Trend up | `fa-solid fa-arrow-trend-up` | Positive trend |
| Trend down | `fa-solid fa-arrow-trend-down` | Negative trend |
| Star | `fa-solid fa-star` | Favourite/highlight |

## Notes

- The HTML Content visual renders HTML inside Power BI — this is a Microsoft-certified custom visual, not an unofficial plugin.
- Icons are loaded from a CDN — the report requires internet access (or a published workspace with CDN access). Works in Power BI Service.
- The `SUBSTITUTE` pattern injects color and icon code into a template string — this avoids building the HTML from scratch in each measure.
- `fa-solid` is the solid icon set (filled). Use `fa-regular` for outline icons if available in the version.
- For static icons, Bittar also imports PNG images (from Flaticon) directly as shape overlays — see [[Process-Tracker-Dynamic-Fill]].

## Related

- [[UNICHAR]] — alternative DAX-native icon approach (fewer options, no CDN needed)
- [[CONTAINSSTRING]] — detect alert state to toggle icons
- [[substitute]] — inject dynamic values into HTML template strings
- [[Dynamic-Alerts]] — full alert pattern using HTML Content visual
