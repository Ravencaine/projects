---
created: 2026-07-27
updated: 2026-08-02
source: "From Messy to Masterpiece The Ultimate Power BI Dashboard Checklist .md"
note_type: workflow
tags: [power-bi, dashboard-design, checklist, deployment, pre-publish]
---

# Power BI Dashboard Pre-Publish Checklist

A 6-category checklist to verify before publishing any Power BI report. Covers data model, DAX, visual design, performance, accessibility, and deployment.

## Category 1: Data Model

- [ ] Date table configured and marked as date table
- [ ] All relationships have correct cardinality (one-to-many default)
- [ ] Bidirectional cross-filtering used only where necessary
- [ ] No many-to-many relationships without explicit justification
- [ ] Hidden unused columns
- [ ] Data types set correctly (dates as dates, numbers as numbers, text as text)

## Category 2: DAX Measures

- [ ] Base measures prefixed with `_` and hidden from business users
- [ ] No duplicated calculation logic across measures
- [ ] All division operations wrapped in DIVIDE with BLANK fallback
- [ ] TEST measures created for every base measure
- [ ] Time intelligence measures tested with non-standard date ranges

## Category 3: Visual Design

- [ ] Consistent color palette (max 6 colors per visual)
- [ ] All labels readable without hovering
- [ ] No decorative visuals (chartjunk)
- [ ] Consistent header/title formatting
- [ ] Mobile layout tested (if applicable)
- [ ] Color-blind friendly palette chosen

## Category 4: Performance

- [ ] All measures complete in <500ms
- [ ] No bidirectional cross-filtering enabled globally
- [ ] Aggregations configured for large fact tables
- [ ] Unused tables/columns removed from the model
- [ ] Query reduction applied to slicers (Sync Slicers)

## Category 5: Accessibility

- [ ] Alt text added to all visuals
- [ ] Report tested with screen reader
- [ ] Sufficient color contrast (WCAG AA minimum)
- [ ] Keyboard navigation tested

## Category 6: Deployment

- [ ] Row-level security (RLS) tested with all roles
- [ ] Subscriptions configured and tested
- [ ] Scheduled refresh configured in Power BI Service
- [ ] External sharing permissions verified
- [ ] pbix file saved with meaningful name and version

## Related

- [[power-bi-performance-troubleshooting]] — deep-dive performance checklist
- [[measure-library-architecture-pattern]]
