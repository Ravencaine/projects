---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "slicer", "filter", "disconnected", "and"]
note_type: pattern

---

# Inverse AND Slicer Pattern

Implementing a slicer where selecting multiple values shows items that match ALL selected filters (AND logic), rather than the default OR behavior.

## Problem

Default Power BI slicers use OR logic — selecting "Red" and "Blue" shows Red OR Blue. For AND logic (must be both Red AND Blue), use disconnected tables with INTERSECT.

## Pattern

```dax
Sales AND Filter :=
VAR __SelectedColors = VALUES( 'Color Selector'[Color] )
VAR __FilteredProducts =
    FILTER(
        'Products',
        CONTAINSSTRING(
            CONCATENATEX( __SelectedColors, [Color], ", " ),
            'Products'[Color]
        )
    )
RETURN
SUMX(
    INTERSECT(
        ALL( 'Products' ),
        __FilteredProducts
    ),
    [Sales Amount]
)
```

## Simpler Alternative

```dax
Sales AND Filter :=
SUMX(
    'Products',
    VAR __AllSelected = CONCATENATEX( 'Color Selector', [Color], "," )
    VAR __ProductColors = 'Products'[Color]
    VAR __Match =
        SUMX(
            'Color Selector',
            IF( CONTAINSSTRING( __ProductColors, [Color] ), 1, 0 )
        ) = COUNTROWS( 'Color Selector' )
    RETURN
    IF( __Match, [Sales Amount], 0 )
)
```

## Notes

- AND slicers require disconnected tables and custom DAX
- Performance depends on the number of selected values

## Related

- [[disconnected-tables-in-dax]]
- [[cross-fact-treatas-virtual-relationships]]
