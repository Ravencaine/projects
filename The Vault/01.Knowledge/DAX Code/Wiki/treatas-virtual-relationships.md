---
created: 2026-08-01
updated: 2026-08-02
source: "TREATAS in DAX - Connecting Unrelated Tables Like Magic.md"
note_type: atomic
tags: [dax, treatas, virtual-relationships, CALCULATE, VALUES, intermediate]
---

# TREATAS: Virtual Relationships in DAX

TREATAS applies filter values from one table onto another as if a relationship existed — no physical join required.

## The Problem It Solves

Physical relationships fail when:
- Both sides contain duplicate keys
- Columns have different data types
- Security/data volume prevents physical joins
- You need temporary mapping for scenarios or What-If analysis

Without TREATAS: disconnected islands in the model, no filter propagation.

## Syntax

```c
TREATAS ( <table_expression>, <target_column1> [, <target_column2>, ...] )
```

Plain English: "Take this column of values and treat it as a filter on that column over there."

## Key Pattern: TREATAS + VALUES

```c
Total Campaign Sales =
CALCULATE(
    [Total Sales],
    TREATAS(
        VALUES(Campaign[PromoCode]),
        Sales[PromoCode]
    )
)
```

**Step by step:**
1. `VALUES(Campaign[PromoCode])` → list of visible promo codes in current filter
2. `TREATAS(...)` → applies those codes as a filter on `Sales[PromoCode]`
3. `CALCULATE` → re-evaluates `[Total Sales]` inside that virtual link

## Marketing Attribution Example

```c
Sales by Campaign Type =
CALCULATE(
    [Total Sales],
    TREATAS(
        VALUES(Campaign[CampaignType]),
        Sales[CampaignType]
    )
)
```

Works even when both tables have duplicate codes — virtual relationship bypasses the unique-key requirement.

## Budget Alignment Example

Budget table had fiscal period as text (`"2025-Q3"`), Sales table used numeric quarter:

```c
Sales vs Budget =
CALCULATE(
    [Total Sales],
    TREATAS(
        VALUES(Budget[FiscalPeriod]),
        Sales[FiscalPeriod]
    )
)
```

No transformation layer needed.

## Ad Spend Attribution

Daily spend file with no common key → linked to Sales via derived "WeekStart" column using TREATAS:

```c
Spend vs Sales =
CALCULATE(
    [Total Sales],
    TREATAS(
        VALUES(Spend[WeekStart]),
        Sales[Date]
    )
)
```

Virtual join by date range without physical duplication.

## Virtual vs Physical Relationships

| Aspect | Physical | Virtual (TREATAS) |
|--------|---------|-------------------|
| Created in | Model view | CALCULATE measure |
| Persists | Always | Only during measure eval |
| Performance | Optimized by VertiPaq | Recreated each evaluation |
| Unique keys | Required | Not required |
| Direction | Fixed | Flexible |

## Related

- [[treatas-uselationship-crossfilter]] — choosing TREATAS vs alternatives
- [[treatas-performance-pitfalls]] — performance cost and debugging
- [[treatas-dynamic-segments-whatif]] — TREATAS for dynamic segment selectors
