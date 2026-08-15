---
created: 2026-08-11
updated: 2026-08-11
source: "5-Power-BI-Slicer-Tricks-Goodly-Transcript.md"
note_type: pattern
tags: [power-bi, slicer, field-parameters]
---

# Fields Parameter — Show Values of Selected Field

A fields parameter normally lets users choose between columns. "Show values of selected field" lets users also filter by the values *within* the chosen column.

## Setup

1. Insert → Modeling → New Field Parameter → pick columns (e.g., Region, Channel)
2. Add the parameter to a slicer
3. Right-click the slicer → Columns → check "Show values of selected field"
4. The slicer now shows the values of whichever column is currently selected

## Result

- User picks "Region" → sees all regions as slicer options
- User picks "Channel" → sees all channels as slicer options
- Further filter the visual using the selected value

## Related

- [[field-parameters-dynamic-axis]] — Field Parameters for dynamic axes
- [[slicer-apply-all-clear-all-buttons]] — Apply/Clear slicer buttons
