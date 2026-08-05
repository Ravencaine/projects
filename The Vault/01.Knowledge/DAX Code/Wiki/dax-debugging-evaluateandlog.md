---

created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: ["dax", "pattern", "debugging", "evaluateandlog", "logging", "diagnostic"]

---

# EVALUATEANDLOG — DAX Debug Print

`EVALUATEANDLOG` logs intermediate DAX values to the external trace log while still returning the value. It is the DAX equivalent of `console.log` in JavaScript or `print()` in Python.

## Purpose

Inspect what values DAX is computing at each step of a complex measure — without changing the final result. Essential for diagnosing unexpected outputs in nested VARs, CALCULATE chains, and filter contexts.

## Structure

```dax
My Measure Debug =
EVALUATEANDLOG( [My Measure], "Step 1 result" )
```

`EVALUATEANDLOG` takes up to three parameters:
- **Value** (required): the expression to evaluate and return
- **Label** (optional): a string label written to the trace log
- **MaxRows** (optional): maximum rows to log (for table expressions)

## Setup — SQL Profiler Integration

`EVALUATEANDLOG` writes to the Analysis Services trace log. To view it:

1. Install SQL Server Management Studio (SSMS) to get SQL Profiler.
2. Create the file `SQLProfiler.pbitool.json` in:
   ```
   C:\Program Files (x86)\Common Files\Microsoft Shared\Power BI Desktop\External Tools\
   ```
   with content:
   ```json
   {
     "version": "1.0",
     "name": "SQL Profiler",
     "description": "SQL Profiler",
     "path": "C:\\Program Files (x86)\\Microsoft SQL Server Management Studio 18\\Common7\\PROFILER.exe",
     "arguments": "/A \"%server%\" /D \"%database%\""
   }
   ```
3. Restart Power BI Desktop — SQL Profiler appears in the External Tools tab.
4. In SQL Profiler, go to **Events Selection → Query Processing** and select DAX events.
5. Interact with your report; `EVALUATEANDLOG` events appear in the trace.

## Example

```dax
Debug Step =
VAR __Result = [My Measure]
RETURN
    EVALUATEANDLOG( __Result, "My Measure intermediate value" )
```

## Notes

- `EVALUATEANDLOG` is a **debugging tool only**: remove it from production measures.
- Works in Power BI Desktop; results may vary in other environments.
- The typical workflow: create a separate debug measure wrapping the target measure with `EVALUATEANDLOG`, verify the output, then remove the wrapper.
- Combine with Performance Analyzer for full diagnostic coverage.

## Related

- [[dax-debugging-tocsv]]
- [[bim-file-ai-dax-generation]]
- [[dax-error-handling-iferror-iserror]]
