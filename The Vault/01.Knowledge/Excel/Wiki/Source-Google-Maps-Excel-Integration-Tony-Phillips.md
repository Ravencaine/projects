---
created: 2026-08-10
updated: 2026-08-14
source: "Google Maps took my Excel spreadsheet to the next level with this little-known tool"
source_url: "https://www.howtogeek.com/microsoft-excel-google-my-maps/"
download_file: 99.System/Attachments/Excel/World-Cup-Stadiums.xlsx
note_type: source
tags: [excel, source, google-my-maps, integration, howtogeek, tony-phillips]
---

# Google Maps + Excel Integration (Tony Phillips / How-To Geek)

Source: How-To Geek. Published 2026-07-29. Author: Tony Phillips.

> **Type:** tutorial
> **Author:** Tony Phillips
> **Published:** 2026-07-29
> **URL:** https://www.howtogeek.com/microsoft-excel-google-my-maps/
> **Routed to:** Excel

## Summary

Step-by-step walkthrough of combining Excel location data with Google My Maps to create an interactive, shareable map. Uses the 2026 FIFA World Cup stadiums as the worked example. Covers data preparation, import, pin customization, multi-layer maps, in-map editing, and sharing.

## Key Claims

### Data Preparation Rules
- One sheet per map layer
- Distinct column headers required (Google reads them as field names)
- Minimum: city + country; full address preferred
- Save as `.xlsx` — legacy `.xls` not supported

### Import Process
- Google My Maps imports the first sheet of the workbook only
- Step 1: check boxes for all location columns (Address, City, State, Country)
- Step 2: select the single column for marker naming
- Step 3: Finish — pins placed automatically via geocoding

### Customization
- Paint bucket icon → change all pins at once (colour + shape)
- Individual pin → Edit → custom colour/icon per category
- Info card: add photos, videos, directions
- Terrain base map for topography visibility
- Custom labels disabled by default (conflicts with Google labels)

### Layers
- One Excel file = one layer
- Layers are independent — toggle on/off individually
- File names become layer names

### Editing
- Local Excel changes do NOT sync automatically
- In-map editing via data table (three dots → Open data table)
- "Reimport and merge" to update map from revised Excel file

### Sharing
- Share settings: Anyone with link (view), or Drive-based access control
- Public discoverability toggle available

## Notable Details

- Download: [[99.System/Attachments/Excel/World-Cup-Stadiums.xlsx]] (World Cup 2026 stadiums workbook — Dropbox origin, now archived locally)
- Brief mention of Excel's 3D Maps as an alternative (same-source article link, not extracted)
- Article is practical and example-driven; no code or advanced configuration

## Extracted Notes

Links to notes derived from this source:

- [[Excel-to-Google-My-Maps-Integration]] — `workflow` — full step-by-step integration guide

## Metadata

| Field | Value |
|-------|-------|
| Source file | [[99.System/InboxArchive/2026-08/Google Maps took my Excel spreadsheet to the next level with this little-known tool.md]] |
| Download | [[99.System/Attachments/Excel/World-Cup-Stadiums.xlsx]] |
| Ingestion date | 2026-08-10 |
| Word count | ~800 |
