---
created: 2026-08-09
updated: 2026-08-09
source: "Elevate Your Power BI Tables with Custom Icons 🥳 1.md"
note_type: atomic
tags: [power-bi, svg, json-theme, url-encoding, data-uri, atomic]
---

# SVG to Theme URL Transformation Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-custom-icons-power-bi-tables]]

SVG code from Figma or SVG Repo must be transformed into a data URI before embedding in a Power BI JSON theme file. Four transformation steps.

## The 4-step transformation

### Step 1 — Replace double quotes with single quotes

```m
// Original
<circle cx="12" cy="12" r="12" fill="#DCE7F2"/>

// Transformed
<circle cx='12' cy='12' r='12' fill='#DCE7F2'/>
```

### Step 2 — Escape special characters

| Original | Encoded |
|----------|---------|
| `#` | `%23` |
| space | `%20` |

### Step 3 — Remove line breaks and whitespace

Collapse the SVG to a single line, removing indentation and line breaks for inline embedding.

```m
// Before
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="12" fill="#DCE7F2"/>
  <path d="M8.04..." fill="#293D61"/>
</svg>

// After (single line)
<svg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><circle cx='12' cy='12' r='12' fill='%23DCE7F2'/><path d='M8.04...' fill='%23293D61'/></svg>
```

### Step 4 — Add data URI prefix

Prepend `data:image/svg+xml;utf8,` to the transformed SVG string.

## Final URL value

```
data:image/svg+xml;utf8,<svg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><circle cx='12' cy='12' r='12' fill='%23DCE7F2'/><path d='...' fill='%23293D61'/></svg>
```

## JSON theme entry

```json
"icons": {
  "IconName": {
    "url": "data:image/svg+xml;utf8,<svg width='24' height='24' viewBox='0 0 24 24'>...</svg>"
  }
}
```

## Related

- [[custom-icons-json-theme-cell-element-pattern]] — pattern overview
- [[embed-custom-icons-theme-workflow]] — workflow using this transformation
