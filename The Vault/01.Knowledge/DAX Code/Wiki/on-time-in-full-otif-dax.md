---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, supply-chain, logistics]
---

# On Time In Full (OTIF)

## Purpose

OTIF is a supply-chain logistics KPI that measures **order fulfillment quality**
on two dimensions simultaneously:

1. **On Time**: delivered by (or before) the customer's promised date
2. **In Full**: all ordered line items were shipped at the requested quantities

```
OTIF % = (Orders On Time AND In Full) / Total Orders × 100
```

An order counts toward OTIF **only if both conditions are met simultaneously**.
A late order with correct quantities scores 0; an early order with partial
shipments scores 0.

## Formula

```dax
OTIF =
    VAR __Table =
        ADDCOLUMNS(
            SELECTCOLUMNS(
                'OTIF',
                "__Order",      [Order],
                "__Ordered",    [Ordered],
                "__Shipped",    [Shipped],
                "__DueDate",    [CustomerDueDate],
                "__DeliverDate",[DeliveredDate]
            ),
            "__OTIF",
                IF(
                    [__Ordered] = [__Shipped] && [__DeliverDate] <= [__DueDate],
                    1,
                    0
                )
        )
    VAR __Orders =
        GROUPBY(
            __Table,
            [__Order],
            "__Count", COUNTX( CURRENTGROUP(), [__Order] ),
            "__OTIF",  SUMX( CURRENTGROUP(),    [__OTIF] )
        )
    VAR __OnTime = COUNTROWS( FILTER( __Orders, [__Count] = [__OTIF] ) )
    VAR __All    = COUNTROWS( __Orders )
    VAR __Result = DIVIDE( __OnTime, __All, 0 )
    RETURN __Result
```

## Components

| Component | Role |
|-----------|------|
| `SELECTCOLUMNS( 'OTIF', ... )` | Project-only required columns from the fact table — a **memory optimization**<br/>that reduces the working set before heavy operations |
| `ADDCOLUMNS( ..., "__OTIF", IF(...) )` | Per line: `1` if the line was shipped in full **and** delivered on/before due date |
| `GROUPBY( __Table, [__Order], ... )` | Roll up from **line granularity** to **order granularity**;<br/>aggregate both the count of lines per order and the OTIF flag sum |
| `FILTER( __Orders, [__Count] = [__OTIF] )` | Orders where *all* lines scored `1` — i.e., complete OTIF compliance |
| `DIVIDE( __OnTime, __All, 0 )` | Final percentage |

## Data Model

The OTIF table is at the **order-line granularity**:

| Column | Description |
|--------|-------------|
| `Order` | Order ID (groups lines into a single order) |
| `Plant` | Warehouse/fulfillment center |
| `Shipment` | Shipment ID (one order may need multiple shipments) |
| `Line` | Line item number within the order |
| `Ordered` | Quantity requested |
| `Shipped` | Quantity actually shipped |
| `CustomerDueDate` | Date the customer requested delivery |
| `DeliveredDate` | Actual delivery date |
| `Customer` | Customer name |
| `Segment` | Product category |

## How the Measure Works

```
Line-level check (ADDCOLUMNS):
  If Ordered == Shipped  AND  DeliveredDate <= CustomerDueDate
  → __OTIF = 1  (passes both On Time AND In Full)
  → __OTIF = 0  (fails one or both conditions)

Order-level rollup (GROUPBY):
  __Count = total lines in the order
  __OTIF  = sum of passing lines

  Order passes OTIF only when __Count == __OTIF
  (every line in the order must pass)
```

## Notes

- **Why SELECTCOLUMNS?** Operational fact tables can have 50–100+ columns.
  Pulling only the 5 required columns dramatically reduces memory pressure
  inside measures that iterate over large tables.
- **GROUPBY** returns one row per group with aggregator expressions evaluated
  via `COUNTX( CURRENTGROUP(), ... )` and `SUMX( CURRENTGROUP(), ... )`.
  It is the correct iterator-based rollup for grouped aggregations in the
  No-CALCULATE style.
- OTIF can be sliced by `Plant`, `Customer`, `Segment`, or `DeliveredDate`
  to surface where fulfillment failures concentrate.

## Related

- [[earned-value-management-evm-dax]] — project delivery variance
- [[overall-equipment-effectiveness-oee-dax]] — manufacturing effectiveness
- [[project-burndown-chart-dax]] — project progress tracking
