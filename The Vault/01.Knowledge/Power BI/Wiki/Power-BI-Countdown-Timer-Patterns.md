---
created: 2026-08-06
updated: 2026-08-06
source: Countdown Timer in Power BI Beginner to Advanced Guide
note_type: pattern
tags: [countdown, dax, time, NOW, TODAY, DATEDIFF, power-bi, visualization, real-time]
---

# Power BI Countdown Timer Patterns

Three DAX patterns for countdown timers in Power BI — beginner static, intermediate per-row dynamic, and advanced real-time.

## Pattern 1 — Beginner: Static Single-Event Countdown

Use for a single, fixed target date. Placed in a Card visual. No row context required.

```dax
Days Remaining = DATEDIFF(TODAY(), DATE(2025, 8, 8), DAY)
```

**Steps:**
1. Create a new measure
2. Paste the DAX — update the target date
3. Drag the measure into a Card visual

**Limitations:** Hard-coded date; cannot scale to multiple events.

## Pattern 2 — Intermediate: Dynamic Per-Row Countdown

Use when you have a table of events, each with its own deadline. Works with Table/Matrix visuals.

```dax
Dynamic Days Remaining =
VAR TargetDate = SELECTEDVALUE('Major Events'[Deadline])
RETURN
    DATEDIFF(TODAY(), TargetDate, DAY)
```

**Steps:**
1. Ensure `Deadline` column exists in your events table
2. Create the measure
3. Place in a Table visual alongside event name and deadline
4. Add conditional formatting → Data bars or Color by rules (red < 7 days, yellow < 30 days)

**Conditional formatting enhancement:**

```
Rule 1: Days Remaining < 0  → Font: Red    (overdue)
Rule 2: Days Remaining < 7  → Font: Orange (critical)
Rule 3: Days Remaining < 30 → Font: Yellow (approaching)
Rule 4: Days Remaining >= 30 → Font: Green  (on track)
```

## Pattern 3 — Advanced: Real-Time Live Timer

Shows days, hours, minutes, and seconds updating dynamically. Requires auto page refresh on the visual.

```dax
Remaining Time =
VAR SecondsLeft = DATEDIFF(NOW(), [TargetDate], SECOND)
VAR Days    = INT(SecondsLeft / 86400)
VAR Hours   = INT(MOD(SecondsLeft, 86400) / 3600)
VAR Minutes = INT(MOD(SecondsLeft, 3600) / 60)
VAR Seconds = MOD(SecondsLeft, 60)
RETURN
    Days & " days, " & Hours & " hours, " & Minutes & " minutes, " & Seconds & " seconds"
```

> ⚠️ This assumes `[TargetDate]` is a scalar — wrap in `SELECTEDVALUE` for per-row use:

```dax
Remaining Time (per event) =
VAR TargetDate  = SELECTEDVALUE('Events'[Deadline])
VAR SecondsLeft = DATEDIFF(NOW(), TargetDate, SECOND)
VAR Days    = INT(SecondsLeft / 86400)
VAR Hours   = INT(MOD(SecondsLeft, 86400) / 3600)
VAR Minutes = INT(MOD(SecondsLeft, 3600) / 60)
VAR Seconds = MOD(SecondsLeft, 60)
RETURN
    Days & "d " & Hours & "h " & Minutes & "m " & Seconds & "s"
```

**Steps:**
1. Create a Date Table with a "Today" column for consistent refresh
2. Create the measure
3. Place in a Card visual
4. Enable **Auto page refresh**: Visualizations → Format → General → Auto page refresh → On
5. Set minimum refresh interval (1 second for testing; consider performance for production)

**Variations:**

```dax
// Compact format: 12d 4h 32m 15s
Days & "d " & Hours & "h " & Minutes & "m " & Seconds & "s"

// Only show non-zero units: "4h 32m 15s" (when days = 0)
IF(
    Days > 0,
    Days & " days, " & Hours & " hours, " & Minutes & " minutes, " & Seconds & " seconds",
    IF(
        Hours > 0,
        Hours & " hours, " & Minutes & " minutes, " & Seconds & " seconds",
        IF(
            Minutes > 0,
            Minutes & " minutes, " & Seconds & " seconds",
            Seconds & " seconds"
        )
    )
)
```

## Implementation Checklist

| Item | Beginner | Intermediate | Advanced |
|------|----------|--------------|----------|
| Events table with Deadline column | ❌ | ✅ | ✅ |
| Date Table with Today column | ✅ | ✅ | ✅ |
| Card visual | ✅ | ✅ | ✅ |
| Table/Matrix visual | ❌ | ✅ | ❌ |
| Auto page refresh | ❌ | ❌ | ✅ |
| Conditional formatting | ❌ | ✅ | ❌ |

## Related

- [[Countdown-Timer-in-Power-BI]] — concept overview
- [[Author-Boniface-Muchendu]] — author note (Data Bear)
