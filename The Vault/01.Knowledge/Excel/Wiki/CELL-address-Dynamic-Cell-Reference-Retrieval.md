---
created: 2026-08-09
updated: 2026-08-09
source: "Excel HYPERLINK function • My Online Training Hub"
note_type: atomic
tags: [excel, cell-function, address, dynamic-reference, hyperlink, string, absolute-address]
---

# CELL("address") for Dynamic Cell Reference Retrieval

`CELL("address", ref)` returns the absolute cell address of a reference as a text string (e.g. `$A$5`). Used to dynamically construct the link_location argument for HYPERLINK when the target cell is determined by a lookup formula.

## Syntax

```
=CELL("address", reference)
```

| Argument | Description |
|----------|-------------|
| "address" | The info_type — always the string "address" |
| reference | The cell or range whose address to retrieve |

## Return Value

```
=CELL("address", XLOOKUP(D6, Orders[OrderID], Orders[OrderID]))
→ "$A$5"   (or whatever row XLOOKUP resolves to)
```

Returns the absolute address of the cell that XLOOKUP returns.

## Why This Matters for HYPERLINK

HYPERLINK needs a text string as its link_location. When the target cell is dynamic (determined by a lookup), you cannot hard-code the address. CELL("address") bridges the gap:

```
HYPERLINK(
  "#"&CELL("address", XLOOKUP(...)),   ← dynamically resolved text
  "Go to Order-1234"
)
```

## CELL Info Types

`CELL()` accepts many info_type values:

| info_type | Returns |
|-----------|---------|
| "address" | Absolute address (e.g. `$A$1`) |
| "col" | Column number |
| "row" | Row number |
| "filename" | Full file path |
| "format" | Number format |
| "type" | "b" (blank), "l" (label), "v" (value) |

## Related

- [[Source-HYPERLINK-Function-Mynda-Treacy]] — source
- [[Dynamic-Hyperlink-XLOOKUP-CELL]] — practical use: HYPERLINK + XLOOKUP + CELL("address") to jump to a matching row
