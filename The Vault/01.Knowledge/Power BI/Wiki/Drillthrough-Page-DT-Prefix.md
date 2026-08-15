---
created: 2026-08-09
updated: 2026-08-09
source: "Creating a Drillthrough Button in Power BI.md"
note_type: atomic
tags: [power-bi, drillthrough, naming-convention, page-design]
---

# Drillthrough Page Naming: DT Prefix

Name drillthrough pages with a `DT` prefix followed by the dimension name. This convention makes drillthrough pages easy to identify in the page list when setting button destinations.

## Rule

```
DT <DimensionName>
```

Examples:
- `DT Country` — drillthrough triggered by country selection
- `DT Product` — drillthrough triggered by product selection
- `DT Salesperson` — drillthrough triggered by salesperson selection

## Rationale

- **Scanability:** `DT` groups all drillthrough pages together in the page list (sorted alphabetically)
- **Self-documenting:** the suffix immediately reveals which field drives the drillthrough without opening the page
- **Button destination clarity:** when selecting the destination in the button's Action properties, `DT Country` is unambiguous vs a generic `Country Detail`

## Note

The page itself must also be hidden (right-click tab → Hide page) so users can only reach it via the drillthrough action, not by clicking the page tab.
