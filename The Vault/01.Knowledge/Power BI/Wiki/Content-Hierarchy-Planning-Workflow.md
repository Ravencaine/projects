---
created: 2026-08-09
updated: 2026-08-09
source: "Designing for Impact 6 Ideas to Enhance the User Experience and Accessibility of Your Power BI Dashboards.md"
note_type: workflow
tags: [power-bi, ux, content-hierarchy, navigation, planning, workflow]
---

# Content Hierarchy Planning — Information Structure to Navigation Workflow

> **Type:** workflow
> **Routed to:** Power BI
> **Primary source:** Isabelle Bittar — 2024-03-02

## Goal

Plan the information structure of a dashboard before any visual design begins, then use the navigation panel to communicate that structure to end users.

## Steps

### Step 1: List All Information

Write out every piece of information the dashboard will contain, grouped by theme or subject area.

Example groupings (EDI Dashboard):
- Overview
- Initiatives Roadmap
- Performance by Department
- Demographics
- Resources / Help

### Step 2: Build Information Structure

Create a visual hierarchy showing groupings and the order of importance.

```
EDI Dashboard
├── Overview (summary + alerts)
├── Initiatives Roadmap
│   ├── By Initiative
│   └── By Workstream
├── Performance
│   ├── By Department
│   └── By Time Period
├── Demographics
└── Help / Resources
```

### Step 3: Map to Navigation Panel

Use the navigation panel (left, top, or icon-triggered) to reflect the hierarchy.

- Each page = one grouping in the structure
- Page order follows the hierarchy
- Consistent naming and icons reinforce the structure

### Step 4: Add Summary/Overview Page

Create a dedicated summary page that:
- Highlights key takeaways
- Uses buttons to link to more detailed pages
- Integrates alerts for critical items needing intervention

## Key Principle

> Users navigate a dashboard the way the navigation panel tells them to. If the nav reflects the content hierarchy, users understand the structure without being told.

## Navigation Placement Options

| Position | When to Use |
|----------|-------------|
| Left (traditional) | Familiar to Power BI users; good for vertical hierarchies |
| Top | Matches modern web patterns; saves vertical space |
| Icon-triggered | Maximum space efficiency; good for mobile/responsive layouts |

## See Also

- [[Source-Designing-for-Impact-6-Ideas]] — source article
- [[Summary-Overview-Page-Pattern]] — summary page pattern with KPI cards and detail buttons
- [[Toolbar-Centralization-Pattern]] — centralizing user actions in a toolbar
