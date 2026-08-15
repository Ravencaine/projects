---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [combiner, m-function]
---


# Combiner.CombineTextByDelimiter

Returns a function that combines a list of text values into a single text value using the specified delimiter.

## Signature

```m
Combiner.CombineTextByDelimiter(delimiter as text, optional quoteStyle as nullable
number) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| delimiter | text | |
| optional quoteStyle | nullable number | |

## Returns

function

### Example 1

Combine a list of text values using a semicolon delimiter.

```m
Combiner.CombineTextByDelimiter(";")({"a", "b", "c"})
```

// Output
```
"a;b;c"
```

### Example 2

Combine the text of two columns using a comma delimiter and CSV-style quoting.

```m
let
Source = #table(
type table [Column1 = text, Column2 = text],
{{"a", "b"}, {"c", "d,e,f"}}
),
Merged = Table.CombineColumns(
Source,
{"Column1", "Column2"},
Combiner.CombineTextByDelimiter(",", QuoteStyle.Csv),
"Merged"
)
in
Merged
```

// Output
```
#table(
type table [Merged = text],
{{"a,b"}, {"c,""d,e,f"""}}
)
```

