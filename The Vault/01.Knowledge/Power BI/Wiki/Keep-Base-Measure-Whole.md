---
created: 2026-08-10
updated: 2026-08-10
source: "Give Users Full Control Over KPI Scale with Dynamic Formatting"
source_url: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Give-Users-Full-Control-Over-KPI-Scale-with-Dynamic-Formatting/ba-p/5297206"
note_type: atomic
tags: [power-bi, atomic, dynamic-format, measure-design, dax]
---

# Keep Base Measure Whole — Don't Scale in DAX

The base KPI measure should return the full, unscaled numeric value. All scaling is handled by the Dynamic Format String, not by dividing in DAX.

## Definition

A "whole" measure is one that returns the raw aggregate (SUM, SUMX, etc.) without any division by 1000, 1,000,000, or any other scale factor. The format string is responsible for display scaling.

## Key Points

- Scaling in DAX (`/1000`, `/1000000`) changes the underlying calculation — not just the display
- When the calculation is scaled, every visual using that measure shows the same scaled value — you cannot get the original back
- Format string scaling is purely cosmetic — the raw value stays in the model for cross-visual consistency
- `SUM(Financials[Profit])` is whole; `SUM(Financials[Profit])/1000` is not

## Why It Matters

| Approach | Calculation | Format String | Actual Value |
|----------|-------------|---------------|--------------|
| Whole + Format | `SUM(Financials[Profit])` | `$#,##0,,.00` (Millions) | Displayed as Millions |
| Scaled in DAX | `SUM(Financials[Profit])/1000000` | `$#,##0.00` (Actuals) | Both show Millions — no way to show Actuals |

With the scaled-in-DAX approach, you cannot build a visual that shows Actuals from the same measure. You need a duplicate measure ("Profit Actual" + "Profit M"), creating technical debt.

With the whole + format approach, a single measure handles every scale via slicer.

## Related

- [[Dynamic-KPI-Scale-Disconnected-Table-SWITCH]] — pattern
- [[Dynamic-Format-String-Implementation]] — workflow
- [[Dynamic-Format-vs-Fixed-Display-Units]] — comparison
