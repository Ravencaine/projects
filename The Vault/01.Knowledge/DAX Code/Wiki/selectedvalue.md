---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: function
tags: [filter-context, slicer, selected-value]
related: [SWITCH, VALUES, FILTER]
---

# SELECTEDVALUE

Returns the single value selected by a slicer or filter context, or a specified alternate result when multiple values are selected or no value is selected.

## Signature

```dax
SELECTEDVALUE(<column>[, <alternateResult>])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `column` | Column reference | The column to read the selected value from |
| `alternateResult` | Scalar (optional) | Value to return when 0 or >1 values are selected |

## Returns

A single scalar value from `column` if exactly one value is selected; otherwise returns `alternateResult` (or `BLANK` if omitted).

## Examples

**Read slicer selection:**
```dax
Selected Stage Order =
VAR _SelectedStage = SELECTEDVALUE(JobReqs[Current Stage])
RETURN _SelectedStage
```

**Read slicer with alternate result:**
```dax
Selected Period = SELECTEDVALUE(Period[Period], "1M")
```

**Use with SWITCH to branch on user selection:**
```dax
Minimum Date =
VAR _MaxDate = [Maximum Date]
VAR _SelectedPeriod = SELECTEDVALUE(Period[Period])
VAR _MinimumDate =
    SWITCH(
        TRUE(),
        _SelectedPeriod = "1W", _MaxDate - 7,
        _SelectedPeriod = "1M", EDATE(_MaxDate, -1),
        _SelectedPeriod = "6M", EDATE(_MaxDate, -6),
        _SelectedPeriod = "1Y", EDATE(_MaxDate, -12)
    )
RETURN _MinimumDate
```

**Build a label from two columns:**
```dax
Description =
SELECTEDVALUE('Key'[Full Name]) & " - " & SELECTEDVALUE('Key'[Description])
```

## Notes

- Use `SELECTEDVALUE` instead of `VALUES(<column>)` when you expect exactly one value — it cleanly handles the multi-value case without returning a table.
- Often paired with `SWITCH(TRUE(), ...)` to branch logic based on the user's slicer choice.
- In Isabelle Bittar's articles, `SELECTEDVALUE` appears in nearly every interactive technique — it's the primary way to read user input from slicers.
- If the column has no filter (nothing selected), returns `alternateResult` if provided, otherwise `BLANK`.
- When multiple values are selected (e.g., multi-select slicer), returns `alternateResult` — use this to guard against ambiguous context.

## Related

- [[SWITCH]] — branch logic on the returned value
- [[VALUES]] — returns a table of selected values
- [[FILTER]] — explicit row filtering
