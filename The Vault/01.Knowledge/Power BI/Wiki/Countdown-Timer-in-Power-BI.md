---
created: 2026-08-06
updated: 2026-08-06
source: Countdown Timer in Power BI Beginner to Advanced Guide
note_type: atomic
tags: [countdown, dax, time, NOW, TODAY, DATEDIFF, power-bi, visualization]
---

# Countdown Timer in Power BI

Three techniques for building countdown timers in Power BI using DAX — ranging from a static single-event day counter (DATEDIFF) to a dynamic real-time timer showing days, hours, minutes, and seconds.

<!-- one-line description: Three approaches — beginner (DATEDIFF static), intermediate (SELECTEDVALUE + dynamic per-row), advanced (NOW() + integer arithmetic for real-time days/hours/min/sec) -->

## Three Levels

| Level | Approach | DAX | Updates |
|-------|----------|-----|---------|
| Beginner | Static single-event countdown | `DATEDIFF(TODAY(), DATE(2025,8,8), DAY)` | Only on data refresh |
| Intermediate | Per-row dynamic countdown | `DATEDIFF(TODAY(), SELECTEDVALUE(Events[Deadline]), DAY)` | Only on data refresh |
| Advanced | Real-time live timer | `DATEDIFF(NOW(), TargetDate, SECOND)` → integer arithmetic | Requires auto page refresh |

## Beginner — Static Single-Event

```dax
Days Remaining = DATEDIFF(TODAY(), DATE(2025, 8, 8), DAY)
```

- Uses a hard-coded target date
- Suitable for one-off countdowns (e.g., a single launch event)
- Placed in a Card visual
- Limitation: cannot scale to multiple events

## Intermediate — Dynamic Per-Event

```dax
Dynamic Days Remaining =
VAR TargetDate = SELECTEDVALUE('Major Events'[Deadline])
RETURN
    DATEDIFF(TODAY(), TargetDate, DAY)
```

- `SELECTEDVALUE` picks the deadline for the current row context
- Displays in a Table or Matrix with conditional formatting (data bars, font color)
- Each row shows its own countdown
- Limitation: `TODAY()` is evaluated at query time — updates only on data refresh, not live

## Advanced — Real-Time Live Timer

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

- `NOW()` gives date + time (vs `TODAY()` which is date-only)
- `DATEDIFF(..., SECOND)` gives total seconds
- Integer arithmetic breaks total into components
- Displayed in a Card visual as a single concatenated string
- Requires **auto page refresh** on the visual for live ticking

## Key DAX Functions

| Function | Role |
|----------|------|
| `TODAY()` | Returns current date (refresh-dependent) |
| `NOW()` | Returns current date and time (refresh-dependent) |
| `DATEDIFF(start, end, interval)` | Returns the difference between two dates in the given interval |
| `SELECTEDVALUE(column)` | Gets the selected value for the current row/context |
| `INT(value)` | Truncates to integer |
| `MOD(value, divisor)` | Returns remainder after division |

## Limitations

- `TODAY()` and `NOW()` are evaluated when the data refreshes — not continuously live
- For true real-time ticking, enable **auto page refresh** on the visual (minimum 1-second interval)
- `DATEDIFF` with `SECOND` on very large date ranges can produce large integers — ensure the target date is in the future

## Related

- [[Power-BI-Countdown-Timer-Patterns]] — all three DAX patterns with implementation details
- [[Author-Boniface-Muchendu]] — author note (Data Bear)
