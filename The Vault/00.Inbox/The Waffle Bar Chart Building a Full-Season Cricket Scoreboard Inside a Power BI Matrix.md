---
title: "The Waffle Bar Chart: Building a Full-Season Cricket Scoreboard Inside a Power BI Matrix"
source: "https://medium.com/microsoft-power-bi/the-waffle-bar-chart-building-a-full-season-cricket-scoreboard-inside-a-power-bi-matrix-526b51c94732"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2026-05-11
created: 2026-08-12
description: "How a single Matrix visual, a helper table, and a handful of DAX measures can replace an entire custom chart — inspired by Bas Dohmen"
Processed: "Unprocessed"
---
## How a single Matrix visual, a helper table, and a handful of DAX measures can replace an entire custom chart — inspired by Bas Dohmen

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*uFs6f5cXarVnnYosr1iGow.png)

The Waffle Bar Chart

When I first watched [Bas Dohmen’s video](https://youtu.be/8Ys3wH7bfQc?si=QBG-FkO5A8TCaglq) on building a waffle bar chart in Power BI, my first thought was: *this is exactly the kind of trick that makes you rethink what a “visual” actually is.*

No custom visual. No Python. No Deneb. Just a Matrix visual, pushed well beyond what Microsoft probably intended for it — and that is exactly what makes it exciting.

So I decided to rebuild this idea for IPL 2026. Every team. All 14 league matches, split into home and away. Colour-coded by result. With a rich tooltip on hover. Here is everything I learned, and how you can build it yourself.

## What We Are Building

Before we touch DAX, let us get the concept straight, because the mental model is the entire trick.

A standard Matrix visual maps **rows × columns → value**. We are going to hijack that structure like this:

- **Rows** = the 10 IPL teams
- **Columns** = a helper series from **−7 to +8** (16 slots total)
- **Values** = a single DAX measure that decides what each cell shows

The column indices do different jobs:

Column index Role −7 to −1 Home matches (chronological, earliest = −7) 0 Team name (the centre anchor) 1 to 7 Away matches (chronological, earliest = 1) 8 Total points (season running total)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EI2dzUGQetBBCmt92J_9Xg.png)

A matrix-tornado

The result looks like a tornado chart — home fixtures fanning out to the left, away fixtures to the right, with the team badge in the middle. Each cell shows the opponent and the points earned (2 for a win, 1 for NR, 0 for a loss). Upcoming matches show the date instead of a points badge. Colour does the rest.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Step 0 — The Helper Table

This is the backbone. Create it as a calculated table in DAX:

```c
hlpNrMatches = GENERATESERIES(-7, 8, 1)
```

That gives you a single-column table with 16 rows: −7, −6, −5 … 0 … 6, 7, 8. Every column in the Matrix maps to one of these values. The measure we write later reads `MAX(hlpNrMatches[Matches])` to know which slot it is currently rendering.

## Step 1 — The Fixtures Query (Power Query)

The existing `Match_Teams` query only holds *completed* matches — that is intentional, since it drives the NRR and points calculations. But the waffle chart needs *all* 70 matches: played, upcoming, and abandoned.

Create a new Power Query named `Fixtures`:

```c
let
    Source        = Excel.Workbook(
                        File.Contents("C:\Users\ankan\Downloads\IPL_2026_Data.xlsx"), true),
    Matches_Sheet = Source{[Item="Matches",Kind="Sheet"]}[Data],
    Typed         = Table.TransformColumnTypes(Matches_Sheet, {
                        {"Match ID",       Int64.Type},
                        {"Date",           type date},
                        {"Home Team",      type text},
                        {"Away Team",      type text},
                        {"Bat First",      type text},
                        {"Result",         type text},
                        {"Winner",         type text},
                        {"Won By Runs",    Int64.Type},
                        {"Won By Wickets", Int64.Type}
                    })
in
    Typed
```

No relationship is needed between `Fixtures` and any other table. The DAX measure will handle all filtering directly using `ALL()` and `FILTER()`.

## Step 2 — The Core Measure: Match Display

This is where the magic happens. The measure needs to answer one question: *“Given the team in this row and the column index in this column, what text should this cell show?”*

The key pattern inside is a **chronological rank** built using `ADDCOLUMNS` + `COUNTROWS`:

```c
VAR HomeRanked =
    ADDCOLUMNS(
        AllHome,
        "_Rank",
            VAR d  = Fixtures[Date]
            VAR id = Fixtures[Match ID]
            RETURN
            COUNTROWS(
                FILTER(AllHome,
                    Fixtures[Date] < d
                 || (Fixtures[Date] = d && Fixtures[Match ID] < id))
            ) + 1
    )
```

This gives each match a 1-based rank within that team’s home (or away) schedule. Rank 1 maps to column −7 (or column 1 for away), rank 2 maps to −6 (or 2), and so on.

Here is the full measure:

```c
Match Display =
VAR _X       = MAX(hlpNrMatches[Matches])
VAR TeamName = SELECTEDVALUE(Teams[Short Name])-- Home match index: column -7 = 1st home match, -1 = 7th
VAR HomeIdx = _X + 8VAR AllHome =
    FILTER(ALL(Fixtures), Fixtures[Home Team] = TeamName)VAR HomeRanked =
    ADDCOLUMNS(AllHome, "_Rank",
        VAR d  = Fixtures[Date]
        VAR id = Fixtures[Match ID]
        RETURN COUNTROWS(FILTER(AllHome,
            Fixtures[Date] < d
         || (Fixtures[Date] = d && Fixtures[Match ID] < id))) + 1)VAR ThisHome   = FILTER(HomeRanked, [_Rank] = HomeIdx)
VAR HomeOpp    = MAXX(ThisHome, Fixtures[Away Team])
VAR HomeResult = MAXX(ThisHome, Fixtures[Result])
VAR HomeWinner = MAXX(ThisHome, Fixtures[Winner])
VAR HomeDate   = MAXX(ThisHome, Fixtures[Date])VAR HomePts =
    SWITCH(TRUE(),
        HomeResult = "completed" && HomeWinner = TeamName,  "2",
        HomeResult = "completed" && HomeWinner <> TeamName, "0",
        HomeResult = "abandoned",                           "1")VAR HomeDisplay =
    IF(ISBLANK(HomeOpp), BLANK(),
        IF(ISBLANK(HomeResult) || HomeResult = "",
            FORMAT(HomeDate, "MMM DD") & UNICHAR(10) & "vs " & HomeOpp,
            HomePts & UNICHAR(10) & "vs " & HomeOpp))-- Away match index: column 1 = 1st away match, 7 = 7th
VAR AwayIdx = _XVAR AllAway =
    FILTER(ALL(Fixtures), Fixtures[Away Team] = TeamName)VAR AwayRanked =
    ADDCOLUMNS(AllAway, "_Rank",
        VAR d  = Fixtures[Date]
        VAR id = Fixtures[Match ID]
        RETURN COUNTROWS(FILTER(AllAway,
            Fixtures[Date] < d
         || (Fixtures[Date] = d && Fixtures[Match ID] < id))) + 1)VAR ThisAway   = FILTER(AwayRanked, [_Rank] = AwayIdx)
VAR AwayOpp    = MAXX(ThisAway, Fixtures[Home Team])
VAR AwayResult = MAXX(ThisAway, Fixtures[Result])
VAR AwayWinner = MAXX(ThisAway, Fixtures[Winner])
VAR AwayDate   = MAXX(ThisAway, Fixtures[Date])VAR AwayPts =
    SWITCH(TRUE(),
        AwayResult = "completed" && AwayWinner = TeamName,  "2",
        AwayResult = "completed" && AwayWinner <> TeamName, "0",
        AwayResult = "abandoned",                           "1")VAR AwayDisplay =
    IF(ISBLANK(AwayOpp), BLANK(),
        IF(ISBLANK(AwayResult) || AwayResult = "",
            FORMAT(AwayDate, "MMM DD") & UNICHAR(10) & "vs " & AwayOpp,
            AwayPts & UNICHAR(10) & "vs " & AwayOpp))RETURN
    SWITCH(TRUE(),
        _X = 0,              TeamName,
        _X = 8,              FORMAT([Points (PTS)], "0"),
        _X < 0,              HomeDisplay,
        _X >= 1 && _X <= 7, AwayDisplay)
```

Two things worth highlighting here:

`**UNICHAR(10)**` — This is the line break character. It splits the points badge onto the first line and "vs OPP" onto the second, giving that clean two-line layout you see in the screenshot. For this to render, you must turn on **Format → Values → Word wrap → On** in the matrix settings. Without that, Power BI ignores the character visually, even though it is there.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-O7xge9KVDWKDk82KGPHyg.png)

Match Display

`**MAXX**` **instead of** `**SELECTEDVALUE**` — Inside a `ADDCOLUMNS` context, using `SELECTEDVALUE` on `Fixtures` Columns would return BLANK because there is no single-row filter context. `MAXX` on the already-filtered `ThisHome` / `ThisAway` table resolves to exactly one value cleanly.

## Step 3 — Colour Measures

The cells are meaningless without colour. Two measures handle this.

**Background colour** — applies each team’s brand colour to the name and points cells, and win/loss/NR/upcoming colours to match cells:

```c
Match BG Color =
VAR _X       = MAX(hlpNrMatches[Matches])
VAR TeamName = SELECTEDVALUE(Teams[Short Name])

VAR TeamColor =
    SWITCH(TeamName,
        "CSK",  "#ECB512", "DC",   "#275FB2",
        "GT",   "#35456E", "KKR",  "#563C83",
        "LSG",  "#0055E0", "MI",   "#144578",
        "PBKS", "#AD141C", "RCB",  "#EF0C26",
        "RR",   "#B917D5", "SRH",  "#ED701C",
                "#F5C518")

-- (rank logic abbreviated — identical to Match Display)
-- IsWin / IsLoss / IsNR / IsUpcoming determined by Result + Winner

RETURN
    SWITCH(TRUE(),
        _X = 0,      TeamColor,
        _X = 8,      TeamColor,
        IsWin,       "#2DC8A8",
        IsLoss,      "#F47C7C",
        IsNR,        "#FFD966",
        IsUpcoming,  "#D9D9D9",
                     "#FFFFFF")
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*2xtQYvVTcmQ3U8B65lXesw.png)

Color System → NR: Loss: Win

**Font colour** — white text on dark brand backgrounds, black everywhere else:

```c
Match Font Color =
VAR _X       = MAX(hlpNrMatches[Matches])
VAR TeamName = SELECTEDVALUE(Teams[Short Name])
VAR DarkTeams = {"GT","KKR","MI","DC","LSG","PBKS","RCB","RR","SRH"}

RETURN
    IF8
 && TeamName IN DarkTeams,
        "#FFFFFF", "#000000")
```

Apply both via **Format pane → Cell elements → Background colour / Font colour → fx → Field value**.

## Step 4 — The Tooltip

A waffle bar chart without a tooltip is like a scorecard without a scoreline. We want to show, on hover, something like:

```c
Match 27
18 Apr 2026
────────────────
SRH  (bat first)
SRH  vs  CSK
────────────────
SRH won by 10 runs
```

The `Match Tooltip` measure uses `UNICHAR(9472)` — the box-drawing horizontal line `─` — for the separator rows, and `UNICHAR(10)` for line breaks between every line. The result-sentence logic handles runs, wickets, and the correct singular/plural form automatically:

```c
VAR Margin =
    SWITCH(TRUE(),
        NOT ISBLANK(WonByWkts),
            FORMAT(WonByWkts, "0") & " wicket" & IF(WonByWkts = 1, "", "s"),
        NOT ISBLANK(WonByRuns),
            FORMAT(WonByRuns, "0") & " run" & IF(WonByRuns = 1, "", "s"),
        "")

VAR ResultLine =
    SWITCH(TRUE(),
        ISBLANK(MatchResult) || MatchResult = "", "Upcoming",
        MatchResult = "abandoned",               "No Result  (match abandoned)",
        TeamWon,      TeamName & " won by " & Margin,
        NOT TeamWon,  TeamName & " lost by " & Margin)
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*7n9x3tyG4JYDrWZF7jrCHg.png)

The Multi-line Tooltip

For the tooltip to render multi-line text correctly, use a **Report Page Tooltip** — not the Tooltips field well:

1. Insert a new page → name it `Tooltip_Waffle`
2. **Format → Page information → Tooltip → On**
3. **Format → Canvas settings → Type → Tooltip**
4. Drop a **Card** visual → add `Match Tooltip` → turn off title and category label
5. On the main page, select the matrix → **Format → Tooltips → Type → Report page → Page → Tooltip\_Waffle**

## Step 5 — Matrix Setup

Field well Value Rows `Teams[Short Name]` Columns `hlpNrMatches[Matches]` Values `Match Display`

Then in the Format pane:

- **Values → Word wrap → On** *(essential for UNICHAR(10) to work)*
- **Row headers → Off** *(the team name is rendered inside column 0)*
- **Column headers → Off** *(the −7 to 8 indices are internal plumbing, not labels)*
- **Row/column subtotals → Off**
- **Grid → Row padding → 8–10px** *(gives the cells breathing room)*
- Apply `Match BG Color` to the background colour and `Match Font Color` to Font colour via conditional formatting

## The Key Insight

The technique that makes all of this work is the combination of **a disconnected helper table + a switch-based measure**. Power BI renders each matrix cell by evaluating the measure inside the intersection of two filter contexts: the team row and the column index. We never need a relationship between `hlpNrMatches` and anything else — the `MAX()` call simply reads whichever column index that particular cell is sitting in, and the `SWITCH` decides what to show.

This pattern — a helper series + a measure that pattern-matches on the series value — is one of the most powerful and underused ideas in Power BI. Bas Dohmen’s original video captures this beautifully. What I have done here is adapt it for a live, updating tournament dataset where matches are added daily, upcoming fixtures show automatically, and tooltips give you the full match story on hover.

## Get the Complete Package

Ready to add these to your reports?

**Connect with me on** [**LinkedIn**](https://www.linkedin.com/in/bandyopadhyay-ankan/), **send me a DM,** and I’ll send you:

- ✅ Complete PBIX file with sample data

## Final Thoughts

The waffle bar chart is one of those builds that makes you realise how far the Matrix visual can be pushed. It is not a matrix anymore. It is a scoreboard, a race chart, a form guide, and a fixture list — all in one visual, with zero custom visuals.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vVVEt4IsRAuYmRX8YnGx5Q.png)

The final output

If you build this for your own dataset — a football league, a basketball season, any round-robin tournament — the pattern is identical. Swap the team names, adjust the `GENERATESERIES` range to match your match count, update the colour palette, and you are live.

Credit where it is due: this would not exist without Bas Dohmen’s original concept. Go watch [his video](https://youtu.be/8Ys3wH7bfQc?si=QBG-FkO5A8TCaglq) — it is worth every minute.

*Enjoyed this? Follow me on* [LinkedIn](https://linkedin.com/in/bandyopadhyay-ankan) *for more Power BI builds, DAX deep-dives, and data storytelling. Drop a comment if you build one of these — I’d love to see what you create!*

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** DAX, Data Visualization

**Tags:** Tutorial, DAX, Data Visualization