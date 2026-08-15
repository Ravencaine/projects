---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, technique, Power BI]
---

# DAX measures for axis bounds adapt to slicer-selected date ranges automatically

<!-- Min Calendar Date and Max Project Date measures use CALCULATE and FILTER over the Projects table with ALL() to return the global extremes regardless of the current filter context, making the Gantt timeline adapt to slicer selections without manual axis resets. -->

## Claim

Min Calendar Date and Max Project Date measures use CALCULATE and FILTER over the Projects table with ALL() to return the global extremes regardless of the current filter context, making the Gantt timeline adapt to slicer selections without manual axis resets.

## Evidence

- Stated in [[Gantt-Chart-Native-Visuals-Overlay-Pattern]] — Key Points / Examples
