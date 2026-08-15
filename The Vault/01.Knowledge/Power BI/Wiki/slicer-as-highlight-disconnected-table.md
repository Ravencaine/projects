---
created: 2026-08-11
updated: 2026-08-11
source: "5-Power-BI-Slicer-Tricks-Goodly-Transcript.md"
note_type: pattern
tags: [power-bi, slicer, disconnected-table, conditional-formatting]
---

# Slicer as Highlight — Disconnected Table + Conditional Formatting

A slicer that highlights rows in a table without filtering them out — using a disconnected table + `SELECTEDVALUE` + conditional formatting.

## Why

Default slicers filter. Sometimes you want to highlight matching rows and still show the full context (non-matching rows visible but dimmed).

## Pattern

### Step 1: Create disconnected table

```m
// New blank query
= DISTINCT('Products'[ProductName])
// Or: DISTINCT(SELECTCOLUMNS('Products', "ProductName", 'Products'[ProductName]))
```

This table has no relationships to any other table.

### Step 2: Use it in a slicer

Replace the slicer field with the disconnected table column.

### Step 3: Write a highlight measure

```dax
Highlight :=
VAR Check = COUNTROWS(
    FILTER(
        'Products Disconnected',
        'Products Disconnected'[ProductName] IN VALUES('Products Disconnected'[ProductName])
    )
)
RETURN
    IF(Check >= 1, 1, BLANK())
```

Or more directly:
```dax
Highlight :=
VAR Check = COUNTROWS(
    FILTER(
        'Products',
        'Products'[ProductName] IN VALUES('Products Disconnected'[ProductName])
    )
)
RETURN
    IF(Check >= 1, 1, BLANK())
```

### Step 4: Apply conditional formatting

On the table visual → Format → Cell elements → select the measure column → Background color → FX → Field value → use the Highlight measure. Apply to each column via the same measure.

## Result

Selected products are highlighted (orange background); unselected products remain visible but dimmed.

## Key Rule

The disconnected table must not have any relationships — that is what prevents filtering and enables highlight-only behavior.

## Related

- [[slicer-default-selection-current-period]] — current period slicer
- [[slicer-apply-all-clear-all-buttons]] — apply/clear buttons
- [[disconnected-table-slicer-pattern]] — disconnected table pattern note
