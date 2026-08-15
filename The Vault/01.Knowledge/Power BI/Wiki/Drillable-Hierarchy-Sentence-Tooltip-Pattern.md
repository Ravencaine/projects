---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into tooltip options in Power BI visuals (Generally Available).md"
note_type: pattern
tags: [power-bi, tooltip, sentence-format, isinscope, switch, selectedvalue, drill, pattern]
---

# Drillable Hierarchy Sentence Tooltip Pattern

> **Type:** pattern
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-06

## Problem

A visual with drill-down hierarchy (e.g., Segment → Product) shows different levels depending on what the user has expanded. The sentence tooltip must read correctly at every drill level — segment-only, product-only, or both combined.

## Solution

Add a measure to the **Tooltip field well** that uses `ISINSCOPE` + `SWITCH` + `SELECTEDVALUE` to resolve the current drill level. Reference that measure in the sentence template.

## DAX Pattern

```dax
Segment or Product Drill =
SWITCH(
    TRUE(),
    -- Both Segment AND Product are in scope (most granular level)
    ISINSCOPE(Financials[Segment]) && ISINSCOPE(Financials[Product]),
        SELECTEDVALUE(Financials[Segment]) & " (Segment) "
        & SELECTEDVALUE(Financials[Product]) & " (Product)",
    -- Only Segment is in scope
    ISINSCOPE(Financials[Segment]),
        SELECTEDVALUE(Financials[Segment]),
    -- Only Product is in scope
    ISINSCOPE(Financials[Product]),
        SELECTEDVALUE(Financials[Product]),
    -- Nothing in scope (fallback)
    BLANK()
)
```

## How It Works

| Drill State | ISINSCOPE Result | Output |
|-------------|-----------------|--------|
| Segment only | Segment = TRUE, Product = FALSE | Segment value only |
| Product only | Segment = FALSE, Product = TRUE | Product value only |
| Segment + Product | Both TRUE | "Segment (Segment) Product (Product)" |
| Neither | Both FALSE | BLANK() |

## Usage

1. Add the measure to the **Tooltip field well** of the visual
2. Turn ON **Sentence format** in the visual's tooltip options
3. Reference the measure in the template:

```
{Segment or Product Drill} has {Sales} in sales, a change of {Sales YoY} ({Sales YoY %}) since last year.
```

**At Segment level:** "Enterprise has $5.2M in sales, a change of $1.1M (27%) since last year."
**At Product level:** "Widget Pro has $800K in sales, a change of $120K (18%) since last year."
**At combined level:** "Enterprise (Segment) Widget Pro (Product) has $300K in sales, a change of $50K (20%) since last year."

## Key Functions

| Function | Purpose |
|----------|---------|
| `ISINSCOPE(column)` | TRUE when that column is the active drill level |
| `SWITCH(TRUE(), ...)` | Branch on which ISINSCOPE conditions are true |
| `SELECTEDVALUE(column)` | Returns the value of the column in the current context |

## See Also

- [[Source-Tooltip-Options-Generally-Available]] — source article
- [[Sentence-Format-Template-Pattern]] — sentence format template syntax
- [[ISINSCOPE-Pattern]] — ISINSCOPE as general-purpose drill detection
