---
created: 2026-08-10
updated: 2026-08-10
source: "Give Users Full Control Over KPI Scale with Dynamic Formatting"
source_url: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Give-Users-Full-Control-Over-KPI-Scale-with-Dynamic-Formatting/ba-p/5297206"
note_type: pattern
tags: [power-bi, pattern, dynamic-format, disconnected-table, switch, dax]
---

# Dynamic KPI Scale via Disconnected Table + SWITCH

A single KPI measure that toggles between Actuals, Thousands, Millions, and Billions based on a slicer selection — using a disconnected dimension table and Dynamic Format Strings.

## Purpose

Give report users full interactive control over number scale without duplicating measures. One measure handles all scales; the format changes based on a slicer selection. Eliminates "Sales (M)" vs "Sales (k)" measure proliferation.

## Components

- Disconnected dimension table (`Scale`) with scale options
- `SELECTEDVALUE` measure to capture slicer selection
- Base KPI measure — returns the raw, unscaled value
- `SWITCH` inside the Dynamic Format String to return the correct format string
- No DAX division for scaling — all scaling handled by the format string

## Structure

**Scale table (DAX):**
```dax
Scale =
DATATABLE(
    "Scale Name", STRING,
    "Scale ID", INTEGER,
    {
        { "Actuals", 1 },
        { "Thousands", 2 },
        { "Millions", 3 },
        { "Billions", 4 }
    }
)
```
Sort `Scale Name` by `Scale ID` so options appear in logical order (smallest to largest).

**Selected Scale measure:**
```dax
Selected Scale = SELECTEDVALUE ( 'Scale'[Scale Name] )
```

**Base KPI measure:**
```dax
Total Profit = SUM ( Financials[Profit] )
```

**Dynamic Format String (via Measure Tools → Format → Dynamic):**
```dax
SWITCH (
    [Selected Scale],
    "Thousands", "$#,##0,.00",
    "Millions",  "$#,##0,,.00",
    "Billions",  "$#,##0,,,.00",
    "Actuals",   "$#,##0.00",
    "$#,##0,,.00"  -- Default fallback (Millions)
)
```

**Format string comma placement:**
| Scale | Format String | Effect |
|-------|--------------|--------|
| Actuals | `$#,##0.00` | No scaling |
| Thousands | `$#,##0,.00` | Divide by 1,000 |
| Millions | `$#,##0,,.00` | Divide by 1,000,000 |
| Billions | `$#,##0,,,.00` | Divide by 1,000,000,000 |

## Related

- [[Dynamic-Format-String-Implementation]] — workflow
- [[Dynamic-Format-vs-Fixed-Display-Units]] — comparison
- [[Multi-Currency-Dynamic-Format-SWITCH]] — pattern (bonus use case)
- [[Keep-Base-Measure-Whole]] — atomic (key principle)
