---
created: 2026-08-13
source: 5 Mistakes to Avoid in Power BI (That Can Ruin Your Reports)
note_type: pattern
tags: [power-bi, report-design, slicers, filters, interactivity, user-experience, beginner]
---

# Report Design Mistake: Filters and Slicers Not Used Properly

<!-- Reports without proper slicers and filter hierarchy limit exploration, frustrate users, and reduce the value of interactive dashboards. -->

## The Mistake

Either:
1. **No slicers at all** — users cannot filter the data they see
2. **Too many slicers** — page is dominated by filter controls, not visuals
3. **Wrong scope** — slicers only apply to one page instead of the whole report
4. **No default context** — report loads showing all data, overwhelming users

```
❌ No slicers:
   Report shows everything → users cannot answer specific questions
   → "What are sales in the Northeast in Q3?"

❌ Too many slicers:
   Page is 60% filters, 40% content
   → Cognitive load is on the filters, not the insights
```

## The Fix Pattern

### Step 1 — Place Slicers for the Most Common Filters

```
Audience: Who will use this report most?
Common filters: Region, Date Period, Product Category, Customer Segment

Place these at the top of the report page as slicers.
```

### Step 2 — Use the Correct Slicer Scope

| Filter Type | Scope | When to Use |
|------------|-------|-------------|
| Slicer | Visual | Filter only one specific visual |
| Page-level filter | Page | All visuals on that page |
| Report-level filter | All pages | Global context (e.g., current year) |
| Drillthrough filter | Single visual | Deep-dive on a specific record |

```
Rule: Push filters as far down the scope as possible.
Global filters on every page slow performance and confuse users.
```

### Step 3 — Set Sensible Defaults

```
❌ Report loads with no filters → all-time totals for all regions
✓ Report loads with current month pre-selected → immediate value
✓ Report loads with user's region pre-selected → personalised start
```

```dax
-- Measure to check if a slicer has a selection:
Has Selection =
IF(
    ISFILTERED(Customers[Region]),
    "Filtered",
    "All Regions"
)
```

### Step 4 — Add Page-Level Filters for Context

```
Use page-level filters to set the baseline:
- Page: "Sales Overview"    → filter: Year = 2026
- Page: "Regional Deep Dive" → filter: Region = [selected region]
```

### Step 5 — Use Sync Slicers Across Pages

```
If the same filter applies across multiple pages:
Model View → Sync Slicers pane → link the slicer across pages
→ User sets Region once, it updates every page
```

## Slicer Types: Which to Use

| Slicer Type | Best For |
|------------|----------|
| Dropdown | Many values (>10), saves space |
| List | 5–15 values, quick scanning |
| Between / Single select | Numeric or date ranges |
| Relative date slicer | "Last 30 days", "This quarter" |
| Top N | High-cardinality (many products) |

## Related

- [[Report-Design-Mistake-Too-Many-Visuals]] — this KB: visual density patterns
- [[pl-data-model-relationships]] — Power BI: relationship effects on filter context
