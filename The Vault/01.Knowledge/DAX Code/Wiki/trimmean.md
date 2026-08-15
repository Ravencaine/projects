---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, statistics, trimmed-mean, average]
note_type: function

---

# TRIMMEAN — Trimmed Mean

Returns the mean of the interior of a data set after excluding a percentage from the top and bottom.

## Signature

```dax
TRIMMEAN( <Column>, <Fraction> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Column | Column | Data column. |
| Fraction | Number | Fraction to exclude (0-1). 0.2 = remove top 10% and bottom 10%. |

## Examples

```dax
Trimmed Avg := TRIMMEAN( 'Scores'[Score], 0.2 )
```

## Notes

- Excludes outliers from both tails before averaging
- 0.2 is common for a 10% trim on each side
- DAX TRIMMEAN requires the column to be in a table

## Related

- [[stdevx.p]]
- [[better-median-workaround-in-dax]]

---

## Deckler Extension — Full RANKX Implementation (ch14)

DAX has no native TRIMMEAN. Deckler provides a complete workaround using RANKX and GROUPBY with concurrent while-loop emulation. The formula below handles duplicate values correctly (matching Excel's TRIMMEAN exactly):

```dax
TRIMMEAN =
    VAR __Table = ADDCOLUMNS(
        'TM',
        "Rank", RANKX( 'TM', [Value] )
    )
    VAR __Percent = MAX( 'Percents'[Value] )
    VAR __Result =
        IF(
            __Percent > 1,
            BLANK(),
            VAR __Count = COUNTROWS( __Table )
            VAR __Points = ROUNDDOWN( __Count * __Percent, 0 )
            VAR __Trim = IF( ISODD( __Points ), __Points - 1, __Points ) / 2
            VAR __MaxRank = MAXX( __Table, [Rank] )
            VAR __MinRank = MINX( __Table, [Rank] )
            VAR __RanksTable =
                ADDCOLUMNS(
                    ADDCOLUMNS(
                        GROUPBY(
                            __Table,
                            [Rank],
                            "Count", COUNTX( CURRENTGROUP(), [Value] ),
                            "Value", MAXX( CURRENTGROUP(), [Value] )
                        ),
                        "CBCount",  COUNTROWS( FILTER( __Table, [Rank] >= EARLIER( [Rank] ) ) ),
                        "CTCount",  COUNTROWS( FILTER( __Table, [Rank] <  EARLIER( [Rank] ) ) ),
                        "BWhile",   __Trim - [CBCount],
                        "TWhile",   __Trim - [CTCount]
                    ),
                    "Product",
                        IF(
                            [BWhile] >= 0,
                            [Count] * [Value],
                            ( [Count] + [BWhile] ) * [Value]
                        )
                )
            VAR __MinBottom = MAXX( FILTER( __RanksTable, [BWhile] <= 0 ), [BWhile] )
            VAR __MinTop    = MAXX( FILTER( __RanksTable, [TWhile] <= 0 ), [TWhile] )
            VAR __FinalBottomRankTable =
                ADDCOLUMNS(
                    FILTER( __RanksTable, [BWhile] >= __MinBottom ),
                    "Product",
                        IF( [BWhile] >= 0, [Count] * [Value], ( [Count] + [BWhile] ) * [Value] )
                )
            VAR __FinalTopRankTable =
                ADDCOLUMNS(
                    FILTER( __RanksTable, [TWhile] >= __MinTop ),
                    "Product",
                        IF( [TWhile] >= 0, [Count] * [Value], ( [Count] + [TWhile] ) * [Value] )
                )
            VAR __Bottom = SUMX( __FinalBottomRankTable, [Product] )
            VAR __Top    = SUMX( __FinalTopRankTable,    [Product] )
            VAR __Result =
                DIVIDE(
                    SUMX( __Table, [Value] ) - __Bottom - __Top,
                    __Count - 2 * __Trim
                )
            RETURN __Result
        )
    RETURN __Result
```

### How It Works

**Step 1 — Rank:** `RANKX` assigns each value a rank (1 = largest). This defines which are "top" and "bottom."

**Step 2 — Trim count:** `ROUNDDOWN(__Count * __Percent, 0)` gives the number of points to exclude total. Excel rounds this to a multiple of 2 for symmetry (half from each end). `ISODD` handles the rounding; `__Trim` is the half (per end).

**Step 3 — Double concurrent while loop:** The `__RanksTable` emulates two simultaneous while loops — one counting up from the bottom, one counting down from the top — using GROUPBY + EARLIER + COUNTROWS.

**Step 4 — Exit points:** `[BWhile]` and `[TWhile]` track how many ranks remain when the loop "exits." The exit rank is the highest rank where `[BWhile] <= 0` / `[TWhile] <= 0`.

**Step 5 — Partial ranks:** When a rank is only partially excluded (e.g., trim 2 but rank has count=3), only `2/3` of that rank's value contributes — handled by `( [Count] + [BWhile] ) * [Value]`.

### Key Insight

> An average is simply `SUM / COUNT`. Don't assume you must use `AVERAGEX` over a filtered table — decompose the average into its parts and you can handle edge cases like TRIMMEAN's partial-rank logic.

**Source:** DAX for Humans (Greg Deckler, ch14) — dax4humans_ch14_trimmean.txt
