---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Format Strings in Power BI.md"
source_url: https://databear.com/dynamic-format-strings-in-power-bi/
note_type: source
tags: [power-bi, dynamic-format-strings, dax, measure-formatting, annamarie-van-wyk, boniface-muchendu]
---

# Dynamic Format Strings in Power BI (Data Bear / Annamarie Van Wyk)

> **Type:** article
> **Author:** Annamarie Van Wyk via Boniface Muchendu (Data Bear)
> **Published:** 2024-03-02
> **URL:** https://databear.com/dynamic-format-strings-in-power-bi/
> **Routed to:** Power BI

## Summary

Dynamic format strings allow one measure to return different number formats (currency, abbreviation, decimal places) based on conditions or context. Enable via Preview Features in Power BI Desktop; select Dynamic from the Format dropdown; write a DAX expression that returns a valid format string. Combined with SWITCH for per-category formatting.

## Key Claims

### Setup
- Enable feature via Power BI Desktop Preview Features (still in preview as of Nov 2023)
- Select measure → Measure Tools ribbon → Format list box → choose Dynamic
- A second expression box appears alongside the DAX formula bar; switch to Format via dropdown
- Format expression must return a valid DAX format string

### Use Cases
- Currency symbol changes based on selected region
- Abbreviated large numbers (K, M, B) with appropriate decimal places
- Different decimal precision per category or measure context

### Implementation Pattern
- DAX SWITCH commonly used to select format string based on conditions
- Example: `SWITCH(TRUE(), [Amount] >= 1000000, "$#,##0.0,,M", [Amount] >= 1000, "$#,##0,.0K", "$#,##0")`

## References
- [Microsoft Docs: Dynamic Format Strings](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-dynamic-format-strings)

## Metadata

| Field | Value |
|-------|-------|
| Source file | Dynamic Format Strings in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
