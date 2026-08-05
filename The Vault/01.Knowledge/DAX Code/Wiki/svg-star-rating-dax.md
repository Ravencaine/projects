---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, visualization, svg, star-rating]
---

# SVG Star Rating in DAX

## Purpose

DAX can generate **Scalable Vector Graphics (SVG)**: text-based, resolution-independent
images — to create dynamic visual elements inside standard Power BI Table and
Matrix visuals. The **Color Star Rating** measure encodes each salesperson's
performance-vs-target ratio as a row of filled or unfilled stars, rendered directly
from DAX with no external assets.

**Key benefit:** The star count updates automatically with the report's current
filter context — a single measure produces a different rating per row.

## Formula

```dax
Color Star Rating =
    VAR __MAX_STARS  = 5
    VAR __Base       = DIVIDE( SUM( 'Sales Targets'[Sales] ), SUM( 'Sales Targets'[Target] ) )
    VAR __Score      = ROUND( __Base * __MAX_STARS, 0 )
    VAR __FinalScore = IF( __Score > __MAX_STARS, __MAX_STARS, __Score )
    VAR __color           = "Red"
    VAR __backgroundColor = "White"

    VAR __header =
        "data:image/svg+xml;utf8," &
        "<svg xmlns='http://www.w3.org/2000/svg'
              x='0px' y='0px'
              width='" & 20 * __MAX_STARS & "' height='20'>"
    VAR __footer = "</svg>"

    /* ── Filled stars (colored) ─────────────────── */
    VAR __Star1 = "<polygon points='10,0 12,9 20,8 13,13 16,20 10,15 4,20 7,13 0,9 8,9' " &
                  "style='fill:" & __color & ";stroke:" & __color &
                  ";stroke-width:0;fill-rule:evenodd;' />"
    VAR __Star2 = "<polygon points='30,0 32,9 40,8 33,13 36,20 30,15 24,20 27,13 20,9 28,9' " &
                  "style='fill:" & __color & ";stroke:" & __color &
                  ";stroke-width:0;fill-rule:evenodd;' />"
    VAR __Star3 = "<polygon points='50,0 52,9 60,8 53,13 56,20 50,15 44,20 47,13 40,9 48,9' " &
                  "style='fill:" & __color & ";stroke:" & __color &
                  ";stroke-width:0;fill-rule:evenodd;' />"
    VAR __Star4 = "<polygon points='70,0 72,9 80,8 73,13 76,20 70,15 64,20 67,13 60,9 68,9' " &
                  "style='fill:" & __color & ";stroke:" & __color &
                  ";stroke-width:0;fill-rule:evenodd;' />"
    VAR __Star5 = "<polygon points='90,0 92,9 100,8 93,13 96,20 90,15 84,20 87,13 80,9 88,9' " &
                  "style='fill:" & __color & ";stroke:" & __color &
                  ";stroke-width:0;fill-rule:evenodd;' />"

    /* ── Empty stars (white with colored border) ── */
    VAR __Star1a = "<polygon points='10,0 12,9 20,8 13,13 16,20 10,15 4,20 7,13 0,9 8,9' " &
                   "style='fill:" & __backgroundColor & ";stroke:" & __color &
                   ";stroke-width:1;fill-rule:evenodd;' />"
    VAR __Star2a = "<polygon points='30,0 32,9 40,8 33,13 36,20 30,15 24,20 27,13 20,9 28,9' " &
                   "style='fill:" & __backgroundColor & ";stroke:" & __color &
                   ";stroke-width:1;fill-rule:evenodd;' />"
    VAR __Star3a = "<polygon points='50,0 52,9 60,8 53,13 56,20 50,15 44,20 47,13 40,9 48,9' " &
                   "style='fill:" & __backgroundColor & ";stroke:" & __color &
                   ";stroke-width:1;fill-rule:evenodd;' />"
    VAR __Star4a = "<polygon points='70,0 72,9 80,8 73,13 76,20 70,15 64,20 67,13 60,9 68,9' " &
                   "style='fill:" & __backgroundColor & ";stroke:" & __color &
                   ";stroke-width:1;fill-rule:evenodd;' />"
    VAR __Star5a = "<polygon points='90,0 92,9 100,8 93,13 96,20 90,15 84,20 87,13 80,9 88,9' " &
                   "style='fill:" & __backgroundColor & ";stroke:" & __color &
                   ";stroke-width:1;fill-rule:evenodd;' />"

    VAR __rating =
        IF(
            __Base <> BLANK(),
            SWITCH( __FinalScore,
                0, __Star1a & __Star2a & __Star3a & __Star4a & __Star5a,
                1, __Star1  & __Star2a & __Star3a & __Star4a & __Star5a,
                2, __Star1  & __Star2  & __Star3a & __Star4a & __Star5a,
                3, __Star1  & __Star2  & __Star3  & __Star4a & __Star5a,
                4, __Star1  & __Star2  & __Star3  & __Star4  & __Star5a,
                5, __Star1  & __Star2  & __Star3  & __Star4  & __Star5,
                BLANK()
            )
        )

    VAR __Result = __header & __rating & __footer
    RETURN __Result
```

## How It Works

1. **Score calculation:** `__Base = Sales / Target` — the ratio of performance
   to goal. Multiply by 5 (max stars) and `ROUND` to get an integer 0–5.
2. **SVG construction:** Each star is a `<polygon>` SVG element with hard-coded
   10-point coordinate sets positioned at 20px intervals across the SVG width.
   Filled stars use `fill: Red`; empty stars use `fill: White` with `stroke: Red`.
3. **SWITCH block:** Selects the correct combination of filled and empty stars
   based on the integer score.
4. **Header/footer:** The `data:image/svg+xml;utf8,` prefix tells Power BI to
   interpret the string as SVG image data. Set the measure's **Data Category**
   to **Image URL** to display it.

## Simple UNICHAR Alternative

For a lightweight text-only alternative without SVG polygon math, use Unicode stars:

```dax
/* Unicode star rating — minimal version */
Star Rating =
    VAR __Base  = DIVIDE( SUM( 'Sales Targets'[Sales] ), SUM( 'Sales Targets'[Target] ) )
    VAR __Score = ROUND( __Base * 5, 0 )
    VAR __Filled = REPT( UNICHAR(9733), __Score )
    VAR __Empty  = REPT( UNICHAR(9734), 5 - __Score )
    VAR __Result = __Filled & __Empty
    RETURN __Result
/*
  UNICHAR(9733) = ★ (filled star)
  UNICHAR(9734) = ☆ (empty star)
*/
```

The UNICHAR approach is simpler but less visually polished; use the SVG version
for professional-quality reports.

## Notes

- **Set Data Category** to *Image URL* on the measure before adding it to a visual.
- If pasted SVG code uses `data&colon;` instead of `data:`, replace `&colon;`
  with `:` for the image to render.
- The SVG header dynamically sets width: `20 * __MAX_STARS` ensures the star
  row scales cleanly with more stars.
- Works in **Table** and **Matrix** visuals. Adjust image size via
  *Format → Visual → Image size* in the Visualizations pane.

## Related

- [[disconnected-tables-deckler]] — SVG + disconnected tables for custom visuals
- [[dax-index-pattern-deckler]] — text-generation patterns
