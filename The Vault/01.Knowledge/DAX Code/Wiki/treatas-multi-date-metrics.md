---
created: 2026-07-31
updated: 2026-08-02
source: "🧠 \"Which Date Is It, Anyway\" — Making Peace with TREATAS in a Multi-Date World.md"
note_type: pattern
tags: [dax, treatas, multi-date, kpi, date-slicer]
---

# Multi-Date Metrics via TREATAS

A single Date table slicer drives multiple KPI measures — each targeting a different date column in the same fact table — using TREATAS to create per-measure virtual relationships.

## Purpose

Finance and Supply Chain fact tables often contain multiple date columns (OrderDate, ShipDate, DueDate, PaymentDate). Standard Power BI models enforce one active relationship per table pair, making it hard to build a single visual that shows Orders by Order Date, Shipments by Ship Date, Overdue by Due Date, and Cash Received by Payment Date simultaneously.

TREATAS solves this by letting each measure define its own virtual relationship at evaluation time, all sharing the same Date dimension.

## Components

- `Date` dimension table — single, shared across all measures
- Fact table with multiple date columns (e.g., CustomerTransactions)
- `TREATAS()` — creates per-measure virtual relationship
- `CALCULATE()` — wraps the aggregation and applies the TREATAS filter
- `VALUES()` — returns the active filter context from the Date slicer

## Structure

```dax
<Measure Name> by Date =
CALCULATE(
    <aggregation on fact column>,
    TREATAS(
        VALUES('Date'[Date]),
        <FactTable>[<TargetDateColumn>]
    )
)
```

## Example

Fact table `CustomerTransactions` has columns: Quantity, OutstandingAmount, PaidAmount across OrderDate, ShipDate, DueDate, PaymentDate.

**Shipped Qty by Date:**
```dax
Shipped Qty by Date =
CALCULATE(
    SUM(CustomerTransactions[Quantity]),
    TREATAS(VALUES('Date'[Date]), CustomerTransactions[ShipDate])
)
```

**Overdue Payments by Date:**
```dax
Overdue Payments by Date =
CALCULATE(
    SUM(CustomerTransactions[OutstandingAmount]),
    TREATAS(VALUES('Date'[Date]), CustomerTransactions[DueDate])
)
```

**Cash Received by Date:**
```dax
Cash Received by Date =
CALCULATE(
    SUM(CustomerTransactions[PaidAmount]),
    TREATAS(VALUES('Date'[Date]), CustomerTransactions[PaymentDate])
)
```

Place all three in the same visual with a Date table slicer — each measure slices by the date column it targets, all driven by the shared slicer.

## Variations

**With intermediate calculated columns** (when fact dates need alignment):
```dax
-- Calculated column on CustomerTransactions:
ShipDateKey = TRUNC(CustomerTransactions[ShipDate])

-- Measure:
Shipped Qty by Date =
CALCULATE(
    SUM(CustomerTransactions[Quantity]),
    TREATAS(VALUES('Date'[Date]), CustomerTransactions[ShipDateKey])
)
```

**With FILTER for conditional date targeting:**
```dax
Measure =
CALCULATE(
    SUM(FactTable[Amount]),
    TREATAS(
        VALUES('Date'[Date]),
        FILTER(ALL(FactTable), FactTable[Status] = "Shipped")[Date]
    )
)
```

## Related

- [[cross-fact-treatas-virtual-relationships]] — `function` — the core mechanism
- [[treatas-vs-userelationship-comparison]] — `comparison` — why TREATAS over inactive relationships
- [[treatas-strictness-gotcha]] — `gotcha` — alignment requirements and blank handling
