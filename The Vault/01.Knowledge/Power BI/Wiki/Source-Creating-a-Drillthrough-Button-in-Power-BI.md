---
created: 2026-08-09
updated: 2026-08-09
source: "Creating a Drillthrough Button in Power BI.md"
source_url: https://databear.com/create-a-drillthrough-button-in-power-bi/
note_type: source
tags: [power-bi, drillthrough, navigation, button, databear, boniface-muchendu]
---

# Creating a Drillthrough Button in Power BI

Create a drillthrough page and button in Power BI to let users jump from a summary page to a detail page by selecting a visual value.

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2023-06-03
> **URL:** https://databear.com/create-a-drillthrough-button-in-power-bi/
> **Routed to:** Power BI

## Summary

Two methods for drillthrough navigation in Power BI: right-click on a visual, or a custom drillthrough button. A drillthrough page is created first, hidden from the page list, named with a `DT` prefix, and populated with detail visuals. A button is then created with action type `Drillthrough` pointing to that page. The back button is auto-generated when drillthrough dimensions are added.

## Key Claims

- Drillthrough pages must be hidden so users access them only via the drillthrough action
- The `DT` prefix on the page name signals the drillthrough dimension being used
- Adding fields to the drillthrough filters pane auto-creates a back button
- Drillthrough buttons are preferable to right-click because they are easier to discover and can be styled

## Notable Details

- Image attachments reference `99.System/Attachments/` (KPI matrix screenshot, conditional formatting screenshot)
- The Zebra BI Sales dashboard is used as the example
- The landing page value (−30) carries into the drillthrough page where it is broken down by salesperson

## Extracted Notes

Links to notes derived from this source:

- [[Drillthrough-Page-Button-Setup]] — `workflow` — end-to-end setup of drillthrough page and button
- [[Drillthrough-Page-DT-Prefix]] — `atomic` — naming convention for drillthrough pages

## Metadata

| Field | Value |
|-------|-------|
| Source file | Creating a Drillthrough Button in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~350 |
