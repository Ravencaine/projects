---
created: 2026-08-10
updated: 2026-08-10
source: "Give Users Full Control Over KPI Scale with Dynamic Formatting"
source_url: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Give-Users-Full-Control-Over-KPI-Scale-with-Dynamic-Formatting/ba-p/5297206"
note_type: pattern
tags: [power-bi, pattern, dynamic-format, multi-currency, switch, disconnected-table]
---

# Multi-Currency via Dynamic Format + SWITCH

Extends the Dynamic Format String pattern to handle multi-currency reporting — switching currency symbols based on a user slicer selection, within a single measure.

## Purpose

Display monetary values in different currency symbols ($, €, £, etc.) based on a user selection — without creating separate measures per currency. Same measure works across all regions and currencies.

## Components

- Disconnected `Currency` dimension table (USD, EUR, GBP, etc.)
- `SELECTEDVALUE` measure to capture currency selection
- Base KPI measure (same as the scale pattern)
- `SWITCH` in Dynamic Format String for currency symbol swap

## Structure

**Currency table:**
```dax
Currency =
DATATABLE(
    "Currency Symbol", STRING,
    "Currency Code", STRING,
    {
        { "$",  "USD" },
        { "€",  "EUR" },
        { "£",  "GBP" },
        { "¥",  "JPY" }
    }
)
```

**Selected Currency measure:**
```dax
Selected Currency = SELECTEDVALUE ( 'Currency'[Currency Symbol] )
```

**Base measure:**
```dax
Total Revenue = SUM ( Financials[Revenue] )
```

**Dynamic Format String:**
```dax
SWITCH (
    [Selected Currency],
    "$",  "$#,##0,.00",
    "€",  "€#,##0,.00",
    "£",  "£#,##0,.00",
    "¥",  "¥#,##0,.00",
    "$#,##0,.00"  -- Default: USD
)
```

## Combining Scale + Currency

For full flexibility, combine the Scale table with the Currency table:

```dax
SWITCH (
    TRUE,
    [Selected Currency] = "$"  && [Selected Scale] = "Millions", "$#,##0,,.00",
    [Selected Currency] = "€"  && [Selected Scale] = "Millions", "€#,##0,,.00",
    "$#,##0,,.00"
)
```

Or layer two separate measures: one for scale (format string) and one for currency (format string), or use a single SWITCH with combined keys.

## Related

- [[Dynamic-KPI-Scale-Disconnected-Table-SWITCH]] — base pattern
- [[Dynamic-Format-String-Implementation]] — workflow
