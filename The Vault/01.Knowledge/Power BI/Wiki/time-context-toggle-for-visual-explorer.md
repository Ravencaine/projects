---
created: 2026-08-02
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data.md
note_type: workflow
tags: [powerbi, time-filter, field-parameters, user-defined-functions, slicer]
---

# Time Context Toggle for Visual Explorer

Add a time period selector (Last Year, Last Quarter, Last Month) to the Visual Explorer so users can see how their selected metric evolves across time periods.

## Prerequisites

- A field parameter or slicer with time period options (e.g. `TimeContext` with values: Last Year, Last Quarter, Last Month).
- Pre-built `Selected Period` measures — DAX measures that accept a time period argument via a UDF (User Defined Function) pattern.
- The `Metric` field parameter must reference these `Selected Period` measures, not static base measures.

## Steps

1. **Create a time period field parameter** (if not already present):

   ```
   TimeContext = {
       ("Last Year", NAMEOF('_Measures'[UDF Time Context]), 0),
       ("Last Quarter", NAMEOF('_Measures'[UDF Time Context]), 1),
       ("Last Month", NAMEOF('_Measures'[UDF Time Context]), 2)
   }
   ```

2. **Add a slicer** to the Visual Explorer section bound to `TimeContext`.

3. **Connect the slicer** to the `Selected Period` measures in the `Metric` field parameter — the UDF pattern routes the slicer value into the measure's calculation logic.

4. **Place the time selector** prominently above or beside the metric/dimension slicers in the Visual Explorer header.

## Common Errors

- The time toggle has no effect if the `Metric` parameter references static base measures instead of `Selected Period` variants. All metric measures must use the UDF pattern to respond to the time context.

## Related

- [[visual-explorer-pattern]]
- [[field-parameters-for-metric-dimension-selection]]
