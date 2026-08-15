---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into tooltip options in Power BI visuals (Generally Available).md"
note_type: atomic
tags: [power-bi, tooltip, help-tooltip, data-tooltip, visual-header]
---

# Data Tooltip vs Help Tooltip — Dual Icon Distinction

> **Type:** atomic
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-06

## Mental Model

Two tooltip types, two purposes, two locations:

| | **Data Tooltip** | **Help Tooltip** |
|---|---|---|
| **Location** | Hover anywhere on the visual | Hover the `(?)` icon in the visual header |
| **Shows** | Data about the hovered point | Guidance about the visual itself |
| **Example** | "Sales changed by $3.7M (44%) since last year" | "Use the drill arrows to explore Category → Subcategory" |
| **Template** | Default, Tooltip fields only, Sentence format | Typed text or report page |

## Why Both Matter

- **Data tooltip:** Answers "what does this data point mean?" for any hovered value
- **Help tooltip:** Answers "how do I interact with this visual?" for new users

Both coexist on the same visual without interfering with each other.

## Help Tooltip Use Cases

- Explaining custom visuals
- Instructions for slicers, filters, or drill interactions
- Defining unusual metrics or calculations
- Quick demo: point a Help tooltip report page at an animated GIF background — it plays on every hover, showing users how to interact with the visual

## Key Rule

> Help tooltip explains the **visual**, not the **data**. If the content is about a specific data point, it belongs in the data tooltip (sentence format or report page).

## See Also

- [[Source-Tooltip-Options-Generally-Available]] — source article
- [[Tooltip-Type-Selection-Workflow]] — how to configure each type
