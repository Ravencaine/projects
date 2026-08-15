---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: relationship
edge_type: builds_on
tags: [Power BI, implicit-edge, builds_on]
source_node: "[[plotly-layout-mutation-gotcha]]"
target_node: "[[chart-base-plotly]]"
weight: 0.5
---

# plotly-layout-mutation-gotcha builds_on chart-base-plotly

<!-- The layout mutation gotcha is a known pitfall when reusing base chart layout dicts; chart-base-plotly likely provides the base layout helper that needs to return a fresh dict each call. -->

## Edge

`[[plotly-layout-mutation-gotcha]]` -- **builds_on** -> `[[chart-base-plotly]]`

## Evidence

The layout mutation gotcha is a known pitfall when reusing base chart layout dicts; chart-base-plotly likely provides the base layout helper that needs to return a fresh dict each call.


## Related

- [[plotly-layout-mutation-gotcha]]
- [[chart-base-plotly]]
