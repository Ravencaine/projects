---
created: 2026-08-13
source: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
source_url: https://www.youtube.com/watch?v=QXMMpabHPS4
note_type: comparison
tags: [custom-visual, deneb, html-content, python-visual, r-visual, decision]
---

# Power BI Custom Visual Approaches

When the native Power BI visual set is not enough — KPI cards with context, dynamic fonts, custom charts — four practical routes exist. They differ on speed, interactivity, learning curve, and how likely Microsoft is to obsolete them.

## Summary

For **dashboards that must reach** end users in production today → **native visuals** first, **HTML Content** for what's not possible natively. Use **Deneb** for charts (heatmaps, hexbins, IBCS) that need interactivity. Avoid **Python/R visuals** unless data egress rules make Deneb infeasible.

## Native Visuals

### Pros
- Full Power BI feature parity: tooltips, drill-through, bookmarks, conditional formatting, mobile layout.
- Zero learning curve.
- Microsoft's roadmap applies — these get better over time.

### Cons
- Limited: cards can't natively show multi-element context (current + prior + delta).
- No custom typography — 26 native fonts.
- Themes are static per report.

## HTML Content (Daniel Marsh Patrick)

### Pros
- Total control: any HTML/CSS, including SVG icons and Google Fonts.
- Plays well with Calculation Groups — see [[dynamic-html-text-via-calculation-groups]].
- Lightweight (no Python runtime).

### Cons
- Cross-visual interaction is limited — HTML visuals don't trigger cross-filter by default.
- Need to know enough HTML/CSS to splice snippets (per Injae Park: "I don't know how to use CSS at all").
- The author labels it as "more effort than it's worth for business use" for color theming.

## Deneb

### Pros
- Full Vega/Vega-Lite declarative spec.
- Cross-visual interaction **works** — unlike Python/R visuals.
- Strong community template library.
- Open spec — Microsoft's roadmap doesn't make it obsolete.

### Cons
- Code-based editing (JSON).
- Learning curve for Vega/Vega-Lite (small language, but still a new mental model).
- Each visual still needs `Values` set before the editor opens.

## Python / R Visuals

### Pros
- Maximum flexibility — full pandas / matplotlib / ggplot2 ecosystem.
- Familiar to data scientists.

### Cons
- **Slow** for tens of thousands of rows.
- **No native cross-visual interaction** (doesn't respond to slicers/cross-filter).
- Requires a Python/R runtime on the rendering machine.
- Microsoft is investing more in Deneb than in Python/R for visual needs.

## Comparison Table

| Criterion | Native | HTML Content | Deneb | Python/R |
|-----------|--------|--------------|-------|----------|
| Speed | Fast | Fast | Fast–Medium | Slow |
| Cross-visual interaction | ✅ | Limited | ✅ | ❌ |
| Custom typography | ❌ (26 fonts) | ✅ | ✅ | ✅ |
| Custom layout / SVG icons | ❌ | ✅ | ✅ | ✅ |
| Learning curve | None | HTML basics | Vega JSON | Python or R |
| Roadmap risk | Lowest (Microsoft-owned) | High — native cards may gain multi-element layout | Low — open spec | Medium |
| Best for | All default reporting | KPI text, dynamic theming | Charts, IBCS, hexbins | Heaviest custom analytics |

## Roadmap Context (per Miguel Myers on the Power BI Guy podcast)

Microsoft has publicly committed to:

- **More native fonts** (currently 26) — would obsolete HTML-driven fonts.
- **Cards holding multiple elements** — would obsolete Calculation-Group-driven KPI context.
- **Dynamic themes via APIs in Power BI** — would obsolete HTML-driven theming.

Deneb is unlikely to be displaced. The HTML / Calculation-Group niche techniques fill gaps that are likely to be filled by native features in the next 12–18 months.

## When to Use

- **Native everywhere** unless you have an explicit gap.
- **HTML Content** for dynamic fonts/themes/icons — knowing they're a stopgap.
- **Deneb** for advanced charts where interactivity is required and templates exist.
- **Python/R visuals** for analytics egress rules (e.g. send data to an external Python sandbox) — never for chart rendering.

## Related

- [[deneb-custom-visual]] — Deneb specifics
- [[dynamic-html-text-via-calculation-groups]] — HTML Content + Calculation Groups pattern
- [[kpi-context-cards-with-calculation-groups]] — native-card workaround
- [[dynamic-color-themes-via-html-rgb]] — dynamic theming workaround
