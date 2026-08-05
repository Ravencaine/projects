---
title: "Multiple-Criteria Lookups in Excel: Five Methods to Master"
source: "https://medium.com/@markchen69/multiple-criteria-lookups-in-excel-five-methods-to-master-a6c22aaa5df0"
author:
  - "[[Mark Chen]]"
published: 2025-05-28
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
Looking up a value based on more than one condition in Excel can feel like wrestling an octopus — once you’ve got one arm under control, another is wriggling away. Over the years, I’ve settled on five go-to approaches, each with its own strengths and trade-offs. Let’s walk through them with the familiar Customer/Product → Sales example:

*Customer Product Sales*

*Alice Widget 1,200*

*Bob Gadget 800*

*Alice Gadget 1,400*

We want to find **Alice + Gadget → 1,400**.

![](99.System/Attachments/1!m4sfxoLZ_tVv1N78CWiEkw.png.webp)

## 1\. Helper Column + XLOOKUP/VLOOKUP

## How it works

**Concatenate** your criteria into a single “key” column.

```c
=A2 & "|" & B2
```

**Lookup** that key. With XLOOKUP:

```c
=XLOOKUP(   
F1 & "|" & G1,       // lookup value: e.g. "Alice|Gadget"   
Table1[Key],         // helper column   
Table1[Sales],       // return column   
"Not found" )
```

## Pros

- **Universal**: Works in all Excel versions (even pre-365).
- **Performance**: Fast, since concatenation happens once per row.
- **Simplicity**: Easy to audit — your key column shows exactly how the match happens.

## Cons

- **Maintenance**: You must keep the helper column updated (or remember to recalc).
- **Extra clutter**: Additional column in your table.

## 2\. INDEX / MATCH with Multiple Criteria

## How it works

```c
=INDEX(
  Table1[Sales],
  MATCH(
    1,
    (Table1[Customer]=F1) * (Table1[Product]=G1),
    0
  )
)
```
- `(Table1[Customer]=F1)` and `(Table1[Product]=G1)` each produce an array of TRUE/FALSE.
- Multiplying them coerces to 1/0, yielding a 1 only where **both** are TRUE.
- `MATCH(1, …,0)` finds that row number.

***Note****: In older Excel (pre-365), confirm with* ***Ctrl+Shift+Enter****; in 365 it’s a normal formula.*

## Pros

- **No helper columns**: All logic lives in one formula.
- **Transparent**: You can easily tweak the criteria arrays.

## Cons

- **Array formulas**: Slightly harder to read/debug, especially for people unfamiliar with array math.
- **Performance**: On very large tables, recalculating those arrays repeatedly can slow things down.

## 3\. XLOOKUP with Multiple Criteria (365 Only)

## How it works

XLOOKUP can replace the INDEX/MATCH pattern:

```c
=XLOOKUP(
  1,
  (Table1[Customer]=F1) * (Table1[Product]=G1),
  Table1[Sales],
  "Not found"
)
```

It’s essentially the same array-math trick, but wrapped in XLOOKUP’s friendlier syntax.

## Pros

- **Concise**: Cleaner argument order (lookup array, return array, not-found…).
- **Built-in not-found**: You get the nice custom “Not found” message.

## Cons

- **365-only**: Not available in older versions.
- **Arrays under the hood**: Shares the same performance caveats as INDEX/MATCH arrays.

## 4\. FILTER Function (365 Only)

## How it works

To return **all** matching rows:

```c
=FILTER(
  Table1[Sales],
  (Table1[Customer]=F1) * (Table1[Product]=G1),
  "No match"
)
```

Or wrap it in `INDEX(…,1)` to get only the first result:

```c
=INDEX(
  FILTER(
    Table1[Sales],
    (Table1[Customer]=F1)*(Table1[Product]=G1),
    ""
  ),
  1
)
```

## Pros

- **Dynamic**: Returns multiple matches in a spill range.
- **Readable**: It’s obvious — “give me the rows where both criteria hold.”

## Cons

- **365-only**.
- **Spill behavior**: If you only want one value, you need that extra `INDEX`.

## 5\. LET + XMATCH + INDEX (365 Only)

## How it works

Combining `LET` with `XMATCH` and `INDEX` avoids recalculating arrays multiple times:

```c
=LET(
  custMatch, Table1[Customer]=F1,
  prodMatch, Table1[Product]=G1,
  bothMatch, custMatch * prodMatch,
  idx,       XMATCH(1, bothMatch, 0),
  result,    INDEX(Table1[Sales], idx),
  IFNA(result, "Not found")
)
```

## Pros

- **Efficiency**: Each sub-expression is calculated once.
- **Clarity**: Breaking the logic into named steps makes the formula self-documenting.
- **Error trapping**: You can wrap the final result in `IFNA` to handle “not found” cleanly.

## Cons

- **Version**: Requires Office 365 with both LET and XMATCH.
- **Learning curve**: LET can feel like a mini programming language at first.

## Which Method Should You Choose?

Method Version Results Ease Performance

Helper Col + XLOOKUP/VLOOKUP All Single ★★★★★ ★★★★★ INDEX/MATCH Array All (arrays) Single ★★★★☆ ★★★★☆

XLOOKUP Array 365+ Single ★★★★☆ ★★★★☆

FILTER 365+ Multiple/1st ★★★★☆ ★★★★☆

LET + XMATCH + INDEX 365+ Single ★★★☆☆ ★★★★★

- **Small to mid-sized** tables: XLOOKUP Array or INDEX/MATCH are quick to set up.
- **Huge datasets**: Helper columns or LET/XMATCH will give you max speed.
- **Multiple results**: Go with FILTER.
- **Readability & maintainability**: LET is your best friend once you’re comfortable with it.

## Final Thoughts

Excel’s lookup toolbox has come a long way. Even if you are familiar with array formulas, the combination of modern functions (XLOOKUP, FILTER, LET) gives you powerful, readable, and maintainable ways to handle multi-criteria lookups — no VBA required. Pick the method that fits your version of Excel, dataset size, and your own taste for “formula elegance,” and you’ll never wrestle octopus-like lookups again.

*Enjoy diving deeper, and feel free to share your own tips and tricks in the comments!*