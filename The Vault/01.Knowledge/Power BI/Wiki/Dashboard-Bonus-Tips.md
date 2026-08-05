---
created: 2026-08-05
source: Power BI Dashboards Decision-Making (Boniface Muchendu)
note_type: atomic
tags: [power-bi, dashboard, q&a, mobile-layout, web-tile, bonus]
---

# Dashboard Bonus Tips

Three bonus dashboard features from the article: Q&A natural-language querying, dedicated mobile layouts, and web page tiles for live external content.

## 1 — Q&A Natural Language

Power BI's **Q&A visual** on a dashboard lets users type questions in plain English ("what were sales last month by region?") and get instant answers with auto-generated visuals.

- Add the Q&A visual to any dashboard
- Users do not need to know DAX or data model structure
- Best placed on analyst or self-service dashboards — not executive one-pagers
- Requires the semantic model to have appropriate relationships and column descriptions for Q&A to interpret correctly

## 2 — Mobile Layout

Power BI Desktop allows dedicated mobile layouts (View → Mobile Layout) that are separate from the default canvas. Dashboards behave differently on mobile:

- Test responsiveness explicitly using the mobile layout view
- Consider removing complex charts and keeping only KPIs, cards, and sparklines
- Alternatively, use the **Auto-fit** page setting and trust Power BI's responsive behaviour
- Dedicated mobile layouts let you reorder and resize visuals specifically for phone/tablet

## 3 — Web Page Tile

The **Web page** tile type embeds a live URL inside a dashboard tile — useful for:

- Industry news or market trackers embedded on executive dashboards
- Live currency or stock price feeds
- External KPI sources that don't live in the Power BI model

**Limitation:** Some external sites block iframe embedding via `X-Frame-Options`. Test the target URL before relying on it.

## Related

- [[Executive-One-Pager-Dashboard-Design]]
- [[KPI-Alert-Setup-Power-BI]]
- [[Dashboard-as-App-Landing-Page]]
