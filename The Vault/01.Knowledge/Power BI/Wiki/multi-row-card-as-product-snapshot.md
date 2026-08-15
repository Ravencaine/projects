---
created: 2026-08-13
source: Top Use Cases of Multi-Row Cards in Power BI
source_url: https://medium.com/write-a-catalyst/top-use-cases-of-multi-row-cards-in-power-bi-19934e239698
note_type: atomic
tags: [power-bi, multi-row-card, product-data, inventory, selection]
---

# Multi-Row Card as Product Snapshot

Display all key product attributes — Product Name, Category, Price, Quantity in Stock, Supplier — when a user clicks or selects a product in a table or visual.

## Purpose

Consolidates product context in one view without requiring a separate product detail report. The card updates dynamically when the selected product changes.

## When to Use

- Product catalogue or e-commerce dashboards
- Inventory management reports
- Click-through reports where a table or matrix is the primary navigation

## Design Notes

- Works by linking the Multi-Row Card to a drill-through page or selection mechanism
- Include visual hierarchy: product name bold/large, secondary fields smaller
- Pair with conditional formatting on stock quantity (red = low stock)

## Related

- [[Multi-Row-Card-for-Inventory-Overview]]
- [[Multi-Row-Card-as-Profile-Detail-Panel]]
- [[Multi-Row-Card-Best-Practices]]
