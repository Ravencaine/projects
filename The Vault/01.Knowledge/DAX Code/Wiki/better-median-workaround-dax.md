---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [median, medianx, workaround, path-functions, statistical]
---

# Better MEDIAN Workaround

Two approaches to correct the `MEDIAN` function's data-type error when used in calculated columns, plus a formula that correctly implements the mathematical median definition.

## The Bug

`MEDIAN` throws `"Expressions that yield variant data-type cannot be used to define calculated columns"` when applied to certain columns — even columns with clean numeric data. This error also affects `MEDIANX`, `PERCENTILE.EXC`, `PERCENTILE.INC`, `PERCENTILEX.EXC`, and `PERCENTILEX.INC`.

The root issue is a data-type mismatch between the column's variant storage type and what MEDIAN returns.

## Fix 1: CONVERT (Simplest)

```dax
Even Better Median =
CONVERT( MEDIAN( 'Table'[Value] ), DOUBLE )
```

Force the output to the `DOUBLE` (decimal number) type. This is the simplest and preferred workaround.

> Note: Use `DOUBLE`, not `INTEGER` — the median of an even-count set is often a decimal.

## Fix 2: Implementing the Mathematical Definition (Educational)

For even-count sets: median = average of the two middle values.
For odd-count sets: median = the middle value.

```dax
Better Median =
VAR __Table = SELECTCOLUMNS( 'Table', "Value", [Value] )
VAR __Path = CONCATENATEX( __Table, [Value], "|", [Value], ASC )
VAR __Length = PATHLENGTH( __Path )
VAR __IsOdd = ISODD( __Length )
VAR __Result =
    IF(
        __IsOdd,
        PATHITEM( __Path, ( __Length + 1 ) / 2, TEXT ) + 0,
        (
            PATHITEM( __Path, ( __Length / 2 ), TEXT )
            + PATHITEM( __Path, ( ( __Length / 2 ) + 1 ), TEXT )
            + 0
        ) / 2
    )
RETURN
    __Result
```

**How it works:**

1. **`SELECTCOLUMNS`**: extracts just the Value column into a simple table
2. **`CONCATENATEX`**: collapses the sorted values into a pipe-delimited string (`"val1|val2|val3"`), with `ASC` sorting smallest to largest
3. **`PATHLENGTH`**: counts the number of values in the path
4. **`ISODD`**: determines whether the count is odd or even
5. **`PATHITEM`**: extracts the middle element (odd) or the two middle elements (even) from the path; `+ 0` converts text to number
6. **`__Result`**: averages the two middle elements for even-count sets

## Mathematical Definition

For a data set `x` of `n` elements, ordered smallest to largest:

- **n is odd:** median(x) = x( (n+1) / 2 )
- **n is even:** median(x) = ( x(n/2) + x((n/2)+1) ) / 2

Both fixes above implement this correctly.

## MEDIANX Companion Patterns

`MEDIANX` iterates over a table and computes the median of an expression — useful when the median must be computed over a filtered or grouped set:

```dax
Median Total Cost by Item =
MEDIANX(
    SUMMARIZE( 'Table', 'Table'[Item], "__Cost", [Total Cost] ),
    [__Cost]
)
```

When used in calculated columns, `MEDIANX` has the same variant-type error as `MEDIAN`. Apply the same `CONVERT` workaround:

```dax
Even Better MedianX =
CONVERT(
    MEDIANX( 'Table', [Value] ),
    DOUBLE
)
```

## Related

- [Better MOD](/wiki/better-mod-workaround-dax.md) — another DAX function with a decimal bug and workaround
- [MEDIAN](/wiki/median.md) — the native (buggy in calculated columns) median function
- [MEDIANX](/wiki/medianx.md) — the iterator version of MEDIAN
- [CONCATENATEX](/wiki/concatenate-concatenatex.md) — the path-building function used in the mathematical implementation
- [PATH functions](/wiki/path.md) — PATHITEM, PATHLENGTH, PATHLENGTH used in the median implementation
