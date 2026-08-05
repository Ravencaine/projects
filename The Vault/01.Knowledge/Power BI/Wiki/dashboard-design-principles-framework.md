---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Dashboard Design Principles Used by Top Companies.md
note_type: pattern
tags: [power-bi, pattern, dashboard-design, ux, kpi, color, layout, five-second-rule]
---

# Dashboard Design Principles — UX Framework

Eight design principles for building Power BI dashboards that people actually use, based on patterns observed across 20+ production dashboards in retail, banking, healthcare, and workforce analytics.

## The Core Insight

Technical correctness has almost nothing to do with dashboard adoption. A dashboard with perfect DAX and a beautiful data model still fails if the executive opening it cannot find the one number they came for in five seconds.

## Eight Principles

### 1. Start with the Question, Not the Data
Before dragging fields onto a canvas, define:
- **Who** opens it and how often
- **What decision** the dashboard needs to support
- **What single number**, if it changed, would change their behavior

A Credit Risk dashboard for a loan committee needs a completely different layout than an Executive Overview for a CFO glancing at it weekly.

### 2. The Five-Second Rule
Executive dashboards must communicate their headline message without scrolling or hunting:
- KPI cards at the top — not buried below charts
- Most important number rendered largest
- Color reserved for meaning (red/green/amber for status) — not decoration

### 3. Progressive Disclosure
Summary first, detail on demand:
- **Overview page**: handful of KPIs that matter most
- **Category pages**: breakdowns by region, product, segment
- **Detail pages**: drill-through for anomaly investigation

Most viewers only ever need the top layer.

### 4. Slicers — Filter Intent, Not Fields
Limit slicers to the 3–4 dimensions that actually change the story. Every slicer is a decision the user must make before seeing anything useful.

Core slicers: Date range, Region/branch, Customer segment or product category.

### 5. Named DAX Measures, Not Buried Calculations
Every KPI must trace to an explicit, named DAX measure — never a calculated column doing double duty, and never a number typed into a text box.

Benefits: single source of truth, trivial auditing, easy inspection when a KPI looks wrong.

### 6. Validate Every KPI Against Source Data
Cross-check headline KPIs programmatically against the raw dataset before stakeholder review. A single bad number erodes confidence in every other number on the page.

### 7. Design for the Story
Guide the viewer through a narrative:
- Order visuals left-to-right, top-to-bottom in the natural question sequence
- Consistent color coding across every page ("red" means the same thing everywhere)
- Annotate anomalies with brief text — do not assume the viewer will notice without help

### 8. Performance Is a Design Constraint
Performance belongs in design, not as an afterthought:
- Aggregate at the grain the dashboard needs — monthly summaries, not row-level transactions
- Star-schema modeling — simple one-to-many relationships
- Limit visuals per page — every additional visual is another query on load

## The Unifying Principle

A dashboard is a **communication tool first, engineering artifact second**. The DAX has to be correct, the model has to be efficient, the data has to be validated — but none of that matters if the viewer cannot find their answer in five seconds, or cannot trust the number once they find it.

**Build for the person opening it at 8 AM before their first meeting. Everything else follows.**

## Related

- [[progressive-disclosure-pattern]] — `pattern`
- [[slicer-discipline-filter-intent]] — `pattern`
- [[kpi-validation-programmatic-check]] — `pattern`
