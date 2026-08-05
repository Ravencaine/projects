---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, pattern, multi-column, wide-to-tall, unpivot, reshape]
---

# Multi-Column Aggregation in DAX

Converting wide, sparse tables into tall, analysis-ready tables using DAX. The "wide-to-tall" reshaping pattern using ADDCOLUMNS + GENERATE.

## Purpose

Business data often arrives in a "wide" format: one row per entity with many attribute columns side by side. DAX aggregation requires a "tall" format: one row per entity per attribute. This pattern reshapes wide data into tall form using DAX's ADDCOLUMNS + GENERATE.

## Wide-to-Tall Reshaping

```dax
Tall Table =
    VAR __Base =
        SELECTCOLUMNS(
            'WideTable',
            "__Entity", [EntityKey],
            "__Date", [Date]
        )
    VAR __Attributes =
        ADDCOLUMNS(
            SELECTCOLUMNS(
                GENERATESERIES( 1, 5 ),
                "ColNum", [Value],
                "AttrName",
                    SWITCH( TRUE(),
                        [Value] = 1, "Revenue",
                        [Value] = 2, "Cost",
                        [Value] = 3, "Units",
                        [Value] = 4, "Returns",
                        "Margin"
                    ),
                "AttrCol",
                    SWITCH( TRUE(),
                        [Value] = 1, [Revenue],
                        [Value] = 2, [Cost],
                        [Value] = 3, [Units],
                        [Value] = 4, [Returns],
                        [Margin]
                    )
            )
        )
    VAR __Result =
        GENERATE(
            __Base,
            __Attributes
        )
    RETURN __Result
```

## Key Functions

- **GENERATE**: cross-joins the base table with the attribute table — creates one row per entity per attribute
- **ADDCOLUMNS**: builds the attribute lookup table (column name → column value mapping)
- **SELECTCOLUMNS**: projects only needed columns, reducing memory pressure
- **GENERATESERIES**: generates the row numbers for iterating over attribute columns

## Use Cases

- Normalizing multiple metric columns into a single Metric + Value structure
- Creating a unified fact table from multiple source tables
- Power Query alternative: Unpivot Columns — more efficient for large data
- DAX approach: useful for virtual tables inside measures (not materialized)

## Notes

- This pattern is expensive for large tables (GENERATE creates a Cartesian product)
- For permanent reshaping: use Power Query's Unpivot instead (more efficient)
- For virtual reshaping inside a measure: this is the only DAX-native option
- Combine with SUMMARIZECOLUMNS after reshaping for final aggregation

## Related

- [[dax-index-pattern-deckler]] — row indexing
- [[streak-detection-in-dax]] — consecutive run detection
- multi-column-aggregation-dax — this pattern
