---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, debugging, evaluateandlog, tocsv, logging]
note_type: pattern

---

# DAX Debugging with EVALUATEANDLOG and TOCSV

Inspecting intermediate DAX values by logging them to output.

## EVALUATEANDLOG

Returns a value while logging it to the diagnostic query output.

```dax
Debug Measure :=
VAR __Step1 = FILTER( 'Table', 'Table'[Status] = "Active" )
VAR __Step2 = SUMX( __Step1, [Amount] )
RETURN
EVALUATEANDLOG( __Step2, "Final Result: " & __Step2 )
```

## TOCSV

Returns a table as a CSV-formatted string for inspection.

```dax
Debug Table :=
TOCSV( FILTER( 'Sales', 'Sales'[Year] = 2024 ), 100 )
```

## Practical Debugging Pattern

```dax
Debug Sum :=
EVALUATEANDLOG(
    SUMX(
        EVALUATEANDLOG( FILTER( 'Sales', 'Dates'[Year] = MAX( 'Dates'[Year] ) ), "Filtered rows" ),
        [Amount]
    ),
    "Sum result"
)
```

## Reading Logs in DAX Studio

1. Run the measure in DAX Studio
2. Check the Query Plan window for EVALUATEANDLOG entries
3. Use the Results pane to see logged values

## Notes

- EVALUATEANDLOG does not change the returned value — it only logs it
- TOCSV is useful for inspecting filtered row counts
- Remove debug code after validation — it adds overhead

## Related

- [[ai-assisted-dax-development]]
- [[storage-engine-vs-formula-engine-in-dax]]
