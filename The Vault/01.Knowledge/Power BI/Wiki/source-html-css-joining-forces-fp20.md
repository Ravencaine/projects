---
created: 2026-08-09
updated: 2026-08-09
source: "Elevating Power BI Reports with HTML & CSS Joining Forces 💪.md"
source_url: "https://medium.com/microsoft-power-bi/elevating-power-bi-reports-with-html-css-joining-forces-f90fbd654e8b"
author: "[[Isabelle Bittar]]"
site: https://medium.com/@isabittar
published: 2024-02-04
source_type: article
kb_routing: Power BI
tags: [power-bi, html, css, html-content-visual, dax, font-awesome, shapes, fp20]
challenge: FP20 Analytics Challenge — Data-Driven Education Management
---

# HTML & CSS Joining Forces in Power BI

Isabelle Bittar · KI Data Science · Medium · 2024-02-04 · FP20 Analytics Challenge

## What this article covers

Using the HTML Content visual (third-party) in Power BI to embed HTML and CSS directly in DAX measures. Three use cases: styled text (bold, color, line breaks), custom shapes (ovals with text + icons), and Font Awesome icons via CDN with dynamic color/size via SUBSTITUTE.

## HTML Content visual

Not a built-in Power BI visual — imported via "Get more visuals". HTML must be enclosed in quotation marks in measures. Combines DAX + HTML/CSS for dynamic, styled content.

## Key technique

DAX measure returns HTML string. SUBSTITUTE replaces placeholders (colors, icons, text) with dynamic values. IF returns BLANK when no data.

## Key measures

- `Visualization Last Semester/Year Average Score` — bold text + `<br>` line breaks
- `Oval Set Up` — HTML/CSS shape template with {BACKGROUND_COLOR}, {FONT_COLOR}, {TEXT} placeholders
- `Formatted Average Score Last Semester Variation` — nested SUBSTITUTE on Oval Set Up; conditional colors + Font Awesome icons
- `Icon Font awesome icon set up` — CDN link + {COLOR}/{ICON_CODE}/{SIZE} placeholders
- `Icon green arrow up` — SUBSTITUTE chain on template → `fa-solid fa-arrow-trend-up` + green color

## Other opportunities

- Interactive maps, animated charts, mini-games
- Custom navigation menus
- Embedded videos, real-time data feeds
- Corporate branding and styling

## Codecademy courses

- Learn HTML (~6 hours)
- Learn CSS (~6 hours)
