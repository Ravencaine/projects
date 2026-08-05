---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, disconnected-table, slicer, parameter-table]
---

# Disconnected Tables (Deckler)

## Purpose

**Disconnected tables** are dimension or parameter tables deliberately left with
**no relationships** to the rest of the semantic model. Normally, no relationship
means no data — but by building the relationship logic *inside DAX measures*,
disconnected tables become extraordinarily flexible. They enable:

- **Parameter tables**: let users select scenarios (best/worst/base case)
- **Custom slicer logic**: NOT slicers, AND slicers, complex selectors
- **Dynamic measure selection**: swap which measure displays based on user choice
- **Attendance / absence tracking**: filter to attended or missed events

The key insight: `CALCULATE`-less DAX has no automatic relationship propagation,
so you *must* use measures to bridge the gap — and those measures can implement
arbitrary logic.

## Formula — Basic Measure "Relationship"

```dax
Measure =
    VAR __Item = MAX( 'Table'[Item] )
    VAR __Result =
        SWITCH( __Item,
            "One",   SUMX( FILTER( 'Table2', [Item] = "One" | [Item] = "Three" ), [Value] ),
            "Two",   SUMX( FILTER( 'Table2', [Item] = "Two" ),                      [Value] ),
            BLANK()
        )
    RETURN __Result
```

The measure **defines** the relationship between the disconnected `Table`
and `Table2`. No relationship in the model — all logic lives in DAX.

## Formula — Attendance / Absence Slicer

A practical example: track employee training attendance, then let the report user
filter to "Attended" or "Not Attended" using a disconnected slicer.

**Attendance Measure (text label):**

```dax
Attendance =
    IF( MAX( 'Training'[Date] ) = BLANK(),
        "Not Attended",
        "Attended"
    )
```

**Attendance Disconnected Table (Enter Data):**

| Attendance |
|------------|
| Attended |
| Not Attended |

**Attendance 2 Measure (bridges the slicer):**

```dax
Attendance 2 =
    VAR __Values    = DISTINCT( 'Attendance'[Attendance] )
    VAR __Attendance = [Attendance]
    VAR __Result    = IF( __Attendance IN __Values, __Attendance, BLANK() )
    RETURN __Result
```

Place `Attendance` from the disconnected table in a **Slicer** visual. Place
`Attendance 2` in a **Matrix** alongside `Employee`. The slicer filters which
employees appear — selecting "Not Attended" reveals only employees who missed
training, while "Attended" shows those who showed up.

## Formula — NOT Selector (Inverse Slicer)

Exclude selected values from the visual instead of including them.

```dax
NOT Selector =
    VAR __Category   = MAX( 'Products'[Category] )
    VAR __Categories = DISTINCT( 'Categories'[Category] )
    VAR __Result     = IF( __Category IN __Categories, BLANK(), 1 )
    RETURN __Result
```

Add this measure to the visual-level filters of the target visual and set the
filter to **Show items when value is 1**. Selected categories are excluded.

```dax
NOT Aggregator =
    VAR __Categories = DISTINCT( 'Categories'[Category] )
    VAR __Table     = FILTER( 'Products', NOT( [Category] IN __Categories ) )
    VAR __Result    = SUMX( __Table, [Value] )
    RETURN __Result
```

## Formula — AND Slicer (Cohort Selector)

Each additional slicer selection makes results *more restrictive* — users must
have **all** selected diagnoses.

```dax
AND Slicer =
    VAR __Diagnoses = COUNTROWS( DISTINCT( 'Diagnoses'[Diagnosis] ) )
    VAR __Patients =
        SUMMARIZE( 'Diagnoses', [Patient], "__Diagnoses",
                   COUNTROWS( DISTINCT( 'Diagnoses'[Diagnosis] ) ) )
    VAR __Table = FILTER( __Patients, [__Diagnoses] = __Diagnoses )
    VAR __Result = CONCATENATEX( __Table, [Patient], ", " )
    RETURN __Result
```

Returns patients who have **all** selected diagnoses. Extended as a selector:

```dax
AND Slicer Selector =
    VAR __Diagnoses    = DISTINCT( 'Diagnoses 2'[Diagnosis] )
    VAR __NumDiagnoses = COUNTROWS( __Diagnoses )
    VAR __Patient      = MAX( 'Diagnoses'[Patient] )
    VAR __PatientDiagnoses =
        COUNTROWS(
            DISTINCT(
                SELECTCOLUMNS(
                    FILTER( 'Diagnoses', [Patient] = __Patient && [Diagnosis] IN __Diagnoses ),
                    "__Diagnosis", [Diagnosis]
                )
            )
        )
    VAR __Result = IF( __PatientDiagnoses = __NumDiagnoses, 1, BLANK() )
    RETURN __Result
```

## Components

| Component | Role |
|-----------|------|
| Disconnected table | User-facing parameter/slicer — no model relationship |
| `DISTINCT( 'Table'[Col] )` | Read what the user has selected |
| `IF( ... IN __Values, ... )` | Match current context against selections |
| `BLANK()` | Suppress rows that don't match the selection |
| `SUMX( FILTER(...) )` | Aggregate with custom filter logic |

## Why No CALCULATE?

Deckler's No-CALCULATE philosophy makes disconnected tables more natural:
CALCULATE modifies filter context, but disconnected tables have **no filter context
to modify**: the relationship is formed by the measure reading selections and
applying custom logic. Using CALCULATE here adds unnecessary complexity.

## Notes

- **Performance:** Disconnected tables with DAX-defined relationships can be slower
  than standard relationships on large fact tables — but for the problems they
  solve, the trade-off is worth it.
- The **Attendance 2** pattern is the canonical disconnected-slicer bridge:
  the disconnected table's selections flow into a `DISTINCT` collection that
  the measure checks against the actual data.
- Extend the pattern to **measure selectors**: put measure names in a disconnected
  table and use `SWITCH( TRUE(), [SelectedMeasure] = "Revenue", [Revenue], ... )`
  to dynamically display the chosen metric.

## Related

- [[svg-star-rating-dax]] — SVG visuals built from disconnected tables
- [[earned-value-management-evm-dax]] — KPI metrics
- [[dax-index-pattern-deckler]] — table generation techniques
