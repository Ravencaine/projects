---
created: 2026-07-30
updated: 2026-08-02
source: Dynamic Ranking in DAX How I Built a Top 5 Dashboard That Actually Worked.md
note_type: pattern
tags: [dax, ranking, top-n, selectedvalue, parameter-table, pattern]
---

# Top N Parameter Slicer Pattern

Let users pick the N value (Top 5, Top 10, Top 15) from a slicer instead of hardcoding it in the measure.

## Purpose

Empower end users to dynamically control how many top-ranked items to display, using a disconnected parameter table and `SELECTEDVALUE()` to drive the threshold in the Top N measure.

## Components

- Disconnected parameter table — a static table of integers (1, 2, 3, …, 20) with no relationships to the model
- `SELECTEDVALUE()` — reads the currently selected value from the slicer
- `RANKX()` + `ALL()` — ranks within the chosen universe
- `IF()` + `BLANK()` — shows only top-ranked rows

## Structure

### Step 1 — Create the parameter table

Create as a DAX calculated table:

```dax
TopN = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25 }
```

Or via Enter Data in Power BI (single column named `TopN`).

### Step 2 — Capture the selected value

```dax
Selected TopN =
SELECTEDVALUE ( TopN[TopN], 5 )
```

Default of `5` used when nothing is selected.

### Step 3 — Combine with the ranking measure

```dax
Top N Customer Sales =
IF (
    [Customer Rank] <= [Selected TopN],
    [Total Sales],
    BLANK ()
)
```

## Example

Full working example combining with the dynamic ranking pattern:

```dax
Customer Rank =
RANKX (
    ALL ( Customers[CustomerName] ),
    [Total Sales],
    ,
    DESC
)

Selected TopN =
SELECTEDVALUE ( TopN[TopN], 5 )

Top N Customer Sales =
IF (
    [Customer Rank] <= [Selected TopN],
    [Total Sales],
    BLANK ()
)
```

Place `TopN[TopN]` as a slicer on the report page. When users change the selection, all visuals using `[Selected TopN]` update instantly.

## Variations

**Allow multiple selection with ALLSELECTED:**

```dax
Selected TopN Multi =
VAR Selected = ALLSELECTED ( TopN[TopN] )
VAR MinN = MIN ( Selected )
RETURN
    MinN
```

Use `MIN` or `MAX` of the selection when users can pick multiple N values.

**Dynamic granularity — different N for different measures:**

```dax
Top N with Fallback =
VAR N = [Selected TopN]
RETURN
    IF (
        NOT ISBLANK ( [Total Sales] ),
        IF ( [Customer Rank] <= N, [Total Sales] ),
        BLANK ()
    )
```

## Related

- [[dynamic-top-n-ranking-pattern]] — the base ranking logic this sits on top of
- [[selectedvalue]] — reading the slicer value
- [[top-n-others-union-pattern]] — extending to show Top N + Others
