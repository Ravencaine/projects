---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: atomic
tags: [design-thinking, divergent-thinking, convergent-thinking, tool-selection]
related: [Data-Narratives-Report-Design, Visual-Design-Principles]
---

# Double Diamond Design (Tool Selection Framework)

A four-stage design framework (British Design Council) that helps decide which Power BI tools and techniques to use at each phase of building a report.

## The Four Stages

```
Discover → Define → Develop → Deliver
   ◇          ◇        ◇         ◇
Divergent  Convergent Divergent  Convergent
```

### Discover (Divergent)

Gather everything — all stakeholder requirements, existing reports, data sources, pain points.

- Interview users.
- Review existing dashboards.
- List all data sources.
- Don't filter yet — include everything.

### Define (Convergent)

Identify the core problem — what decision does this report support?

- Synthesise findings into 1–3 key questions.
- Prioritise by impact on decisions.
- Discard requirements that don't map to a decision.

### Develop (Divergent)

Generate many solutions — sketch multiple approaches.

- Create 3+ lo-fi wireframes.
- Explore different visual types for the same data.
- Test different layout options.

### Deliver (Convergent)

Select the best solution and build it.

- Choose the wireframe with the clearest communication.
- Build in Power BI.
- Test with real users.

## Mapping to Power BI Workflow

| Diamond Stage | Power BI Activity |
|--------------|------------------|
| Discover | Stakeholder interviews, data audit |
| Define | Define the 3/30/300-second questions (see [[The-3-30-300-Rule]]) |
| Develop | Lo-fi wireframes, sketch multiple layouts |
| Deliver | Build report, apply [[Visual-Design-Principles]] |

## The Chart Selection Principle

During Develop, match the chart to the data *story*, not the data *type*:

| Story | Chart Type |
|-------|-----------|
| "How much?" | Bar, Column |
| "Over time?" | Line, Area |
| "Parts of a whole?" | Pie, Donut, Treemap |
| "Relationship between variables?" | Scatter |
| "How does A compare to B?" | Bullet, Bar |
| "Where in space?" | Map |

## Notes

- Bittar's Data Narratives article applies the Double Diamond to all client projects.
- The divergent/convergent rhythm prevents both "analysis paralysis" (too much divergent thinking) and "wrong solution" (too little).
- [[Data-Narratives-Report-Design]] is the Power BI-specific implementation of this framework.

## Related

- [[Data-Narratives-Report-Design]] — Power BI-specific implementation
- [[The-3-30-300-Rule]] — convergent "Define" output
- [[Visual-Design-Principles]] — criteria for evaluating wireframe solutions
