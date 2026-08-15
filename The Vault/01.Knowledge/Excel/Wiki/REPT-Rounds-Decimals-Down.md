---
created: 2026-08-10
updated: 2026-08-10
source: "Excel REPT Function In Cell Charts • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
note_type: gotcha
tags: [excel, gotcha, rounding, decimals]
---

# REPT Rounds Decimals Down, Not Nearest

REPT silently truncates decimal values to the nearest lower integer instead of rounding to the nearest.

## Expected Behaviour

`=REPT("█", 3.9)` — you might expect 4 blocks.

## Actual Behaviour

`=REPT("█", 3.9)` returns **3 blocks**.

## Why It Happens

Excel REPT accepts only an integer for `number_times`. It uses `FLOOR` rounding internally — effectively `INT` — dropping the decimal portion entirely.

## How to Handle It

Wrap the value with a rounding function before passing to REPT:

```excel
=REPT("█", ROUND([@Value] * 20, 0))      ' round to nearest
=REPT("█", ROUNDDOWN([@Value] * 20, 0))   ' always down
=REPT("█", ROUNDUP([@Value] * 20, 0))     ' always up
```

For progress bars, ROUND is typically correct:

```excel
=LET(
  width, 20,
  filled, ROUND([@[Completion Rate]] * width, 0),
  REPT("█", filled) & REPT("▒", width - filled)
)
```

For star ratings, ROUNDDOWN ensures the unfilled star count is correct:

```excel
=REPT("★", [@Score]) & REPT("☆", 5 - ROUNDDOWN([@Score], 0))
```

## Related

- [[REPT-Function]] — function
- [[Progress-Bar-REPT-LET]] — pattern where ROUND is required
- [[Star-Rating-REPT]] — pattern where ROUNDDOWN is required
