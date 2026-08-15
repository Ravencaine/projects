---
created: 2026-08-13
source: "Injae Park (Power BI Park)"
source_url: https://www.youtube.com/watch?v=QXMMpabHPS4
note_type: source
tags: [html-visual, calculation-group, deneb, custom-visuals, remixicon, google-fonts, transcript]
---

# Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb

> **Type:** video / transcript
> **Author:** Injae Park — Power BI Park
> **Published:** 2023-02-15
> **URL:** https://www.youtube.com/watch?v=QXMMpabHPS4
> **Routed to:** Power BI

A 46-minute tutorial walk-through of three advanced Power BI customisations: HTML custom visuals for dynamic fonts/themes/icons, Calculation Groups for KPI cards with context, and Deneb for custom interactive charts.

## Summary

Injae Park ("NJ"), a Power BI custom-visual specialist, walks through three techniques he uses daily. The first half covers the "HTML Content" custom visual combined with the Google Fonts API to deliver text in 1,400+ fonts at user-selectable sizes and colors — extending beyond CSS into dynamic themes driven by R/G/B numeric parameters and bookmark-toggled color pickers. The second half introduces two power-user patterns: Calculation Groups that drive "KPIs with context" using `SELECTEDMEASURE()` and a Format String Expression, and the Deneb visual for declarative Vega/Vega-Lite charts that participate in Power BI's interaction model.

## Key Claims

- HTML custom visuals (e.g. HTML Content by Daniel Marsh Patrick) accept any CSS, including Google Fonts referenced via the Google Fonts Developer API.
- Power BI Calculation Groups can be exposed as a "Color" filter column with multiple calculation items (Black / Solid / Gradient) — extending filters beyond measures.
- The `SELECTEDMEASURE()` and `SELECTEDMEASUREFORMATSTRING()` functions are only available inside Calculation Groups / Calculation Items.
- Calculation Items' numbers render as text unless a **Format String Expression** is set in Tabular Editor — Kane Snyder's "integer-length switch" beat logarithm-based scaling for speed.
- Deneb charts (Vega / Vega-Lite) participate in Power BI's slicer/cross-filter/tooltip system; Python/R visuals do not.
- Microsoft's roadmap (per PM Miguel Myers on the Power BI Guy podcast) is likely to bring native multi-element cards, more fonts, and dynamic themes — making the HTML-Content workarounds potentially obsolete within 12–18 months. Deneb is unlikely to be displaced.

## Notable Details

- The Google Fonts Developer API returns ~1,400 `items.family` values; a single call covers the entire font catalogue.
- 9 numeric parameters were used for the demo's gradient/background/foreground color system; Injae calls this "more effort than it's worth for most people."
- Border-on-color is implemented as two overlaid HTML visuals (one full-bleed, one smaller) — not a CSS border.
- Remix Icon ships 2,271 free, open-licensed SVG icons; can be imported as a Power BI table via the Folder connector with a single Power Query "Transform to Text" step.
- Iwanjae explicitly recommends importing Deneb templates from JSON rather than authoring specs from scratch.
- The author credits Flavio Meneses (BIEvolution) for the original R/G/B slider theme idea, and Kane Snyder for the integer-length format-string approach.

## Extracted Notes

- [[google-fonts-api-power-bi]] — `workflow` — load Google Fonts into Power BI as a slicer-bound table
- [[dynamic-html-text-via-calculation-groups]] — `pattern` — HTML text driven by Calculation Groups
- [[dynamic-color-themes-via-html-rgb]] — `pattern` — dynamic RGB/named/gradient theme via HTML + bookmarks
- [[dynamic-svg-icons-via-html-remixicon]] — `workflow` — RemixIcon import + dynamic color substitution
- [[kpi-context-cards-with-calculation-groups]] — `pattern` — calculation-group-based KPI cards with context
- [[deneb-custom-visual]] — `reference` — Deneb visual overview, editor, template workflow
- [[power-bi-custom-visual-approaches]] — `comparison` — native vs HTML vs Deneb vs Python/R

## Metadata

| Field | Value |
|-------|-------|
| Source file | `00.Inbox/Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb.md` |
| Transcript file | `00.Inbox/Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb.md` |
| Video file | `99.System/Attachments/Video/LEVEL UP with Custom Visuals： Power BI🔹HTML🔹Calculation Groups🔹Deneb-QXMMpabHPS4.webm` |
| Archived at | `99.System/InboxArchive/2026-08/` (pending) |
| Ingestion date | 2026-08-13 |
| Duration | 46:49 |
| Word count | ~3,400 (transcript) |
