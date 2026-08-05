---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "matrix", "hierarchy", "visual", "drill-down"]
note_type: pattern

---

# Custom Matrix Hierarchy in DAX

Controlling row hierarchy expansion in Power BI Matrix visuals with DAX.

## Purpose

Standard matrix hierarchies expand all levels at once. Custom logic lets you control which levels expand based on data.

## Pattern

```dax
Matrix Level :=
SWITCH(
    TRUE(),
    ISINSCOPE( 'Hierarchy'[L1] ), 1,
    ISINSCOPE( 'Hierarchy'[L2] ), 2,
    ISINSCOPE( 'Hierarchy'[L3] ), 3,
    0
)
```

## Notes

- `ISINSCOPE()` detects which hierarchy level is currently visible
- Use to show different measures at different hierarchy levels

## Related

- [[disconnected-tables-in-dax]]
- [[dynamic-text-titles-in-power-bi]]
