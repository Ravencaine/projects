---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, technique, Power BI]
---

# A transparent date start buffer measure is needed to align Gantt bars with the timeline

<!-- Without a left-side buffer, Gantt bars start at X=0 and float disconnected from the timeline. A Date Start Buffer measure using DATEDIFF pushes each bar to its true horizontal position so the left edge aligns with the first gridline. -->

## Claim

Without a left-side buffer, Gantt bars start at X=0 and float disconnected from the timeline. A Date Start Buffer measure using DATEDIFF pushes each bar to its true horizontal position so the left edge aligns with the first gridline.

## Evidence

- Stated in [[Gantt-Chart-Native-Visuals-Overlay-Pattern]] — Key Points
