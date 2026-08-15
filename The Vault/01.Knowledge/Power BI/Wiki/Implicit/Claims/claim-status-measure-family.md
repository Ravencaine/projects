---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, technique, Power BI]
---

# Color-by-status in Gantt charts requires one measure per status, not conditional formatting on a single measure

<!-- Rather than fight Power BI conditional formatting on a single measure, build one measure per status (Not Started, Delayed, Pending, In Progress, Completed), each gated by IF(SELECTEDVALUE(Status) = '...', [Task Duration]). Assign each series its own color. -->

## Claim

Rather than fight Power BI conditional formatting on a single measure, build one measure per status (Not Started, Delayed, Pending, In Progress, Completed), each gated by IF(SELECTEDVALUE(Status) = '...', [Task Duration]). Assign each series its own color.

## Evidence

- Stated in [[Gantt-Chart-Native-Visuals-Overlay-Pattern]] — Key Points
