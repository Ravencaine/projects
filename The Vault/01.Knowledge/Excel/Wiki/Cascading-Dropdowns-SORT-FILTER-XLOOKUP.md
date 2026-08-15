---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Drop-Down Lists in Excel • My Online Training Hub"
note_type: pattern
tags: [excel, dropdown, data-validation, cascading, dependent-dropdown, sort, filter, xlookup, spill, dynamic-arrays]
see_also: [Dependent-Dropdown-via-FILTER-UNIQUE-SORT]
---

# Cascading Dropdowns with SORT + FILTER + XLOOKUP

Cascading (dependent) dropdowns show different sub-options based on the parent selection. Built with: SORT + FILTER to generate the filtered list, then XLOOKUP to expose the spill range to Data Validation.

## Architecture

```
Category cell (D6)  ──XLOOKUP──▶  Spill range  ──▶  Product dropdown source
       │
       └── drives FILTER(product_table, Category = D6)
```

## Setup Steps

**1. Build a lookup table** with Category and Product columns.

**2. Create the product list formula** in a helper cell:
```
=SORT(FILTER(ProductsTbl[Product], ProductsTbl[Category]=D6))
```

**3. Expose via XLOOKUP:** XLOOKUP returns the spill range for the DV source:
```
=XLOOKUP(D6, CategoryList, ProductList)
```
Where `ProductList` is a named range pointing to the SORT(FILTER(...)) formula.

**4. Data Validation source** on the product cell references the XLOOKUP cell with `#`:
```
=D6#
```

## How Each Part Works

| Component | Role |
|----------|------|
| `FILTER(ProductsTbl[Product], Category=D6)` | Returns only products for the selected category |
| `SORT(...)` | Alphabetically sorted list |
| `XLOOKUP(D6, CategoryList, ProductList)` | Looks up the SORT(FILTER) result for the selected category |
| `D6#` (spill reference) | Passes the spilled result to DV as the source list |

## Result

- Select Electronics → dropdown shows only electronics products
- Select Furniture → dropdown shows only furniture products
- Both lists auto-update when the lookup table is extended

## Related

- [[Source-Dynamic-Drop-Down-Lists-Mynda-Treacy]] — source
- [[Dependent-Dropdown-via-FILTER-UNIQUE-SORT]] — simpler dependent dropdown pattern (country → category); this note covers the XLOOKUP-to-DV integration and lookup table approach
- [[XLOOKUP-AutoFill-Related-Data-from-Dropdown]] — related: XLOOKUP from dropdown fills other fields
- [[FILTER-Boolean-AND-OR-Logic]] — FILTER's boolean logic that drives the filtering
