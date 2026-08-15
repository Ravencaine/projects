---

created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, pattern, slicer, and, multi-select, disconnected-table, cohort]

---

# AND Slicer / Multi-Select Pattern in DAX

Default Power BI slicers use OR logic — selecting more values returns more rows. An AND slicer inverts this: selecting more values narrows the result to only rows matching ALL selected values.

## Purpose

Enable cohort-style filtering where users select multiple criteria (e.g., diagnoses, attributes) and only entities having ALL selected values are returned. Critical for patient cohorts, multi-symptom analysis, and intersection filtering.

## Approach 1 — Patient Cohort Pattern

```dax
AND Slicer =
VAR __Diagnoses = COUNTROWS( DISTINCT( 'Diagnoses'[Diagnosis] ) )
VAR __Patients =
    SUMMARIZE(
        'Diagnoses',
        [Patient],
        "__Diagnoses", COUNTROWS( DISTINCT( 'Diagnoses'[Diagnosis] ) )
    )
VAR __Table = FILTER( __Patients, [__Diagnoses] = __Diagnoses )
VAR __Result = CONCATENATEX( __Table, [Patient], ", " )
RETURN __Result
```

## Approach 2 — Complex Selector (Disconnected Table)

```dax
Diagnoses 2 = DISTINCT( 'Diagnoses'[Diagnosis] )
```

```dax
AND Slicer Selector =
VAR __Diagnoses = DISTINCT( 'Diagnoses 2'[Diagnosis] )
VAR __NumDiagnoses = COUNTROWS( __Diagnoses )
VAR __Patient = MAX( 'Diagnoses'[Patient] )
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

Apply this measure to a Table visual with Visual Level Filter set to show non-blank values.

## Approach 3 — GENERATE/EXCEPT (Cohort)

```dax
Cohort =
VAR __Table =
    GENERATE(
        DISTINCT( 'Diagnoses'[Patient]),
        EXCEPT(
            DISTINCT( 'Diagnoses'[Diagnosis] ),
            CALCULATETABLE( DISTINCT( 'Diagnoses'[Diagnosis]) )
        )
    )
VAR __Table2 = SUMMARIZE( __Table, 'Diagnoses'[Patient] )
VAR __Table3 = EXCEPT( DISTINCT( 'Diagnoses'[Patient] ), __Table2 )
VAR __Result = CONCATENATEX( __Table3, [Patient], ", " )
RETURN __Result
```

The `Cohort` approach uses `GENERATE` + `EXCEPT` + `CALCULATETABLE` to perform a set-difference operation, returning patients diagnosed with all selected codes.

## Example

Selecting F91 and F92 in the diagnosis slicer returns only patients who have **both** F91 and F92 — not patients who have either one.

## Notes

- Approach 2 (Complex Selector) uses a disconnected table so the measure can be applied directly to a Table visual as a visual-level filter.
- If showing both approaches on one page, use **Edit Interactions** to disable the original slicer from filtering the Table visual.
- `GENERATE` with related tables creates a context-aware Cartesian product — the second table expression is evaluated within each row's context, which is key to the Cohort approach.
- Approach 3 (Cohort) is the most complex but demonstrates the No-CALCULATE philosophy: it uses `CALCULATETABLE` to restore row context rather than relying on CALCULATE's filter override behavior.

## Related

- [[inverse-and-slicer-pattern-in-dax]]
- [[disconnected-tables-in-dax]]
- [[generate|GENERATE in DAX]]
