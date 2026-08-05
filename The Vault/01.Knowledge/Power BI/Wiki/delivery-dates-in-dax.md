---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "operations", "delivery", "logistics", "lead-time"]
note_type: pattern

---

# Delivery Dates in DAX

Calculating expected and actual delivery dates for orders.

## Pattern

```dax
Expected Delivery :=
VAR __ShipDate = [OrderDate]
VAR __LeadTime = LOOKUPVALUE( 'ShippingRates'[LeadTime], 'ShippingRates'[Region], [Region] )
RETURN
__ShipDate + __LeadTime

Is On Time :=
VAR __Expected = [Expected Delivery]
VAR __Actual = [DeliveryDate]
RETURN
__Actual <= __Expected
```

## Notes

- Use a shipping rates table keyed by region for lead time lookup
- Combine with [[on-time-in-full-otif-dax]] for complete logistics KPIs

## Related

- [[order-cycle-time-oct-dax]]
- [[on-time-in-full-otif-dax]]
