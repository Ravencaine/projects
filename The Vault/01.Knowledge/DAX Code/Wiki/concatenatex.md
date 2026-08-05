---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: function
tags: [string-aggregation, iterator, delimiter, text-list]
related: [CALCULATE, FILTER, VALUES, SWITCH]
---

# CONCATENATEX

Concatenates the result of an expression evaluated for each row of a table, using a specified delimiter between each concatenated value.

## Signature

```dax
CONCATENATEX(<table>, <expression>[, <delimiter>[, <orderBy_expression>[, <order>]]])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `table` | Table | Table or table expression to iterate over |
| `expression` | Text | Expression returning text for each row |
| `delimiter` | String (optional) | Text to insert between each concatenated value (default: comma) |
| `orderBy_expression` | Any (optional) | Expression to sort rows before concatenating |
| `order` | Enum (optional) | `ASC` or `DESC` |

## Examples

**Build alert message with list of regions (Bittar alerts pattern):**
```dax
Alert Regions HTML =
    "<p>Alerts in the following regions:</p><ul>"
    & CONCATENATEX(
        FILTER(
            ALLSELECTED('Regions'[Region]),
            [Alert Value] > 0
        ),
        "<li>" & 'Regions'[Region] & " (" & FORMAT([Alert Value], "$#,##0") & " increase)</li>",
        ""
    )
    & "</ul>"
```

**Comma-separated list of top categories:**
```dax
Top Categories =
    CONCATENATEX(
        TOPN(5, VALUES('Product'[Category]), [Sales]),
        'Product'[Category],
        ", "
    )
```

**Dynamic text with formatted numbers:**
```dax
Score Card Text =
    CONCATENATEX(
        'Metrics'[Metric Name],
        [Metric Name] & ": " & FORMAT([Metric Value], "$#,##0"),
        " | "
    )
```

## Notes

- `CONCATENATEX` is an iterator (like `SUMX`, `AVERAGEX`) — it scans every row of `table`.
- In Bittar's dynamic alerts pattern, `CONCATENATEX` generates an HTML `<ul>` list of regions where a metric exceeded a threshold. The HTML is then rendered by the HTML Content custom visual.
- Use `FILTER(ALLSELECTED(...), ...)` to include only user-visible (slicer-selected) rows that meet the condition.
- Combine with `FORMAT` inside the expression to include formatted numbers, percentages, or dates in the concatenated string.
- `CONCATENATEX` with `TOPN` or `FILTER` can build a ranked list of items.
- Sorting with `orderBy_expression` and `order` is useful for consistent output (e.g., alphabetically sorted region lists).

## Related

- [[CALCULATE]] — wrap CONCATENATEX to modify filter context
- [[FILTER]] — filter rows before concatenation
- [[VALUES]] — provide row context for concatenation
- [[SWITCH]] — conditionally switch between different concatenated outputs
