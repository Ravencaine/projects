---
created: 2026-08-13
source: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
source_url: https://www.youtube.com/watch?v=QXMMpabHPS4
note_type: workflow
tags: [google-fonts, web-connector, html-visual, dynamic-text]
---

# Google Fonts API in Power BI

Load Google's 1,400+ web fonts into Power BI as a slicer-driven table, then drive an HTML visual via DAX.

## Prerequisites

- Google account (for the API key)
- Power BI Desktop with HTML custom visual installed (e.g. HTML Content by Daniel Marsh Patrick)

## Steps

### 1 — Get a Google Fonts Developer API Key

Visit [Google Fonts Developer API](https://developers.google.com/fonts/docs/developer_api), scroll to **Get a Key**, generate the key, and copy it.

### 2 — Build the URL with Your Key

```
https://www.googleapis.com/webfonts/v1/webfonts?key=YOUR_API_KEY
```

### 3 — Load via Web Connector

In Power BI: **Get Data → Web** → paste the URL → click **OK**.

### 4 — Trim to One Column

The response has many columns from the JSON payload. Only `items.family` (font family name) is needed. Remove all other columns.

### 5 — Rename

- Column: `items.family` → `Font Name`
- Table: → `Google Fonts`

### 6 — Use in DAX

```dax
Selected Font = SELECTEDVALUE('Google Fonts'[Font Name], "Roboto")
```

Now `Selected Font` returns whichever font the slicer picks; pass it to an HTML visual as `<span style="font-family: ...">`.

## Static Variant (No API Key)

You don't need the API for static text. Hardcode in the measure:

```dax
Hello World =
"<span style=""font-family: Roboto; font-size: 100px;"">Hello World</span>"
```

## Notes

- One call to the Google Fonts API returns the entire ~1,400 font catalogue — refresh is rarely needed.
- The DAX measure using the font must append `px` to the size value (e.g. `100px`).
- Beyond static text, this table can feed a `Calculation Group` filter so users can pick font + size + color from the Filter pane.

## Related

- [[dynamic-html-text-via-calculation-groups]] — the DAX / HTML pattern that consumes this font table
- [[deneb-custom-visual]] — alternative custom-visual route
