---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [new-slicer, market-watch, field-parameters, image-slicer, stock-data]
related: [New-Power-BI-Slicer-Features, Field-Parameters, Time-Period-Slicers]
---

# Market Watch Dashboard

Builds a financial dashboard that lets users select assets (stocks, crypto, currencies) and time periods to view dynamic price charts.

## Components

| Component | Type | Purpose |
|-----------|------|---------|
| Asset slicer | New Slicer | Image + ticker + description per asset |
| Period slicer | New Slicer | Time range selection (1W, 1M, 6M, 1Y) |
| Area chart | Native | Price over time |
| KPI cards | Card + Shapes | Current price, change, volume |
| Field Parameter | Parameter | Switch between Price, Open, Volume |

## Asset Slicer Setup

1. Create a `Key` table (Enter Data):
   | Abbr | Full Name | Description | Image |
   |------|-----------|-------------|-------|
   | AAPL | Apple Inc. | Tech stock | `https://logo.clearbit.com/apple.com` |
   | MSFT | Microsoft Corp. | Software | `https://logo.clearbit.com/microsoft.com` |

2. Set `Image` column → **Data category → Image URL** in model view.
3. Create a new **Slicer** → add `Abbr` to Field, `Image` to Image well.
4. Format: Image fit → Normal, Position → Left, Image area → 10%.
5. Add `Description` measure to Callout values → Label:
   ```dax
   Description = SELECTEDVALUE('Key'[Full Name]) & " - " & SELECTEDVALUE('Key'[Description])
   ```

## Time Period Slicer

See: [[Time-Period-Slicers]]

## Field Parameter (Switch Metrics)

See: [[Field-Parameters]]

## Notes

- Bittar's Market Watch dashboard combines all three patterns — new slicer for assets, period slicer for time range, Field Parameters for metric switching.
- The data source is Investing.com CSV exports, shaped in Power Query.
- The `Description` measure uses `SELECTEDVALUE` to pull the full name and description for the currently selected asset.
- Download the PBIX from the article's Google Drive link.

## Related

- [[New-Power-BI-Slicer-Features]] — new slicer capabilities
- [[Time-Period-Slicers]] — dynamic chart range
- [[Field-Parameters]] — metric switching
- [[Import-Stock-Data]] — Power Query workflow
